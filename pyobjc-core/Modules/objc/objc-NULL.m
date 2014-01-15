/*
 * Implementation for objc.NULL
 */
#include "pyobjc.h"

PyObject* PyObjC_NULL = NULL;

static PyObject*
obj_repr(PyObject* self __attribute__((__unused__)))
{
    return PyText_FromString("objc.NULL");
}

PyTypeObject PyObjC_NULL_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.NULL_type",
    .tp_basicsize   = sizeof(PyObject),
    .tp_itemsize    = 0,
    .tp_repr        = obj_repr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
};

PyObject* PyObjCInitNULL(void)
{
    PyObject* result;

    result = PyObjC_NULL = PyObject_New(PyObject, &PyObjC_NULL_Type);
    Py_XINCREF(PyObjC_NULL);

    return result;
}
