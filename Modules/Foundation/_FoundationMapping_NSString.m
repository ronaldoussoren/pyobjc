/*
 * Special wrappers for NSString methods with 'difficult' arguments.
 *
 * -getCString:maxLength:range:remainingRange:	[call]
 * -getCString:maxLength:			[call]
 *
 * TODO:
 * -getCharacters:
 * -getCharacters:range:
 * -getCString:
 *
 * Unsupported methods: 
 * -initWithCharactersNoCopy:length:freeWhenDone:
 * 
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"


static PyObject*
call_NSString_getCString_maxLength_range_remainingRange_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* rangeObj;
	NSRange aRange;
	NSRange leftoverRange;
	char* buf;
	int maxLength;
	struct objc_super super;
	PyObject* res;

	if  (!PyArg_ParseTuple(arguments, "iO", &maxLength, &rangeObj)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSRange), rangeObj, &aRange) < 0) {
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

		(void)objc_msgSendSuper(&super,
			@selector(getCString:maxLength:range:remainingRange:),
			buf, maxLength, aRange, &leftoverRange);
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

	PyTuple_SET_ITEM(res, 0, PyString_FromString(buf));
	free(buf);
	if (PyErr_Occurred()) {
		Py_DECREF(res);
		free(buf);
		return NULL;
	}

	rangeObj = PyObjC_ObjCToPython(@encode(NSRange), &leftoverRange);
	if (rangeObj == NULL) {
		Py_DECREF(res);
		return NULL;
	}

	PyTuple_SET_ITEM(res, 1, rangeObj);
	return res;
}

static PyObject*
call_NSString_getCString_maxLength_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	char* buf;
	int maxLength;
	struct objc_super super;
	PyObject* res;

	if  (!PyArg_ParseTuple(arguments, "i", &maxLength)) {
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

		(void)objc_msgSendSuper(&super,
			@selector(getCString:maxLength:),
			buf, maxLength);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		free(buf);
		return NULL;
	}
	
	res = PyString_FromString(buf);
	free(buf);
	if (res == NULL) {
		return NULL;
	}

	return res;
}


static int 
_pyobjc_install_NSString(void)
{
	Class classNSString = objc_lookUpClass("NSString");
	if (classNSString == NULL) return 0;

	if (PyObjC_RegisterMethodMapping(
		classNSString,
		@selector(initWithCharactersNoCopy:length:freeWhenDone:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSString,
		@selector(getCString:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSString,
		@selector(getCharacters:range:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSString,
		@selector(getCharacters:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
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
