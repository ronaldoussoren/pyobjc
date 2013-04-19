/*
 * A custom wrapper for the (opaque) FSRef structure.
 */
#include "pyobjc.h"
#import <CoreServices/CoreServices.h>

#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#pragma clang diagnostic ignored "-Wdeprecated-declarations"


#if USE_TOOLBOX_OBJECT_GLUE
#include "pymactoolbox.h"
#endif

/*
 * Interface of the FSRef type:
 *
 * FSRef.from_pathname(value)
 *   # -> returns new FSRef instance for posix path 'value'
 *
 * aref.as_pathname()
 *  # -> returns a Unicode string with the posix path
 *
 * aref.as_carbon()
 *  # -> return a Carbon.File.FSRef instance (only
 *  #    available when Carbon support is enabled in Python)
 *
 * aref.data
 *  # -> read-only property with the bytes in the FSRef
 *
 * This is more or less the same interface as Carbon.File.FSRef, but
 * excluding API wrappers.
 */

typedef struct {
    PyObject_HEAD

    FSRef    ref;
} PyObjC_FSRefObject;

static PyObject*
fsref_as_bytes(PyObject* ref, void* closure __attribute__((__unused__)))
{
    if (!PyObjC_FSRefCheck(ref)) {
        PyErr_SetString(PyExc_TypeError, "self is not a FSRef");
    }

    return PyBytes_FromStringAndSize(
        (char*)&((PyObjC_FSRefObject*)ref)->ref,
        sizeof(FSRef));
}

static PyObject*
fsref_sizeof(PyObject* ref)
{
    return PyLong_FromSsize_t(Py_TYPE(ref)->tp_basicsize);
}

#if USE_TOOLBOX_OBJECT_GLUE
static PyObject*
fsref_as_carbon(PyObject* ref)
{
    if (!PyObjC_FSRefCheck(ref)) {
        PyErr_SetString(PyExc_TypeError, "self is not a FSRef");
    }

    return PyMac_BuildFSRef((&((PyObjC_FSRefObject*)ref)->ref));
}
#endif /* USE_TOOLBOX_OBJECT_GLUE */

static PyObject*
fsref_as_path(PyObject* ref)
{
    OSStatus rc;
    UInt8 buffer[1024];

    if (!PyObjC_FSRefCheck(ref)) {
        PyErr_SetString(PyExc_TypeError, "self is not a FSRef");
    }

    rc = FSRefMakePath( &((PyObjC_FSRefObject*)ref)->ref,
            buffer, sizeof(buffer));
    if (rc != 0) {
#if (PY_MAJOR_VERSION == 2) && defined (USE_TOOLBOX_OBJECT_GLUE)
        PyMac_Error(rc);

#else /* (PY_MAJOR_VERSION == 3) || !defined (USE_TOOLBOX_OBJECT_GLUE) */
        PyErr_Format(PyExc_OSError, "MAC Error %d", rc);

#endif /* (PY_MAJOR_VERSION == 3) || !defined (USE_TOOLBOX_OBJECT_GLUE) */
        return NULL;
    }

    return PyUnicode_DecodeUTF8((char*)buffer,
            strlen((char*)buffer), NULL);
}


static PyObject*
fsref_from_path(PyObject* self __attribute__((__unused__)), PyObject* path)
{
    PyObject* value;
    FSRef result;
    Boolean isDirectory;
    OSStatus rc;

    if (PyUnicode_Check(path)) {
        value = PyUnicode_AsEncodedString(path, NULL, NULL);

#if PY_MAJOR_VERSION == 2
    } else if(PyString_Check(path)) {
        value = path; Py_INCREF(path);
#endif /* PY_MAJOR_VERSION == 2 */

    } else {
        PyErr_SetString(PyExc_TypeError, "Expecting string");
        return NULL;
    }

    if (value == NULL) return NULL;

    rc = FSPathMakeRef((UInt8*)PyBytes_AsString(value), &result, &isDirectory);
    Py_DECREF(value);
    if (rc != 0) {

#if (PY_MAJOR_VERSION == 2) && defined(USE_TOOLBOX_OBJECT_GLUE)
        PyMac_Error(rc);

#else /* (PY_MAJOR_VERSION == 3) || !defined(USE_TOOLBOX_OBJECT_GLUE) */
        PyErr_Format(PyExc_OSError, "MAC Error %d", rc);

#endif /* (PY_MAJOR_VERSION == 3) || !defined(USE_TOOLBOX_OBJECT_GLUE) */

        return NULL;
    }

    return PyObjC_decode_fsref(&result);
}

static PyGetSetDef fsref_getset[] = {
    {
        .name   = "data",
        .get    = fsref_as_bytes,
        .doc    = "bytes in the FSRef",
    },
    {
        .name   = NULL /* SENTINEL */
    }
};


static PyMethodDef fsref_methods[] = {
    {
        .ml_name    = "as_pathname",
        .ml_meth    = (PyCFunction)fsref_as_path,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "return POSIX path for this object (Unicode string)"
    },
    {
        .ml_name    = "from_pathname",
        .ml_meth    = (PyCFunction)fsref_from_path,
        .ml_flags   = METH_O|METH_CLASS,
        .ml_doc     = "create FSRef instance for an POSIX path"
    },

#if USE_TOOLBOX_OBJECT_GLUE
    {
        .ml_name    = "as_carbon",
        .ml_meth    = (PyCFunction)fsref_as_carbon,
        .ml_flags   = METH_NOARGS,
        .ml_doc     = "return Carbon.File.FSRef instance for this object"
    },
#endif /* USE_TOOLBOX_OBJECT_GLUE */

    {
        .ml_name    = "__sizeof__",
        .ml_meth    = (PyCFunction)fsref_sizeof,
        .ml_flags   = METH_NOARGS,
    },
    {
        .ml_name    = NULL /* SENTINEL */
    }
};


PyTypeObject PyObjC_FSRefType = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0)
    .tp_name        = "objc.FSRef",
    .tp_basicsize   = sizeof(PyObjC_FSRefObject),
    .tp_itemsize    = 0,
    .tp_getattro    = PyObject_GenericGetAttr,
    .tp_setattro    = PyObject_GenericSetAttr,
    .tp_flags       = Py_TPFLAGS_DEFAULT,
    .tp_methods     = fsref_methods,
    .tp_getset      = fsref_getset,
};


int
PyObjC_encode_fsref(PyObject* value, void* buffer)
{
#if USE_TOOLBOX_OBJECT_GLUE
    /* We cannot test if 'arg' is an instance of Carbon.File.FSRef... */
    if (PyMac_GetFSRef(value, (FSRef*)buffer) == 1) {
        return 0;
    }
    PyErr_Clear();

#endif /* USE_TOOLBOX_OBJECT_GLUE */

    if (PyObjC_FSRefCheck(value)) {
        *(FSRef*)buffer = ((PyObjC_FSRefObject*)value)->ref;
        return 0;
    }

    PyErr_SetString(PyExc_ValueError, "Cannot convert value to FSRef");
    return -1;
}


PyObject*
PyObjC_decode_fsref(void* buffer)
{
    PyObjC_FSRefObject* result = PyObject_New(
            PyObjC_FSRefObject, &PyObjC_FSRefType);

    if (result == NULL) {
        return NULL;
    }
    result->ref = *(FSRef*)buffer;
    return (PyObject*)result;
}
