/*
 * NSData mappings for special methods:
 * - initWithBytes_length_
 * - bytes
 * - mutableBytes
 *
 * Should add:
 * -initWithBytesNoCopy:length:
 * -initWithBytesNoCopy:length:freeWhenDone
 * +dataWith... version of above
 * -getBytes...
 * 
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"


static PyObject* call_NSData_dataWithBytes_length_(
		PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
	char*     bytes;
	int       bytes_len;
	int       len;
	PyObject* result;
	struct objc_super super;
	id        objc_result;

	if  (PyArg_ParseTuple(arguments, "t#i", &bytes, &bytes_len, &len) < 0) {
		return NULL;
	}

	if (bytes_len < len) {
		PyErr_SetString(PyExc_ValueError, "Not enough bytes in data");
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuperCls(&super, PyObjCClass_GetClass(self));

		objc_result = objc_msgSendSuper(&super,
				@selector(dataWithBytes:length:),
				bytes, len);
		result = ObjC_IdToPython(objc_result);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
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
		ObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromStringAndSize(data, len));
	PyTuple_SetItem(arglist, 1, PyInt_FromLong(len));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		ObjCErr_ToObjC();
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	objc_result = ObjC_PythonToId(result);
	Py_DECREF(result);

	if (PyErr_Occurred()) {
		ObjCErr_ToObjC();
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

	if  (PyArg_ParseTuple(arguments, "t#i", &bytes, &bytes_len, &len) < 0) {
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
		result = ObjC_IdToPython(objc_result);

		/* XXX Ronald: If you try to use the result of 
		 * PyObjCObject_GetObject(self) after the call to objc_msgSend 
		 * it will crash with large enough values of len (>=32). 
		 * Appearently the original self is recycled during the init.
		 */
		if (self != result) {
			PyObjCObject_ClearObject(self);
		}
	NS_HANDLER
		ObjCErr_FromObjC(localException);
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
		ObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromStringAndSize(data, len));
	PyTuple_SetItem(arglist, 1, PyInt_FromLong(len));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		ObjCErr_ToObjC();
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	objc_result = ObjC_PythonToId(result);
	Py_DECREF(result);

	if (PyErr_Occurred()) {
		ObjCErr_ToObjC();
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

  if (PyArg_ParseTuple(arguments, "") < 0) {
    return NULL;
  }

  NS_DURING
    PyObjC_InitSuper(&super,
	    PyObjCClass_GetClass((PyObject*)(self->ob_type)),
	    PyObjCObject_GetObject(self));

    /* bbum: Not at all sure what to do here....   send both to super?  
     *       Just -bytes?
     * ronald: I think both is more correct, neiter one is perfect.
     */
    bytes = objc_msgSendSuper(&super, @selector(bytes));
    bytes_len = (unsigned) objc_msgSendSuper(&super, @selector(length));

    result = PyBuffer_FromMemory((void*)bytes, bytes_len);
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static void *imp_NSData_bytes(id self, SEL sel)
{
  PyObject* result;

  result = PyObjC_CallPython(self, sel, NULL);
  if (result == NULL) {
    ObjCErr_ToObjC();
    return NULL;
  }

  if (result == Py_None)
    return NULL;

  if (PyBuffer_Check(result)) {
    const void *p;
    int len;
    if (PyObject_AsReadBuffer(result, &p, &len) == -1) {
      ObjCErr_ToObjC();
      return NULL;
    }
    return (void *)p;
  }

  PyErr_SetString(PyExc_ValueError, "No idea what to do with result.");
  return NULL;
}


static PyObject* call_NSMutableData_mutableBytes(PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
  void*     bytes;
  unsigned  bytes_len;
  PyObject* result;
  struct objc_super super;

  if (PyArg_ParseTuple(arguments, "") < 0) {
    return NULL;
  }

  NS_DURING
    PyObjC_InitSuper(&super,
    	PyObjCClass_GetClass((PyObject*)(self->ob_type)),
    	PyObjCObject_GetObject(self));

    /* bbum: Not at all sure what to do here....   
     *       send both to super?  Just -bytes?
     */
    bytes = objc_msgSendSuper(&super, @selector(mutableBytes));
    bytes_len = (unsigned) objc_msgSendSuper(&super, @selector(length));

    result = PyBuffer_FromReadWriteMemory((void*)bytes, bytes_len);
  NS_HANDLER
    ObjCErr_FromObjC(localException);
    result = NULL;
  NS_ENDHANDLER

  return result;
}

static void *imp_NSMutableData_mutableBytes(id self, SEL sel)
{
  PyObject* result;

  result = PyObjC_CallPython(self, sel, NULL);
  if (result == NULL) {
    ObjCErr_ToObjC();
    return NULL;
  }

  if (result == Py_None)
    return NULL;

  if (PyBuffer_Check(result)) {
    void *p;
    int len;
    if (PyObject_AsWriteBuffer(result, &p, &len) == -1) {
      ObjCErr_ToObjC();
      return NULL;
    }
    return (void *)p;
  }

  PyErr_SetString(PyExc_ValueError, "No idea what to do with result.");
  return NULL;
}

int _pyobjc_install_NSData(void)
{
  if (ObjC_RegisterMethodMapping(objc_lookUpClass("NSData"), 
				 @selector(initWithBytes:length:),
				 call_NSData_initWithBytes_length_,
				 (IMP)imp_NSData_initWithBytes_length_) < 0 ) {
    NSLog(@"Error occurred while installing NSData method bridge (initWithBytes:length:).");
    PyErr_Print();
    return -1;
  }

  if (ObjC_RegisterMethodMapping(objc_lookUpClass("NSData"), 
				 @selector(dataWithBytes:length:),
				 call_NSData_dataWithBytes_length_,
				 (IMP)imp_NSData_dataWithBytes_length_) < 0 ) {
    NSLog(@"Error occurred while installing NSData method bridge (initWithBytes:length:).");
    PyErr_Print();
    return -1;
  }
  
  if (ObjC_RegisterMethodMapping(objc_lookUpClass("NSData"), 
				 @selector(bytes),
				 call_NSData_bytes,
				 (IMP)imp_NSData_bytes) < 0 ) {
    NSLog(@"Error occurred while installing NSData method bridge (bytes).");
    PyErr_Print();
    return -1;
  }

  if (ObjC_RegisterMethodMapping(objc_lookUpClass("NSMutableData"), 
				 @selector(mutableBytes),
				 call_NSMutableData_mutableBytes,
				 (IMP)imp_NSMutableData_mutableBytes) < 0 ) {
    NSLog(@"Error occurred while installing NSMutableData method bridge (mutableBytes).");
    PyErr_Print();
    return -1;
  }
  
  return 0;
}

