NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable objc_NSApplicationMain(PyObject* meth,
                                                  PyObject* _Nonnull const* _Nonnull args,
                                                  size_t nargs)
{
    char**     argv = NULL;
    Py_ssize_t argc;
    int        i;
    PyObject*  v;
    PyObject*  argv_arg;
    int        res;
    Py_ssize_t argc_arg = -1;
    PyObject*  seq;

    if (PyObjC_CheckArgCount(meth, 1, 2, nargs) == -1) {
        return NULL;
    }

    if (nargs == 1) {
        argv_arg = args[0];
    } else {
        if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[0], &argc_arg) == -1) {
            return NULL;
        }
        argv_arg = args[1];
    }

    seq = PySequence_Tuple(argv_arg);
    if (seq == NULL) {
        PyErr_Format(PyExc_TypeError, "need sequence of strings as argument, got %s",
                     Py_TYPE(argv_arg)->tp_name);
        return NULL;
    }

    argc = PyTuple_GET_SIZE(seq);
    if (argc_arg != -1) {
        if (argc != argc_arg) {
            PyErr_Format(PyExc_ValueError, "expecting sequence of %ld strings, got %ld",
                         argc_arg, argc);
            Py_CLEAR(seq);
            return NULL;
        }
    }
    argv = calloc((argc + 1), sizeof(char**));
    if (argv == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_NoMemory();
        Py_CLEAR(seq);
        return NULL;
        // LCOV_EXCL_STOP
    }

    for (i = 0; i < argc; i++) {
        v = PyTuple_GET_ITEM(seq, i);
        if (PyUnicode_Check(v)) {
            PyObject* bytes = PyUnicode_AsEncodedString(v, NULL, NULL);
            if (!bytes) {
                Py_CLEAR(seq);
                goto error_cleanup;
            }
            argv[i] = strdup(PyBytes_AsString(bytes));
        } else {
            Py_CLEAR(seq);
            PyErr_SetString(PyExc_TypeError, "need sequence of strings "
                                             "as argument");
            goto error_cleanup;
        }

        if (argv[i] == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_CLEAR(seq);
            PyErr_NoMemory();
            goto error_cleanup;
            // LCOV_EXCL_STOP
        }
    }
    Py_CLEAR(seq);

    argv[argc] = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
#ifdef COVERAGE
            extern void __llvm_gcov_writeout(void);
            __llvm_gcov_writeout();
#endif
            res = NSApplicationMain(argc, (const char**)argv);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
            res = -1;                            // LCOV_EXCL_LINE
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS // LCOV_EXCL_LINE

    // LCOV_EXCL_START
    // NSApplicatonMain never returns (as documented), hence this
    // code is dead and only included for completeness sake.

    for (i = 0; i < argc; i++) {
        free(argv[i]);
    }
    free(argv);

    if (res == -1 && PyErr_Occurred())
        return NULL;
    return PyLong_FromLong(res);

    // LCOV_EXCL_STOP

error_cleanup:
    if (argv != NULL) {
        for (i = 0; i < argc; i++) {
            if (argv[i] != NULL) {
                free(argv[i]);
                argv[i] = NULL;
            }
        }
        free(argv);
        argv = NULL;
    }

    return NULL;
}

static int
setup_appmain(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(NSApplicationMain, objc_NSApplicationMain)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
