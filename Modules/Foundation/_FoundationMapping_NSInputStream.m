/*
 * Special wrappers for NSInputStream methods with 'difficult' arguments.
 *
 * -getBuffer:length:	[call]
 *
 * PLATFORM: MacOS X 10.3
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject*
call_NSInputStream_getBuffer_length_(PyObject* method,
	PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	char* buf;
	int   buflen;
	BOOL res;
	PyObject* retVal;
	PyObject* v;

	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		res = (BOOL)(int)objc_msgSendSuper(&super, @selector(getBuffer:length:),
			&buf, &buflen);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		buf = NULL;
		buflen = -1;
	NS_ENDHANDLER

	if (buf == NULL && PyErr_Occurred()) {
		return NULL;
	}

	retVal = PyTuple_New(3);
	if (retVal == NULL) {
		return NULL;
	}

	v = PyObjC_ObjCToPython(@encode(BOOL), &res);
	if (v == NULL) {
		return NULL;
	}
	PyTuple_SET_ITEM(retVal, 0, v);

	v = PyBuffer_FromReadWriteMemory(buf, buflen);
	if (v == NULL) {
		return NULL;
	}
	PyTuple_SET_ITEM(retVal, 1, v);

	v = PyInt_FromLong(buflen);
	if (v == NULL) {
		return NULL;
	}
	PyTuple_SET_ITEM(retVal, 2, v);

	return retVal;
}


static int 
_pyobjc_install_NSInputStream(void)
{
	Class classNSInputStream = objc_lookUpClass("NSInputStream");
	if (classNSInputStream == NULL) {
		return 0;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSInputStream,
		@selector(getBuffer:length:),
		call_NSInputStream_getBuffer_length_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
