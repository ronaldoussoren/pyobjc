/*
 * NSInputStream mappings for 'difficult' methods:
 *
 * -read:maxLength:
 * -getBuffer:length:
 * 
 * NSOutputStream mappings for 'difficult' methods:
 *
 * -write:maxLength:
 * 
 * Unsupported Methods
 * 
 * initToBuffer:capacity:
 * outputStreamToBuffer:capacity:
 *
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject* call_NSOutputStream_write_maxLength_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	void*		bytes;
	int		bytes_len;
	PyObject* volatile	result;
	struct objc_super super;
	long retVal;

	if (!PyArg_ParseTuple(arguments, "s#", &bytes, &bytes_len)) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		retVal = (long)objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method), bytes, bytes_len);
		
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		Py_DECREF(result);
		result = NULL;
		retVal = -1;
	PyObjC_ENDHANDLER

	if (retVal == -1 && PyErr_Occurred()) return NULL;

	result = PyInt_FromLong(retVal);

	return result;
}


static PyObject* call_NSInputStream_read_maxLength_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	int   bytes_len;
	int	  bytes_read;
	PyObject*	result;
	struct objc_super super;

	if (!PyArg_ParseTuple(arguments, "i", &bytes_len)) {
		return NULL;
	}

	result = PyString_FromStringAndSize((char *)0, bytes_len);
	if (result == NULL)
		return NULL;
	
	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		bytes_read = (int)objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method), 
				PyString_AS_STRING(result), bytes_len);
		

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		Py_XDECREF(result);
		result = NULL;
		bytes_read = -1;
	PyObjC_ENDHANDLER

	if (bytes_read == -1) {
		if (!PyErr_Occurred()) {
			Py_INCREF(Py_None);
			return Py_None;
		}
		return NULL;
	}

	if (bytes_read != bytes_len) {
		if (_PyString_Resize(&result, bytes_read) < 0) {
			return NULL;
		}
	}

	return result;
}

static PyObject* call_NSInputStream_getBytes_length_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	const void* bytes;
	unsigned    bytes_len;
	PyObject*	result;
	struct objc_super super;
	int retVal;

	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		retVal = (int)objc_msgSendSuper(&super, 
			PyObjCSelector_GetSelector(method), &bytes, &bytes_len);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		retVal = -1;
	PyObjC_ENDHANDLER


	if (retVal == -1 && PyErr_Occurred()) return NULL;

	if (retVal) {
		result = PyBuffer_FromMemory((void*)bytes, bytes_len);
	} else {
		Py_INCREF(Py_None);
		result = Py_None;
	}

	return result;
}


static int 
_pyobjc_install_NSStream(void)
{
	Class classNSInputStream = objc_lookUpClass("NSInputStream");
	Class classNSOutputStream = objc_lookUpClass("NSOutputStream");

	if (classNSInputStream != NULL) {

		if (PyObjC_RegisterMethodMapping(classNSInputStream, 
				 @selector(read:maxLength:),
				 call_NSInputStream_read_maxLength_,
				 PyObjCUnsupportedMethod_IMP) < 0 ) {
			return -1;
		}

		if (PyObjC_RegisterMethodMapping(classNSInputStream, 
				 @selector(getBytes:length:),
				 call_NSInputStream_getBytes_length_,
				 PyObjCUnsupportedMethod_IMP) < 0 ) {
			return -1;
		}
	}
	if (classNSOutputStream != NULL) {
		if (PyObjC_RegisterMethodMapping(classNSOutputStream, 
				 @selector(write:maxLength:),
				 call_NSOutputStream_write_maxLength_,
				 PyObjCUnsupportedMethod_IMP) < 0 ) {
			return -1;
		}
		if (PyObjC_RegisterMethodMapping(
				classNSOutputStream,
				@selector(outputStreamToBuffer:capacity:),
				PyObjCUnsupportedMethod_Caller,
				PyObjCUnsupportedMethod_IMP) < 0) {
			return -1;
		}
		if (PyObjC_RegisterMethodMapping(
				classNSOutputStream,
				@selector(initToBuffer:capacity:),
				PyObjCUnsupportedMethod_Caller,
				PyObjCUnsupportedMethod_IMP) < 0) {
			return -1;
		}
	}

	return 0;
}
