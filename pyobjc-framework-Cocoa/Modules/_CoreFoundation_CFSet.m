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

    if (args[1] == Py_None) {
        count  = CFSetGetCount(set);
        values = PyMem_Malloc(sizeof(void*) * count);
        if (values == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_NoMemory();
            return NULL;
            // LCOV_EXCL_STOP
        }
    } else {
        PyErr_SetString(PyExc_ValueError, "'values' must be None");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFSetGetValues(set, values); // LCOV_BR_EXCL_LINE

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        assert(values != NULL);
        PyMem_Free(values);
        return NULL;
        // LCOV_EXCL_STOP
    }

    assert(values != NULL);
    PyObject* pyValues;
    pyValues = PyObjC_CArrayToPython(@encode(id), values, count);
    PyMem_Free(values);

    return pyValues;
}

static int
setup_set(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFSetGetValues, mod_CFSetGetValues)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
