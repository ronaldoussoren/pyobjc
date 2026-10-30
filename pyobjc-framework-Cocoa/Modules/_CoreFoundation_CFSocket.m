NS_ASSUME_NONNULL_BEGIN

static const void*
mod_socket_retain(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_socket_release(const void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

static CFSocketContext mod_CFSocketContext = {0, NULL, mod_socket_retain,
                                              mod_socket_release, NULL};

static void
mod_CFSocketCallBack(CFSocketRef s, CFSocketCallBackType type, CFDataRef address,
                     const void* data, void* _info)
{
    PyObject*        info  = (PyObject*)_info;
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_s = PyObjC_ObjCToPython(@encode(CFSocketRef), &s);
    if (py_s == NULL) {                       // LCOV_BR_EXCL_LINE
        PyObjCErr_ToObjCWithGILState(&state); // LCOV_EXCL_LINE
    }
    PyObject* py_type = PyObjC_ObjCToPython(@encode(CFSocketCallBackType), &type);
    if (py_type == NULL) {                    // LCOV_BR_EXCL_LINE
        PyObjCErr_ToObjCWithGILState(&state); // LCOV_EXCL_LINE
    }
    PyObject* py_address = PyObjC_ObjCToPython(@encode(CFDataRef), &address);
    if (py_address == NULL) {                 // LCOV_BR_EXCL_LINE
        PyObjCErr_ToObjCWithGILState(&state); // LCOV_EXCL_LINE
    }
    PyObject* py_data = NULL;

    if (data == NULL) {
        py_data = Py_None;
        Py_INCREF(py_data);
    } else {
        switch (type) {
        case kCFSocketConnectCallBack:
            py_data = PyLong_FromLong(*(SInt32*)data);
            if (py_data == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyObjCErr_ToObjCWithGILState(&state);
                // LCOV_EXCL_STOP
            }
            break;
        case kCFSocketAcceptCallBack:
            py_data = PyLong_FromLong(*(CFSocketNativeHandle*)data);
            if (py_data == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyObjCErr_ToObjCWithGILState(&state);
                // LCOV_EXCL_STOP
            }
            break;
        case kCFSocketDataCallBack:
            py_data = PyObjC_ObjCToPython(@encode(CFDataRef), &data);
            if (py_data == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                PyObjCErr_ToObjCWithGILState(&state);
                // LCOV_EXCL_STOP
            }
            break;
        default:
            break; // LCOV_EXCL_LINE
        }
    }

    PyObject* result =
        PyObject_CallFunction(PyTuple_GET_ITEM(info, 0), "NNNNO", py_s, py_type,
                              py_address, py_data, PyTuple_GET_ITEM(info, 1));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject* _Nullable mod_CFSocketCreate(PyObject* meth,
                                              PyObject* _Nonnull const* _Nonnull args,
                                              size_t nargs)
{
    SInt32          protocolFamily;
    SInt32          socketType;
    SInt32          protocol;
    CFAllocatorRef  allocator;
    CFOptionFlags   callBackTypes;
    CFSocketContext context = mod_CFSocketContext;

    if (PyObjC_CheckArgCount(meth, 7, 7, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(SInt32), args[1], &protocolFamily) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(SInt32), args[2], &socketType) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(SInt32), args[3], &protocol) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFOptionFlags), args[4], &callBackTypes) < 0) {
        return NULL;
    }

    context.info = PyTuple_Pack(2, args[5], args[6]);
    if (context.info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;            // LCOV_EXCL_LINE
    }

    CFSocketRef rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFSocketCreate(allocator, protocolFamily, socketType, protocol,
                                callBackTypes, mod_CFSocketCallBack, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            rv = NULL;                           // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* result = PyObjC_ObjCToPython(@encode(CFSocketRef), &rv);
    if (rv != NULL) {
        CFRelease(rv);
    }
    return result;
}

static PyObject* _Nullable mod_CFSocketCreateWithNative(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef       allocator;
    CFSocketNativeHandle sock;
    CFOptionFlags        callBackTypes;
    CFSocketContext      context = mod_CFSocketContext;

    if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFSocketNativeHandle), args[1], &sock) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFOptionFlags), args[2], &callBackTypes) < 0) {
        return NULL;
    }

    context.info = PyTuple_Pack(2, args[3], args[4]);
    if (context.info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;            // LCOV_EXCL_LINE
    }

    CFSocketRef rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFSocketCreateWithNative(allocator, sock, callBackTypes,
                                          mod_CFSocketCallBack, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            rv = NULL;                           // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* result = PyObjC_ObjCToPython(@encode(CFSocketRef), &rv);
    if (rv != NULL) {
        CFRelease(rv);
    }
    return result;
}

static PyObject* _Nullable mod_CFSocketCreateWithSocketSignature(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef    allocator;
    CFSocketSignature signature;
    CFOptionFlags     callBackTypes;
    CFSocketContext   context = mod_CFSocketContext;

    if (PyObjC_CheckArgCount(meth, 5, 5, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFSocketSignature), args[1], &signature) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFOptionFlags), args[2], &callBackTypes) < 0) {
        return NULL;
    }

    context.info = PyTuple_Pack(2, args[3], args[4]);
    if (context.info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;            // LCOV_EXCL_LINE
    }

    CFSocketRef rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFSocketCreateWithSocketSignature(allocator, &signature, callBackTypes,
                                                   mod_CFSocketCallBack, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            rv = NULL;                           // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* result = PyObjC_ObjCToPython(@encode(CFSocketRef), &rv);
    if (rv != NULL) {
        CFRelease(rv);
    }
    return result;
}

static PyObject* _Nullable mod_CFSocketCreateConnectedToSocketSignature(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFAllocatorRef    allocator;
    CFSocketSignature signature;
    CFOptionFlags     callBackTypes;
    CFTimeInterval    timeout;
    CFSocketContext   context = mod_CFSocketContext;

    if (PyObjC_CheckArgCount(meth, 6, 6, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), args[0], &allocator) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFSocketSignature), args[1], &signature) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFOptionFlags), args[2], &callBackTypes) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFTimeInterval), args[5], &timeout) < 0) {
        return NULL;
    }

    context.info = PyTuple_Pack(2, args[3], args[4]);
    if (context.info == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;            // LCOV_EXCL_LINE
    }

    CFSocketRef rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFSocketCreateConnectedToSocketSignature(
                allocator, &signature, callBackTypes, mod_CFSocketCallBack, &context,
                timeout);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            rv = NULL;                           // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    PyObject* result = PyObjC_ObjCToPython(@encode(CFSocketRef), &rv);
    if (rv != NULL) {
        CFRelease(rv);
    }
    return result;
}

static PyObject* _Nullable mod_CFSocketGetContext(PyObject* meth,
                                                  PyObject* _Nonnull const* _Nonnull args,
                                                  size_t nargs)
{
    CFSocketRef     sock;
    CFSocketContext context;

    if (PyObjC_CheckArgCount(meth, 2, 2, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFSocketRef), args[0], &sock) < 0) {
        return NULL;
    }
    if (args[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "context argument must be None");
        return NULL;
    }

    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFSocketGetContext(sock, &context);

        } @catch (NSException* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);  // LCOV_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    if (context.retain != mod_socket_retain) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
        // LCOV_EXCL_STOP
    }

    assert(context.info != NULL);

    Py_INCREF(PyTuple_GetItem(context.info, 1));
    return PyTuple_GetItem(context.info, 1);
}

static int
setup_socket(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFSocketCreate, mod_CFSocketCreate)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFSocketCreateWithNative,
                                      mod_CFSocketCreateWithNative)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFSocketCreateWithSocketSignature,
                                      mod_CFSocketCreateWithSocketSignature)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFSocketCreateConnectedToSocketSignature,
                                      mod_CFSocketCreateConnectedToSocketSignature)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyObjCRegister_FunctionCaller(CFSocketGetContext, mod_CFSocketGetContext)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

NS_ASSUME_NONNULL_END
