/*
 * Implementation of weakrefs to Cocoa objects.
 *
 * This cannot be accomplished through the weakref
 * module, its implementation can only work for
 * references to Python objects, not to 'foreign'
 * objects.
 */
#include "pyobjc.h"

#if PyObjC_BUILD_RELEASE >= 1007

NS_ASSUME_NONNULL_BEGIN

PyDoc_STRVAR(weakref_cls_doc,
             "objc.WeakRef(object)\n" CLINIC_SEP "\n"
             "Create zeroing weak reference to a Cocoa object.\n"
             "Raises `ValueError` when *object* is not a Cocoa \n"
             "object.\n"
             "\n"
             "NOTE: Some Cocoa classes do not support weak references, \n"
             "      and creating them anyway can be a fatal error, see \n"
             "      Apple's documentation for more information.\n"
             "");

typedef struct {
    PyObject_HEAD

    NSObject* _Nullable object;
#if PY_VERSION_HEX >= 0x03090000
    vectorcallfunc vectorcall;
#endif
} PyObjC_WeakRef;

static void
weakref_dealloc(PyObject* object)
{
    PyObjC_WeakRef* self = (PyObjC_WeakRef*)object;

    objc_storeWeak(&self->object, nil);
    Py_TYPE(object)->tp_free(object);
}

static PyObject* _Nullable weakref_vectorcall(PyObject* object,
                                              PyObject* const* _Nullable args
                                              __attribute__((__unused__)),
                                              size_t nargsf, PyObject* _Nullable kwnames)
{
    PyObjC_WeakRef* self = (PyObjC_WeakRef*)object;
    NSObject*       tmp;

    if (PyObjC_CheckNoKwnames(object, kwnames) == -1) {
        return NULL;
    }

    if (PyObjC_CheckArgCount(object, 0, 0, nargsf) == -1) {
        return NULL;
    }

    tmp = objc_loadWeak(&self->object);
    return id_to_python(tmp);
}

#if PY_VERSION_HEX < 0x03090000

static PyObject* _Nullable weakref_call(PyObject* s, PyObject* _Nullable args,
                                        PyObject* _Nullable kwds)
{
    if (kwds != NULL && (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError, "keyword arguments not supported");
        return NULL;
    }

    return weakref_vectorcall(s, PyTuple_ITEMS(args), PyTuple_GET_SIZE(args), NULL);
}

#endif /* PY_VERSION_HEX < 0x03090000 */

/* XXX: vectorcall variant for weakref_new? */
static PyObject* _Nullable weakref_new(PyTypeObject* type __attribute__((__unused__)),
                                       PyObject* _Nullable args, PyObject* _Nullable kwds)
{
    static char* keywords[] = {"object", NULL};

    PyObjC_WeakRef* result;
    PyObject*       tmp;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &tmp)) {
        return NULL;
    }

    if (!PyObjCObject_Check(tmp)) {
        PyErr_Format(PyExc_TypeError,
                     "Executing a Cocoa object, got instance of '%.100s'",
                     Py_TYPE(tmp)->tp_name);
        return NULL;
    }

    if ((PyObjCObject_GetFlags(tmp) & PyObjCObject_kCFOBJECT) != 0) {
        PyErr_Format(
            PyExc_TypeError,
            "Executing a Cocoa object, got instance of CoreFoundation type '%.100s'",
            Py_TYPE(tmp)->tp_name);
        return NULL;
    }

    result = (PyObjC_WeakRef*)PyObject_New(PyObjC_WeakRef, &PyObjCWeakRef_Type);
    if (result == NULL) {
        return NULL;
    }

    result->object = nil;
#if PY_VERSION_HEX >= 0x03090000
    result->vectorcall = weakref_vectorcall;
#endif
    objc_storeWeak(&result->object, PyObjCObject_GetObject(tmp));

    return (PyObject*)result;
}

PyTypeObject PyObjCWeakRef_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.WeakRef",
    .tp_basicsize                                  = sizeof(PyObjC_WeakRef),
    .tp_itemsize                                   = 0,
    .tp_dealloc                                    = weakref_dealloc,
#if PY_VERSION_HEX >= 0x03090000
    .tp_flags             = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_VECTORCALL,
    .tp_vectorcall_offset = offsetof(PyObjC_WeakRef, vectorcall),
    .tp_call              = PyVectorcall_Call,
#else
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_call  = weakref_call,
#endif
    .tp_getattro = PyObject_GenericGetAttr,
    .tp_doc      = weakref_cls_doc,
    .tp_new      = weakref_new,
};

NS_ASSUME_NONNULL_END

#endif /* PyObjC_BUILD_RELEASE >= 1007 */
