/*
 * Python object wrapping a Py_buffer
 *
 * This type is not used in pyobjc-core itself, but is used
 * by the Quartz framework bindings.
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

struct pyobjc_memview {
    PyObject_HEAD

    Py_buffer view;
};

static PyObject* PyObjCMemView_Type;

static PyObject*
memview_repr(PyObject* self __attribute__((__unused__)))
{
    Py_INCREF(PyObjCNM_objc_memview_object);
    return PyObjCNM_objc_memview_object;
}

static void
memview_dealloc(PyObject* self)
{
    /* Users or this type must release the buffer after use */

#ifdef PyObjC_DEBUG
    /* Users of this API must release the buffer, enforce this
     * at runtime.
     *
     * This code is only active in debug builds because the check
     * above is not a documented API invariant for PyBuffer_Release
     * (but does match the behaviour of that function).
     */
    assert(((((struct pyobjc_memview*)self))->view).obj == NULL);
#endif

    PyTypeObject* tp = Py_TYPE(self);
    PyObject_Free(self);
    Py_DECREF(tp);
}

static PyType_Slot memview_slots[] = {
    {.slot = Py_tp_repr, .pfunc = (void*)&memview_repr},
    {.slot = Py_tp_dealloc, .pfunc = (void*)&memview_dealloc},
    {0, NULL} /* sentinel */
};

static PyType_Spec memview_spec = {
    .name      = "objc._memview_type",
    .basicsize = sizeof(struct pyobjc_memview),
    .itemsize  = 0,
    .flags     = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HEAPTYPE | Py_TPFLAGS_IMMUTABLETYPE
             | Py_TPFLAGS_DISALLOW_INSTANTIATION,
    .slots = memview_slots,
};

PyObject* _Nullable PyObjCMemView_New(void)
{
    struct pyobjc_memview* result =
        PyObject_New(struct pyobjc_memview, (PyTypeObject*)PyObjCMemView_Type);
    if (unlikely(result == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;                // LCOV_EXCL_LINE
    }
    memset(&result->view, 0, sizeof(result->view));
    return (PyObject*)result;
}

int
PyObjCMemView_Check(PyObject* view)
{
    return PyObject_TypeCheck(view, (PyTypeObject*)PyObjCMemView_Type);
}

Py_buffer* _Nullable PyObjCMemView_GetBuffer(PyObject* object)
{
    if (!PyObjCMemView_Check(object)) {
        PyErr_SetString(PyExc_TypeError, "Expecting a memview object");
        return NULL;
    }

    return &((((struct pyobjc_memview*)object))->view);
}

int
PyObjCMemView_Setup(PyObject* module __attribute__((__unused__)))
{
    PyObjCMemView_Type = PyType_FromSpec(&memview_spec);
    if (unlikely(PyObjCMemView_Type == NULL)) { // LCOV_BR_EXCL_LINE
        return -1;                              // LCOV_EXCL_LINE
    }

    return 0;
}

NS_ASSUME_NONNULL_END
