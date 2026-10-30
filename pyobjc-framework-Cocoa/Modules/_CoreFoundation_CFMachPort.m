NS_ASSUME_NONNULL_BEGIN

static const void*
mod_machport_retain(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_machport_release(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

// LCOV_EXCL_START
// Calls to this function cannot be triggered during testing, primarily
// useful for debugging at the C level.
static CFStringRef
mod_machport_copyDescription(const void* info)
{
    return CFStringCreateWithFormat(NULL, NULL, CFSTR("PyObjC Context %p"),
                                    PyTuple_GetItem((PyObject*)info, 1));
}
// LCOV_EXCL_STOP

/*
 * NOTE: 'copyDescription' isn't actually used as far as I know,
 *       but at least on OSX 10.9 testing for the value of
 *       the copyDescription callback is more reliable than
 *       looking at the other callbacks to detect a PyObjC
 *       context (the other two callbacks seem to be replaced
 *       by some other value).
 */

static CFMachPortContext mod_CFMachPortContext = {
    0, NULL, mod_machport_retain, mod_machport_release, mod_machport_copyDescription};

static void
mod_CFMachPortCallBack(CFMachPortRef f, void* msg, CFIndex size, void* _info)
{
    PyObject*        info  = (PyObject*)_info;
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_f    = PyObjC_ObjCToPython(@encode(CFMachPortRef), &f);
    PyObject* py_msg  = PyBytes_FromStringAndSize(msg, size);
    PyObject* py_size = PyLong_FromLongLong(size);

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "NNNO", py_f,
                                             py_msg, py_size, PyTuple_GetItem(info, 1));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static void
mod_CFMachPortInvalidationCallBack(CFMachPortRef f, void* _info)
{
    PyObject*        info  = (PyObject*)_info;
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_f = PyObjC_ObjCToPython(@encode(CFMachPortRef), &f);

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 2), "NO", py_f,
                                             PyTuple_GetItem(info, 1));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject* _Nullable mod_CFMachPortCreate(PyObject* meth,
                                                PyObject* _Nonnull const* _Nonnull args,
                                                size_t nargs)
{
    CFAllocatorRef allocator;
    Boolean        shouldFree;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }

    if (args[3] != Py_None && args[3] != PyObjC_NULL) {
        PyErr_SetString(PyExc_ValueError, "'shouldFree' should be None or NULL");
        return NULL;
    }

    CFMachPortContext context = mod_CFMachPortContext;
    context.info              = PyTuple_Pack(3, args[1], args[2], Py_None);
    if (context.info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;            // LCOV_EXCL_LINE
    }

    CFMachPortRef rv = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFMachPortCreate(allocator, mod_CFMachPortCallBack, &context,
                                  args[3] == PyObjC_NULL ? NULL : &shouldFree);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            rv = NULL;                           // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    PyObject* result;
    if (args[3] == PyObjC_NULL) {
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

static PyObject* _Nullable mod_CFMachPortCreateWithPort(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef allocator;
    mach_port_t    port;
    Boolean        shouldFree;

    if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(mach_port_t), args[1], &port) < 0) {
        return NULL;
    }

    if (args[4] != Py_None && args[4] != PyObjC_NULL) {
        PyErr_SetString(PyExc_ValueError, "'shouldFree' should be None or NULL");
        return NULL;
    }

    CFMachPortContext context = mod_CFMachPortContext;
    context.info              = PyTuple_Pack(2, args[2], args[3]);
    if (context.info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;            // LCOV_EXCL_LINE
    }

    CFMachPortRef rv = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFMachPortCreateWithPort(allocator, port, mod_CFMachPortCallBack,
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

static PyObject* _Nullable mod_CFMachPortGetContext(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFMachPortRef     f;
    CFMachPortContext context = {.version = 0};

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFMachPortRef), args[0], &f) < 0) {
        return NULL;
    }

    if (args[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "'context' must be None");
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFMachPortGetContext(f, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    if (context.version != 0) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_Format(PyExc_ValueError, "retrieved context with version %ld is not valid",
                     (long)context.version);
        return NULL;
        // LCOV_EXCL_STOP
    }
    if (context.copyDescription != mod_machport_copyDescription) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_INCREF(PyTuple_GetItem((PyObject*)context.info, 1));
    return PyTuple_GetItem((PyObject*)context.info, 1);
}

/*
 * Invalidation callbacks are supported only on MachPorts created from Python.
 */
static PyObject* _Nullable mod_CFMachPortSetInvalidationCallBack(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFMachPortRef port;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFMachPortRef), args[0], &port) < 0) {
        return NULL;
    }

    CFMachPortContext context;
    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFMachPortGetContext(port, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    if (context.version != 0
        || context.copyDescription != mod_machport_copyDescription) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "C context is not supported");
        return NULL;
        // LCOV_EXCL_STOP
    }

    Py_DECREF(PyTuple_GetItem((PyObject*)context.info, 2));
    Py_INCREF(args[1]);
    /* XXX: This is using a PyTuple as mutable storage! */
    PyTuple_SET_ITEM((PyObject*)context.info, 2, args[1]);

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFMachPortSetInvalidationCallBack(port, mod_CFMachPortInvalidationCallBack);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject* _Nullable mod_CFMachPortGetInvalidationCallBack(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFMachPortRef port;

    if (PyObjC_CheckArgCount(meth, 1, 1, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFMachPortRef), args[0], &port) < 0) {
        return NULL;
    }

    CFMachPortContext context;
    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFMachPortGetContext(port, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    if (context.version != 0
        || context.copyDescription != mod_machport_copyDescription) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "C context is not supported");
        return NULL;
        // LCOV_EXCL_STOP
    }

    CFMachPortInvalidationCallBack rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFMachPortGetInvalidationCallBack(port);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    if (rv == NULL) {
        Py_INCREF(Py_None);
        return Py_None;
    }

    if (rv == mod_CFMachPortInvalidationCallBack) {
        PyObject* result = PyTuple_GetItem((PyObject*)context.info, 2);
        Py_INCREF(result);
        return result;
    }

    // LCOV_EXCL_START
    PyErr_SetString(PyExc_ValueError, "Unsupported value for invalidate callback");
    return NULL;
    // LCOV_EXCL_STOP
}

static int
setup_machport(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFMachPortCreate, mod_CFMachPortCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFMachPortCreateWithPort,
                                      mod_CFMachPortCreateWithPort)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFMachPortGetContext, mod_CFMachPortGetContext)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFMachPortSetInvalidationCallBack,
                                      mod_CFMachPortSetInvalidationCallBack)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFMachPortGetInvalidationCallBack,
                                      mod_CFMachPortGetInvalidationCallBack)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
