/*
 * Manual wrappers for CFBag
 */
NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable mod_CFBagGetValues(PyObject* meth,
                                              PyObject* _Nonnull const* _Nonnull args,
                                              size_t nargs)
{
    CFBagRef bag;

    if (nargs == 1) {
        if (PyErr_WarnEx(PyExc_DeprecationWarning,
                         "leaving of the second argument is deprecated", 0)
            == -1) {
            return NULL;
        }
        if (PyObjC_PythonToObjC(@encode(CFBagRef), args[0], &bag) < 0) {
            return NULL;
        }
    } else {
        if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
            return NULL;
        }

        if (PyObjC_PythonToObjC(@encode(CFBagRef), args[0], &bag) < 0) {
            return NULL;
        }

        if (args[1] != Py_None) {
            PyErr_SetString(PyExc_ValueError, "'values' must be None");
            return NULL;
        }
    }

    CFIndex    count   = CFBagGetCount(bag);
    NSObject** members = malloc(sizeof(NSObject*) * count);
    if (members == NULL) {
        PyErr_NoMemory();
        return NULL;
    }
    memset(members, 0, sizeof(NSObject*) * count);

    CFBagGetValues(bag, (const void**)members);
    PyObject* result =
        PyObjC_CArrayToPython(@encode(NSObject*), members, (Py_ssize_t)count);
    free(members);
    return result;
}

static PyObject* _Nullable mod_CFBagCreate(PyObject* meth,
                                           PyObject* _Nonnull const* _Nonnull args,
                                           size_t nargs)
{
    Py_ssize_t     count;
    CFAllocatorRef allocator;
    void**         members;
    int            r;
    PyObject*      buf = NULL;
    Py_buffer      view;
    CFBagRef       bag;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[2], &count) < 0) {
        return NULL;
    }

    r = PyObjC_PythonToCArray(NO, NO, @encode(NSObject*), args[1], (void**)&members,
                              &count, &buf, &view);
    if (r == -1) {
        return NULL;
    }

    bag = CFBagCreate(allocator, (const void**)members, (CFIndex)count,
                      &kCFTypeBagCallBacks);

    PyObjC_FreeCArray(r, &view);
    Py_XDECREF(buf);

    PyObject* result = PyObjC_ObjCToPython(@encode(CFBagRef), &bag);
    if (bag) {
        CFRelease(bag);
    }
    return result;
}

static PyObject* _Nullable mod_CFBagCreateMutable(PyObject* meth,
                                                  PyObject* _Nonnull const* _Nonnull args,
                                                  size_t nargs)
{
    Py_ssize_t     count;
    CFAllocatorRef allocator;
    CFBagRef       bag;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(Py_ssize_t), args[1], &count) < 0) {
        return NULL;
    }

    bag = CFBagCreateMutable(allocator, count, &kCFTypeBagCallBacks);

    PyObject* result = PyObjC_ObjCToPython(@encode(CFBagRef), &bag);
    if (bag) {
        CFRelease(bag);
    }
    return result;
}

static int
setup_cfbag(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFBagCreate, mod_CFBagCreate) == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFBagCreateMutable, mod_CFBagCreateMutable) == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFBagGetValues, mod_CFBagGetValues) == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
