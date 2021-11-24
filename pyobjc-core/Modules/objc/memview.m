/*
 * Python object wrapping a Py_buffer
 *
 * This type is not used in pyobjc-core itself, but is used
 * by the Quartz framework bindings.
 *
 * XXX: Add tests in ctests.m
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

struct pyobjc_memview {
    PyObject_HEAD

    Py_buffer view;
};

static PyObject*
obj_repr(PyObject* self __attribute__((__unused__)))
{
    Py_INCREF(PyObjCNM_objc_memview_object);
    return PyObjCNM_objc_memview_object;
}

static void
obj_dealloc(PyObject* self)
{
    /* Users or this type must release the buffer after use */
    /* XXX: Check the users if this is actually done */
    if (((((struct pyobjc_memview*)self))->view).obj != NULL) {
        /* Users of this API must release the buffer, enforce this
         * at runtime.
         *
         * XXX: This matches the implementation of PyBuffer_Release,
         * but setting .obj to NULL is not a documented API invariant!
         */
        PyObjCErr_InternalError();
    }

    PyObject_Free(self);
}

static PyTypeObject PyObjCMemView_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.memview_type",
    .tp_basicsize                                  = sizeof(struct pyobjc_memview),
    .tp_itemsize                                   = 0,
    .tp_repr                                       = obj_repr,
    .tp_dealloc                                    = obj_dealloc,
    .tp_flags                                      = Py_TPFLAGS_DEFAULT,
};

PyObject* _Nullable PyObjCMemView_New(void)
{
    struct pyobjc_memview* result =
        PyObject_New(struct pyobjc_memview, &PyObjCMemView_Type);
    memset(&result->view, 0, sizeof(result->view));
    return (PyObject*)result;
}

int
PyObjCMemView_Check(PyObject* view)
{
    return PyObject_TypeCheck(view, (PyTypeObject*)&PyObjCMemView_Type);
}

Py_buffer* _Nullable PyObjCMemView_GetBuffer(PyObject* object)
{
    if (!PyObjCMemView_Check(object)) {
        PyErr_SetString(PyExc_TypeError, "Expecting a memview object");
        return NULL;
    }

    return &((((struct pyobjc_memview*)object))->view);
}

NS_ASSUME_NONNULL_END
