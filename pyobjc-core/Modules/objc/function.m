/*
 * Wrapper for simple global functions. Simple functions are those without
 * arguments that require additional effort.
 *
 * TODO:
 * - Cache FFI for non-variadic functions (calculate on first call)
 * - "Simple" variant
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

typedef struct {
    PyObject_HEAD

    ffi_cif*               cif;
    PyObjCMethodSignature* methinfo;
    void*                  function;
    PyObject* _Nullable doc;
    PyObject* _Nullable name;
    PyObject* _Nullable module;
#if PY_VERSION_HEX >= 0x03090000
    vectorcallfunc vectorcall;
#endif
} func_object;

static PyObject* _Nullable func_metadata(PyObject* _self)
{
    func_object* self = (func_object*)_self;
    PyObject*    result;
    result = PyObjCMethodSignature_AsDict(self->methinfo);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    if (self->doc) {
        if (PyDict_SetItemString( // LCOV_BR_EXCL_LINE
                result, "__doc__", self->doc)
            == -1) {
            Py_DECREF(result); // LCOV_EXCL_LINE
            return NULL;       // LCOV_EXCL_LINE
        }
    }
    return result;
}

static PyMethodDef func_methods[] = {
    {.ml_name  = "__metadata__",
     .ml_meth  = (PyCFunction)func_metadata,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "Return a dict that describes the metadata for this function."},
    {
        .ml_name = NULL /* SENTINEL */
    }};

static PyGetSetDef func_getset[] = {{
                                        .name = "__doc__",
                                        .get  = PyObjC_callable_docstr_get,
                                        .doc  = "Documentation for a function",
                                    },
                                    {
                                        .name = "__signature__",
                                        .get  = PyObjC_callable_signature_get,
                                        .doc  = "inspect.Signature for a function",
                                    },
                                    {
                                        .name = NULL /* SENTINEL */
                                    }};

static PyMemberDef func_members[] = {{
                                         .name   = "__name__",
                                         .type   = T_OBJECT,
                                         .offset = offsetof(func_object, name),
                                         .flags  = READONLY,
                                     },
                                     {
                                         .name   = "__module__",
                                         .type   = T_OBJECT,
                                         .offset = offsetof(func_object, module),
                                     },
                                     {
                                         .name = NULL /* SENTINEL */
                                     }};

static PyObject* _Nullable func_repr(PyObject* _self)
{
    func_object* self = (func_object*)_self;

    if (self->name == NULL) {
        return PyUnicode_FromFormat("<objc.function at %p>", self);
    } else {
        return PyUnicode_FromFormat("<objc.function %R at %p>", self->name, self);
    }
}

static PyObject* _Nullable func_vectorcall(PyObject* s, PyObject* const* args,
                                           size_t nargsf, PyObject* _Nullable kwnames)
{
    func_object* self = (func_object*)s;
    Py_ssize_t   byref_in_count;
    Py_ssize_t   byref_out_count;
    Py_ssize_t   plain_count;
    Py_ssize_t   argbuf_len;
    int          r;
    Py_ssize_t   cif_arg_count;
    BOOL         variadicAllArgs = NO;

    unsigned char*    argbuf = NULL;
    ffi_type*         arglist[MAX_ARGCOUNT];
    void*             values[MAX_ARGCOUNT];
    void*             byref[MAX_ARGCOUNT]      = {0};
    struct byref_attr byref_attr[MAX_ARGCOUNT] = {BYREF_ATTR_INT};
    ffi_cif           cif;
    ffi_cif*          cifptr;

    PyObject* retval;

    if (PyObjC_CheckNoKwnames(s, kwnames) == -1) {
        return NULL;
    }

    /*
     * The PY_VECTORCALL_ARGUMENTS_OFFSET feature is not used by this function.
     * fetch the raw number of arguments to make it possible to ignore that flag
     * in the rest of the implementation.
     */
    nargsf = PyVectorcall_NARGS(nargsf);

    if (version_is_deprecated(self->methinfo->deprecated)) {
        char buf[128];

        snprintf(buf, 128, "%s() is a deprecated API (macOS %d.%d)",
                 (self->name ? PyUnicode_AsUTF8(self->name) : "objc.function instance"),
                 self->methinfo->deprecated / 100, self->methinfo->deprecated % 100);

        if (PyErr_Warn(PyObjCExc_DeprecationWarning, buf) < 0) {
            return NULL;
        }
    }

    if (self->methinfo->suggestion != NULL) {
        PyErr_SetObject(PyExc_TypeError, self->methinfo->suggestion);
        return NULL;
    }

    if (Py_SIZE(self->methinfo) >= 63) {
        PyErr_Format(PyObjCExc_Error,
                     "wrapping a function with %" PY_FORMAT_SIZE_T
                     "d arguments, at most 62 "
                     "are supported",
                     Py_SIZE(self->methinfo));
        return NULL;
    }

    argbuf_len = PyObjCRT_SizeOfReturnType(self->methinfo->rettype->type);
    argbuf_len = align(argbuf_len, sizeof(void*));
    r = PyObjCFFI_CountArguments(self->methinfo, 0, &byref_in_count, &byref_out_count,
                                 &plain_count, &argbuf_len, &variadicAllArgs);
    if (r == -1) {
        return NULL;
    }

    variadicAllArgs |=
        self->methinfo->variadic
        && (self->methinfo->null_terminated_array || self->methinfo->arrayArg != -1);

    if (variadicAllArgs) {
        if (byref_in_count != 0 || byref_out_count != 0) {
            PyErr_Format(PyExc_TypeError,
                         "Sorry, printf format with by-ref args not supported");
            return NULL;
        }

        if (nargsf < (size_t)Py_SIZE(self->methinfo)) {
            PyErr_Format(PyExc_TypeError,
                         "Need %" PY_FORMAT_SIZE_T "d arguments, got %zu",
                         Py_SIZE(self->methinfo) - 2, nargsf);
            return NULL;
        }

    } else if (nargsf != (size_t)Py_SIZE(self->methinfo)) {
        PyErr_Format(PyExc_TypeError, "Need %" PY_FORMAT_SIZE_T "d arguments, got %zu",
                     Py_SIZE(self->methinfo), nargsf);
        return NULL;
    }

    argbuf = PyMem_Malloc(argbuf_len);
    if (argbuf == NULL) { // LCOV_BR_EXCL_LINE
        PyErr_NoMemory(); // LCOV_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }

    cif_arg_count = PyObjCFFI_ParseArguments(
        self->methinfo, 0, args, nargsf,
        align(PyObjCRT_SizeOfReturnType(self->methinfo->rettype->type), sizeof(void*)),
        argbuf, argbuf_len, byref, byref_attr, arglist, values);

    if (cif_arg_count == -1) {
        goto error;
    }

    if (variadicAllArgs) {
#if PyObjC_BUILD_RELEASE >= 1015

#ifdef __arm64__
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"
#endif

#ifndef __arm64__
        if (@available(macOS 10.15, *)) {
#endif
            r = ffi_prep_cif_var(
                &cif, FFI_DEFAULT_ABI, (int)Py_SIZE(self->methinfo), (int)cif_arg_count,
                PyObjCFFI_Typestr2FFI(self->methinfo->rettype->type), arglist);
#ifndef __arm64__
        } else
#endif
#endif

#ifndef __arm64__
        {
            r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, (int)cif_arg_count,
                             PyObjCFFI_Typestr2FFI(self->methinfo->rettype->type),
                             arglist);
        }

#else
#pragma clang diagnostic pop
#endif

        if (r != FFI_OK) {
            PyErr_Format(PyExc_RuntimeError, "Cannot setup FFI CIF [%d]", r);
            goto error;
        }
        cifptr = &cif;

    } else {
        cifptr = self->cif;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            ffi_call(cifptr, FFI_FN(self->function), argbuf, values);

        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        goto error;
    }

    retval = PyObjCFFI_BuildResult(self->methinfo, 0, argbuf, byref, byref_attr,
                                   byref_out_count, NULL, 0, values);

    if (variadicAllArgs) {
        if (PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo) + nargsf, byref, byref_attr)
            < 0) {
            goto error;
        }

    } else {
        if (PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo), byref, byref_attr) < 0) {
            goto error;
        }
    }

    PyMem_Free(argbuf);
    argbuf = NULL;
    return retval;

error:
    if (variadicAllArgs) {
        PyObjCFFI_FreeByRef(nargsf, byref, byref_attr); /* XXX: Compare with call above */

    } else {
        PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo), byref, byref_attr);
    }

    if (argbuf) {
        PyMem_Free(argbuf);
    }
    return NULL;
}

#if PY_VERSION_HEX >= 0x03090000
/*
 * A variant of func_vectorcall that only handles "simple" functions. This allows
 * for a number of simplifications that significantly speed up functions calls
 * (about 50% faster on my M1 laptop)
 */
static PyObject* _Nullable func_vectorcall_simple(PyObject* s, PyObject* const* args,
                                                  size_t nargsf,
                                                  PyObject* _Nullable kwnames)
{
    func_object* self = (func_object*)s;

    unsigned char argbuf[SHORTCUT_MAX_ARGBUF];
    void*         values[MAX_ARGCOUNT_SIMPLE];

    PyObjC_Assert(self->methinfo->shortcut_signature, NULL);

    if (unlikely(kwnames != NULL
                 && (PyTuple_CheckExact(kwnames) && PyTuple_GET_SIZE(kwnames) != 0))) {
        PyErr_Format(PyExc_TypeError, "%R does not accept keyword arguments", s);
        return NULL;
    }

    /*
     * The PY_VECTORCALL_ARGUMENTS_OFFSET feature is not used by this function.
     * fetch the raw number of arguments to make it possible to ignore that flag
     * in the rest of the implementation.
     */
    nargsf = PyVectorcall_NARGS(nargsf);

    if (version_is_deprecated(self->methinfo->deprecated)) {
        char buf[128];

        snprintf(buf, 128, "%s() is a deprecated API (macOS %d.%d)",
                 (self->name ? PyUnicode_AsUTF8(self->name) : "objc.function instance"),
                 self->methinfo->deprecated / 100, self->methinfo->deprecated % 100);
        if (PyErr_Warn(PyObjCExc_DeprecationWarning, buf) < 0) {
            return NULL;
        }
    }

    if (unlikely(nargsf != (size_t)Py_SIZE(self->methinfo))) {
        PyErr_Format(PyExc_TypeError,
                     "Need %" PY_FORMAT_SIZE_T "d arguments, got %" PY_FORMAT_SIZE_T "d",
                     Py_SIZE(self->methinfo), nargsf);
        return NULL;
    }
    if (unlikely(PyObjCFFI_ParseArguments_Simple(
                     self->methinfo, 0, args, nargsf,
                     align(PyObjCRT_SizeOfReturnType(self->methinfo->rettype->type),
                           sizeof(void*)),
                     argbuf, sizeof(argbuf), /*arglist,*/ values)
                 == -1)) {

        goto error;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            ffi_call(self->cif, FFI_FN(self->function), argbuf, values);
        } @catch (NSObject* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (unlikely(PyErr_Occurred())) {
        goto error;
    }

    return PyObjCFFI_BuildResult_Simple(self->methinfo, argbuf, NULL, 0);

error:
    return NULL;
}
#endif

#if PY_VERSION_HEX < 0x03090000
static PyObject* _Nullable func_call(PyObject* s, PyObject* _Nullable args,
                                     PyObject* _Nullable kwds)
{
    if (kwds != NULL && (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError, "keyword arguments not supported");
        return NULL;
    }

    return func_vectorcall(s, PyTuple_ITEMS(args), PyTuple_GET_SIZE(args), NULL);
}
#endif

static void
func_dealloc(PyObject* s)
{
    func_object* self = (func_object*)s;

    Py_XDECREF(self->doc);
    Py_XDECREF(self->name);
    Py_XDECREF(self->module);
    Py_XDECREF(self->methinfo);
    if (self->cif != NULL) {
        PyObjCFFI_FreeCIF(self->cif);
    }
    PyObject_Free(s);
}

static PyObject*
func_descr_get(PyObject* self, PyObject* _Nullable obj __attribute__((__unused__)),
               PyObject* _Nullable type __attribute__((__unused__)))
{
    Py_INCREF(self);
    return self;
}

PyTypeObject PyObjCFunc_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.function",
    .tp_basicsize                                  = sizeof(func_object),
    .tp_itemsize                                   = 0,
    .tp_dealloc                                    = func_dealloc,
    .tp_repr                                       = func_repr,
#if PY_VERSION_HEX >= 0x03090000
    .tp_flags             = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_VECTORCALL,
    .tp_vectorcall_offset = offsetof(func_object, vectorcall),
    .tp_call              = PyVectorcall_Call,
#else
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_call  = func_call,
#endif

    .tp_getattro  = PyObject_GenericGetAttr,
    .tp_setattro  = PyObject_GenericSetAttr,
    .tp_doc       = "Wrapper around a Objective-C function",
    .tp_methods   = func_methods,
    .tp_members   = func_members,
    .tp_getset    = func_getset,
    .tp_descr_get = func_descr_get,
};

PyObject* _Nullable PyObjCFunc_WithMethodSignature(PyObject* _Nullable name, void* func,
                                                   PyObjCMethodSignature* methinfo)
{
    func_object* result;

    PyObjC_Assert(!name || PyUnicode_Check(name), NULL);

    result = PyObject_NEW(func_object, &PyObjCFunc_Type);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

#if PY_VERSION_HEX >= 0x03090000
    result->vectorcall = func_vectorcall;
#endif
    result->function = func;
    result->doc      = NULL;
    result->name     = name;
    Py_XINCREF(name);
    result->module   = NULL;
    result->methinfo = methinfo;
    Py_XINCREF(methinfo);

    /* XXX: Set ->cif on first call? */
    ffi_cif* cif = PyObjCFFI_CIFForSignature(result->methinfo);
    if (cif == NULL) {
        Py_DECREF(result);
        return NULL;
    }
    result->cif = cif;

    return (PyObject*)result;
}

PyObject* _Nullable PyObjCFunc_New(PyObject* name, void* func, const char* signature,
                                   PyObject* doc, PyObject* meta)
{
    func_object* result;

    PyObjC_Assert(!name || PyUnicode_Check(name), NULL);
    if (doc && PyUnicode_GetLength(doc) == 0) {
        /* Ignore empty docstring */
        doc = NULL;
    }

    result = PyObject_New(func_object, &PyObjCFunc_Type);
    if (result == NULL) // LCOV_BR_EXCL_LINE
        return NULL;    // LCOV_EXCL_LINE

#if PY_VERSION_HEX >= 0x03090000
    result->vectorcall = func_vectorcall;
#endif
    result->function = func;

    /* set later in this function */
    result->doc    = (PyObject* _Nonnull)NULL;
    result->name   = (PyObject* _Nonnull)NULL;
    result->module = NULL;
    result->cif    = NULL;

    result->methinfo = PyObjCMethodSignature_WithMetaData(signature, meta, NO);
    if (result->methinfo == NULL) {
        Py_DECREF(result);
        return NULL;
    }

#if PY_VERSION_HEX >= 0x03090000
    if (result->methinfo->shortcut_signature) {
        result->vectorcall = func_vectorcall_simple;
    }
#endif

    SET_FIELD_INCREF(result->doc, doc);
    SET_FIELD_INCREF(result->name, name);

    /* XXX: Set ->cif on first call? */
    result->cif = PyObjCFFI_CIFForSignature(result->methinfo);
    if (result->cif == NULL) { // LCOV_BR_EXCL_LINE
        Py_DECREF(result);     // LCOV_EXCL_LINE
        return NULL;           // LCOV_EXCL_LINE
    }

    return (PyObject*)result;
}

PyObjCMethodSignature* _Nullable PyObjCFunc_GetMethodSignature(PyObject* func)
{
    return ((func_object*)func)->methinfo;
}

NS_ASSUME_NONNULL_END
