NS_ASSUME_NONNULL_BEGIN

static const void*
mod_observer_retain(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_observer_release(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

static CFRunLoopObserverContext mod_CFRunLoopObserverContext = {
    0, NULL, mod_observer_retain, mod_observer_release, NULL};

static void
mod_CFRunLoopObserverCallBack(CFRunLoopObserverRef f, CFRunLoopActivity activity,
                              void* _info)
{
    PyObject*        info  = (PyObject*)_info;
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_f        = PyObjC_ObjCToPython(@encode(CFRunLoopObserverRef), &f);
    PyObject* py_activity = PyObjC_ObjCToPython(@encode(CFRunLoopActivity), &activity);

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "NNO", py_f,
                                             py_activity, PyTuple_GetItem(info, 1));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject* _Nullable mod_CFRunLoopObserverCreate(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef allocator;
    CFOptionFlags  activities;
    Boolean        repeats;
    CFIndex        order;

    if (PyObjC_CheckArgCount(meth, 6, 6, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFOptionFlags), args[1], &activities) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(bool), args[2], &repeats) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFIndex), args[3], &order) < 0) {
        return NULL;
    }

    CFRunLoopObserverContext context = mod_CFRunLoopObserverContext;
    context.info                     = PyTuple_Pack(2, args[4], args[5]);
    if (context.info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;            // LCOV_EXCL_LINE
    }

    CFRunLoopObserverRef rv = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFRunLoopObserverCreate(allocator, activities, repeats, order,
                                         mod_CFRunLoopObserverCallBack, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            rv = NULL;                           // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* result = PyObjC_ObjCToPython(@encode(CFRunLoopObserverRef), &rv);
    if (rv != NULL) {
        CFRelease(rv);
    }
    return result;
}

static PyObject* _Nullable mod_CFRunLoopObserverGetContext(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFRunLoopObserverRef     f;
    CFRunLoopObserverContext context;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFRunLoopObserverRef), args[0], &f) < 0) {
        return NULL;
    }

    if (args[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "'context' must be None");
        return NULL;
    }

    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFRunLoopObserverGetContext(f, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    if (context.version != 0) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "retrieved context is not valid");
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (context.retain != mod_observer_retain) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
        // LCOV_EXCL_STOP
    }

    if (context.info == NULL) {
        Py_INCREF(PyObjC_NULL);
        return PyObjC_NULL;
    }

    return PySequence_GetItem((PyObject*)context.info, 1);
}

static int
setup_runloop(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFRunLoopObserverCreate,
                                      mod_CFRunLoopObserverCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFRunLoopObserverGetContext,
                                      mod_CFRunLoopObserverGetContext)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
