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


static CFMessagePortContext mod_CFMessagePortContext = {
	0,		
	NULL,
	mod_messageport_retain,
	mod_messageport_release,
	NULL
};

static CFDataRef
mod_CFMessagePortCallBack(	
	CFMessagePortRef f,
	SInt32 msgid,
	CFDataRef data,
	void* _info)
{
	PyObject* info = (PyObject*)_info;
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_f = PyObjC_ObjCToPython(@encode(CFMessagePortRef), &f);
	PyObject* py_msgid = PyObjC_ObjCToPython(
		@encode(SInt32), &msgid);
	PyObject* py_data = PyObjC_ObjCToPython(
		@encode(CFDataRef), &data);

	PyObject* result = PyObject_CallFunction(
		PyTuple_GetItem(info, 0),
		"NNNO", py_f, py_msgid, py_data, PyTuple_GetItem(info, 1));
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

static PyObject*
mod_CFMessagePortCreateLocal(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_name;
	PyObject* callout;
	PyObject* info;
	PyObject* py_shouldFree;
	CFAllocatorRef allocator;
	CFStringRef name;
	Boolean shouldFree;

	if (!PyArg_ParseTuple(args, "OOOOO", &py_allocator, &py_name, &callout, &info, &py_shouldFree)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFStringRef), py_name, &name) < 0) {
		return NULL;
	}
	if (py_shouldFree != Py_None && py_shouldFree != PyObjC_NULL) {
		PyErr_SetString(PyExc_ValueError, 
				"shouldFree not None or NULL");
		return NULL;
	}

	
	CFMessagePortContext context = mod_CFMessagePortContext;
	context.info = Py_BuildValue("OO", callout, info);
	if (context.info == NULL) {
		return NULL;
	}

	CFMessagePortRef rv = NULL;
	PyObjC_DURING
		rv = CFMessagePortCreateLocal(
			allocator, name, 
			mod_CFMessagePortCallBack, &context, &shouldFree);
		

	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);
	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* result =  Py_BuildValue("NN",
			PyObjC_ObjCToPython(@encode(CFMachPortRef), &rv),
			PyBool_FromLong(shouldFree));

	if (rv != NULL) {
		CFRelease(rv);
	}

	return result;
}

static PyObject*
mod_CFMessagePortGetContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_f;
	PyObject* py_context;
	CFMessagePortRef f;
	CFMessagePortContext context;

	if (!PyArg_ParseTuple(args, "OO", &py_f, &py_context)) {
		return NULL;
	}

	if (py_context != NULL &&  py_context != Py_None) {
		PyErr_SetString(PyExc_ValueError, "invalid context");
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFMessagePortRef), py_f, &f) < 0) {
		return NULL;
	}

	context.version = 0;

	PyObjC_DURING
		CFMessagePortGetContext(f, &context);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (context.version != 0) {
		PyErr_SetString(PyExc_ValueError, "retrieved context is not valid");
		return NULL;
	}

	if (context.retain != mod_messageport_retain) {
		PyErr_SetString(PyExc_ValueError, 
			"retrieved context is not supported");
		return NULL;
	}

	Py_INCREF(PyTuple_GetItem((PyObject*)context.info, 1));
	return PyTuple_GetItem((PyObject*)context.info, 1);
}

#define COREFOUNDATION_MESSAGEPORT_METHODS \
        {	\
		"CFMessagePortCreateLocal",	\
		(PyCFunction)mod_CFMessagePortCreateLocal,	\
		METH_VARARGS,	\
		NULL	\
	},	\
        {	\
		"CFMessagePortGetContext",	\
		(PyCFunction)mod_CFMessagePortGetContext,	\
		METH_VARARGS,	\
		NULL	\
	},
