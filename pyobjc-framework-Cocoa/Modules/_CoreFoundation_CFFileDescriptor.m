NS_ASSUME_NONNULL_BEGIN

static void*
mod_filedescr_retain(void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_filedescr_release(void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

static CFFileDescriptorContext mod_CFFileDescriptorContext = {
    0, NULL, mod_filedescr_retain, mod_filedescr_release, NULL};

static void
mod_CFFileDescriptorCallBack(CFFileDescriptorRef f, CFOptionFlags callBackType,
                             void* _info)
{
    PyObject*        info  = (PyObject*)_info;
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_f = PyObjC_ObjCToPython(@encode(CFFileDescriptorRef), &f);
    PyObject* py_callBackType =
        PyObjC_ObjCToPython(@encode(CFOptionFlags), &callBackType);

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "NNO", py_f,
                                             py_callBackType, PyTuple_GetItem(info, 1));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject* _Nullable mod_CFFileDescriptorCreate(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef                   allocator;
    CFFileDescriptorNativeDescriptor descriptor;
    Boolean                          closeOnInvalidate;

    if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFFileDescriptorNativeDescriptor), args[1],
                            &descriptor)
        < 0) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(bool), args[2], &closeOnInvalidate) < 0) {
        return NULL;
    }

    CFFileDescriptorContext context = mod_CFFileDescriptorContext;
    context.info                    = PyTuple_Pack(2, args[3], args[4]);
    if (context.info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;            // LCOV_EXCL_LINE
    }

    CFFileDescriptorRef rv = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFFileDescriptorCreate(allocator, descriptor, closeOnInvalidate,
                                        mod_CFFileDescriptorCallBack, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            rv = NULL;                           // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    PyObject* result = PyObjC_ObjCToPython(@encode(CFFileDescriptorRef), &rv);
    if (rv != NULL) {
        CFRelease(rv);
    }
    return result;
}

static PyObject* _Nullable mod_CFFileDescriptorGetContext(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFFileDescriptorRef     f;
    CFFileDescriptorContext context;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFFileDescriptorRef), args[0], &f) < 0) {
        return NULL;
    }

    if (args[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "'context' must be None");
        return NULL;
    }

    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFFileDescriptorGetContext(f, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    if (context.version != 0
        || context.retain != mod_filedescr_retain) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_INCREF(PyTuple_GetItem((PyObject*)context.info, 1));
    return PyTuple_GetItem((PyObject*)context.info, 1);
}

static int
setup_filedescriptor(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFFileDescriptorCreate, mod_CFFileDescriptorCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFFileDescriptorGetContext,
                                      mod_CFFileDescriptorGetContext)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
