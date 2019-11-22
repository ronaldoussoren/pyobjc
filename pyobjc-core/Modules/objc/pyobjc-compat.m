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
