/*
 * This file implements support for the "Blocks" feature of Objective-C
 *
 * Most of the code in this file implements a single manually coded block that
 * is manipulated at runtime, basically similarly to how method descriptors are
 * manipulated by pyobjc.
 *
 * WARNING: The blocks implementation is technically private, the interfaces we
 * use here are extracted from the Blocks implementation documentation from clang.
 */
#import "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

/*
 * Definitions for block functions. These definitions are technically
 * private, but are the only way to interact with the block machinery.
 *
 * Definitions are copied from the clang documentation on blocks.
 */

enum {
    BLOCK_IS_NOESCAPE      = (1 << 23),
    BLOCK_HAS_COPY_DISPOSE = (1 << 25),
    BLOCK_HAS_CTOR         = (1 << 26),
    BLOCK_IS_GLOBAL        = (1 << 28),
    BLOCK_HAS_STRET        = (1 << 29),
    BLOCK_HAS_SIGNATURE    = (1 << 30)
};

/*
 * End of definitions.
 */

static Class gGlobalBlockClass = nil;
static Class gStackBlockClass  = nil;

struct block_descriptor {
    unsigned long int reserved;
    unsigned long int size;
    void (*copy_helper)(void* dst, void* src);
    void (*dispose_helper)(void* src);
    const char* signature;
};

struct block_descriptor_basic {
    unsigned long int reserved;
    unsigned long int size;
    void* _Nullable rest[1];
};

struct block_literal {
    void* isa;
    int   flags;
    int   reserved;
    void (*invoke)(void*, ...);
    struct block_descriptor* descriptor;
    PyObject* _Nullable invoke_cleanup;
    PyObject* _Nullable descriptor_memory;
    PyObject* _Nullable signature_memory;
};

const char* _Nullable PyObjCBlock_GetSignature(void* _block)
{
    struct block_literal* block = (struct block_literal*)_block;

    if (((intptr_t)(block->isa)) & 0x1) { // LCOV_BR_EXCL_LINE
        /* XXX: Hack to avoid a hard crash that I haven't been able
         * to pintpoint yet (test doesn't fail reliably, and I haven't
         * been able to trigger it with a unittest.
         *
         * Without this test the tests for blocks without metadata
         * sometimes crash due to invalid block pointers :-(
         */
        return NULL; // LCOV_EXCL_LINE
    }

    if ((block->flags & BLOCK_HAS_SIGNATURE) != 0) {
        const char* signature_loc = (void*)(block->descriptor);
        signature_loc += sizeof(unsigned long) * 2;
        if (block->flags & BLOCK_HAS_COPY_DISPOSE) {
            signature_loc += sizeof(void (*)(void)) * 2;
        }
        return *(const char**)signature_loc;
    }
    return NULL;
}

static void
oc_copy_helper(void* _dst, void* _src)
{
    struct block_literal* dst = (struct block_literal*)_dst;
    struct block_literal* src = (struct block_literal*)_src;

    PyObjC_BEGIN_WITH_GIL
        dst->invoke_cleanup    = Py_XNewRef(src->invoke_cleanup);
        dst->descriptor_memory = Py_XNewRef(src->descriptor_memory);
        dst->signature_memory  = Py_XNewRef(src->signature_memory);

    PyObjC_END_WITH_GIL
}

static void
oc_dispose_helper(void* _src)
{
    struct block_literal* src = (struct block_literal*)_src;

    PyObjC_BEGIN_WITH_GIL
        Py_CLEAR(src->invoke_cleanup);
        Py_CLEAR(src->descriptor_memory);
        Py_CLEAR(src->signature_memory);

    PyObjC_END_WITH_GIL
}

static struct block_descriptor gDescriptorTemplate = {
    .reserved       = 0,
    .size           = sizeof(struct block_literal),
    .copy_helper    = oc_copy_helper,
    .dispose_helper = oc_dispose_helper,
    .signature      = 0,
};

static struct block_literal gLiteralTemplate = {
    .isa               = 0,
    .flags             = BLOCK_HAS_COPY_DISPOSE,
    .reserved          = 0,
    .invoke            = NULL,
    .descriptor        = &gDescriptorTemplate,
    .invoke_cleanup    = NULL,
    .descriptor_memory = NULL,
    .signature_memory  = NULL,
};

/*
 * PyObjCBlock_Call is exposed to python code as objc._block_call(block, signature, args,
 * kwds), and is called from the __call__ method on blocks.
 *
 * The tp_call of blocks isn't set directly because that's annoyingly hard to arrange for
 * in objc-class.m, just setting the tp_call slot isn't good enough: you somehow have to
 * update the class dictionary as well (including those of subclasses). There is no public
 * API for that.
 */
PyObject* _Nullable PyObjCBlock_Call(PyObject* module __attribute__((__unused__)),
                                     PyObject* func_args)
{
    PyObject*              self;
    PyObjCMethodSignature* signature;
    PyObject*              args;
    PyObject*              kwds;
    NSObject*              block_ptr;
    _block_func_ptr        call_func;
    Py_ssize_t             byref_in_count;
    Py_ssize_t             byref_out_count;
    Py_ssize_t             plain_count;
    Py_ssize_t             argbuf_len;
    Py_ssize_t             cif_arg_count;
    BOOL                   variadicAllArgs = NO;
    int                    r;
    unsigned char*         argbuf = NULL;
    ffi_type*              arglist[MAX_ARGCOUNT];
    void*                  values[MAX_ARGCOUNT];
    void*                  byref[MAX_ARGCOUNT]      = {0};
    struct byref_attr      byref_attr[MAX_ARGCOUNT] = {BYREF_ATTR_INT};
    ffi_cif                cif;
    PyObject*              retval;

    if (!PyArg_ParseTuple(func_args, "OOOO", &self, &signature, &args, &kwds)) {
        return NULL;
    }

    if (!PyObjCObject_Check(self) || !PyObjCObject_IsBlock(self)) {
        PyErr_SetString(PyExc_TypeError, "object is not a block");
        return NULL;
    }

    if ((PyObject*)signature == Py_None) {
        PyErr_SetString(PyExc_TypeError, "cannot call block without a signature");
        return NULL;
    }

    if (!PyObjCMethodSignature_Check(signature)) {
        PyErr_SetString(PyExc_TypeError, "signature is not a signature object");
        return NULL;
    }

    if (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0) {
        PyErr_SetString(PyExc_TypeError, "keyword arguments not supported");
        return NULL;
    }

    block_ptr = PyObjCObject_GetObject(self);
    assert(block_ptr != nil);

    call_func = PyObjCBlock_GetFunction(block_ptr);

    argbuf_len = PyObjCRT_SizeOfReturnType(signature->rettype->type);
    argbuf_len = align(argbuf_len, sizeof(void*));

#ifndef __arm64__
    int useStret = PyObjCRT_ResultUsesStret(signature->rettype->type);
    if (useStret == -1) {
        goto error;
    }
#endif

    argbuf_len += sizeof(void*); /* Argument 0: the block itself */
    r = PyObjCFFI_CountArguments(signature, 1, &byref_in_count, &byref_out_count,
                                 &plain_count, &argbuf_len, &variadicAllArgs);
    if (r == -1) {
        return NULL;
    }

    variadicAllArgs |= signature->variadic
                       && (signature->null_terminated_array || signature->arrayArg != -1);

    if (variadicAllArgs) {
        if (byref_in_count != 0 || byref_out_count != 0) {
            PyErr_Format(PyExc_TypeError, "printf format with by-ref args not supported");
            return NULL;
        }

        if (PyTuple_Size(args) < Py_SIZE(signature) - 1) {
            PyErr_Format(PyExc_TypeError,
                         "Need %" PY_FORMAT_SIZE_T "d arguments, got %" PY_FORMAT_SIZE_T
                         "d",
                         Py_SIZE(signature) - 1, PyTuple_Size(args));
            return NULL;
        }

    } else if (PyTuple_Size(args) != Py_SIZE(signature) - 1) {
        PyErr_Format(PyExc_TypeError,
                     "Need %" PY_FORMAT_SIZE_T "d arguments, got %" PY_FORMAT_SIZE_T "d",
                     Py_SIZE(signature) - 1, PyTuple_Size(args));
        return NULL;
    }

    if (PyTuple_Size(args) > MAX_ARGCOUNT - 1) {
        PyErr_Format(PyExc_TypeError,
                     "At most %d arguments are supported, got %" PY_FORMAT_SIZE_T
                     "d arguments",
                     MAX_ARGCOUNT, PyTuple_Size(args));
        return NULL;
    }

    argbuf = PyMem_Malloc(argbuf_len);
    if (argbuf == NULL) { // LCOV_BR_EXCL_LINE
        PyErr_NoMemory(); // LCOV_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

#ifdef __arm64__
    cif_arg_count = PyObjCFFI_ParseArguments(
        signature, 1, PyTuple_ITEMS(args), PyTuple_GET_SIZE(args),
        align(PyObjCRT_SizeOfReturnType(signature->rettype->type), sizeof(void*))
            + sizeof(void*),
        argbuf, argbuf_len, byref, byref_attr, arglist, values);
#else
    cif_arg_count = PyObjCFFI_ParseArguments(
        signature, 1, PyTuple_ITEMS(args), PyTuple_GET_SIZE(args),
        align(PyObjCRT_SizeOfReturnType(signature->rettype->type), sizeof(void*))
            + sizeof(void*),
        argbuf, argbuf_len, byref, byref_attr, useStret ? arglist + 1 : arglist,
        useStret ? values + 1 : values);
#endif

    if (cif_arg_count == -1) {
        goto error;
    }

#ifdef __arm64__
    arglist[0] = &ffi_type_pointer;
    values[0]  = &block_ptr;

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"

    if (signature->variadic) {
        r = ffi_prep_cif_var(&cif, FFI_DEFAULT_ABI, (int)Py_SIZE(signature),
                             (int)cif_arg_count,
                             PyObjCFFI_Typestr2FFI(signature->rettype->type), arglist);
    } else {
        r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, (int)cif_arg_count,
                         PyObjCFFI_Typestr2FFI(signature->rettype->type), arglist);
    }
#pragma clang diagnostic pop

#else
    if (useStret) {
        arglist[0] = &ffi_type_pointer;
        byref[0]   = argbuf;
        values[0]  = byref;
        arglist[1] = &ffi_type_pointer;
        values[1]  = &block_ptr;
    } else {
        arglist[0] = &ffi_type_pointer;
        values[0]  = &block_ptr;
    }

#if PyObjC_BUILD_RELEASE >= 1015
    if (@available(macOS 10.15, *)) {
        if (signature->variadic) {
            r = ffi_prep_cif_var(
                &cif, FFI_DEFAULT_ABI,
                (int)(useStret ? Py_SIZE(signature) + 1 : Py_SIZE(signature)),
                (int)(useStret ? cif_arg_count + 1 : cif_arg_count),
                useStret ? &ffi_type_void
                         : PyObjCFFI_Typestr2FFI(signature->rettype->type),
                arglist);
        } else {
            r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI,
                             (int)(useStret ? cif_arg_count + 1 : cif_arg_count),
                             useStret ? &ffi_type_void
                                      : PyObjCFFI_Typestr2FFI(signature->rettype->type),
                             arglist);
        }
    } else
#endif
    {
        r = ffi_prep_cif(
            &cif, FFI_DEFAULT_ABI, (int)(useStret ? cif_arg_count + 1 : cif_arg_count),
            useStret ? &ffi_type_void : PyObjCFFI_Typestr2FFI(signature->rettype->type),
            arglist);
    }

#endif

    if (r != FFI_OK) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Format(PyExc_RuntimeError, "Cannot setup FFI CIF [%d]", r);
        goto error;
        // LCOV_EXCL_STOP
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            ffi_call(&cif, FFI_FN(call_func), argbuf, values);

        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

#ifndef __arm64__
    if (useStret) {
        byref[0] = NULL;
    }
#endif

    if (PyErr_Occurred()) {
        goto error;
    }

#ifdef __arm64__
    retval = PyObjCFFI_BuildResult(signature, 1, argbuf, byref, byref_attr,
                                   byref_out_count, values);
#else
    retval = PyObjCFFI_BuildResult(signature, 1, argbuf, byref, byref_attr,
                                   byref_out_count, useStret ? values + 1 : values);
#endif

    if (variadicAllArgs) {
        PyObjCFFI_FreeByRef(Py_SIZE(signature) + PyTuple_Size(args), byref, byref_attr);

    } else {
        PyObjCFFI_FreeByRef(Py_SIZE(signature), byref, byref_attr);
    }

    PyMem_Free(argbuf);
    argbuf = NULL;
    return retval;

error:
    if (variadicAllArgs) {
        PyObjCFFI_FreeByRef(Py_SIZE(signature) + PyTuple_Size(args), byref, byref_attr);
    } else {
        PyObjCFFI_FreeByRef(Py_SIZE(signature), byref, byref_attr);
    }
    if (argbuf) { // LCOV_BR_EXCL_LINE
        PyMem_Free(argbuf);
    }
    return NULL;
} // LCOV_BR_EXCL_LINE

static void
PyObjCBlock_CleanupCapsule(PyObject* ptr)
{
    PyObjCBlockFunction block_func =
        (PyObjCBlockFunction)PyCapsule_GetPointer(ptr, "objc.__block_release__");
    if (block_func == NULL) // LCOV_BR_EXCL_LINE
        return;             // LCOV_EXCL_LINE

    PyObjCFFI_FreeBlockFunction(block_func);
} // LCOV_BR_EXCL_LINE

static PyObject* _Nullable block_signature(PyObjCMethodSignature* signature)
{
    Py_ssize_t i;
    Py_ssize_t buflen = 1;
    PyObject*  buf;
    char*      cur;

    buflen += strlen(signature->rettype->type);
    for (i = 0; i < Py_SIZE(signature); i++) {
        buflen += strlen(signature->argtype[i]->type);
    }

    buf = PyBytes_FromStringAndSize(NULL, buflen);
    if (buf == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }

    cur = PyBytes_AsString(buf);
    if (cur == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_CLEAR(buf);
        return NULL;
        // LCOV_EXCL_STOP
    }
    strlcpy(cur, signature->rettype->type, buflen);
    for (i = 0; i < Py_SIZE(signature); i++) {
        strlcat(cur, signature->argtype[i]->type, buflen);
    }
    return buf;
}

void* _Nullable PyObjCBlock_Create(PyObjCMethodSignature* signature, PyObject* callable)
{
    struct block_literal block = gLiteralTemplate;

    assert(gGlobalBlockClass != Nil);
    assert(callable != NULL);

    block.descriptor_memory =
        PyBytes_FromStringAndSize(NULL, sizeof(struct block_descriptor));
    if (block.descriptor_memory == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;                       // LCOV_EXCL_LINE
    }
    block.descriptor =
        (struct block_descriptor*)PyBytes_AsString(block.descriptor_memory);
    *(block.descriptor) = *(gLiteralTemplate.descriptor);

    /* The value of "signature->signature" cannot be trusted, it
     * contains the raw signature without any updates from metadata.
     * Furthermore the value is bogus for block signatures in metadata.
     *
     * The function below only fails when running out of memory
     */
    block.signature_memory = block_signature(signature);
    if (block.signature_memory == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_CLEAR(block.descriptor_memory);
        return NULL;
        // LCOV_EXCL_STOP
    }
    block.descriptor->signature = PyBytes_AsString(block.signature_memory);
    block.flags |= BLOCK_HAS_SIGNATURE;
    block.isa                      = gStackBlockClass;
    PyObjCBlockFunction block_func = PyObjCFFI_MakeBlockFunction(signature, callable);
    if (block_func == NULL) {
        Py_CLEAR(block.descriptor_memory);
        Py_CLEAR(block.signature_memory);
        return NULL;
    }
    block.invoke = block_func;

    block.invoke_cleanup = PyCapsule_New((void*)(block.invoke), "objc.__block_release__",
                                         PyObjCBlock_CleanupCapsule);
    if (block.invoke_cleanup == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyObjCFFI_FreeBlockFunction(block.invoke);
        Py_CLEAR(block.descriptor_memory);
        Py_CLEAR(block.signature_memory);
        return NULL;
        // LCOV_EXCL_STOP
    }

    /* We've started with a stack block, make sure it is stored into global memory */
    id block_value = [(id)&block copy];
    Py_CLEAR(block.invoke_cleanup);
    Py_CLEAR(block.descriptor_memory);
    Py_CLEAR(block.signature_memory);

    return (void*)block_value;
}

_block_func_ptr
PyObjCBlock_GetFunction(void* block)
{
    return ((struct block_literal*)block)->invoke;
}

/*
 * Support for converting blocks to python objects.
 */

static PyObject* _Nullable pyobjc_PythonObject(NSObject* self,
                                               SEL       _sel __attribute__((__unused__)))
{
    PyObject* rval;

    /* Stack blocks are allocated on the stack and cause problems with
     * Python's garbage collections. Therefore uncondationally copy them,
     * which converts them to dynamically allocated blocks.
     */
    self = [self copy];

    rval = (PyObject*)PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
    [self release];
    if (rval == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        return NULL;
        // LCOV_EXCL_STOP
    } else {
        PyObject* actual = PyObjC_RegisterPythonProxy(self, rval);
        Py_DECREF(rval);
        return actual;
    }
}

/* the __pyobjc_PythonTransient__ method is only used in the
 * implementation of Python methods on a class. Those aren't
 * supported for blocks.
 */
// LCOV_EXCL_START
static PyObject* _Nullable pyobjc_PythonTransient(NSObject* self,
                                                  SEL  _sel __attribute__((__unused__)),
                                                  int* cookie)
{
    /* Stack blocks are allocated on the stack and cause problems with
     * Python's garbage collections. Therefore uncondationally copy them,
     * which converts them to dynamically allocated blocks.
     */

    self = [self copy];

    *cookie          = 1;
    PyObject* result = PyObjCObject_New(self, PyObjCObject_kDEFAULT, YES);
    [self release];
    if (result == NULL) {
        return NULL;
    }
    return result;
}
// LCOV_EXCL_STOP

int
PyObjCBlock_Setup(PyObject* module __attribute__((__unused__)))
{
    Class StackBlock;
    Class GlobalBlock = objc_lookUpClass("__NSGlobalBlock__");
    if (GlobalBlock == Nil) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        /* This should never happen... */
        PyErr_SetString(PyObjCExc_InternalError, "Cannot find __NSGlobalBlock__ class");
        return -1;
        // LCOV_EXCL_STOP
    }
    gGlobalBlockClass = GlobalBlock;

    StackBlock = objc_lookUpClass("__NSStackBlock__");
    if (StackBlock == Nil) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        /* This should never happen... */
        PyErr_SetString(PyObjCExc_InternalError, "Cannot find __NSGlobalBlock__ class");
        return -1;
        // LCOV_EXCL_STOP
    }
    gStackBlockClass = StackBlock;

    if (!class_addMethod(StackBlock, // LCOV_BR_EXCL_LINE
                         @selector(__pyobjc_PythonObject__), (IMP)pyobjc_PythonObject,
                         "^{_object}@:")) {
        // LCOV_EXCL_START
        PyErr_SetString(PyObjCExc_InternalError, "Cannot initialize block support");
        return -1;
        // LCOV_EXCL_STOP
    }
    if (!class_addMethod(StackBlock, // LCOV_BR_EXCL_LINE
                         @selector(__pyobjc_PythonTransient__:),
                         (IMP)pyobjc_PythonTransient, "^{_object}@:^i")) {
        // LCOV_EXCL_START
        PyErr_SetString(PyObjCExc_InternalError, "Cannot initialize block support");
        return -1;
        // LCOV_EXCL_STOP
    }
    if (!class_addMethod(GlobalBlock, // LCOV_BR_EXCL_LINE
                         @selector(__pyobjc_PythonObject__), (IMP)pyobjc_PythonObject,
                         "^{_object}@:")) {
        // LCOV_EXCL_START
        PyErr_SetString(PyObjCExc_InternalError, "Cannot initialize block support");
        return -1;
        // LCOV_EXCL_STOP
    }
    if (!class_addMethod(GlobalBlock, // LCOV_BR_EXCL_LINE
                         @selector(__pyobjc_PythonTransient__:),
                         (IMP)pyobjc_PythonTransient, "^{_object}@:^i")) {
        // LCOV_EXCL_START
        PyErr_SetString(PyObjCExc_InternalError, "Cannot initialize block support");
        return -1;
        // LCOV_EXCL_STOP
    }

    return 0;
}

NS_ASSUME_NONNULL_END
