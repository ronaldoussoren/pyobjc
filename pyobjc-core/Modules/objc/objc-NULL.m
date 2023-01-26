/*
 * Implementation for objc.NULL
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

PyObject* PyObjC_NULL = NULL;

static PyObject*
null_repr(PyObject* self __attribute__((__unused__)))
{
    Py_INCREF(PyObjCNM_objc_NULL);
    return PyObjCNM_objc_NULL;
}

#if PY_VERSION_HEX < 0x030a0000
static PyObject* _Nullable null_new(PyObject* self __attribute__((__unused__)),
                                    PyObject* args __attribute__((__unused__)),
                                    PyObject* kwds __attribute__((__unused__)))
{
    PyErr_SetString(PyExc_TypeError, "cannot create 'objc._NULL_type' instances");
    return NULL;
}
#endif

static PyType_Slot null_slots[] = {
    {.slot = Py_tp_repr, .pfunc = (void*)&null_repr},
#if PY_VERSION_HEX < 0x030a0000
    {.slot = Py_tp_new, .pfunc = (void*)&null_new},
#endif

    {0, NULL} /* sentinel */
};

static PyType_Spec null_spec = {
    .name      = "objc._NULL_type",
    .basicsize = sizeof(PyObject),
    .itemsize  = 0,
#if PY_VERSION_HEX >= 0x030a0000
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
#else
    .flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE,
#endif
    .slots = null_slots,
};

static PyObject* PyObjC_NULL_Type;

int
PyObjCInitNULL(PyObject* module)
{
    PyObjC_NULL_Type = PyType_FromSpec(&null_spec);
    if (PyObjC_NULL_Type == NULL) { // LCOV_BR_EXCL_LINE
        return -1;                  // LCOV_EXCL_LINE
    }

    PyObjC_NULL = PyObject_New(PyObject, (PyTypeObject*)PyObjC_NULL_Type);
    if (PyObjC_NULL == NULL) { // LCOV_BR_EXCL_LINE
        return -1;             // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(module, "NULL", PyObjC_NULL) == -1) { // LCOV_BR_EXCL_LINE
        return -1;                                               // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjC_NULL);

    return 0;
}

NS_ASSUME_NONNULL_END
