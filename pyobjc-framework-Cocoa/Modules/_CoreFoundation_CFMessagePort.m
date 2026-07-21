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

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "NNNO", py_f,
                                             py_msgid, py_data, PyTuple_GetItem(info, 1));
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
        PyErr_SetString(PyExc_ValueError, "shouldFree not None or NULL");
        return NULL;
    }

    CFMessagePortContext context = mod_CFMessagePortContext;
    context.info                 = PyTuple_Pack(2, args[2], args[3]);
    if (context.info == NULL) {
        return NULL;
    }

    CFMessagePortRef rv = NULL;
    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = CFMessagePortCreateLocal(allocator, name, mod_CFMessagePortCallBack,
                                          &context,
                                          args[4] == PyObjC_NULL ? NULL : &shouldFree);

        } @catch (NSException* localException) {
            rv = NULL;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) {
        return NULL;
    }

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

    if (args[1] != NULL && args[1] != Py_None) {
        PyErr_SetString(PyExc_ValueError, "invalid context");
        return NULL;
    }

    context.version = 0;

    Py_BEGIN_ALLOW_THREADS
        @try {
            CFMessagePortGetContext(f, &context);

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

    if (context.retain != mod_messageport_retain) {
        PyErr_SetString(PyExc_ValueError, "retrieved context is not supported");
        return NULL;
    }

    Py_INCREF(PyTuple_GetItem((PyObject*)context.info, 1));
    return PyTuple_GetItem((PyObject*)context.info, 1);
}

static int
setup_messageport(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFMessagePortCreateLocal,
                                      mod_CFMessagePortCreateLocal)
        == -1) {
        return -1;
    }
    if (PyObjCRegister_FunctionCaller(CFMessagePortGetContext,
                                      mod_CFMessagePortGetContext)
        == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
