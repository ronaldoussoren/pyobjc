/*
 * Specific support to make it easier to wrap Security/Authorization.h
 *
 * This is a bit of a hack, to be replaced later with generic support.
 */
#import "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

struct auth_item_set {
    char* _Nullable name;
    size_t valueLength;
    void* _Nullable value;
    unsigned int flags;
};

int
IS_AUTHORIZATIONITEM(const char* typestr)
{
    return strncmp(typestr, "{_AuthorizationItem=^cL^vI}", 27) == 0;
}

PyObject* _Nullable pythonify_authorizationitem(const void* _value)
{
    const struct auth_item_set* value = (const struct auth_item_set*)_value;
    PyObject*                   result;
    Py_ssize_t                  pack;
    int                         have_tuple = 0;
    PyObject*                   t;
    int                         r;

    result =
        PyObjC_CreateRegisteredStruct("{_AuthorizationItem=^cL^vI}", 27, NULL, &pack);
    if (result == NULL) {
        have_tuple = 1;
        /* XXX: restructure this function to be able to use PyTuple_Pack */
        result = PyTuple_New(4);
        if (unlikely(result == NULL)) { // LCOV_BR_EXCL_LINE
            return NULL;                // LCOV_EXCL_LINE
        }
    }

    if (value->name) {
        t = PyBytes_FromString(value->name);
    } else {
        t = Py_None;
        Py_INCREF(Py_None);
    }
    if (unlikely(t == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }
    if (have_tuple) {
        PyTuple_SET_ITEM(result, 0, t);
    } else {
        r = PyObjC_SetStructField(result, 0, t);
        Py_DECREF(t);
        if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    t = PyLong_FromSize_t(value->valueLength);
    if (unlikely(t == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }
    if (have_tuple) {
        PyTuple_SET_ITEM(result, 1, t);
    } else {
        r = PyObjC_SetStructField(result, 1, t);
        Py_DECREF(t);
        if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    if (value->value == NULL) {
        t = Py_None;
        Py_INCREF(t);
    } else {
        t = PyBytes_FromStringAndSize(value->value, value->valueLength);
        if (unlikely(t == NULL)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    if (have_tuple) {
        PyTuple_SET_ITEM(result, 2, t);
    } else {
        r = PyObjC_SetStructField(result, 2, t);
        Py_DECREF(t);
        if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    t = PyLong_FromLong(value->flags);
    if (unlikely(t == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(result);
        return NULL;
        // LCOV_EXCL_STOP
    }
    if (have_tuple) {
        PyTuple_SET_ITEM(result, 3, t);
    } else {
        r = PyObjC_SetStructField(result, 3, t);
        Py_DECREF(t);
        if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
    }

    return result;
}

int
depythonify_authorizationitem(PyObject* value, void* _out)
{
    struct auth_item_set* out = (struct auth_item_set*)_out;
    PyObject*             seq;

    if (PyObjCStruct_Check(value)) {
        seq = StructAsTuple(value);
    } else {
        seq = PyObjCSequence_Tuple(value, "depythonifying struct, got no sequence");
    }
    if (seq == NULL) {
        return -1;
    }

    if (PyTuple_GET_SIZE(seq) != 4) {
        PyErr_Format(PyExc_ValueError,
                     "depythonifying struct of %ld "
                     "members, got tuple of %ld",
                     4, PyTuple_GET_SIZE(seq));
        Py_DECREF(seq);
        return -1;
    }

    if (PyTuple_GET_ITEM(seq, 0) == Py_None) {
        out->name = NULL;

    } else if (PyBytes_Check(PyTuple_GET_ITEM(seq, 0))) {
        out->name = PyBytes_AsString(PyTuple_GET_ITEM(seq, 0));
    } else {
        PyErr_Format(PyExc_TypeError,
                     "AuthorizationItem.name should be a byte string, not %s",
                     Py_TYPE(PyTuple_GET_ITEM(seq, 0))->tp_name);
        Py_DECREF(seq);
        return -1;
    }

    if (PyLong_Check(PyTuple_GET_ITEM(seq, 1))) {
        out->valueLength = PyLong_AsSize_t(PyTuple_GET_ITEM(seq, 1));
        if (PyErr_Occurred()) {
            Py_DECREF(seq);
            return -1;
        }

    } else {
        PyErr_Format(PyExc_TypeError,
                     "AuthorizationItem.valueLength should be an integer, not %s",
                     Py_TYPE(PyTuple_GET_ITEM(seq, 1))->tp_name);
        Py_DECREF(seq);
        return -1;
    }

    if (PyTuple_GET_ITEM(seq, 2) == Py_None) {
        out->value = NULL;

    } else if (PyBytes_Check(PyTuple_GET_ITEM(seq, 2))) {
        Py_ssize_t len;
        if (unlikely( // LCOV_BR_EXCL_LINE
                PyBytes_AsStringAndSize(PyTuple_GET_ITEM(seq, 2), (char**)&out->value,
                                        &len)
                == -1)) {
            // LCOV_EXCL_START
            Py_DECREF(seq);
            return -1;
            // LCOV_EXCL_STOP
        } else if ((size_t)len < out->valueLength) {
            PyErr_Format(PyExc_ValueError,
                         "AuthorizationItem.value too small; expecting at least %ld "
                         "bytes, got %ld",
                         (long)out->valueLength, (long)len);
            Py_DECREF(seq);
            return -1;
        }

    } else {
        PyErr_Format(PyExc_TypeError,
                     "AuthorizationItem.value should be a byte string, not %s",
                     Py_TYPE(PyTuple_GET_ITEM(seq, 2))->tp_name);
        Py_DECREF(seq);
        return -1;
    }

    if (PyLong_Check(PyTuple_GET_ITEM(seq, 3))) {
        out->flags = (unsigned int)PyLong_AsUnsignedLong(PyTuple_GET_ITEM(seq, 3));
        if (PyErr_Occurred()) {
            Py_DECREF(seq);
            return -1;
        }

    } else {
        PyErr_Format(PyExc_TypeError,
                     "AuthorizationItem.flags should be an integer, not %s",
                     Py_TYPE(PyTuple_GET_ITEM(seq, 3))->tp_name);
        Py_DECREF(seq);
        return -1;
    }

    Py_DECREF(seq);
    return 0;
}

NS_ASSUME_NONNULL_END
