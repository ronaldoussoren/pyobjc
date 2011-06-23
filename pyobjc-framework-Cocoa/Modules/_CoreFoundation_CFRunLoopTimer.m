static const void* 
mod_timer_retain(const void* info) 
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_INCREF((PyObject*)info);
	PyGILState_Release(state);
	return info;
}

static void
mod_timer_release(const void* info)
{
	PyGILState_STATE state = PyGILState_Ensure();
	Py_DECREF((PyObject*)info);
	PyGILState_Release(state);
}


static CFRunLoopTimerContext mod_CFRunLoopTimerContext = {
	0,		
	NULL,
	mod_timer_retain,
	mod_timer_release,
	NULL
};

static void
mod_CFRunLoopTimerCallBack(	
	CFRunLoopTimerRef f,
	void* _info)
{
	PyObject* info = (PyObject*)_info;
	PyGILState_STATE state = PyGILState_Ensure();

	PyObject* py_f = PyObjC_ObjCToPython(@encode(CFRunLoopTimerRef), &f);

	PyObject* result = PyObject_CallFunction(
		PyTuple_GetItem(info, 0),
		"NO", py_f, PyTuple_GetItem(info, 1));
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static PyObject*
mod_CFRunLoopTimerCreate(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_allocator;
	PyObject* py_fireDate;
	PyObject* py_interval;
	PyObject* py_flags;
	PyObject* py_order;
	PyObject* callout;
	PyObject* info;
	CFAllocatorRef allocator;
	CFAbsoluteTime fireDate;
	CFTimeInterval interval;
	CFOptionFlags flags;
	CFIndex order;

	if (!PyArg_ParseTuple(args, "OOOOOOO", &py_allocator, &py_fireDate, &py_interval, &py_flags, &py_order, &callout, &info)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFAllocatorRef), py_allocator, &allocator) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFAbsoluteTime), py_fireDate, &fireDate) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFTimeInterval), py_interval, &interval) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFOptionFlags), py_flags, &flags) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFIndex), py_order, &order) < 0) {
		return NULL;
	}

	CFRunLoopTimerContext context = mod_CFRunLoopTimerContext;
	context.info = Py_BuildValue("OO", callout, info);
	if (context.info == NULL) {
		return NULL;
	}

	CFRunLoopTimerRef rv = NULL;
	PyObjC_DURING
		rv = CFRunLoopTimerCreate(
			allocator, fireDate, interval, flags, order,
			mod_CFRunLoopTimerCallBack, &context);
		

	PyObjC_HANDLER
		rv = NULL;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF((PyObject*)context.info);
	if (PyErr_Occurred()) {
		return NULL;
	}

	PyObject* result =  PyObjC_ObjCToPython(@encode(CFRunLoopTimerRef), &rv);
	if (rv != NULL) {
		CFRelease(rv);
	}
	return result;
}


static PyObject*
mod_CFRunLoopTimerGetContext(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* py_f;
	PyObject* py_context = NULL;
	CFRunLoopTimerRef f;
	CFRunLoopTimerContext context;

	if (!PyArg_ParseTuple(args, "O|O", &py_f, &py_context)) {
		return NULL;
	}

	if (py_context != NULL &&  py_context != Py_None) {
		PyErr_SetString(PyExc_ValueError, "invalid context");
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFRunLoopTimerRef), py_f, &f) < 0) {
		return NULL;
	}

	context.version = 0;

	PyObjC_DURING
		CFRunLoopTimerGetContext(f, &context);

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

	if (context.retain != mod_timer_retain) {
		PyErr_SetString(PyExc_ValueError, 
			"retrieved context is not supported");
		return NULL;
	}

	if (context.info == NULL) {
		Py_INCREF(PyObjC_NULL);
		return PyObjC_NULL;
	}

	Py_INCREF(PyTuple_GetItem((PyObject*)context.info, 1));
	return PyTuple_GetItem((PyObject*)context.info, 1);
}

#define COREFOUNDATION_RUNLOOPTIMER_METHODS \
        {	\
		"CFRunLoopTimerCreate",	\
		(PyCFunction)mod_CFRunLoopTimerCreate, \
		METH_VARARGS,	\
		NULL	\
	},	\
        {	\
		"CFRunLoopTimerGetContext",	\
		(PyCFunction)mod_CFRunLoopTimerGetContext,	\
		METH_VARARGS,	\
		NULL	\
	},
