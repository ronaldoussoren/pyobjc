/*
 * This file implements support for the "Blocks" feature of Objective-C
 *
 * Most of the code in this file implements a single manually coded block that
 * is manipulated at runtime, basicly simularly to how method descriptors are
 * manipulated by pyobjc.
 *
 * WARNING: The blocks implementation is technically private, the interfaces we
 * use here are extracted from the Blocks implementation documentation from clang.
 */
#import "pyobjc.h"

/*
 * Definitions for block functions. These definitions are technically
 * private, but are the only way to interact with the block machinary.
 *
 * Definitions are copied from the clang documentation on blocks.
 */

enum {
    BLOCK_HAS_COPY_DISPOSE =  (1 << 25),
    BLOCK_IS_GLOBAL        =  (1 << 28),
    BLOCK_HAS_STRET        =  (1 << 29),
    BLOCK_HAS_SIGNATURE    =  (1 << 30)
};

/*
 * End of definitions.
 */

static Class gStackBlockClass = nil;

struct block_descriptor {
    unsigned long int reserved;
    unsigned long int size;
    void (*copy_helper)(void* dst, void*src);
    void (*dispose_helper)(void* src);
    const char* signature;
};

struct block_descriptor_basic {
    unsigned long int reserved;
    unsigned long int size;
    void* rest[1];
};

struct block_literal {
    void* isa;
    int   flags;
    int   reserved;
    void (*invoke)(void*, ...);
    struct block_descriptor* descriptor;
    PyObject* invoke_cleanup;
};

const char*
PyObjCBlock_GetSignature(void* _block)
{
    struct block_literal* block = (struct block_literal*)_block;
    struct block_descriptor_basic* descriptor = (struct block_descriptor_basic*)block->descriptor;
    size_t offset = 0;

    if (block->flags & BLOCK_HAS_COPY_DISPOSE) {
        offset += 2;
    }

    if (block->flags & BLOCK_HAS_SIGNATURE) {
        return descriptor->rest[offset];
    }
    return NULL;
}

static void
oc_copy_helper(void* _dst, void* _src)
{
    struct block_literal* dst = (struct block_literal*)_dst;
    struct block_literal* src = (struct block_literal*)_src;

    PyObjC_BEGIN_WITH_GIL
        dst->invoke_cleanup = src->invoke_cleanup;
        Py_XINCREF(dst->invoke_cleanup);

    PyObjC_END_WITH_GIL

}

static void
oc_dispose_helper(void* _src)
{
    struct block_literal* src = (struct block_literal*)_src;

    PyObjC_BEGIN_WITH_GIL
        Py_CLEAR(src->invoke_cleanup);

    PyObjC_END_WITH_GIL
}

static struct block_descriptor gDescriptorTemplate = {
    0,
    sizeof(struct block_literal),
    oc_copy_helper,
    oc_dispose_helper,
    0
};

static struct block_literal gLiteralTemplate = {
    0,     /* ISA */
    BLOCK_HAS_COPY_DISPOSE,
    0,
    0,
    &gDescriptorTemplate,
    0
};


/*
 * PyObjCBlock_Call is exposed to python code as objc._block_call(block, signature, args, kwds),
 * and is called from the __call__ method on blocks.
 *
 * The tp_call of blocks isn't set directly because that's annoyingly hard to arrange for
 * in objc-class.m, just setting the tp_call slot isn't good enough: you somehow have to update
 * the class dictionary as well (including those of subclasses). There is no public API for
 * that.
 */
PyObject*
PyObjCBlock_Call(PyObject* module __attribute__((__unused__)), PyObject* func_args)
{
    PyObject* self;
    PyObjCMethodSignature* signature;
    PyObject* args;
    PyObject* kwds;
    NSObject* block_ptr;
    _block_func_ptr call_func;
    Py_ssize_t byref_in_count;
    Py_ssize_t byref_out_count;
    Py_ssize_t plain_count;
    Py_ssize_t argbuf_len;
    Py_ssize_t cif_arg_count;
    BOOL variadicAllArgs = NO;
    int r;
    unsigned char* argbuf = NULL;
    ffi_type* arglist[MAX_ARGCOUNT];
    void* values[MAX_ARGCOUNT];
    void* byref[MAX_ARGCOUNT] =  { 0 };
    struct byref_attr byref_attr[MAX_ARGCOUNT] =  { {0, 0} };
    ffi_cif cif;
    PyObject* retval;

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

    if (kwds != NULL && (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError, "keyword arguments not supported");
        return NULL;
    }

    block_ptr = PyObjCObject_GetObject(self);
    call_func = PyObjCBlock_GetFunction(block_ptr);

    argbuf_len = PyObjCRT_SizeOfReturnType(signature->rettype->type);
    argbuf_len = align(argbuf_len, sizeof(void*));

    int useStret =  PyObjCRT_ResultUsesStret(signature->rettype->type);
    if (useStret == -1) {
        goto error;
    }

    argbuf_len += sizeof(void*); /* Argument 0: the block itself */
    r = PyObjCFFI_CountArguments(
        signature, 1,
        &byref_in_count, &byref_out_count, &plain_count,
        &argbuf_len, &variadicAllArgs);
    if (r == -1) {
        return NULL;
    }

    variadicAllArgs |= signature->variadic && (signature->null_terminated_array || signature->arrayArg != -1);

    if (variadicAllArgs) {
        if (byref_in_count != 0 || byref_out_count != 0) {
            PyErr_Format(PyExc_TypeError, "Sorry, printf format with by-ref args not supported");
            return NULL;
        }

        if (PyTuple_Size(args) < Py_SIZE(signature) - 1) {
            PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
            Py_SIZE(signature) - 2, PyTuple_Size(args));
            return NULL;
        }

        if (PyTuple_Size(args) > MAX_ARGCOUNT - 1) {
            PyErr_Format(PyExc_TypeError, "At most %d arguments are supported, got %" PY_FORMAT_SIZE_T "d arguments", MAX_ARGCOUNT, PyTuple_Size(args));
            return NULL;
        }

    } else if (PyTuple_Size(args) != Py_SIZE(signature) - 1) {
        if (Py_SIZE(signature) > MAX_ARGCOUNT) {
            PyErr_Format(PyExc_TypeError, "At most %d arguments are supported, got %" PY_FORMAT_SIZE_T "d arguments", MAX_ARGCOUNT, PyTuple_Size(args));
            return NULL;
        }

        PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
            Py_SIZE(signature), PyTuple_Size(args));
        return NULL;
    }

    argbuf = PyMem_Malloc(argbuf_len);
    if (argbuf == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    cif_arg_count = PyObjCFFI_ParseArguments(
        signature, 1, args,
        align(PyObjCRT_SizeOfReturnType(signature->rettype->type), sizeof(void*)) + sizeof(void*),
        argbuf, argbuf_len, byref, byref_attr, useStret ? arglist + 1 : arglist, useStret ? values + 1 : values);

    if (cif_arg_count == -1) {
        goto error;
    }


    if (useStret) {
        arglist[0] = &ffi_type_pointer;
        byref[0] = argbuf;
        values[0] = byref;
        arglist[1] = &ffi_type_pointer;
        values[1] = &block_ptr;
    } else {
        arglist[0] = &ffi_type_pointer;
        values[0] = &block_ptr;
    }

    r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, (int)(useStret ? cif_arg_count + 1 : cif_arg_count),
            useStret ? &ffi_type_void : PyObjCFFI_Typestr2FFI(signature->rettype->type), arglist);
    if (r != FFI_OK) {
        PyErr_Format(PyExc_RuntimeError, "Cannot setup FFI CIF [%d]", r);
        goto error;
    }

    PyObjC_DURING
        ffi_call(&cif, FFI_FN(call_func), argbuf, values);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (useStret) {
        byref[0] = NULL;
    }

    if (PyErr_Occurred()) {
        goto error;
    }

    retval = PyObjCFFI_BuildResult(signature, 1, argbuf, byref,
                   byref_attr, byref_out_count, NULL, 0, useStret ? values + 1: values );

    if (variadicAllArgs) {
        if (PyObjCFFI_FreeByRef(Py_SIZE(signature)+PyTuple_Size(args), byref, byref_attr) < 0) {
            goto error;
        }

    } else {
        if (PyObjCFFI_FreeByRef(Py_SIZE(signature), byref, byref_attr) < 0) {
            goto error;
        }
    }

    PyMem_Free(argbuf); argbuf = NULL;
    return retval;

error:
    if (variadicAllArgs) {
        PyObjCFFI_FreeByRef(Py_SIZE(signature)+PyTuple_Size(args), byref, byref_attr);
    } else {
        PyObjCFFI_FreeByRef(Py_SIZE(signature), byref, byref_attr);
    }
    if (argbuf) {
        PyMem_Free(argbuf);
    }
    return NULL;
}

#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION < 7

static void PyObjCBlock_CleanupCapsule(void* ptr)
{
    PyObjCFFI_FreeBlockFunction(ptr);
}

#else /* Python <= 2.6 */

static void PyObjCBlock_CleanupCapsule(PyObject* ptr)
{
    PyObjCFFI_FreeBlockFunction(PyCapsule_GetPointer(ptr, "objc.__block_release__"));
}

#endif /* Python <= 2.6 */

static char*
block_signature(PyObjCMethodSignature* signature)
{
    Py_ssize_t i;
    Py_ssize_t buflen = 1;
    char* buf;
    char* cur;

    buflen += strlen(signature->rettype->type);
    for (i = 0; i < Py_SIZE(signature); i++) {
        buflen += strlen(signature->argtype[i]->type);
    }

    buf = PyMem_Malloc(buflen);
    if (buf == NULL) {
        return NULL;
    }

    cur = buf;
    strcpy(cur, signature->rettype->type);
    cur = strchr(cur, '\0');
    for (i = 0; i < Py_SIZE(signature); i++) {
        strcpy(cur, signature->argtype[i]->type);
        cur = strchr(cur, '\0');
    }
    return buf;
}

void*
PyObjCBlock_Create(PyObjCMethodSignature* signature, PyObject* callable)
{
    struct block_literal* block;

    if (gStackBlockClass == NULL) {
        PyErr_SetString(PyObjCExc_Error, "Blocks not supported on this platform");
        return NULL;
    }

    block = PyMem_Malloc(sizeof(struct block_literal) + sizeof(struct block_literal));
    if (block == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    *block = gLiteralTemplate;
    block->descriptor = (struct block_descriptor*)(((char*)block) + sizeof(struct block_literal));
    *(block->descriptor) = *(gLiteralTemplate.descriptor);
    if (signature->signature == NULL) {
        signature->signature = block_signature(signature);
        if (signature->signature == NULL) {
            PyMem_Free(block);
            return NULL;
        }
    }
    block->descriptor->signature = signature->signature;
    block->flags |= BLOCK_HAS_SIGNATURE;
    block->isa = gStackBlockClass;
    block->invoke = PyObjCFFI_MakeBlockFunction(signature, callable);
    if (block->invoke == NULL) {
        PyMem_Free(block);
        return NULL;
    }

    block->invoke_cleanup = PyCapsule_New(block->invoke, "objc.__block_release__",
            PyObjCBlock_CleanupCapsule);
    if (block->invoke_cleanup == NULL) {
        PyObjCFFI_FreeBlockFunction(block->invoke);
        PyMem_Free(block);
        return NULL;
    }
    return (void*)block;
}

void
PyObjCBlock_Release(void* _block)
{
    struct block_literal* block = (struct block_literal*)_block;
    Py_CLEAR(block->invoke_cleanup);
    PyMem_Free(block);
}


int
PyObjCBlock_Setup(void)
{
    gStackBlockClass = objc_lookUpClass("__NSGlobalBlock__");

    return 0;
}


_block_func_ptr
PyObjCBlock_GetFunction(void* block)
{
    return ((struct block_literal*)block)->invoke;
}
