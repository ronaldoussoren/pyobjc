static PyObject* 
call_NSView_getRectsBeingDrawn_count_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	PyObject* v;
	NSRect* rects;
	PyObject* arg1, *arg2;
	NSInteger count;

	if  (!PyArg_ParseTuple(arguments, "OO", &arg1, &arg2)) {
		return NULL;
	}

	if (arg1 != Py_None) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}
	if (arg2 != Py_None) {
		PyErr_SetString(PyExc_ValueError, "count must be None");
		return NULL;
	}


	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

			
		((void(*)(struct objc_super*, SEL, NSRect**, NSInteger*))objc_msgSendSuper)(&super,
				PyObjCSelector_GetSelector(method),
				&rects, &count);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	v = PyObjC_CArrayToPython(
#ifdef __LP64__
	"{_NSRect={_NSPoint=dd}{_NSSize=dd}}",
#else
	"{_NSRect={_NSPoint=ff}{_NSSize=ff}}",
#endif
		rects, count);
	if (v == NULL) return NULL;

	result = Py_BuildValue("Oi", v, count);
	Py_XDECREF(v);

	return result;
}



static int setup_nsview(PyObject* m __attribute__((__unused__)))
{
	Class classNSView = objc_lookUpClass("NSView");
	if (classNSView == NULL) {
		return 0;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSView,
		@selector(getRectsBeingDrawn:count:),
		call_NSView_getRectsBeingDrawn_count_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
