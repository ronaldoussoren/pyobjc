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
    if (py_s == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    PyObject* py_type = PyObjC_ObjCToPython(@encode(CFSocketCallBackType), &type);
    if (py_type == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    PyObject* py_address = PyObjC_ObjCToPython(@encode(CFDataRef), &address);
    if (py_address == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    PyObject* py_data = NULL;

    if (data == NULL) {
        py_data = Py_None;
        Py_INCREF(py_data);
    } else if (type == kCFSocketConnectCallBack) {
        py_data = PyLong_FromLong(*(SInt32*)data);
        if (py_data == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
    } else if (type == kCFSocketAcceptCallBack) {
        py_data = PyLong_FromLong(*(CFSocketNativeHandle*)data);
        if (py_data == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
    } else if (type == kCFSocketDataCallBack) {
        py_data = PyObjC_ObjCToPython(@encode(CFDataRef), &data);
        if (py_data == NULL) {
            PyObjCErr_ToObjCWithGILState(&state);
        }
    } else {
        /* FIXME: should warn about unhandled data */
        py_data = Py_None;
        Py_INCREF(py_data);
    }

    PyObject* result =
        PyObject_CallFunction(PyTuple_GetItem(info, 0), "NNNNO", py_s, py_type,
                              py_address, py_data, PyTuple_GetItem(info, 1));
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
    if (context.info == NULL) {
        return NULL;
    }

    CFSocketRef rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFSocketCreate(allocator, protocolFamily, socketType, protocol,
                                callBackTypes, mod_CFSocketCallBack, &context);

        } @catch (NSException* localException) {
            rv = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) {
        return NULL;
    }

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
    if (context.info == NULL) {
        return NULL;
    }

    CFSocketRef rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFSocketCreateWithNative(allocator, sock, callBackTypes,
                                          mod_CFSocketCallBack, &context);

        } @catch (NSException* localException) {
            rv = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) {
        return NULL;
    }

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
    if (context.info == NULL) {
        return NULL;
    }

    CFSocketRef rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFSocketCreateWithSocketSignature(allocator, &signature, callBackTypes,
                                                   mod_CFSocketCallBack, &context);

        } @catch (NSException* localException) {
            rv = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) {
        return NULL;
    }

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
    if (context.info == NULL) {
        return NULL;
    }

    CFSocketRef rv = NULL;

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFSocketCreateConnectedToSocketSignature(
                allocator, &signature, callBackTypes, mod_CFSocketCallBack, &context,
                timeout);

        } @catch (NSException* localException) {
            rv = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) {
        return NULL;
    }

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

        } @catch (NSException* localException) {
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    if (context.retain != mod_socket_retain) {
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
    }

    if (context.info == NULL) {
        Py_INCREF(PyObjC_NULL);
        return PyObjC_NULL;
    }

    Py_INCREF(PyTuple_GetItem(context.info, 1));
    return PyTuple_GetItem(context.info, 1);
}

static int
setup_socket(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFSocketCreate, mod_CFSocketCreate) == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFSocketCreateWithNative,
                                      mod_CFSocketCreateWithNative)
        == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFSocketCreateWithSocketSignature,
                                      mod_CFSocketCreateWithSocketSignature)
        == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFSocketCreateConnectedToSocketSignature,
                                      mod_CFSocketCreateConnectedToSocketSignature)
        == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFSocketGetContext, mod_CFSocketGetContext) == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
