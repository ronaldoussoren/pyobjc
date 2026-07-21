NS_ASSUME_NONNULL_BEGIN

static const void*
mod_source_retain(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_source_release(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

static void
mod_schedule(void* info, CFRunLoopRef rl, CFStringRef mode)
{
    if (info == NULL)
        return;

    PyGILState_STATE state = PyGILState_Ensure();
    if (PyTuple_GetItem(info, 1) != Py_None) {
        PyObject* py_info = PyTuple_GetItem(info, 4);
        PyObject* py_rl   = PyObjC_ObjCToPython(@encode(CFRunLoopRef), &rl);
        if (py_rl == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
        PyObject* py_mode = PyObjC_ObjCToPython(@encode(CFStringRef), &mode);
        if (py_rl == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }

        PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 1), "ONN", py_info,
                                                 py_rl, py_mode);
        if (result == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
        Py_DECREF(result);
    }
    PyGILState_Release(state);
}

static void
mod_cancel(void* info, CFRunLoopRef rl, CFStringRef mode)
{
    if (info == NULL)
        return;

    PyGILState_STATE state = PyGILState_Ensure();
    if (PyTuple_GetItem(info, 2) != Py_None) {
        PyObject* py_info = PyTuple_GetItem(info, 4);
        PyObject* py_rl   = PyObjC_ObjCToPython(@encode(CFRunLoopRef), &rl);
        if (py_rl == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
        PyObject* py_mode = PyObjC_ObjCToPython(@encode(CFStringRef), &mode);
        if (py_rl == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }

        PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 2), "ONN", py_info,
                                                 py_rl, py_mode);
        if (result == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
        Py_DECREF(result);
    }
    PyGILState_Release(state);
}

static void
mod_perform(void* info)
{
    if (info == NULL)
        return;

    PyGILState_STATE state = PyGILState_Ensure();
    if (PyTuple_GetItem(info, 3) != Py_None) {
        PyObject* py_info = PyTuple_GetItem(info, 4);

        PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 3), "O", py_info);
        if (result == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
        Py_DECREF(result);
    }
    PyGILState_Release(state);
}

static CFRunLoopSourceContext mod_CFRunLoopSourceContext = {
    0,    NULL, mod_source_retain, mod_source_release, NULL,
    NULL, NULL, mod_schedule,      mod_cancel,         mod_perform};

static PyObject* _Nullable mod_CFRunLoopSourceCreate(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef         allocator;
    CFIndex                order;
    CFRunLoopSourceContext context = mod_CFRunLoopSourceContext;

    if (PyObjC_CheckArgCount(meth, 3, 3, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFIndex), args[1], &order) < 0) {
        return NULL;
    }

    if (!PyTuple_Check(args[2]) || PyTuple_GET_SIZE(args[2]) != 5) {
        PyErr_SetString(PyExc_ValueError, "context must be tuple of length 5");
        return NULL;
    }

    PyObject* v = PyTuple_GET_ITEM(args[2], 0);
    NSInteger i;

    if (PyObjC_PythonToObjC(@encode(NSInteger), v, &i) == -1) {
        PyErr_SetString(PyExc_ValueError, "Version field must be 0");
        return NULL;
    } else if (i != 0) {
        PyErr_SetString(PyExc_ValueError, "Version field must be 0");
        return NULL;
    }

    context.info = args[2];
    Py_INCREF(args[2]);

    CFRunLoopSourceRef rv = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFRunLoopSourceCreate(allocator, order, &context);

        } @catch (NSException* localException) {
            rv = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) {
        return NULL;
    }

    PyObject* result = PyObjC_ObjCToPython(@encode(CFRunLoopSourceRef), &rv);
    if (rv != NULL) {
        CFRelease(rv);
    }
    return result;
}

static PyObject* _Nullable mod_CFRunLoopSourceGetContext(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFRunLoopSourceRef     f;
    CFRunLoopSourceContext context;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFRunLoopSourceRef), args[0], &f) < 0) {
        return NULL;
    }

    if (args[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "invalid context");
        return NULL;
    }

    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFRunLoopSourceGetContext(f, &context);

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    if (context.version != 0) {
        PyErr_SetString(PyExc_ValueError, "retrieved context is not valid");
        return NULL;
    }

    if (context.retain != mod_source_retain) {
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
    }

    if (context.info == NULL) {
        Py_INCREF(PyObjC_NULL);
        return PyObjC_NULL;
    }

    Py_INCREF((PyObject*)(context.info));
    return (PyObject*)(context.info);
}

static int
setup_runloop_source(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFRunLoopSourceCreate, mod_CFRunLoopSourceCreate)
        == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFRunLoopSourceGetContext,
                                      mod_CFRunLoopSourceGetContext)
        == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
