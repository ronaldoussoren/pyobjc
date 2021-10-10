/*
 * A custom wrapper for the (opaque) FSSpec structure.
 */
#include "pyobjc.h"
#import <CoreServices/CoreServices.h>

NS_ASSUME_NONNULL_BEGIN

/*
 * Interface of the FSSpec type:
 *
 * aspec.as_carbon()
 *  # -> return a Carbon.File.FSSpec instance (only
 *  #    available when Carbon support is enabled in Python)
 *
 * aspec.data
 *  # -> read-only property with the bytes in the FSSpec
 */

typedef struct {
    PyObject_HEAD

    FSSpec ref;
} PyObjC_FSSpecObject;

static PyObject* _Nullable fsspec_as_bytes(PyObject* ref, void* _Nullable closure
                                           __attribute__((__unused__)))
{
    if (!PyObjC_FSSpecCheck(ref)) {
        PyErr_SetString(PyExc_TypeError, "self is not a FSSpec");
    }

    return PyBytes_FromStringAndSize((char*)&((PyObjC_FSSpecObject*)ref)->ref,
                                     sizeof(FSSpec));
}

static PyObject* _Nullable fsspec_sizeof(PyObject* ref)
{
    return PyLong_FromSsize_t(Py_TYPE(ref)->tp_basicsize);
}

static PyGetSetDef fsspec_getset[] = {{
                                          .name = "data",
                                          .get  = fsspec_as_bytes,
                                          .doc  = "bytes in the FSSpec",
                                      },
                                      {
                                          .name = NULL /* SENTINEL */
                                      }};

static PyMethodDef fsspec_methods[] = {{
                                           .ml_name  = "__sizeof__",
                                           .ml_meth  = (PyCFunction)fsspec_sizeof,
                                           .ml_flags = METH_NOARGS,
                                       },
                                       {
                                           .ml_name = NULL /* SENTINEL */
                                       }};

PyTypeObject PyObjC_FSSpecType = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.FSSpec",
    .tp_basicsize                                  = sizeof(PyObjC_FSSpecObject),
    .tp_itemsize                                   = 0,
    .tp_getattro                                   = PyObject_GenericGetAttr,
    .tp_setattro                                   = PyObject_GenericSetAttr,
    .tp_flags                                      = Py_TPFLAGS_DEFAULT,
    .tp_methods                                    = fsspec_methods,
    .tp_getset                                     = fsspec_getset,
};

int
PyObjC_encode_fsspec(PyObject* value, void* buffer)
{
    if (PyObjC_FSSpecCheck(value)) {
        *(FSSpec*)buffer = ((PyObjC_FSSpecObject*)value)->ref;
        return 0;
    }

    PyErr_SetString(PyExc_ValueError, "Cannot convert value to FSSpec");
    return -1;
}

PyObject* _Nullable PyObjC_decode_fsspec(void* buffer)
{
    PyObjC_FSSpecObject* result = PyObject_New(PyObjC_FSSpecObject, &PyObjC_FSSpecType);

    if (result == NULL) {
        return NULL;
    }

    result->ref = *(FSSpec*)buffer;
    return (PyObject*)result;
}

NS_ASSUME_NONNULL_END
