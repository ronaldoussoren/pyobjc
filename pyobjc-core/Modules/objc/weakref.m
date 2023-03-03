/*
 * Implementation of weakrefs to Cocoa objects.
 *
 * This cannot be accomplished through the weakref
 * module, its implementation can only work for
 * references to Python objects, not to 'foreign'
 * objects.
 */
#include "pyobjc.h"

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

static PyObject* PyObjCWeakRef_Type;

static void
weakref_dealloc(PyObject* object)
{
    PyObjC_WeakRef* self = (PyObjC_WeakRef*)object;

    objc_storeWeak(&self->object, nil);
#if PY_VERSION_HEX >= 0x030a0000
    PyTypeObject* tp = Py_TYPE(object);
#endif
    PyObject_Del(object);
#if PY_VERSION_HEX >= 0x030a0000
    Py_DECREF(tp);
#endif
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
                     "Expecting a Cocoa object, got instance of '%.100s'",
                     Py_TYPE(tmp)->tp_name);
        return NULL;
    }

    if ((PyObjCObject_GetFlags(tmp) & PyObjCObject_kCFOBJECT) != 0) {
        PyErr_Format(
            PyExc_TypeError,
            "Expecting a Cocoa object, got instance of CoreFoundation type '%.100s'",
            Py_TYPE(tmp)->tp_name);
        return NULL;
    }

    result =
        (PyObjC_WeakRef*)PyObject_New(PyObjC_WeakRef, (PyTypeObject*)PyObjCWeakRef_Type);
    if (unlikely(result == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;                // LCOV_EXCL_LINE
    }

    result->object = nil;
#if PY_VERSION_HEX >= 0x03090000
    result->vectorcall = weakref_vectorcall;
#endif
    objc_storeWeak(&result->object, PyObjCObject_GetObject(tmp));

    return (PyObject*)result;
}

#if PY_VERSION_HEX >= 0x03090000
static PyMemberDef weakref_members[] = {
    {
        .name   = "__vectorcalloffset__",
        .type   = T_PYSSIZET,
        .offset = offsetof(PyObjC_WeakRef, vectorcall),
        .flags  = READONLY,
    },
    {
        .name = NULL /* SENTINEL */
    }};
#endif

static PyType_Slot weakref_slots[] = {
    {.slot = Py_tp_dealloc, .pfunc = (void*)&weakref_dealloc},
    {.slot = Py_tp_getattro, .pfunc = (void*)&PyObject_GenericGetAttr},
    {.slot = Py_tp_doc, .pfunc = (void*)&weakref_cls_doc},
    {.slot = Py_tp_new, .pfunc = (void*)&weakref_new},
#if PY_VERSION_HEX >= 0x03090000
    {.slot = Py_tp_call, .pfunc = (void*)&PyVectorcall_Call},
    {.slot = Py_tp_members, .pfunc = (void*)&weakref_members},
#else
    {.slot = Py_tp_call, .pfunc = (void*)&weakref_call},
#endif

    {0, NULL} /* sentinel */
};

static PyType_Spec weakref_spec = {
    .name      = "objc.WeakRef",
    .basicsize = sizeof(PyObjC_WeakRef),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_HAVE_VECTORCALL,
#elif PY_VERSION_HEX >= 0x03090000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_HAVE_VECTORCALL,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = weakref_slots,
};

int
PyObjCWeakRef_Setup(PyObject* module)
{
    PyObjCWeakRef_Type = PyType_FromSpec(&weakref_spec);
    if (PyObjCWeakRef_Type == NULL) { // LCOV_BR_EXCL_LINE
        return -1;                    // LCOV_EXCL_LINE
    }

    if ( // LCOV_BR_EXCL_LINE
        PyModule_AddObject(module, "WeakRef", PyObjCWeakRef_Type) == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjCWeakRef_Type);

    return 0;
}

NS_ASSUME_NONNULL_END
