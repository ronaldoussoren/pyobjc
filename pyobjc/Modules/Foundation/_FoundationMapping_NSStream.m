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

	if (!PyArg_ParseTuple(arguments, "s#", &bytes, &bytes_len)) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		result = PyInt_FromLong((long)objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method), bytes, bytes_len));
		
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		Py_DECREF(result);
		result = NULL;
	NS_ENDHANDLER

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
	
	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		bytes_read = (int)objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method), 
				PyString_AS_STRING(result), bytes_len);
		
		if (bytes_read != bytes_len) {
			if (_PyString_Resize(&result, bytes_read) < 0) {
				return NULL;
			}
		}

	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		Py_XDECREF(result);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject* call_NSInputStream_getBytes_length_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	const void* bytes;
	unsigned    bytes_len;
	PyObject*	result;
	struct objc_super super;

	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		if (objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method), &bytes, &bytes_len)) {
			result = PyBuffer_FromMemory((void*)bytes, bytes_len);
		} else {
			Py_INCREF(Py_None);
			result = Py_None;
		}

	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

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
