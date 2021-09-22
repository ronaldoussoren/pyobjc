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

PyDoc_STRVAR(weakref_cls_doc,
             "objc.WeakRef(object)\n" CLINIC_SEP "\n"
             "Create zeroing weak reference to a Cocoa object.\n"
             "Raises `VAlueError` when *object* is not a Cocoa \n"
             "object.\n"
             "\n"
             "NOTE: Some Cocoa classes do not support weak references, \n"
             "      and creating them anyway can be a fatal error, see \n"
             "      Apple's documentation for more information.\n"
             "");

typedef struct {
    PyObject_HEAD

    NSObject* object;
#if PY_VERSION_HEX >= 0x03090000
    vectorcallfunc         vectorcall;
#endif
} PyObjC_WeakRef;

static void
weakref_dealloc(PyObject* object)
{
    PyObjC_WeakRef* self = (PyObjC_WeakRef*)object;

    objc_storeWeak(&self->object, nil);
    Py_TYPE(object)->tp_free(object);
}

static PyObject*
weakref_vectorcall(PyObject* object, PyObject*const* args __attribute__((__unused__)), size_t nargsf, PyObject* kwnames)
{
    PyObjC_WeakRef* self       = (PyObjC_WeakRef*)object;
    NSObject*       tmp;

    if (PyObjC_CheckNoKwnames(object, kwnames) == -1) {
        return NULL;
    }

    if (PyObjC_CheckArgCount(object, 0, 0, nargsf) == -1) {
        return NULL;
    }

    tmp = objc_loadWeak(&self->object);
    return pythonify_c_value(@encode(id), &tmp);
}

static PyObject*
weakref_call(PyObject* s, PyObject* args, PyObject* kwds)
{
    if (kwds != NULL && (!PyDict_Check(kwds) || PyDict_Size(kwds) != 0)) {
        PyErr_SetString(PyExc_TypeError, "keyword arguments not supported");
        return NULL;
    }

    return weakref_vectorcall(s, PyTuple_ITEMS(args), PyTuple_GET_SIZE(args), NULL);
}


static PyObject*
weakref_new(PyTypeObject* type __attribute__((__unused__)), PyObject* args,
            PyObject* kwds)
{
    static char* keywords[] = {"object", NULL};

    PyObjC_WeakRef* result;
    PyObject*       tmp;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &tmp)) {
        return NULL;
    }

    if (!PyObjCObject_Check(tmp)) {
        PyErr_Format(PyExc_TypeError,
                     "Excecting a Cocoa object, got instance of '%.100s'",
                     Py_TYPE(tmp)->tp_name);
        return NULL;
    }

    if ((PyObjCObject_GetFlags(tmp) & PyObjCObject_kCFOBJECT) != 0) {
        PyErr_Format(
            PyExc_TypeError,
            "Excecting a Cocoa object, got instance of CoreFoundation type '%.100s'",
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
    .tp_call                                       = weakref_call,
#if PY_VERSION_HEX >= 0x03090000
    .tp_flags                                      = Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VECTORCALL,
    .tp_vectorcall_offset                          = offsetof(PyObjC_WeakRef, vectorcall),
#else
    .tp_flags                                      = Py_TPFLAGS_DEFAULT,
#endif
    .tp_getattro                                   = PyObject_GenericGetAttr,
    .tp_doc                                        = weakref_cls_doc,
    .tp_new                                        = weakref_new,
};

#endif /* PyObjC_BUILD_RELEASE >= 1007 */
