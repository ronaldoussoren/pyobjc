/*
 * NSData mappings for 'difficult' methods:
 *
 * -initWithBytes:length:
 * +dataWithBytes:length:
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


static PyObject* 
call_NSData_dataWithBytes_length_(
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

	PyObjC_DURING
		PyObjC_InitSuperCls(&super, 
			PyObjCSelector_GetClass(method), 
			PyObjCClass_GetClass(self));

		objc_result = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				bytes, len);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		objc_result = nil;
	PyObjC_ENDHANDLER
	
	if (objc_result == nil && PyErr_Occurred()) return NULL;

	result = PyObjC_IdToPython(objc_result);

	return result;
}


static void 
imp_NSData_dataWithBytes_length_(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	char* data = *(char**)args[2];
	unsigned len = *(unsigned*)args[3];
	id* pretval = (id*)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0, v); 

	v = PyString_FromStringAndSize(data, len);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v); 

	v = PyInt_FromLong(len);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 2, v); 


	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	*pretval = PyObjC_PythonToId(result);
	Py_DECREF(result);

	if (*pretval == nil && PyErr_Occurred()) goto error;

	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
	*pretval = nil;
}


static PyObject* call_NSData_initWithBytes_length_(
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

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		objc_result = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				bytes, len);
		result = PyObjC_IdToPython(objc_result);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	PyObjC_ENDHANDLER

	/* XXX Ronald: If you try to use the result of 
	 * PyObjCObject_GetObject(self) after the call to objc_msgSend 
	 * it will crash with large enough values of len (>=32). 
	 * Appearently the original self is recycled during the init.
	 */
	if (self != result) {
		PyObjCObject_ClearObject(self);
	}

	return result;
}


static void
imp_NSData_initWithBytes_length_(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	char* data = *(char**)args[2];
	unsigned len = *(unsigned*)args[3];
	id* pretval = (id*)resp;

	PyObject* result;
	PyObject* v;
	PyObject* arglist = NULL;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 0, v); 

	v = PyString_FromStringAndSize(data, len);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 1, v); 

	v = PyInt_FromLong(len);
	if (v == NULL) goto error;
	PyTuple_SetItem(arglist, 2, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	*pretval = PyObjC_PythonToId(result);
	Py_DECREF(result);

	if (*pretval == nil && PyErr_Occurred()) goto error;

	PyGILState_Release(state);
	return;

error:
	*pretval = nil;
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
}


static PyObject* call_NSData_bytes(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	const void* bytes;
	unsigned    bytes_len;
	PyObject* result;
	struct objc_super super;

	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		bytes = objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method));
		bytes_len = (unsigned) objc_msgSendSuper(&super, @selector(length));


	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		bytes = NULL;
	PyObjC_ENDHANDLER

	if (bytes == NULL && PyErr_Occurred()) return NULL;

	result = PyBuffer_FromMemory((void*)bytes, bytes_len);

	return result;
}

static void 
imp_NSData_bytes(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	void** pretval = (void**)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 0, v);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	if (result == Py_None) {
		*pretval = NULL;
		Py_DECREF(result);
		PyGILState_Release(state);
		return;
	}

	if (PyBuffer_Check(result)) {
		/* XXX: Is this correct?? */
		const void *p;
		int len;
		if (PyObject_AsReadBuffer(result, &p, &len) == -1) {
			goto error;
		}
		Py_DECREF(result);
		*pretval =  (void *)p;
		PyGILState_Release(state);
		return;
	} else if (PyString_Check(result)) {
		/* XXX: Is this correct */
		void* p;

		p = PyString_AsString(result);
		*pretval = (void*)p;
		PyGILState_Release(state);
		return;
	}

	PyErr_SetString(PyExc_ValueError, "No idea what to do with result.");
	goto error;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
	*pretval = NULL;
}


static PyObject* 
call_NSMutableData_mutableBytes(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	void*     bytes;
	unsigned  bytes_len;
	PyObject* result;
	struct objc_super super;

	if (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super,
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		bytes = objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method));
		bytes_len = (unsigned) objc_msgSendSuper(&super, @selector(length));

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		bytes = NULL;
	PyObjC_ENDHANDLER

	if (bytes == NULL && PyErr_Occurred()) return NULL;

	result = PyBuffer_FromReadWriteMemory((void*)bytes, bytes_len);

	return result;
}

static void
imp_NSMutableData_mutableBytes(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	void** pretval = (void**)resp;
	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 0, v);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	if (result == Py_None) {
		Py_DECREF(result);
		goto error;
	}

	if (result == Py_None) {
		*pretval = NULL;
		Py_DECREF(result);
		PyGILState_Release(state);
		return;
	}

	if (PyBuffer_Check(result)) {
		/* XXX: Is this correct? */
		void *p;
		int len;
		if (PyObject_AsWriteBuffer(result, &p, &len) == -1) goto error;
		Py_DECREF(result);
		*pretval = (void *)p;
		PyGILState_Release(state);
		return;
	}

	PyErr_SetString(PyExc_ValueError, "No idea what to do with result.");
	PyObjCErr_ToObjCWithGILState(&state);
	*pretval = NULL;
	return;

error:
	Py_XDECREF(arglist);
	*pretval = NULL;
	PyObjCErr_ToObjCWithGILState(&state);
}

static int 
_pyobjc_install_NSData(void)
{
	Class classNSData = objc_lookUpClass("NSData");
	Class classNSMutableData = objc_lookUpClass("NSMutableData");

	if (classNSData != NULL) {

		if (PyObjC_RegisterMethodMapping(classNSData, 
				 @selector(initWithBytes:length:),
				 call_NSData_initWithBytes_length_,
				 imp_NSData_initWithBytes_length_) < 0 ) {
			return -1;
		}

		if (PyObjC_RegisterMethodMapping(classNSData, 
				 @selector(dataWithBytes:length:),
				 call_NSData_dataWithBytes_length_,
				 imp_NSData_dataWithBytes_length_) < 0 ) {
			return -1;
		}
  
		if (PyObjC_RegisterMethodMapping(classNSData, 
				 @selector(bytes),
				 call_NSData_bytes,
				 imp_NSData_bytes) < 0 ) {
			return -1;
		}

		if (PyObjC_RegisterMethodMapping(
				classNSData,
				@selector(initWithBytes:length:copy:freeWhenDone:bytesAreVM:),
				PyObjCUnsupportedMethod_Caller,
				PyObjCUnsupportedMethod_IMP) < 0) {
			return -1;	
		}
	}

	if (classNSMutableData != NULL) {

		if (PyObjC_RegisterMethodMapping(classNSMutableData, 
				@selector(mutableBytes),
				call_NSMutableData_mutableBytes,
				imp_NSMutableData_mutableBytes) < 0 ) {
			return -1;
		}
	}

  
	return 0;
}
