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
        if (keys == NULL) {
            PyErr_NoMemory();
            return NULL;
        }
    } else {
        PyErr_SetString(PyExc_ValueError, "keys must be None of NULL");
        return NULL;
    }

    if (args[1] == PyObjC_NULL) {
        values = NULL;
    } else if (args[1] == Py_None) {
        if (count == -1) {
            count = CFDictionaryGetCount(dict);
        }
        values = malloc(sizeof(void*) * count);
        if (values == NULL) {
            if (keys != NULL) {
                free(keys);
            }
            PyErr_NoMemory();
            return NULL;
        }
    } else {
        PyErr_SetString(PyExc_ValueError, "values must be None of NULL");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFDictionaryGetKeysAndValues(dict, keys, values);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        if (keys != NULL) {
            free(keys);
        }
        if (values != NULL) {
            free(values);
        }
        return NULL;
    }

    PyObject* pyKeys;
    if (keys != NULL) {
        pyKeys = PyObjC_CArrayToPython(@encode(id), keys, count);
        free(keys);
    } else {
        pyKeys = Py_None;
        Py_INCREF(pyKeys);
    }

    PyObject* pyValues;
    if (values != NULL) {
        pyValues = PyObjC_CArrayToPython(@encode(id), values, count);
        free(values);
    } else {
        pyValues = Py_None;
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
        == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
