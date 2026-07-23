NS_ASSUME_NONNULL_BEGIN

static const void*
mod_messageport_retain(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_messageport_release(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

static CFMessagePortContext mod_CFMessagePortContext = {0, NULL, mod_messageport_retain,
                                                        mod_messageport_release, NULL};

static CFDataRef
mod_CFMessagePortCallBack(CFMessagePortRef f, SInt32 msgid, CFDataRef data, void* _info)
{
    PyObject*        info  = (PyObject*)_info;
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_f     = PyObjC_ObjCToPython(@encode(CFMessagePortRef), &f);
    PyObject* py_msgid = PyObjC_ObjCToPython(@encode(SInt32), &msgid);
    PyObject* py_data  = PyObjC_ObjCToPython(@encode(CFDataRef), &data);

    PyObject* result =
        PyObject_CallFunction(PyTuple_GET_ITEM(info, 0), "NNNO", py_f, py_msgid, py_data,
                              PyTuple_GET_ITEM(info, 1));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }

    CFDataRef rv;
    if (PyObjC_PythonToObjC(@encode(CFDataRef), result, &rv) < 0) {
        Py_DECREF(result);
        PyObjCErr_ToObjCWithGILState(&state);
    }

    Py_DECREF(result);
    PyGILState_Release(state);
    CFRetain(rv);
    return rv;
}

static PyObject* _Nullable mod_CFMessagePortCreateLocal(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef allocator;
    CFStringRef    name;
    Boolean        shouldFree;

    if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFStringRef), args[1], &name) < 0) {
        return NULL;
    }
    if (args[4] != Py_None && args[4] != PyObjC_NULL) {
        PyErr_SetString(PyExc_ValueError, "'shouldFree' should be None or NULL");
        return NULL;
    }

    CFMessagePortContext context = mod_CFMessagePortContext;
    context.info                 = PyTuple_Pack(2, args[2], args[3]);
    if (context.info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;            // LCOV_EXCL_LINE
    }

    CFMessagePortRef rv = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFMessagePortCreateLocal(allocator, name, mod_CFMessagePortCallBack,
                                          &context,
                                          args[4] == PyObjC_NULL ? NULL : &shouldFree);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            rv = NULL;                           // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* result;
    if (args[4] == PyObjC_NULL) {
        result = Py_BuildValue("NO", PyObjC_ObjCToPython(@encode(CFMachPortRef), &rv),
                               PyObjC_NULL);
    } else {
        result = Py_BuildValue("NN", PyObjC_ObjCToPython(@encode(CFMachPortRef), &rv),
                               PyBool_FromLong(shouldFree));
    }

    if (rv != NULL) {
        CFRelease(rv);
    }

    return result;
}

static PyObject* _Nullable mod_CFMessagePortGetContext(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFMessagePortRef     f;
    CFMessagePortContext context;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFMessagePortRef), args[0], &f) < 0) {
        return NULL;
    }

    if (args[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "'context' must be None");
        return NULL;
    }

    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFMessagePortGetContext(f, &context);

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

    if (context.retain != mod_messageport_retain) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_INCREF(PyTuple_GetItem((PyObject*)context.info, 1));
    return PyTuple_GetItem((PyObject*)context.info, 1);
}

static int
setup_messageport(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFMessagePortCreateLocal,
                                      mod_CFMessagePortCreateLocal)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFMessagePortGetContext,
                                      mod_CFMessagePortGetContext)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
