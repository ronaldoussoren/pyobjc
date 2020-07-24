#include "pyobjc.h"

struct pyobjc_memview {
    PyObject_HEAD

    Py_buffer view;
};

static PyObject*
obj_repr(PyObject* self __attribute__((__unused__)))
{
    return PyUnicode_FromString("objc.memview object");
}

static void
obj_dealloc(PyObject* self)
{
    PyObject_Free(self);
}



static PyTypeObject PyObjCMemView_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name                                       = "objc.memview_type",
    .tp_basicsize                                  = sizeof(struct pyobjc_memview),
    .tp_itemsize                                   = 0,
    .tp_repr                                       = obj_repr,
    .tp_dealloc                                    = obj_dealloc,
    .tp_flags                                      = Py_TPFLAGS_DEFAULT,
};

PyObject* PyObjCMemView_New(void)
{
	struct pyobjc_memview* result = PyObject_New(struct pyobjc_memview, &PyObjCMemView_Type);
        memset(&result->view, 0, sizeof(result->view));
        return (PyObject*)result;
}

int       PyObjCMemView_Check(PyObject* view)
{
    return PyObject_TypeCheck(view, (PyTypeObject*)&PyObjCMemView_Type);
}

Py_buffer* PyObjCMemView_GetBuffer(PyObject* object)
{
    if (!PyObjCMemView_Check(object)) {
        PyErr_SetString(PyExc_TypeError, "Expecting a memview object");
        return NULL;
    }

    return &((((struct pyobjc_memview*)object))->view);
}
