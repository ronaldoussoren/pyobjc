/*
 * NSCoder mappings for special methods:
 * - encodeValueOfObjCType:at: (DONE)
 * - decodeValueOfObjCType:at:
 *
 * Later we'll add (varargs functions):
 * - encodeValuesOfObjCType:
 * - decodeValuesOfObjCType:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>
#endif
#include "pyobjc-api.h"
#include "objc_support.h"

static PyObject* call_NSCoder_encodeValueOfObjCType_at_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char* signature;
	PyObject* value;
	PyObject* result;
	void*     buf;
	size_t    size;
	int err;

	if  (PyArg_ParseTuple(arguments, "sO", &signature, &value) < 0) {
		return NULL;
	}

	size = ObjC_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	err = ObjC_PythonToObjC(signature, value, buf);
	if (err == -1) {
		return NULL;
	}

	NS_DURING
		(void)objc_msgSend(ObjCObject_GetObject(self),
				@selector(encodeValueOfObjCType:at:),
				signature, buf);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject* supercall_NSCoder_encodeValueOfObjCType_at_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char* signature;
	PyObject* value;
	PyObject* result;
	void*     buf;
	size_t    size;
	int err;
	struct objc_super super;

	if  (PyArg_ParseTuple(arguments, "sO", &signature, &value) < 0) {
		return NULL;
	}

	size = ObjC_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	err = ObjC_PythonToObjC(signature, value, buf);
	if (err == -1) {
		return NULL;
	}

	NS_DURING
		RECEIVER(super) = ObjCObject_GetObject(self);
		super.class = ObjCClass_GetClass((PyObject*)(self->ob_type));

		(void)objc_msgSendSuper(&super,
				@selector(encodeValueOfObjCType:at:),
				signature, buf);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void imp_NSCoder_encodeValueOfObjCType_at_(id self, SEL sel,
		char* signature, void* buf)	
{
	PyObject* result;
	PyObject* arglist;

	arglist = PyTuple_New(2);
	if (arglist == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromString(signature));
	PyTuple_SetItem(arglist, 1, ObjC_ObjCToPython(signature, buf));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		ObjCErr_ToObjC();
		return;
	}

	result = ObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	if (result != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Must return None");
		Py_DECREF(result);
		ObjCErr_ToObjC();
		return;
	}
	Py_DECREF(result);
}

/* XXX */
static PyObject* call_NSCoder_encodeArrayOfObjCType_count_at_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char* signature;
	int   count;
	int   value_len, i;
	PyObject* value;
	PyObject* result;
	void*     buf;
	size_t    size;
	int err;

	if  (PyArg_ParseTuple(arguments, "siO", &signature, &count, &value) < 0) {
		return NULL;
	}

	if (count < 0) {
		PyErr_SetString(PyExc_ValueError, "negative count");
		return NULL;
	}

	size = ObjC_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size * (count+1));
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	if (!PySequence_Check(value)) {
		PyErr_SetString(PyExc_TypeError, "Need sequence of objects");
		return NULL;
	}

	value_len = PySequence_Size(value);
	if (value_len > count) {
		PyErr_SetString(PyExc_ValueError, "Inconsistent arguments");
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = ObjC_PythonToObjC(signature, 
				PySequence_GetItem(value, i), 
				((char*)buf) + (size * i));
		if (err == -1) {
			return NULL;
		}
	}

	NS_DURING
		(void)objc_msgSend(ObjCObject_GetObject(self),
				@selector(encodeArrayOfObjCType:count:at:),
				signature, count, buf);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static PyObject* supercall_NSCoder_encodeArrayOfObjCType_count_at_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	char* signature;
	int   count;
	int   value_len, i;
	PyObject* value;
	PyObject* result;
	void*     buf;
	size_t    size;
	int err;
	struct objc_super super;

	if  (PyArg_ParseTuple(arguments, "siO", &signature, &count, &value) < 0) {
		return NULL;
	}

	if (count < 0) {
		PyErr_SetString(PyExc_ValueError, "negative count");
		return NULL;
	}

	size = ObjC_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size * (count+1));
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	if (!PySequence_Check(value)) {
		PyErr_SetString(PyExc_TypeError, "Need sequence of objects");
		return NULL;
	}

	value_len = PySequence_Size(value);
	if (value_len > count) {
		PyErr_SetString(PyExc_ValueError, "Inconsistent arguments");
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = ObjC_PythonToObjC(signature, 
				PySequence_GetItem(value, i), 
				((char*)buf) + (size * i));
		if (err == -1) {
			return NULL;
		}
	}

	NS_DURING
		RECEIVER(super) = ObjCObject_GetObject(self);
		super.class = ObjCClass_GetClass((PyObject*)(self->ob_type));

		(void)objc_msgSendSuper(&super,
				@selector(encodeArrayOfObjCType:count:at:),
				signature, count, buf);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void imp_NSCoder_encodeArrayOfObjCType_count_at_(id self, SEL sel,
		char* signature, unsigned count, void* buf)	
{
	PyObject* result;
	PyObject* arglist;
	PyObject* values;
	int       size;
	int       i;

	arglist = PyTuple_New(3);
	if (arglist == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	size = ObjC_SizeOfType(signature);
	if (size == -1) {
		ObjCErr_ToObjC();
		return;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromString(signature));
	PyTuple_SetItem(arglist, 1, PyInt_FromLong(count));

	values = PyTuple_New(count);
	if (values == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	for (i = 0; i < count; i++) {
		PyTuple_SetItem(values, i, ObjC_ObjCToPython(signature, 
			((char*)buf)+(i*size)));
	}
	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		Py_DECREF(values);
		ObjCErr_ToObjC();
		return;
	}
	PyTuple_SetItem(arglist, 2, values);

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		ObjCErr_ToObjC();
		return;
	}

	result = ObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	if (result != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Must return None");
		Py_DECREF(result);
		ObjCErr_ToObjC();
		return;
	}
	Py_DECREF(result);
}

int __pyobjc_install_NSCoder(void)
{
  Class classNSCoder = objc_lookUpClass("NSCoder");
  
  if (ObjC_RegisterMethodMapping(
				 classNSCoder,
				 @selector(encodeArrayOfObjCType:count:at:),
				 call_NSCoder_encodeArrayOfObjCType_count_at_,
				 supercall_NSCoder_encodeArrayOfObjCType_count_at_,
				 (IMP)imp_NSCoder_encodeArrayOfObjCType_count_at_) < 0) {
    NSLog(@"Error occurred while installing NSCoder bridge method -encodeArrayOfObjCType:count:at:");
    PyErr_Print();
    return -1;
  }
  if (ObjC_RegisterMethodMapping(
				 classNSCoder,
				 @selector(encodeValueOfObjCType:at:),
				 call_NSCoder_encodeValueOfObjCType_at_,
				 supercall_NSCoder_encodeValueOfObjCType_at_,
				 (IMP)imp_NSCoder_encodeValueOfObjCType_at_) < 0) {
    NSLog(@"Error occurred while installing NSCoder bridge method -encodeArrayOfObjCType:at:");
    PyErr_Print();
    return -1;
  }

  return 0;
}
