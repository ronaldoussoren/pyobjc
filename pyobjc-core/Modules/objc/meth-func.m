#include "pyobjc.h"

#include "compile.h" /* from Python */
#include "opcode.h"

NS_ASSUME_NONNULL_BEGIN

int
PyObjC_is_pyfunction(PyObject* value)
{
    return PyFunction_Check(value)
           || PyObject_IsInstance(value, (PyObject*)&PyFunction_Type);
}

int
PyObjC_is_pymethod(PyObject* value)
{
    return PyMethod_Check(value) || PyObject_IsInstance(value, (PyObject*)&PyMethod_Type);
}

PyCodeObject* _Nullable PyObjC_get_code(PyObject* value)
{
    if (PyObjC_is_pyfunction(value)) {
        PyObject* code = PyObject_GetAttrString(value, "__code__");
        if (code == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;    // LCOV_EXCL_LINE
        } else if (!PyCode_Check(code)) {
            PyErr_Format(PyExc_ValueError,
                         "%R does not have a valid '__code__' attribute", value);
            Py_DECREF(code);
            return NULL;
        }
        return (PyCodeObject*)code;

    } else if (PyObjC_is_pymethod(value)) {
        PyObject* func = PyObject_GetAttrString(value, "__func__");
        if (func == NULL) { // LCOV_BR_EXCL_LINE
            return NULL;    // LCOV_EXCL_LINE
        }
        if (PyObjC_is_pyfunction(func)) {
            PyObject* code = PyObject_GetAttrString(func, "__code__");
            Py_DECREF(func);
            if (code == NULL) { // LCOV_BR_EXCL_LINE
                return NULL;    // LCOV_EXCL_LINE
            } else if (!PyCode_Check(code)) {
                PyErr_Format(PyExc_ValueError,
                             "%R does not have a valid '__code__' attribute", value);
                Py_DECREF(code);
                return NULL;
            }
            return (PyCodeObject*)code;
        } else {
            Py_DECREF(func);
        }
    }
    PyErr_Format(PyExc_TypeError, "%R is not a python function or method", value);
    return NULL;
}

/*
 * XXX: This duplicates code in Lib/objc/_transform.py!
 */
bool
PyObjC_returns_value(PyObject* value)
{
    bool      rv = false;
    Py_buffer buf;

    if (!PyFunction_Check(value) && !PyMethod_Check(value)) {
        return true;
    }

    PyCodeObject* func_code = PyObjC_get_code(value);
    if (func_code == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Clear();
        return true;
        // LCOV_EXCL_STOP
    }
#if PY_VERSION_HEX >= 0x030b0000
    PyObject* co = PyCode_GetCode(func_code);
    if (co == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Clear();
        Py_DECREF(func_code);
        return true;
        // LCOV_EXCL_STOP
    }
    if (PyObject_GetBuffer( // LCOV_BR_EXCL_LINE
            co, &buf, PyBUF_CONTIG_RO)
        == -1) {
        /* This should not happened: A function where co_code does not implement
         * the buffer protocol.
         *
         * Note that the CPython documentation promises that the "co" object
         * will be a bytes object.
         */
        // LCOV_EXCL_START
        Py_DECREF(func_code);
        Py_DECREF(co);
        return NULL;
        // LCOV_EXCL_STOP
    }

    /* The buffer owns a strong reference */
    Py_DECREF(co);

#else
    if (PyObject_GetBuffer( // LCOV_BR_EXCL_LINE
            func_code->co_code, &buf, PyBUF_CONTIG_RO)
        == -1) {
        /* This should not happened: A function where co_code does not implement
         * the buffer protocol.
         */
        // LCOV_EXCL_START
        Py_DECREF(func_code);
        return NULL;
        // LCOV_EXCL_STOP
    }
#endif

    /*
       Scan bytecode to find return statements. If any non-bare return
       statement exists, then set the return type to @ (id).

       In Python 3.6 the interpreter switched to a 16-bit word-code instead
       of 8-bit bytecode, hence the two code paths
    */
    bool was_none = false;

#if PY_VERSION_HEX >= 0x03060000
    PyObjC_Assert(buf.len % 2 == 0, NULL);

    for (Py_ssize_t i = 0; i < buf.len; i += 2) {
        int op = ((unsigned char*)buf.buf)[i];
        if (op == LOAD_CONST && ((unsigned char*)buf.buf)[i + 1] == 0) {
            was_none = true;
        } else {
            if (op == RETURN_VALUE && !was_none) {
                rv = true;
                break;
            }
#if PY_VERSION_HEX >= 0x030c0000
            else if (op == RETURN_CONST && ((unsigned char*)buf.buf)[i + 1] != 0) {
                rv = true;
                break;
            }
#endif /* PY_VERSION_HEX >= 0x030c0000 */

            was_none = false;
        }
    }

#else  /* PY_VERSION_HEX < 0x03060000 */
    for (i = 0; i < buf.len; ++i) {
        int op = ((unsigned char*)buf.buf)[i];
        if (op == LOAD_CONST && ((unsigned char*)buf.buf)[i + 1] == 0
            && ((unsigned char*)buf.buf)[i + 2] == 0) {
            was_none = true;
        } else {
            if (op == RETURN_VALUE) {
                if (!was_none) {

                    break;
                }
            }
            was_none = false;
        }
        if (op >= HAVE_ARGUMENT) {
            i += 2;
        }
    }
#endif /* PY_VERSION_HEX < 0x03060000 */
    PyBuffer_Release(&buf);
    Py_DECREF(func_code);
    return rv;
}

Py_ssize_t
PyObjC_num_defaults(PyObject* value)
{
    PyObjC_Assert(PyObjC_is_pyfunction(value) || PyObjC_is_pymethod(value), -1);

    PyObject* defaults = PyObject_GetAttrString(value, "__defaults__");
    if (defaults == NULL) { // LCOV_BR_EXCL_LINE
        return -1;          // LCOV_EXCL_LINE
    }
    if (PyTuple_Check(defaults)) {
        Py_ssize_t num = PyTuple_Size(defaults);
        Py_DECREF(defaults);
        return num;
    } else if (defaults != Py_None) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(defaults);
        PyErr_Format(PyExc_ValueError, "%R has an invalid '__defaults__' attribute",
                     value);
        return -1;
        // LCOV_EXCL_STOP
    } else {
        Py_DECREF(defaults);
        return 0;
    }
}

Py_ssize_t
PyObjC_num_kwdefaults(PyObject* value)
{
    PyObjC_Assert(PyObjC_is_pyfunction(value) || PyObjC_is_pymethod(value), -1);

    PyObject* defaults = PyObject_GetAttrString(value, "__kwdefaults__");
    if (defaults == NULL) {
        return -1;
    }
    if (PyDict_Check(defaults)) {
        Py_ssize_t num = PyDict_Size(defaults);
        Py_DECREF(defaults);
        return num;
    } else if (defaults != Py_None) {
        Py_DECREF(defaults);
        PyErr_Format(PyExc_ValueError, "%R has an invalid '__kwdefaults__' attribute",
                     value);
        return -1;
    } else {
        Py_DECREF(defaults);
        return 0;
    }
}

Py_ssize_t
PyObjC_num_arguments(PyObject* value)
{
    PyObjC_Assert(PyObjC_is_pyfunction(value) || PyObjC_is_pymethod(value), -1);

    PyCodeObject* func_code = PyObjC_get_code(value);
    if (func_code == NULL) {
        return -1;
    }
    Py_ssize_t num = func_code->co_argcount;
    Py_DECREF(func_code);
    return num;
}

NS_ASSUME_NONNULL_END
