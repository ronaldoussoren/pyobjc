/*
 * Special wrappers for NSString methods with 'difficult' arguments.
 *
 * -getCString:maxLength:range:remainingRange:	[call]
 * -getCString:maxLength:			[call]
 *
 */

static PyObject*
call_NSString_getCString_maxLength_range_remainingRange_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* rangeObj;
	NSRange aRange;
	NSRange leftoverRange;
	NSRange* leftoverPtr;
	char* buf;
	NSUInteger maxLength;
	struct objc_super super;
	PyObject* res;
	PyObject* buf1, *buf2;

	if  (!PyArg_ParseTuple(arguments, "O" Py_ARG_NSUInteger "OO", &buf1, &maxLength, &rangeObj, &buf2)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSRange), rangeObj, &aRange) < 0) {
		return NULL;
	}

	if (buf1 != Py_None) {
		PyErr_SetString(PyExc_ValueError, "output buffer must be None");
		return NULL;
	}
	if (buf2 != Py_None && buf2 != PyObjC_NULL) {
		PyErr_SetString(PyExc_ValueError, "range buffer must be None or NULL");
		return NULL;
	}
	if (buf2 == PyObjC_NULL) {
		leftoverPtr = NULL;
	} else { 
		leftoverPtr = &leftoverRange;
	}


	buf = malloc(maxLength+1);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		((void(*)(struct objc_super*, SEL, void*, NSInteger, NSRange, NSRange*))objc_msgSendSuper)(&super,
			@selector(getCString:maxLength:range:remainingRange:),
			buf, maxLength, aRange, leftoverPtr);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		free(buf);
		return NULL;
	}
	
	res = PyTuple_New(2);
	if (res == NULL) {
		free(buf);
		return NULL;
	}

	PyTuple_SetItem(res, 0, PyBytes_FromString(buf));
	free(buf);
	if (PyErr_Occurred()) {
		Py_DECREF(res);
		free(buf);
		return NULL;
	}

	if (leftoverPtr != NULL) {
		rangeObj = PyObjC_ObjCToPython(@encode(NSRange), &leftoverRange);
		if (rangeObj == NULL) {
			Py_DECREF(res);
			return NULL;
		}

		PyTuple_SetItem(res, 1, rangeObj);
	} else {
		PyTuple_SetItem(res, 1, PyObjC_NULL);
	}
	return res;
}

static PyObject*
call_NSString_getCString_maxLength_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* buf;
	NSUInteger maxLength;
	struct objc_super super;
	PyObject* res;
	PyObject* py_buf;

	if  (!PyArg_ParseTuple(arguments, "O" Py_ARG_NSUInteger, &py_buf, &maxLength)) {
		return NULL;
	}
	if (py_buf != Py_None) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}

	buf = malloc(maxLength+1);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		((void(*)(struct objc_super*, SEL, void*, NSUInteger))objc_msgSendSuper)(&super,
			@selector(getCString:maxLength:),
			buf, maxLength);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		free(buf);
		return NULL;
	}
	
	res = PyBytes_FromString(buf);
	free(buf);
	if (res == NULL) {
		return NULL;
	}

	return res;
}

static int setup_nssstring(PyObject* m __attribute__((__unused__)))
{
	Class classNSString = objc_lookUpClass("NSString");
	if (classNSString == NULL) {
		return 0;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSString,
		@selector(getCString:maxLength:range:remainingRange:),
		call_NSString_getCString_maxLength_range_remainingRange_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSString,
		@selector(getCString:maxLength:),
		call_NSString_getCString_maxLength_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
