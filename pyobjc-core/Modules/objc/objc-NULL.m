/*
 * Implementation for objc.NULL
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

PyObject* PyObjC_NULL = NULL;

static PyObject*
obj_repr(PyObject* self __attribute__((__unused__)))
{
    Py_INCREF(PyObjCNM_objc_NULL);
    return PyObjCNM_objc_NULL;
}

PyTypeObject PyObjC_NULL_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.NULL_type",
    .tp_basicsize                                  = sizeof(PyObject),
    .tp_itemsize                                   = 0,
    .tp_repr                                       = obj_repr,
    .tp_flags                                      = Py_TPFLAGS_DEFAULT,
};

PyObject* _Nullable PyObjCInitNULL(void)
{
    PyObject* result;

    if (PyType_Ready(&PyObjC_NULL_Type) == -1) { // LCOV_BR_EXCL_LINE
        return NULL;                             // LCOV_EXCL_LINE
    }

    result = PyObjC_NULL = PyObject_New(PyObject, &PyObjC_NULL_Type);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    Py_XINCREF(PyObjC_NULL);

    return result;
}

NS_ASSUME_NONNULL_END
