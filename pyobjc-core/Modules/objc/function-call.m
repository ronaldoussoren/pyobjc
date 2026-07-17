#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

/* Dict mapping from signature-string to a 'PyObjC_FunctionCallFunc' */
static PyObject* signature_registry = (PyObject* _Nonnull)NULL;

/* Dict mapping from function to a 'PyObjC_FunctionCallFunc' */
static PyObject* special_registry = (PyObject* _Nonnull)NULL;

/*
 * Initialize the data structures
 */
int
PyObjC_InitFunctionCallRegistry(void)
{
    assert(signature_registry == NULL);
    assert(special_registry == NULL);

    signature_registry = PyDict_New();
    if (unlikely(signature_registry == NULL)) // LCOV_BR_EXCL_LINE
        return -1;                            // LCOV_EXCL_LINE

    special_registry = PyDict_New();
    if (unlikely(special_registry == NULL)) // LCOV_BR_EXCL_LINE
        return -1;                          // LCOV_EXCL_LINE

    return 0;
}

int
PyObjCRegister_FunctionCaller(void* func, PyObjC_FunctionCallFunc call_to_objc)
{
    PyObject* py_func;
    PyObject* entry;
    int       retval = 0;

    assert(special_registry != NULL);
    assert(call_to_objc != NULL);

    py_func = PyLong_FromVoidPtr(func);
    if (unlikely(py_func == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        return -1;
        // LCOV_EXCL_STOP
    }

    entry = PyCapsule_New(call_to_objc, "objc.__funblock__", NULL);
    if (unlikely(entry == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_func);
        return -1;
        // LCOV_EXCL_STOP
    }

    if (unlikely(PyDict_SetItem(special_registry, py_func, entry)
                 == -1)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(py_func);
        Py_DECREF(entry);
        return -1;
        // LCOV_EXCL_STOP
    }
    Py_DECREF(py_func);
    Py_DECREF(entry);

    return retval;
}

int
PyObjC_RegisterFunctionSignatureMapping(char*                   signature,
                                        PyObjC_FunctionCallFunc call_to_objc)
{
    PyObject* entry;
    int       r;
    int       retval = 0;

    assert(signature_registry != NULL);

    PyObject* key = PyBytes_FromStringAndSize(NULL, strlen(signature) + 10);
    if (unlikely(key == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        return -1;
        // LCOV_EXCL_STOP
    }

    r = PyObjCRT_SimplifySignature(signature, PyBytes_AS_STRING(key),
                                   PyBytes_GET_SIZE(key));
    if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key);
        PyErr_Format(PyObjCExc_Error, "cannot simplify signature '%s'", signature);
        return -1;
        // LCOV_EXCL_STOP
    }

#ifdef PyObjC_DEBUG
    if (unlikely(!call_to_objc)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key);
        PyErr_SetString(
            PyObjCExc_Error,
            "PyObjC_RegisterFunctionSignatureMapping: all functions required");
        return -1;
        // LCOV_EXCL_STOP
    }
#endif

    entry = PyCapsule_New(call_to_objc, "objc.__funcblock__", NULL);
    if (unlikely(entry == NULL)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key);
        return -1;
        // LCOV_EXCL_STOP
    }

    if (unlikely( // LCOV_BR_EXCL_LINE
            _PyBytes_Resize(&key, strlen(PyBytes_AS_STRING(key)) + 1))) {
        // LCOV_EXCL_START
        Py_DECREF(entry);
        return -1;
        // LCOV_EXCL_STOP
    }

    if (unlikely( // LCOV_BR_EXCL_LINE
            PyDict_SetItem(signature_registry, key, entry) < 0)) {
        // LCOV_EXCL_START
        Py_DECREF(key);
        Py_DECREF(entry);
        return -1;
        // LCOV_EXCL_STOP
    }
    Py_DECREF(key);
    Py_DECREF(entry);

    return retval;
}

static PyObject* _Nullable find_signature(const char* signature)
{
    int       res;
    PyObject* result = NULL;

    assert(signature_registry != NULL);

    PyObject* key = PyBytes_FromStringAndSize(NULL, strlen(signature) + 10);
    if (unlikely(key == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;
        ; // LCOV_EXCL_LINE
    }

    res = PyObjCRT_SimplifySignature(signature, PyBytes_AS_STRING(key),
                                     PyBytes_GET_SIZE(key));
    if (unlikely(res == -1)) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        Py_DECREF(key);
        PyErr_Format(PyObjCExc_Error, "cannot simplify signature '%s'", signature);
        return NULL;
        // LCOV_EXCL_STOP
    }

    int r = _PyBytes_Resize(&key, strlen(PyBytes_AS_STRING(key)) + 1);
    if (unlikely(r == -1)) { // LCOV_BR_EXCL_LINE
        return NULL;         // LCOV_EXCL_LINE
    }
    if (PyDict_GetItemRef(signature_registry, key, &result) != 1) {
        Py_DECREF(key);
        return NULL;
    }
    Py_DECREF(key);

    return result;
}

PyObjC_FunctionCallFunc _Nullable PyObjC_FindFunctionCaller(void*       func,
                                                            const char* signature)
{
    PyObject*               py_func;
    PyObject*               found;
    PyObjC_FunctionCallFunc result;

    assert(special_registry != NULL);

    py_func = PyLong_FromVoidPtr(func);
    if (unlikely(py_func == NULL)) { // LCOV_BR_EXCL_LINE
        return NULL;                 // LCOV_EXCL_LINE
    }
    found = PyDict_GetItem(special_registry, py_func);
    Py_CLEAR(py_func);
    if (found == NULL && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;                         // LCOV_EXCL_LINE
    }

    found = find_signature(signature);
    if (found == NULL) {
        return NULL;
    }

    result = (PyObjC_FunctionCallFunc)PyCapsule_GetPointer(found, "objc.__funcblock__");
    Py_CLEAR(found);
    return result;
}

NS_ASSUME_NONNULL_END
