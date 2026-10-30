NS_ASSUME_NONNULL_BEGIN

static const void*
mod_timer_retain(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_timer_release(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

static CFRunLoopTimerContext mod_CFRunLoopTimerContext = {0, NULL, mod_timer_retain,
                                                          mod_timer_release, NULL};

static void
mod_CFRunLoopTimerCallBack(CFRunLoopTimerRef f, void* _info)
{
    PyObject*        info  = (PyObject*)_info;
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_f = PyObjC_ObjCToPython(@encode(CFRunLoopTimerRef), &f);

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "NO", py_f,
                                             PyTuple_GetItem(info, 1));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject* _Nullable mod_CFRunLoopTimerCreate(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef allocator;
    CFAbsoluteTime fireDate;
    CFTimeInterval interval;
    CFOptionFlags  flags;
    CFIndex        order;

    if (PyObjC_CheckArgCount(meth, 7, 7, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFAbsoluteTime), args[1], &fireDate) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFTimeInterval), args[2], &interval) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFOptionFlags), args[3], &flags) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFIndex), args[4], &order) < 0) {
        return NULL;
    }

    CFRunLoopTimerContext context = mod_CFRunLoopTimerContext;
    context.info                  = PyTuple_Pack(2, args[5], args[6]);
    if (context.info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;            // LCOV_EXCL_LINE
    }

    CFRunLoopTimerRef rv = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFRunLoopTimerCreate(allocator, fireDate, interval, flags, order,
                                      mod_CFRunLoopTimerCallBack, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            rv = NULL;                           // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* result = PyObjC_ObjCToPython(@encode(CFRunLoopTimerRef), &rv);
    if (rv != NULL) {
        CFRelease(rv);
    }
    return result;
}

static PyObject* _Nullable mod_CFRunLoopTimerGetContext(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFRunLoopTimerRef     f;
    CFRunLoopTimerContext context;

    if (nargs == 1) {
        if (PyErr_WarnEx(PyExc_DeprecationWarning,
                         "Leaving off last argument is deprecated", 0)
            == -1) {
            return NULL;
        }
        if (PyObjC_PythonToObjC(@encode(CFRunLoopTimerRef), args[0], &f) < 0) {
            return NULL;
        }
    } else {
        if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
            return NULL;
        }

        if (PyObjC_PythonToObjC(@encode(CFRunLoopTimerRef), args[0], &f) < 0) {
            return NULL;
        }

        if (args[1] != Py_None) {
            PyErr_SetString(PyExc_ValueError, "'context' must be None");
            return NULL;
        }
    }

    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFRunLoopTimerGetContext(f, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    if (context.version != 0) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "retrieved context is not valid");
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (context.retain != mod_timer_retain) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (context.info == NULL) {
        Py_INCREF(PyObjC_NULL);
        return PyObjC_NULL;
    }

    Py_INCREF(PyTuple_GetItem((PyObject*)context.info, 1));
    return PyTuple_GetItem((PyObject*)context.info, 1);
}

static int
setup_runloop_timer(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFRunLoopTimerCreate, mod_CFRunLoopTimerCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFRunLoopTimerGetContext,
                                      mod_CFRunLoopTimerGetContext)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
