#include "pyobjc.h"

typedef struct {
    PyObject_HEAD

    PyObject* callable;
} PyObjCPythonMethod;


PyObject*
PyObjCPythonMethod_GetMethod(PyObject* value)
{
    if (!PyObjCPythonMethod_Check(value)) {
        PyErr_SetString(PyExc_TypeError, "Expecting a python-method object");
        return NULL;
    }

    return ((PyObjCPythonMethod*)value)->callable;
}

static PyMemberDef meth_members[] = {
    {
        .name   = "callable",
        .type   = T_OBJECT,
        .offset = offsetof(PyObjCPythonMethod, callable),
        .flags  = READONLY,
    },
    {
        .name   = NULL  /* SENTINEL */
    }
};


static PyObject*
meth_new(PyTypeObject* type __attribute__((__unused__)),
        PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "callable", NULL };
    PyObject* callable;
    PyObjCPythonMethod* result;

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &callable)) {
        return NULL;
    }

    result = (PyObjCPythonMethod*)PyObject_New(PyObjCPythonMethod, &PyObjCPythonMethod_Type);
    if (result == NULL) {
        return NULL;
    }
    result->callable = callable;
    Py_INCREF(callable);

    return (PyObject*)result;
}

static PyObject*
meth_descr_get(PyObject* self, PyObject* obj, PyObject* class)
{
    descrgetfunc f;
    PyObject* result;

    result = ((PyObjCPythonMethod*)self)->callable;
    if (unlikely(result == NULL)) {
        PyErr_SetString(PyExc_ValueError, "Empty objc.python-method");
        return NULL;
    }
    f = Py_TYPE(result)->tp_descr_get;
    if (f == NULL) {
        Py_INCREF(result);
    } else {
        result = f(result, obj, class);
    }
    return result;
}

static int
meth_traverse(PyObject* self, visitproc visit, void* arg)
{
    return visit(((PyObjCPythonMethod*)self)->callable, arg);
}

static int
meth_clear(PyObject* self)
{
    Py_CLEAR(((PyObjCPythonMethod*)self)->callable);
    return 0;
}

static void
meth_dealloc(PyObject* self)
{
    meth_clear(self);
    Py_TYPE(self)->tp_free(self);
}

static PyObject*
meth_call(PyObject* self, PyObject* args, PyObject* kwds)
{
    return PyObject_Call(((PyObjCPythonMethod*)self)->callable, args, kwds);
}

PyDoc_STRVAR(meth_doc,
    "objc.python_method(callable)\n"
    CLINIC_SEP
    "\nReturns a descriptor that won't be converted to a selector object \n"
    "and won't be registered with the Objective-C runtime.\n"
    );


PyTypeObject PyObjCPythonMethod_Type = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.python_method",
    .tp_basicsize   = sizeof(PyObjCPythonMethod),
    .tp_itemsize    = 0,
    .tp_dealloc     = meth_dealloc,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_doc         = meth_doc,
    .tp_members     = meth_members,
    .tp_new         = meth_new,
    .tp_descr_get   = meth_descr_get,
    .tp_traverse    = meth_traverse,
    .tp_clear       = meth_clear,
    .tp_call        = meth_call,
};
