/*
 * A custom wrapper for the (opaque) FSSpec structure.
 */
#include "pyobjc.h"
#import <CoreServices/CoreServices.h>

#if USE_TOOLBOX_OBJECT_GLUE
  /* As of the 10.12 SDK it is no longer safe to inlcude pymactoolbox.h
   * (due to an include that can no longer be resolved). Therefore provide
   * local declarations.
   */

  /* #include "pymactoolbox.h" */

extern PyObject *PyMac_Error(OSErr);                   /* Uses PyMac_GetOSErrException */
extern int PyMac_GetFSSpec(PyObject *, FSSpec *);      /* argument parser for FSSpec */
extern PyObject *PyMac_BuildFSSpec(FSSpec *);          /* Convert FSSpec to PyObject */

#endif

/*
 * Interface of the FSSpec type:
 *
 * FSSpec.from_pathname(value)
 *   # -> returns new FSSpec instance for posix path 'value'
 *
 * aspec.as_pathname()
 *  # -> returns a Unicode string with the posix path
 *
 * aspec.as_carbon()
 *  # -> return a Carbon.File.FSSpec instance (only
 *  #    available when Carbon support is enabled in Python)
 *
 * aspec.data
 *  # -> read-only property with the bytes in the FSSpec
 *
 * This is more or less the same interface as Carbon.File.FSSpec, but
 * excluding API wrappers.
 */

typedef struct {
    PyObject_HEAD

    FSSpec ref;
} PyObjC_FSSpecObject;

static PyObject* fsspec_as_bytes(PyObject* ref, void* closure __attribute__((__unused__)))
{
    if (!PyObjC_FSSpecCheck(ref)) {
        PyErr_SetString(PyExc_TypeError, "self is not a FSSpec");
    }

    return PyBytes_FromStringAndSize(
            (char*)&((PyObjC_FSSpecObject*)ref)->ref,
            sizeof(FSSpec));
}

static PyObject* fsspec_sizeof(PyObject* ref)
{
    return PyLong_FromSsize_t(Py_TYPE(ref)->tp_basicsize);
}

#if defined(USE_TOOLBOX_OBJECT_GLUE) && !defined(__LP64__)
static PyObject* fsspec_as_carbon(PyObject* ref)
{
    if (!PyObjC_FSSpecCheck(ref)) {
        PyErr_SetString(PyExc_TypeError, "self is not a FSSpec");
    }

    return PyMac_BuildFSSpec((&((PyObjC_FSSpecObject*)ref)->ref));
}
#endif /* defined(USE_TOOLBOX_OBJECT_GLUE) && !defined(__LP64__) */

static PyGetSetDef fsspec_getset[] = {
    {
        .name   = "data",
        .get    = fsspec_as_bytes,
        .doc    = "bytes in the FSSpec",
    },
    {
        .name   = NULL /* SENTINEL */
    }
};


static PyMethodDef fsspec_methods[] = {
#if defined(USE_TOOLBOX_OBJECT_GLUE) && !defined(__LP64__)
    {
        .ml_name    = "as_carbon",
        .ml_meth    = (PyCFunction)fsspec_as_carbon,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "as_carbon()\n" CLINIC_SEP "\nReturn Carbon.File.FSSpec instance for this object"
    },
#endif /* defined(USE_TOOLBOX_OBJECT_GLUE) && !defined(__LP64__) */
    {
        .ml_name    = "__sizeof__",
        .ml_meth    = (PyCFunction)fsspec_sizeof,
        .ml_flags   = METH_NOARGS,
    },
    {
        .ml_name    = NULL /* SENTINEL */
    }
};


PyTypeObject PyObjC_FSSpecType = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.FSSpec",
    .tp_basicsize   = sizeof(PyObjC_FSSpecObject),
    .tp_itemsize    = 0,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_setattro    = PyObject_GenericSetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_methods     = fsspec_methods,
    .tp_getset      = fsspec_getset,
};


int PyObjC_encode_fsspec(PyObject* value, void* buffer)
{
#if defined(USE_TOOLBOX_OBJECT_GLUE) && !defined(__LP64__)
    /* We cannot test if 'arg' is an instance of Carbon.File.FSSpec... */
    if (PyMac_GetFSSpec(value, (FSSpec*)buffer) == 1) {
        return 0;
    }
    PyErr_Clear();
#endif /* defined(USE_TOOLBOX_OBJECT_GLUE) && !defined(__LP64__) */

    if (PyObjC_FSSpecCheck(value)) {
        *(FSSpec*)buffer = ((PyObjC_FSSpecObject*)value)->ref;
        return 0;
    }

    PyErr_SetString(PyExc_ValueError, "Cannot convert value to FSSpec");
    return -1;
}


PyObject* PyObjC_decode_fsspec(void* buffer)
{
    PyObjC_FSSpecObject* result = PyObject_New(
            PyObjC_FSSpecObject, &PyObjC_FSSpecType);

    if (result == NULL) {
        return NULL;
    }

    result->ref = *(FSSpec*)buffer;
    return (PyObject*)result;
}
