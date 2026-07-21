NS_ASSUME_NONNULL_BEGIN

static void*
mod_readstream_retain(void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_INCREF((PyObject*)info);
    PyGILState_Release(state);
    return info;
}

static void
mod_readstream_release(void* info)
{
    PyGILState_STATE state = PyGILState_Ensure();
    Py_DECREF((PyObject*)info);
    PyGILState_Release(state);
}

static CFStreamClientContext mod_CFStreamClientContext_Read = {
    0, NULL, mod_readstream_retain, mod_readstream_release, NULL};

static void
mod_CFReadStreamClientCallBack(CFReadStreamRef f, CFStreamEventType eventType,
                               void* _info)
{
    PyObject*        info  = (PyObject*)_info;
    PyGILState_STATE state = PyGILState_Ensure();

    PyObject* py_f         = PyObjC_ObjCToPython(@encode(CFReadStreamRef), &f);
    PyObject* py_eventType = PyObjC_ObjCToPython(@encode(CFStreamEventType), &eventType);

    PyObject* result = PyObject_CallFunction(PyTuple_GetItem(info, 0), "NNO", py_f,
                                             py_eventType, PyTuple_GetItem(info, 1));
    if (result == NULL) {
        PyObjCErr_ToObjCWithGILState(&state);
    }
    Py_DECREF(result);
    PyGILState_Release(state);
}

static PyObject* _Nullable mod_CFReadStreamSetClient(
    PyObject* meth, PyObject* _Nonnull const* _Nonnull args, size_t nargs)
{
    CFReadStreamRef       stream;
    CFOptionFlags         streamEvents;
    CFStreamClientContext context;

    if (PyObjC_CheckArgCount(meth, 4, 4, nargs) == -1) {
        return NULL;
    }

    if (PyObjC_PythonToObjC(@encode(CFReadStreamRef), args[0], &stream) < 0) {
        return NULL;
    }
    if (PyObjC_PythonToObjC(@encode(CFOptionFlags), args[1], &streamEvents) < 0) {
        return NULL;
    }

    if (args[2] != NULL && (args[3] != PyObjC_NULL && args[3] != Py_None)) {
        context      = mod_CFStreamClientContext_Read;
        context.info = PyTuple_Pack(2, args[2], args[3]);
        if (context.info == NULL) {
            return NULL;
        }
    }

    Boolean rv = FALSE;
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (args[2] == Py_None) {
                if (args[3] == PyObjC_NULL || args[3] == Py_None) {
                    rv = CFReadStreamSetClient(stream, streamEvents, NULL, NULL);
                }

            } else {
                if (args[3] == PyObjC_NULL || args[3] == Py_None) {
                    rv = CFReadStreamSetClient(stream, streamEvents,
                                               mod_CFReadStreamClientCallBack, NULL);
                } else {
                    rv = CFReadStreamSetClient(stream, streamEvents,
                                               mod_CFReadStreamClientCallBack, &context);
                }
            }

        } @catch (NSException* localException) {
            rv = FALSE;
            PyObjCErr_FromObjC(localException);
        }
    Py_END_ALLOW_THREADS
    if (args[3] != PyObjC_NULL) {
        Py_DECREF((PyObject*)context.info);
    }

    if (PyErr_Occurred()) {
        return NULL;
    }

    return PyBool_FromLong(rv);
}

static int
setup_readstream(PyObject* m __attribute__((__unused__)))
{
    if (PyObjCRegister_FunctionCaller(CFReadStreamSetClient, mod_CFReadStreamSetClient)
        == -1) {
        return -1;
    }
    return 0;
}

NS_ASSUME_NONNULL_END
