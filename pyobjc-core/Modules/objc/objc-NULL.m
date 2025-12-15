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

static PyType_Slot null_slots[] = {
    {.slot = Py_tp_repr, .pfunc = (void*)&null_repr}, {0, NULL} /* sentinel */
};

static PyType_Spec null_spec = {
    .name      = "objc._NULL_type",
    .basicsize = sizeof(PyObject),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
    .slots = null_slots,
};

static PyObject* PyObjC_NULL_Type;

int
PyObjCInitNULL(PyObject* module)
{
    PyObjC_NULL_Type = PyType_FromSpec(&null_spec);
    if (unlikely(PyObjC_NULL_Type == NULL)) { // LCOV_BR_EXCL_LINE
        return -1;                            // LCOV_EXCL_LINE
    }

    PyObjC_NULL = PyObject_New(PyObject, (PyTypeObject*)PyObjC_NULL_Type);
    if (unlikely(PyObjC_NULL == NULL)) { // LCOV_BR_EXCL_LINE
        return -1;                       // LCOV_EXCL_LINE
    }

    if (unlikely(PyModule_AddObject(module, "NULL", PyObjC_NULL)
                 == -1)) { // LCOV_BR_EXCL_LINE
        return -1;         // LCOV_EXCL_LINE
    }
    Py_INCREF(PyObjC_NULL);

    return 0;
}

NS_ASSUME_NONNULL_END
