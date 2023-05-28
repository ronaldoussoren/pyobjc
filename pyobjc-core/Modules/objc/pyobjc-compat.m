#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

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

static PyObject* _Nullable _intern_bytes(PyObject* key)
{
    PyObject* value;
    if (key == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;   // LCOV_EXCL_LINE
    }

    if (registry == NULL) {
        registry = PyDict_New();
        if (registry == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(key);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }
    value = PyDict_GetItemWithError(registry, key);
    if (value == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key);
        return NULL;
        // LCOV_EXCL_STOP
    } else if (value == NULL) {
        int r = PyDict_SetItem(registry, key, key);
        if (r == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(key);
            return NULL;
            // LCOV_EXCL_STOP
        } else {
            return key;
        }
    } else {
        Py_DECREF(key);
        Py_INCREF(value);
        return value;
    }
}

PyObject* _Nullable PyObjCBytes_InternFromString(const char* v)
{
    return _intern_bytes(PyBytes_FromString(v));
}

PyObject* _Nullable PyObjCBytes_InternFromStringAndSize(const char* v, Py_ssize_t l)
{
    return _intern_bytes(PyBytes_FromStringAndSize(v, l));
}

/* XXX: Can we do without this function, it is a little too intimate with
 * unicode details.
 */
const char* _Nullable PyObjC_Unicode_Fast_Bytes(PyObject* object)
{
    /* Having a unicode string is a precondition, checked manually
     * that callers check the type beforehand.
     */
    PyObjC_Assert(PyUnicode_Check(object), NULL);

    if (!PyUnicode_IS_ASCII(object)) {
        /* The code below raises the correct error in a roundabout
         * way. That's because UnicodeEncodeError expects more
         * than one argument.
         */
        PyObject* r = PyUnicode_AsASCIIString(object);
        if (unlikely(r != NULL)) {
            PyErr_SetString(PyObjCExc_Error, "Raising UnicodeError failed");
            Py_DECREF(r);
            return NULL;
        }

        PyObjC_Assert(r == NULL, NULL);
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

PyObject* _Nullable PyObject_Vectorcall(PyObject* callable,
                                        PyObject* _Nonnull const* _Nonnull args,
                                        size_t nargsf, PyObject* _Nullable kwnames)
{
    size_t i;
    if (kwnames != NULL) {
        PyErr_SetString(PyExc_RuntimeError,
                        "PyObjC's vectorcall compat does not support keyword arguments");
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
PyObject_VectorcallMethod(PyObject* name, PyObject* _Nonnull const* _Nonnull args,
                          size_t    nargsf, PyObject* _Nullable kwnames)
{
    size_t i;
    if (kwnames != NULL) {
        PyErr_SetString(PyExc_RuntimeError,
                        "PyObjC's vectorcall compat does not support keyword arguments");
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

    PyObject* tuple = PyTuple_New(PyVectorcall_NARGS(nargsf) - 1);
    if (tuple == NULL) {
        return NULL;
    }

    for (i = 1; i < PyVectorcall_NARGS(nargsf); i++) {
        if (args[i] == NULL) {
            PyErr_SetString(PyExc_RuntimeError, "NULL argument");
            Py_DECREF(tuple);
            return NULL;
        }
        PyTuple_SET_ITEM(tuple, i - 1, args[i]);
        Py_INCREF(args[i]);
    }

    PyObject* res = PyObject_CallObject(callable, tuple);
    Py_DECREF(tuple);
    Py_DECREF(callable);
    return res;
}

#endif

#if PY_VERSION_HEX >= 0x030c0000
extern PyObject* _Nonnull _PyType_GetDict(PyTypeObject* _Nonnull tp);

extern PyObject*
PyObjC_get_tp_dict(PyTypeObject* tp)
{
    return _PyType_GetDict(tp);
}

#else

extern PyObject*
PyObjC_get_tp_dict(PyTypeObject* tp)
{
    return tp->tp_dict;
}

#endif

NS_ASSUME_NONNULL_END
