/*
 * Wrapper for simple global functions. Simple functions are those without
 * arguments that require additional effort.
 */
#include "pyobjc.h"

typedef struct {
    PyObject_HEAD

    ffi_cif*  cif;
    PyObjCMethodSignature* methinfo;
    void* function;
    PyObject* doc;
    PyObject* name;
    PyObject* module;
} func_object;



static PyObject* func_metadata(PyObject* self)
{
    return PyObjCMethodSignature_AsDict(((func_object*)self)->methinfo);
}

static PyMethodDef func_methods[] = {
    {
        .ml_name    = "__metadata__",
        .ml_meth    = (PyCFunction)func_metadata,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "Return a dict that describes the metadata for this function."
    },
    {
        .ml_name    = NULL  /* SENTINEL */
    }
};

static PyGetSetDef func_getset[] = {
    {
        .name   = "__doc__",
        .get    = PyObjC_callable_docstr_get,
        .doc    = "Documentation for a function",
    },

#if PY_VERSION_HEX >= 0x03030000
    {
        .name   = "__signature__",
        .get    = PyObjC_callable_signature_get,
        .doc    = "inspect.Signature for a function",
    },
#endif /* PY_VERSION_HEX >= 0x03030000 */

    {
        .name   = NULL /* SENTINEL */
    }
};



static PyMemberDef func_members[] = {
    {
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
        .name   = NULL  /* SENTINEL */
    }
};


static PyObject*
func_repr(PyObject* _self)
{
    func_object* self = (func_object*)_self;

    if (self->name == NULL) {
        return PyText_FromFormat("<objc.function object at %p>", self);

#if PY_MAJOR_VERSION == 2
    } else if (PyString_Check(self->name)) {
        return PyString_FromFormat("<objc.function '%s' at %p>", PyString_AsString(self->name), self);
#endif /* PY_MAJOR_VERSION == 2 */


    } else {

#if PY_MAJOR_VERSION == 2
        PyObject* result;
        PyObject* name_repr = PyObject_Repr(self->name);

        if (name_repr == NULL) {
            return NULL;
        }

        if (!PyString_Check(name_repr)) {
            result = PyString_FromFormat("<objc.function object at %p>", self);

        } else {
            result = PyString_FromFormat("<objc.function '%s' at %p>",
                    PyString_AsString(name_repr), self);
        }
        Py_DECREF(name_repr);
        return result;

#else /* PY_MAJOR_VERSION == 3 */
        return PyUnicode_FromFormat("<objc.function %R at %p>", self->name, self);

#endif /* PY_MAJOR_VERSION == 3 */
    }
}


static PyObject*
func_call(PyObject* s, PyObject* args, PyObject* kwds)
{
    func_object* self = (func_object*)s;
    Py_ssize_t byref_in_count;
    Py_ssize_t byref_out_count;
    Py_ssize_t plain_count;
    Py_ssize_t argbuf_len;
    int r;
    Py_ssize_t cif_arg_count;
    BOOL variadicAllArgs = NO;

    unsigned char* argbuf = NULL;
    ffi_type* arglist[MAX_ARGCOUNT];
    void*     values[MAX_ARGCOUNT];
    void*      byref[MAX_ARGCOUNT] = { 0 };
    struct byref_attr byref_attr[MAX_ARGCOUNT] = { {0, 0} };
    ffi_cif cif;
    ffi_cif* cifptr;

    PyObject* retval;

    if (self->methinfo->suggestion != NULL) {
        PyErr_SetObject(PyExc_TypeError, self->methinfo->suggestion);
        return NULL;
    }

    if (Py_SIZE(self->methinfo) >= 63) {
        PyErr_Format(PyObjCExc_Error,
            "wrapping a function with %"PY_FORMAT_SIZE_T"d arguments, at most 64 "
            "are supported", Py_SIZE(self->methinfo));
        return NULL;
    }

    if (kwds != NULL && (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError,
            "keyword arguments not supported");
        return NULL;
    }

    argbuf_len = PyObjCRT_SizeOfReturnType(self->methinfo->rettype->type);
    argbuf_len = align(argbuf_len, sizeof(void*));
    r = PyObjCFFI_CountArguments(
        self->methinfo, 0,
        &byref_in_count, &byref_out_count, &plain_count,
        &argbuf_len, &variadicAllArgs);
    if (r == -1) {
        return NULL;
    }

    variadicAllArgs |= self->methinfo->variadic && (self->methinfo->null_terminated_array || self->methinfo->arrayArg != -1);

    if (variadicAllArgs) {
        if (byref_in_count != 0 || byref_out_count != 0) {
            PyErr_Format(PyExc_TypeError, "Sorry, printf format with by-ref args not supported");
            return NULL;
        }

        if (PyTuple_Size(args) < Py_SIZE(self->methinfo)) {
            PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
            Py_SIZE(self->methinfo) - 2, PyTuple_Size(args));
            return NULL;
        }

    } else if (PyTuple_Size(args) != Py_SIZE(self->methinfo)) {
        PyErr_Format(PyExc_TypeError, "Need %"PY_FORMAT_SIZE_T"d arguments, got %"PY_FORMAT_SIZE_T"d",
            Py_SIZE(self->methinfo), PyTuple_Size(args));
        return NULL;
    }

    argbuf = PyMem_Malloc(argbuf_len);
    if (argbuf == NULL) {
        PyErr_NoMemory();
        return NULL;
    }

    cif_arg_count = PyObjCFFI_ParseArguments(
        self->methinfo, 0, args,
        align(PyObjCRT_SizeOfReturnType(self->methinfo->rettype->type), sizeof(void*)),
        argbuf, argbuf_len, byref, byref_attr, arglist, values);

    if (cif_arg_count == -1) {
        goto error;
    }

    if (variadicAllArgs) {
        r = ffi_prep_cif(&cif, FFI_DEFAULT_ABI, (int)cif_arg_count,
        PyObjCFFI_Typestr2FFI(self->methinfo->rettype->type), arglist);

        if (r != FFI_OK) {
            PyErr_Format(PyExc_RuntimeError,
                "Cannot setup FFI CIF [%d]", r);
                goto error;
        }
        cifptr = &cif;

    } else {
        cifptr = self->cif;
    }

    PyObjC_DURING
        ffi_call(cifptr, FFI_FN(self->function), argbuf, values);

    PyObjC_HANDLER
        PyObjCErr_FromObjC(localException);

    PyObjC_ENDHANDLER

    if (PyErr_Occurred()) {
        goto error;
    }

    retval = PyObjCFFI_BuildResult(self->methinfo, 0, argbuf, byref,
            byref_attr, byref_out_count, NULL, 0, values);

    if (variadicAllArgs) {
        if (PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo)+PyTuple_Size(args), byref, byref_attr) < 0) {
            goto error;
        }

    } else {
        if (PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo), byref, byref_attr) < 0) {
            goto error;
        }
    }

    PyMem_Free(argbuf); argbuf = NULL;
    return retval;

error:
    if (variadicAllArgs) {
        PyObjCFFI_FreeByRef(PyTuple_Size(args), byref, byref_attr);

    } else {
        PyObjCFFI_FreeByRef(Py_SIZE(self->methinfo), byref, byref_attr);
    }

    if (argbuf) {
        PyMem_Free(argbuf);
    }
    return NULL;
}

static void
func_dealloc(PyObject* s)
{
    func_object* self = (func_object*)s;

    Py_CLEAR(self->doc);
    Py_CLEAR(self->name);
    Py_CLEAR(self->module);
    Py_CLEAR(self->methinfo);
    if (self->cif != NULL) {
        PyObjCFFI_FreeCIF(self->cif);
    }
    PyObject_Free(s);
}

static PyObject *
func_descr_get(PyObject *self, PyObject *obj __attribute__((__unused__)), PyObject *type __attribute__((__unused__)))
{
    Py_INCREF(self);
    return self;
}


PyTypeObject PyObjCFunc_Type =
{
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.function",
    .tp_basicsize   = sizeof (func_object),
    .tp_itemsize    = 0,
    .tp_dealloc     = func_dealloc,
    .tp_repr        = func_repr,
    .tp_call        = func_call,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = "Wrapper around a Objective-C function",
    .tp_methods     = func_methods,
    .tp_members     = func_members,
    .tp_getset      = func_getset,
    .tp_descr_get   = func_descr_get,
};

PyObject*
PyObjCFunc_WithMethodSignature(PyObject* name, void* func, PyObjCMethodSignature* methinfo)
{
    func_object* result;

    result = PyObject_NEW(func_object, &PyObjCFunc_Type);
    if (result == NULL) return NULL;

    result->function = func;
    result->doc = NULL;
    result->name = name;
    Py_XINCREF(name);
    result->module = NULL;
    result->methinfo = methinfo;
    Py_XINCREF(methinfo);

    result->cif = PyObjCFFI_CIFForSignature(result->methinfo);
    if (result->cif == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    return (PyObject*)result;
}


PyObject*
PyObjCFunc_New(PyObject* name, void* func, const char* signature, PyObject* doc, PyObject* meta)
{
    func_object* result;

    result = PyObject_NEW(func_object, &PyObjCFunc_Type);
    if (result == NULL) return NULL;

    result->function = NULL;
    result->doc = NULL;
    result->name = NULL;
    result->module = NULL;
    result->cif = NULL;

    result->methinfo= PyObjCMethodSignature_WithMetaData(signature, meta, NO);
    if (result->methinfo == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    result->function = func;

    SET_FIELD_INCREF(result->doc, doc);
    SET_FIELD_INCREF(result->name, name);
    result->cif = PyObjCFFI_CIFForSignature(result->methinfo);
    if (result->cif == NULL) {
        Py_DECREF(result);
        return NULL;
    }

    return (PyObject*)result;
}

PyObjCMethodSignature* PyObjCFunc_GetMethodSignature(PyObject* func)
{
    return ((func_object*)func)->methinfo;
}
