/*
 * Implementation of weakrefs to Cocoa objects.
 *
 * This cannot be accomplished through the weakref
 * module, its implementation can only work for
 * references to Python objects, not to 'foreign'
 * objects.
 *
 * TODO:
 * 1) Ensure the API is only made available when
 *    building on a new enough platform
 *
 * 2) Look into useing MAZeroingWeakRef for older
 *    platforms.
 */
#include "pyobjc.h"

#if PyObjC_BUILD_RELEASE >= 1007


PyDoc_STRVAR(weakref_cls_doc,
"objc.WeakRef(object)\n"
"\n"
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
} PyObjC_WeakRef;


static void
weakref_dealloc(PyObject* object)
{
    PyObjC_WeakRef* self = (PyObjC_WeakRef*)object;

    objc_storeWeak(&self->object, nil);
    Py_TYPE(object)->tp_free(object);
}

static PyObject*
weakref_call(PyObject* object, PyObject* args, PyObject* kwds)
{
static char* keywords[] = { NULL };
    PyObjC_WeakRef* self = (PyObjC_WeakRef*)object;
    NSObject* tmp;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "", keywords)) {
        return NULL;
    }

    tmp = objc_loadWeak(&self->object);
    return pythonify_c_value(@encode(id), &tmp);
}

static PyObject*
weakref_new(PyTypeObject* type __attribute__((__unused__)),
    PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "object", NULL };

    PyObjC_WeakRef* result;
    PyObject* tmp;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O",
            keywords, &tmp)) {
        return NULL;
    }

    if (!PyObjCObject_Check(tmp)) {
        PyErr_Format(PyExc_TypeError, "Excecting a Cocoa object, got instance of '%.100s'",
                Py_TYPE(tmp)->tp_name);
        return NULL;
    }

    if ((PyObjCObject_GetFlags(tmp) & PyObjCObject_kCFOBJECT) != 0) {
        PyErr_Format(PyExc_TypeError,
                "Excecting a Cocoa object, got instance of CoreFoundation type '%.100s'",
                Py_TYPE(tmp)->tp_name);
        return NULL;
    }

    result = (PyObjC_WeakRef*)PyObject_New(PyObjC_WeakRef, &PyObjCWeakRef_Type);
    if (result == NULL) {
        return NULL;
    }

    result->object = nil;
    objc_storeWeak(&result->object, PyObjCObject_GetObject(tmp));

    return (PyObject*)result;
}

PyTypeObject PyObjCWeakRef_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.WeakRef",
    .tp_basicsize   = sizeof(PyObjC_WeakRef),
    .tp_itemsize    = 0,
    .tp_dealloc     = weakref_dealloc,
    .tp_call        = weakref_call,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = weakref_cls_doc,
    .tp_new         = weakref_new,
};

#endif /* PyObjC_BUILD_RELEASE >= 1007 */

