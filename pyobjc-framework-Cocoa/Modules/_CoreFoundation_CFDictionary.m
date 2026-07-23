NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable mod_CFDictionaryGetKeysAndValues(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    PyObject*       result;
    CFDictionaryRef dict;
    void*           keys;
    void*           values;
    CFIndex         count;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), args[0], &dict) < 0) {
        return NULL;
    }

    count = -1;
    if (args[1] == PyObjC_NULL) {
        keys = NULL;
    } else if (args[1] == Py_None) {
        count = CFDictionaryGetCount(dict);
        keys  = malloc(sizeof(void*) * count);
        if (keys == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_NoMemory();
            return NULL;
            // LCOV_EXCL_STOP
        }
    } else {
        PyErr_SetString(PyExc_ValueError, "keys must be None of NULL");
        return NULL;
    }

    if (args[2] == PyObjC_NULL) {
        values = NULL;
    } else if (args[2] == Py_None) {
        if (count == -1) {
            count = CFDictionaryGetCount(dict);
        }
        values = malloc(sizeof(void*) * count);
        if (values == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            if (keys != NULL) {
                free(keys);
            }
            PyErr_NoMemory();
            return NULL;
            // LCOV_EXCL_STOP
        }
    } else {
        PyErr_SetString(PyExc_ValueError, "values must be None of NULL");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFDictionaryGetKeysAndValues(dict, keys, values);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_EXCL_LINE
        // LCOV_EXCL_START
        if (keys != NULL) {
            free(keys);
        }
        if (values != NULL) {
            free(values);
        }
        return NULL;
        // LCOV_EXCL_STOP
    }

    PyObject* pyKeys;
    if (keys != NULL) {
        pyKeys = PyObjC_CArrayToPython(@encode(id), keys, count);
        free(keys);
    } else {
        pyKeys = PyObjC_NULL;
        Py_INCREF(pyKeys);
    }

    PyObject* pyValues;
    if (values != NULL) {
        pyValues = PyObjC_CArrayToPython(@encode(id), values, count);
        free(values);
    } else {
        pyValues = PyObjC_NULL;
        Py_INCREF(pyValues);
    }

    result = Py_BuildValue("NN", pyKeys, pyValues);
    return result;
}

static int
setup_dictionary(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFDictionaryGetKeysAndValues,
                                      mod_CFDictionaryGetKeysAndValues)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
