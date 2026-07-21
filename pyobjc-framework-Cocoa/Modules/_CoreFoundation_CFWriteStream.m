NS_ASSUME_NONNULL_BEGIN

static void*
mod_writestream_retain(void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_writestream_release(void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

static CFStreamClientContext mod_CFStreamClientContext_Write = {
    0, NULL, mod_writestream_retain, mod_writestream_release, NULL};

static void
mod_CFWriteStreamClientCallBack(CFWriteStreamRef f, CFStreamEventType eventType,
                                void* _info)
{
    PyObject*        info  = (PyObject*)_info;
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_f         = PyObjC_ObjCToPython(@encode(CFWriteStreamRef), &f);
    PyObject* py_eventType = PyObjC_ObjCToPython(@encode(CFStreamEventType), &eventType);

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "NNO", py_f,
                                             py_eventType, PyTuple_GetItem(info, 1));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject* _Nullable mod_CFWriteStreamSetClient(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFWriteStreamRef stream;
    CFOptionFlags    streamEvents;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFWriteStreamRef), args[0], &stream) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFOptionFlags), args[1], &streamEvents) < 0) {
        return NULL;
    }

    CFStreamClientContext context = mod_CFStreamClientContext_Write;
    context.info                  = PyTuple_Pack(2, args[2], args[3]);
    if (context.info == NULL) {
        return NULL;
    }

    Boolean rv = FALSE;
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (args[2] == Py_None) {
                rv = CFWriteStreamSetClient(stream, streamEvents, NULL, &context);
            } else {
                rv = CFWriteStreamSetClient(stream, streamEvents,
                                            mod_CFWriteStreamClientCallBack, &context);
            }

        } @catch (NSException* localException) {
            rv = FALSE;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS

    Py_DECREF((PyObject*)context.info);
    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyBool_FromLong(rv);
}

static int
setup_writestream(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFWriteStreamSetClient, mod_CFWriteStreamSetClient)
        == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
