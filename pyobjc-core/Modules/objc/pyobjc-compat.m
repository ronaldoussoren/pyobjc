#include "pyobjc.h"

int
PyObjC_Cmp(PyObject* o1, PyObject* o2, int* result)
{
    int r;

    r = PyObject_RichCompareBool(o1, o2, Py_EQ);
    if (r == -1) {
        return -1;
    } else if (r == 1) {
        *result = 0;
        return 0;
    }

    r = PyObject_RichCompareBool(o1, o2, Py_LT);
    if (r == -1) {
        return -1;
    } else if (r == 1) {
        *result = -1;
        return 0;
    }

    r = PyObject_RichCompareBool(o1, o2, Py_GT);
    if (r == -1) {
        return 1;
    } else if (r == 1) {
        *result = 1;
        return 0;
    }

    PyErr_Format(PyExc_TypeError, "%R and %R cannot be compared", o1, o2);
    return -1;
}

static PyObject* registry = NULL;

PyObject*
PyBytes_InternFromString(const char* v)
{
    PyObject* key;
    PyObject* value;

    if (registry == NULL) {
        registry = PyDict_New();
        if (registry == NULL) {
            return NULL;
        }
    }

    key = PyBytes_FromString(v);
    if (key == NULL) {
        return NULL;
    }
    value = PyDict_GetItemWithError(registry, key);
    if (value == NULL && PyErr_Occurred()) {
        Py_DECREF(key);
        return NULL;
    } else if (value == NULL) {
        int r = PyDict_SetItem(registry, key, key);
        if (r == -1) {
            Py_DECREF(key);
            return NULL;
        } else {
            return key;
        }
    } else {
        Py_DECREF(key);
        Py_INCREF(value);
        return value;
    }
}

PyObject*
PyBytes_InternFromStringAndSize(const char* v, Py_ssize_t l)
{
    PyObject* key;
    PyObject* value;

    if (registry == NULL) {
        registry = PyDict_New();
        if (registry == NULL) {
            return NULL;
        }
    }

    key = PyBytes_FromStringAndSize(v, l);
    if (key == NULL) {
        return NULL;
    }

    value = PyDict_GetItemWithError(registry, key);
    if (value == NULL && PyErr_Occurred()) {
        Py_DECREF(key);
        return NULL;
    } else if (value == NULL) {
        int r = PyDict_SetItem(registry, key, key);
        if (r == -1) {
            Py_DECREF(key);
            return NULL;
        } else {
            return key;
        }
    } else {
        Py_DECREF(key);
        Py_INCREF(value);
        return value;
    }
}

const char*
PyObjC_Unicode_Fast_Bytes(PyObject* object)
{
    if (!PyUnicode_Check(object)) {
        PyErr_SetString(PyExc_UnicodeDecodeError, "Not a unicode object");
        return NULL;
    }
    if (!PyUnicode_IS_ASCII(object)) {
        PyErr_SetString(PyExc_UnicodeDecodeError, "Not an ASCII string");
        return NULL;
    }
    return (const char*)(PyUnicode_DATA(object));
}

#if PY_VERSION_HEX < 0x03090000
/*
 * Internal compatibility stubs for some parts of the vectorcall API.
 *
 * This implementation does not support keyword names, ass that both
 * complicates the implementation and is not necessary for PyObjC.
 */

PyObject*
PyObject_Vectorcall(PyObject* callable, PyObject*const* args, size_t nargsf, PyObject* kwnames)
{
    size_t i;
    if (kwnames != NULL) {
        PyErr_SetString(PyExc_RuntimeError, "PyObjC's vectorcall compat does not support keyword arguments");
        return NULL;
    }

    PyObject* tuple = PyTuple_New(PyVectorcall_NARGS(nargsf));
    if (tuple == NULL) {
        return NULL;
    }

    for (i = 0; i < PyVectorcall_NARGS(nargsf); i++) {
        if (args[i] == NULL) {
            PyErr_SetString(PyExc_RuntimeError, "NULL argument");
            Py_DECREF(tuple);
            return NULL;
        }
        PyTuple_SET_ITEM(tuple, i, args[i]);
        Py_INCREF(args[i]);
    }

    PyObject* res = PyObject_CallObject(callable, tuple);
    Py_DECREF(tuple);
    return res;
}

PyObject*
PyObject_VectorcallMethod(PyObject *name, PyObject *const *args, size_t nargsf, PyObject *kwnames)
{
    size_t i;
    if (kwnames != NULL) {
        PyErr_SetString(PyExc_RuntimeError, "PyObjC's vectorcall compat does not support keyword arguments");
        return NULL;
    }
    if (name == NULL) {
        PyObjC_Assert(PyErr_Occurred(), NULL);
        return NULL;
    }
    if (PyVectorcall_NARGS(nargsf) == 0) {
        PyErr_SetString(PyExc_ValueError, "Missing first argument");
        return NULL;
    }

    PyObject* callable = PyObject_GetAttr(args[0], name);
    if (callable == NULL) {
        return NULL;
    }

    if (PyVectorcall_NARGS(nargsf) == 1) {
        PyObject* res = PyObject_CallFunction(callable, NULL);
        Py_DECREF(callable);
        return res;
    }

    PyObject* tuple = PyTuple_New(PyVectorcall_NARGS(nargsf)-1);
    if (tuple == NULL) {
        return NULL;
    }

    for (i = 1; i < PyVectorcall_NARGS(nargsf); i++) {
        if (args[i] == NULL) {
            PyErr_SetString(PyExc_RuntimeError, "NULL argument");
            Py_DECREF(tuple);
            return NULL;
        }
        PyTuple_SET_ITEM(tuple, i-1, args[i]);
        Py_INCREF(args[i]);
    }

    PyObject* res = PyObject_CallObject(callable, tuple);
    Py_DECREF(tuple);
    Py_DECREF(callable);
    return res;
}

#endif
