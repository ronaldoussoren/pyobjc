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
	0,		
	NULL,
	mod_readstream_retain,
	mod_readstream_release,
	NULL
};

static void
mod_CFReadStreamClientCallBack(	
	CFReadStreamRef f,
	CFStreamEventType eventType,
	void* _info)
{
	PyObject* info = (PyObject*)_info;
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_f = PyObjC_ObjCToPython(@encode(CFReadStreamRef), &f);
	PyObject* py_eventType = PyObjC_ObjCToPython(
		@encode(CFStreamEventType), &eventType);

	PyObject* result = PyObject_CallFunction(
		PyTuple_GetItem(info, 0),
		"NNO", py_f, py_eventType, PyTuple_GetItem(info, 1));
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static PyObject*
mod_CFReadStreamSetClient(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_stream;
	PyObject* py_streamEvents;
	PyObject* callout;
	PyObject* info;
	CFReadStreamRef stream;
	CFOptionFlags streamEvents;
	CFStreamClientContext context;

	if (!PyArg_ParseTuple(args, "OOOO", &py_stream, &py_streamEvents, &callout, &info)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFReadStreamRef), py_stream, &stream) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFOptionFlags), py_streamEvents, &streamEvents) < 0) {
		return NULL;
	}

	if (info != PyObjC_NULL) {
		context = mod_CFStreamClientContext_Read;
		context.info = Py_BuildValue("OO", callout, info);
		if (context.info == NULL) {
			return NULL;
		}
	}


	Boolean rv = FALSE;
	PyObjC_DURING
		if (info == PyObjC_NULL) {
			rv = CFReadStreamSetClient(
				stream, streamEvents, 
				mod_CFReadStreamClientCallBack, NULL);
		} else {
			rv = CFReadStreamSetClient(
				stream, streamEvents, 
				mod_CFReadStreamClientCallBack, &context);
		}

		
	PyObjC_HANDLER
		rv = FALSE;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER
	if (info != PyObjC_NULL) {
		Py_DECREF((PyObject*)context.info);
	}

	if (PyErr_Occurred()) {
		return NULL;
	}

	return PyBool_FromLong(rv);
}

#define COREFOUNDATION_READSTREAM_METHODS \
        {	\
		"CFReadStreamSetClient",	\
		(PyCFunction)mod_CFReadStreamSetClient,	\
		METH_VARARGS,	\
		NULL	\
	},
