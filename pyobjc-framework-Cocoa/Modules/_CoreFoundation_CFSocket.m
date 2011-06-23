
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


static CFSocketContext mod_CFSocketContext = {
	0,		
	NULL,
	mod_socket_retain,
	mod_socket_release,
	NULL
};

static void
mod_CFSocketCallBack(	
	CFSocketRef s,
	CFSocketCallBackType type,
	CFDataRef address,
	const void* data,
	void* _info)
{
	PyObject* info = (PyObject*)_info;
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_s = PyObjC_ObjCToPython(@encode(CFSocketRef), &s);
	if (py_s == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	PyObject* py_type = PyObjC_ObjCToPython(
		@encode(CFSocketCallBackType), &type);
	if (py_type == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	PyObject* py_address = PyObjC_ObjCToPython(
		@encode(CFDataRef), &address);
	if (py_address == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	PyObject* py_data = NULL;

	if (data == NULL) {
		py_data = Py_None;
		Py_INCREF(py_data);
	} else if (type ==  kCFSocketConnectCallBack) {
		py_data = PyInt_FromLong(*(SInt32*)data);
		if (py_data == NULL) {
			PyObjCErr_ToObjCWithGILState(&state);
		}
	} else if (type == kCFSocketAcceptCallBack) {
		py_data = PyInt_FromLong(*(CFSocketNativeHandle*)data);
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


	PyObject* result = PyObject_CallFunction(
		PyTuple_GetItem(info, 0),
		"NNNNO", py_s, py_type, py_address, py_data, PyTuple_GetItem(info, 1));
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static PyObject*
mod_CFSocketCreate(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	SInt32 protocolFamily;
	SInt32 socketType;
	SInt32 protocol;
	PyObject* py_callBackTypes;
	PyObject* callout;
	PyObject* info;
	CFAllocatorRef allocator;
	CFOptionFlags callBackTypes;
	CFSocketContext	context = mod_CFSocketContext;

	if (!PyArg_ParseTuple(args, "OiiiOOO", &py_allocator, &protocolFamily, &socketType, &protocol,
		&py_callBackTypes, &callout, &info)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFOptionFlags), py_callBackTypes, &callBackTypes) < 0) {
		return NULL;
	}

	context.info = Py_BuildValue("OO", callout, info);
	if (context.info == NULL) {
		return NULL;
	}

	CFSocketRef rv = NULL;

	PyObjC_DURING
		rv = CFSocketCreate(allocator, protocolFamily, socketType, protocol, callBackTypes,
			mod_CFSocketCallBack, &context);
		
	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);
	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* result =  PyObjC_ObjCToPython(@encode(CFSocketRef), &rv);
	if (rv != NULL) {
		CFRelease(rv);
	}
	return result;
}

static PyObject*
mod_CFSocketCreateWithNative(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_sock;
	PyObject* py_callBackTypes;
	PyObject* callout;
	PyObject* info;
	CFAllocatorRef allocator;
	CFSocketNativeHandle sock;
	CFOptionFlags callBackTypes;
	CFSocketContext	context = mod_CFSocketContext;

	if (!PyArg_ParseTuple(args, "OOOOO", &py_allocator, &py_sock, 
		&py_callBackTypes, &callout, &info)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFSocketNativeHandle), py_sock, &sock) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFOptionFlags), py_callBackTypes, &callBackTypes) < 0) {
		return NULL;
	}

	context.info = Py_BuildValue("OO", callout, info);
	if (context.info == NULL) {
		return NULL;
	}

	CFSocketRef rv = NULL;

	PyObjC_DURING
		rv = CFSocketCreateWithNative(allocator, sock, callBackTypes,
			mod_CFSocketCallBack, &context);
		
	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);
	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* result =  PyObjC_ObjCToPython(@encode(CFSocketRef), &rv);
	if (rv != NULL) {
		CFRelease(rv);
	}
	return result;
}

static PyObject*
mod_CFSocketCreateWithSocketSignature(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_signature;
	PyObject* py_callBackTypes;
	PyObject* callout;
	PyObject* info;
	CFAllocatorRef allocator;
	CFSocketSignature signature;
	CFOptionFlags callBackTypes;
	CFSocketContext	context = mod_CFSocketContext;

	if (!PyArg_ParseTuple(args, "OOOOO", &py_allocator, &py_signature, 
		&py_callBackTypes, &callout, &info)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFSocketSignature), py_signature, &signature) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFOptionFlags), py_callBackTypes, &callBackTypes) < 0) {
		return NULL;
	}

	context.info = Py_BuildValue("OO", callout, info);
	if (context.info == NULL) {
		return NULL;
	}

	CFSocketRef rv = NULL;

	PyObjC_DURING
		rv = CFSocketCreateWithSocketSignature(allocator, &signature, callBackTypes,
			mod_CFSocketCallBack, &context);
		
	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);
	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* result =  PyObjC_ObjCToPython(@encode(CFSocketRef), &rv);
	if (rv != NULL) {
		CFRelease(rv);
	}
	return result;
}

static PyObject*
mod_CFSocketCreateConnectedToSocketSignature(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_signature;
	PyObject* py_callBackTypes;
	PyObject* callout;
	PyObject* info;
	PyObject* py_timeout;
	CFAllocatorRef allocator;
	CFSocketSignature signature;
	CFOptionFlags callBackTypes;
	CFTimeInterval timeout;
	CFSocketContext	context = mod_CFSocketContext;

	if (!PyArg_ParseTuple(args, "OOOOOO", &py_allocator, &py_signature, 
		&py_callBackTypes, &callout, &info, &py_timeout)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFSocketSignature), py_signature, &signature) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFOptionFlags), py_callBackTypes, &callBackTypes) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFTimeInterval), py_timeout, &timeout) < 0) {
		return NULL;
	}

	context.info = Py_BuildValue("OO", callout, info);
	if (context.info == NULL) {
		return NULL;
	}

	CFSocketRef rv = NULL;

	PyObjC_DURING
		rv = CFSocketCreateConnectedToSocketSignature(allocator, &signature, callBackTypes,
			mod_CFSocketCallBack, &context, timeout);
		
	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);
	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* result =  PyObjC_ObjCToPython(@encode(CFSocketRef), &rv);
	if (rv != NULL) {
		CFRelease(rv);
	}
	return result;
}

static PyObject*
mod_CFSocketGetContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_sock;
	PyObject* py_context;
	CFSocketRef sock;
	CFSocketContext context;

	if (!PyArg_ParseTuple(args, "OO", &py_sock, &py_context)) { 
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFSocketRef), py_sock, &sock) < 0) {
		return NULL;
	}
	if (py_context != Py_None) {
		PyErr_SetString(PyExc_ValueError, "context argument must be None");
		return NULL;
	}

	context.version = 0;

	PyObjC_DURING
		CFSocketGetContext(sock, &context);
		
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

        if (context.retain != mod_socket_retain) {
		PyErr_SetString(PyExc_ValueError,
			"retrieved context is not supported");
		return NULL;
	}

	if (context.info == NULL) {
		Py_INCREF(PyObjC_NULL);
		return PyObjC_NULL;
	}


	Py_INCREF(PyTuple_GetItem(context.info, 1));
	return PyTuple_GetItem(context.info, 1);
}

#define COREFOUNDATION_SOCKET_METHODS \
        {	\
		"CFSocketCreate",	\
		(PyCFunction)mod_CFSocketCreate,	\
		METH_VARARGS,	\
		NULL	\
	},	\
        {	\
		"CFSocketCreateWithNative",	\
		(PyCFunction)mod_CFSocketCreateWithNative,	\
		METH_VARARGS,	\
		NULL	\
	},	\
        {	\
		"CFSocketCreateWithSocketSignature",	\
		(PyCFunction)mod_CFSocketCreateWithSocketSignature,	\
		METH_VARARGS,	\
		NULL	\
	},	\
        {	\
		"CFSocketCreateConnectedToSocketSignature",	\
		(PyCFunction)mod_CFSocketCreateConnectedToSocketSignature,	\
		METH_VARARGS,	\
		NULL	\
	},	\
        {	\
		"CFSocketGetContext",	\
		(PyCFunction)mod_CFSocketGetContext,	\
		METH_VARARGS,	\
		NULL	\
	},
