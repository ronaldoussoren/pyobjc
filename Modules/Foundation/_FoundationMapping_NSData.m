/*
 * NSData mappings for 'difficult' methods:
 *
 * -initWithBytes:length:
 * +dataWithBytes:lenght:
 * -bytes
 * -mutableBytes
 *
 * TODO:
 * -getBytes:
 * -getBytes:length:
 * -getBytes:range:
 *
 *
 * Unsupported methods:
 * +dataWithBytesNoCopy:length:
 * +dataWithBytesNoCopy:length:freeWhenDone:
 * -initWithBytesNoCopy:length:
 * -initWithBytesNoCopy:length:freeWhenDone:

 * Undocumented methods:
 * -initWithBytes:length:copy:freeWhenDone:bytesAreVM:
 * 
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"


static PyObject* call_NSData_dataWithBytes_length_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	struct objc_super super;
	id        objc_result;

	if  (!PyArg_ParseTuple(arguments, "t#i", &bytes, &bytes_len, &len)) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuperCls(&super, PyObjCSelector_GetClass(method), PyObjCClass_GetClass(self));

		objc_result = objc_msgSendSuper(&super,
				@selector(dataWithBytes:length:),
				bytes, len);
		result = PyObjC_IdToPython(objc_result);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}


static id imp_NSData_dataWithBytes_length_(id self, SEL sel,
		char* data, unsigned len)
{
	PyObject* result;
	PyObject* arglist;
	id        objc_result;

	arglist = PyTuple_New(2);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromStringAndSize(data, len));
	PyTuple_SetItem(arglist, 1, PyInt_FromLong(len));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	objc_result = PyObjC_PythonToId(result);
	Py_DECREF(result);

	if (PyErr_Occurred()) {
		PyObjCErr_ToObjC();
		return nil;
	}

	return objc_result;
}


static PyObject* call_NSData_initWithBytes_length_(
		PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	struct objc_super super;
	id        objc_result;

	if  (!PyArg_ParseTuple(arguments, "t#i", &bytes, &bytes_len, &len)) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));

		objc_result = objc_msgSendSuper(&super,
				@selector(initWithBytes:length:),
				bytes, len);
		result = PyObjC_IdToPython(objc_result);

		/* XXX Ronald: If you try to use the result of 
		 * PyObjCObject_GetObject(self) after the call to objc_msgSend 
		 * it will crash with large enough values of len (>=32). 
		 * Appearently the original self is recycled during the init.
		 */
		if (self != result) {
			PyObjCObject_ClearObject(self);
		}
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}


static id imp_NSData_initWithBytes_length_(id self, SEL sel,
		char* data, unsigned len)
{
	PyObject* result;
	PyObject* arglist;
	id        objc_result;

	arglist = PyTuple_New(2);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromStringAndSize(data, len));
	PyTuple_SetItem(arglist, 1, PyInt_FromLong(len));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	objc_result = PyObjC_PythonToId(result);
	Py_DECREF(result);

	if (PyErr_Occurred()) {
		PyObjCErr_ToObjC();
		return nil;
	}

	return objc_result;
}


static PyObject* call_NSData_bytes(PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
	const void* bytes;
	unsigned    bytes_len;
	PyObject* result;
	struct objc_super super;

	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));

		bytes = objc_msgSendSuper(&super, @selector(bytes));
		bytes_len = (unsigned) objc_msgSendSuper(&super, @selector(length));

		result = PyBuffer_FromMemory((void*)bytes, bytes_len);

	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void *imp_NSData_bytes(id self, SEL sel)
{
	PyObject* result;

	result = PyObjC_CallPython(self, sel, NULL, NULL);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return NULL;
	}

	if (result == Py_None) {
		Py_DECREF(result);
		return NULL;
	}

	if (PyBuffer_Check(result)) {
		const void *p;
		int len;
		if (PyObject_AsReadBuffer(result, &p, &len) == -1) {
			PyObjCErr_ToObjC();
			return NULL;
		}
		Py_DECREF(result);
		return (void *)p;
	}

	PyErr_SetString(PyExc_ValueError, "No idea what to do with result.");
	PyObjCErr_ToObjC();
	return NULL;
}


static PyObject* call_NSMutableData_mutableBytes(PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
	void*     bytes;
	unsigned  bytes_len;
	PyObject* result;
	struct objc_super super;

	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
		PyObjCClass_GetClass((PyObject*)(self->ob_type)),
		PyObjCObject_GetObject(self));

		bytes = objc_msgSendSuper(&super, @selector(mutableBytes));
		bytes_len = (unsigned) objc_msgSendSuper(&super, @selector(length));

		result = PyBuffer_FromReadWriteMemory((void*)bytes, bytes_len);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void *imp_NSMutableData_mutableBytes(id self, SEL sel)
{
	PyObject* result;

	result = PyObjC_CallPython(self, sel, NULL, NULL);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return NULL;
	}

	if (result == Py_None) {
		Py_DECREF(result);
		return NULL;
	}

	if (PyBuffer_Check(result)) {
		void *p;
		int len;
		if (PyObject_AsWriteBuffer(result, &p, &len) == -1) {
			PyObjCErr_ToObjC();
			return NULL;
		}
		Py_DECREF(result);
		return (void *)p;
	}

	PyErr_SetString(PyExc_ValueError, "No idea what to do with result.");
	PyObjCErr_ToObjC();
	return NULL;
}

static int 
_pyobjc_install_NSData(void)
{
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSData"), 
				 @selector(initWithBytes:length:),
				 call_NSData_initWithBytes_length_,
				 (IMP)imp_NSData_initWithBytes_length_) < 0 ) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSData"), 
				 @selector(dataWithBytes:length:),
				 call_NSData_dataWithBytes_length_,
				 (IMP)imp_NSData_dataWithBytes_length_) < 0 ) {
		return -1;
	}
  
	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSData"), 
				 @selector(bytes),
				 call_NSData_bytes,
				 (IMP)imp_NSData_bytes) < 0 ) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(objc_lookUpClass("NSMutableData"), 
				@selector(mutableBytes),
				call_NSMutableData_mutableBytes,
				(IMP)imp_NSMutableData_mutableBytes) < 0 ) {
		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
				objc_lookUpClass("NSData"),
				@selector(initWithBytes:length:copy:freeWhenDone:bytesAreVM:),
				PyObjCUnsupportedMethod_Caller,
				PyObjCUnsupportedMethod_IMP) < 0) {
		return -1;	
	}
  
	return 0;
}
