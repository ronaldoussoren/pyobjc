/*
 * Workaround to make NSAppicationMain more usable from Python.
 */
NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable objc_NSApplicationMain(PyObject* meth,
                                                  PyObject* _Nonnull const* _Nonnull args,
                                                  size_t nargs)
{
    char**    argv = NULL;
    int       argc;
    int       i;
    PyObject* v;
    int       res;

    if (PyObjC_CheckArgCount(meth, 1, 1, nargs) == -1) {
        return NULL;
    }

    if (!PySequence_Check(args[0])) {
        PyErr_SetString(PyExc_TypeError,
                        "NSApplicationMain: need list of strings as argument");
        return NULL;
    }

    argc = PySequence_Size(args[0]);
    argv = calloc((argc + 1), sizeof(char**));
    if (argv == NULL) {
        PyErr_SetString(PyExc_MemoryError, "Out of memory");
        return NULL;
    }

    for (i = 0; i < argc; i++) {
        v = PySequence_GetItem(args[0], i);
        if (v == NULL) {
            goto error_cleanup;
        }
        if (PyUnicode_Check(v)) {
            PyObject* bytes = PyUnicode_AsEncodedString(v, NULL, NULL);
            if (!bytes) {
                Py_CLEAR(v);
                goto error_cleanup;
            }
            argv[i] = strdup(PyBytes_AsString(bytes));
        } else {
            Py_CLEAR(v);
            PyErr_SetString(PyExc_TypeError, "NSApplicationMain: need list of strings "
                                             "as argument");
            goto error_cleanup;
        }

        if (argv[i] == NULL) {
            Py_CLEAR(v);
            PyErr_SetString(PyExc_MemoryError, "Out of memory");
            goto error_cleanup;
        }
        Py_CLEAR(v);
    }

    argv[argc] = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            res = NSApplicationMain(argc, (const char**)argv);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
            res = -1;
        }
    Py_END_ALLOW_THREADS

    for (i = 0; i < argc; i++) {
        free(argv[i]);
    }
    free(argv);

    if (res == -1 && PyErr_Occurred())
        return NULL;
    return PyLong_FromLong(res);

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
    if (PyObjCRegister_FunctionCaller(NSApplicationMain, objc_NSApplicationMain) == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
