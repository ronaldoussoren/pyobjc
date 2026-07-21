NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable mod_CFSetGetValues(PyObject* meth,
                                              PyObject* _Nonnull const* _Nonnull args,
                                              size_t nargs)
{
    CFSetRef set;
    void*    values;
    CFIndex  count;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFSetRef), args[0], &set) < 0) {
        return NULL;
    }

    if (args[1] == PyObjC_NULL) {
        values = NULL;
        count  = 0;
    } else if (args[1] == Py_None) {
        count  = CFSetGetCount(set);
        values = malloc(sizeof(void*) * count);
        if (values == NULL) {
            PyErr_NoMemory();
            return NULL;
        }
    } else {
        PyErr_SetString(PyExc_ValueError, "values must be None of NULL");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFSetGetValues(set, values);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        if (values != NULL) {
            free(values);
        }
        return NULL;
    }

    PyObject* pyValues;
    if (values != NULL) {
        pyValues = PyObjC_CArrayToPython(@encode(id), values, count);
        free(values);
    } else {
        pyValues = Py_None;
        Py_INCREF(pyValues);
    }

    return pyValues;
}

static int
setup_set(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFSetGetValues, mod_CFSetGetValues) == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
