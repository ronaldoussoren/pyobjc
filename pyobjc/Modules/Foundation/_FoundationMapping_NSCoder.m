/*
 * NSCoder mappings for special methods:
 * - encodeValueOfObjCType:at: 
 * - decodeValueOfObjCType:at:
 * - encodeArrayOfObjCType:count:at:
 * - decodeArrayOfObjCType:count:at:
 *
 * TODO:
 * - encodeBytes:length:
 * - decodeBytesWithReturnedLength:
 * - encodeValuesOfObjCType: 
 * - decodeValuesOfObjCType:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"


static PyObject* call_NSCoder_encodeValueOfObjCType_at_(
		PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
	char* signature;
	PyObject* value;
	PyObject* result;
	void*     buf;
	int    size;
	int err;
	struct objc_super super;

	if  (PyArg_ParseTuple(arguments, "sO", &signature, &value) < 0) {
		return NULL;
	}

	size = PyObjC_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	err = PyObjC_PythonToObjC(signature, value, buf);
	if (err == -1) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
				@selector(encodeValueOfObjCType:at:),
				signature, buf);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
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
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromString(signature));
	PyTuple_SetItem(arglist, 1, PyObjC_ObjCToPython(signature, buf));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	if (result != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Must return None");
		Py_DECREF(result);
		PyObjCErr_ToObjC();
		return;
	}
	Py_DECREF(result);
}


static PyObject* call_NSCoder_encodeArrayOfObjCType_count_at_(
		PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
	char* signature;
	int   count;
	int   value_len, i;
	PyObject* value;
	PyObject* result;
	void*     buf;
	int    size;
	int err;
	struct objc_super super;

	if  (PyArg_ParseTuple(arguments, "siO", &signature, &count, &value) < 0) {
		return NULL;
	}

	if (count < 0) {
		PyErr_SetString(PyExc_ValueError, "negative count");
		return NULL;
	}

	size = PyObjC_SizeOfType(signature);
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
		err = PyObjC_PythonToObjC(signature, 
				PySequence_GetItem(value, i), 
				((char*)buf) + (size * i));
		if (err == -1) {
			return NULL;
		}
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
				@selector(encodeArrayOfObjCType:count:at:),
				signature, count, buf);
		result = Py_None;
		Py_INCREF(result);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
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
		PyObjCErr_ToObjC();
		return;
	}

	size = PyObjC_SizeOfType(signature);
	if (size == -1) {
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromString(signature));
	PyTuple_SetItem(arglist, 1, PyInt_FromLong(count));

	values = PyTuple_New(count);
	if (values == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	for (i = 0; (unsigned)i < count; i++) {
		PyTuple_SetItem(values, i, PyObjC_ObjCToPython(signature, 
			((char*)buf)+(i*size)));
	}
	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		Py_DECREF(values);
		PyObjCErr_ToObjC();
		return;
	}
	PyTuple_SetItem(arglist, 2, values);

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	if (result != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Must return None");
		Py_DECREF(result);
		PyObjCErr_ToObjC();
		return;
	}
	Py_DECREF(result);
}

static PyObject* call_NSCoder_decodeValueOfObjCType_at_(
		PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
	char* signature;
	PyObject* value;
	PyObject* result;
	void*     buf;
	int    size;
	struct objc_super super;

	if  (PyArg_ParseTuple(arguments, "s", &signature) < 0) {
		return NULL;
	}

	size = PyObjC_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}


	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
				@selector(decodeValueOfObjCType:at:),
				signature, buf);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	value = PyObjC_ObjCToPython(signature, buf);
	if (value == NULL) {
		return NULL;
	}

	result = PyTuple_New(2);
	if (result == NULL) {
		Py_DECREF(value);
		return NULL;
	}

	PyTuple_SET_ITEM(result, 0, Py_None);
	Py_INCREF(Py_None);
	PyTuple_SET_ITEM(result, 1, value);

	return result;
}

static void imp_NSCoder_decodeValueOfObjCType_at_(id self, SEL sel,
		char* signature, void* buf)	
{
	PyObject* result;
	PyObject* arglist;
	PyObject* seq;
	int err;

	arglist = PyTuple_New(1);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromString(signature));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	seq = PySequence_Fast(result, "Must return a sequence of length 2");
	if (seq == NULL) {
		Py_DECREF(result);
		PyObjCErr_ToObjC();
		return;
	}
	Py_DECREF(result);

	if (PySequence_Fast_GET_SIZE(seq) != 2) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_TypeError,
			"Must return a sequence of length 2");
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return;
	}

	if (PySequence_Fast_GET_ITEM(seq, 0) != Py_None) {
		PyErr_SetString(PyExc_TypeError,
			"returnvalue[0] must be Py_None");
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return;
	}

	err = PyObjC_PythonToObjC(signature, 
		PySequence_Fast_GET_ITEM(seq, 1), buf);
	if (err == -1) {
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return;
	}

	Py_DECREF(seq);
}

static PyObject* call_NSCoder_decodeArrayOfObjCType_count_at_(
		PyObject* method __attribute__((__unused__)), PyObject* self, PyObject* arguments)
{
	char* signature;
	int   count;
	int   i;
	PyObject* result;
	void*     buf;
	int    size;
	struct objc_super super;

	if  (PyArg_ParseTuple(arguments, "si", &signature, &count) < 0) {
		return NULL;
	}

	if (count < 0) {
		PyErr_SetString(PyExc_ValueError, "negative count");
		return NULL;
	}

	size = PyObjC_SizeOfType(signature);
	if (size == -1) {
		return NULL;
	}
	buf = alloca(size * (count+1));
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCClass_GetClass((PyObject*)(self->ob_type)),
			PyObjCObject_GetObject(self));

		(void)objc_msgSendSuper(&super,
				@selector(decodeArrayOfObjCType:count:at:),
				signature, count, buf);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	result = PyTuple_New(count);
	if (result == NULL) {
		return NULL;
	}

	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(result, i,  PyObjC_ObjCToPython(signature, 
				((char*)buf) + (size * i)));
		if (PyTuple_GET_ITEM(result, i) == NULL) {
			Py_DECREF(result);
			return NULL;
		}

		/* XXX: Isn't this incorrect??, we get a crash without this */
		//Py_INCREF(PyTuple_GET_ITEM(result, i)); 
	}

	return result;
}

static void imp_NSCoder_decodeArrayOfObjCType_count_at_(id self, SEL sel,
		char* signature, unsigned count, void* buf)	
{
	PyObject* result;
	PyObject* arglist;
	PyObject* values;
	PyObject* seq;
	int       size;
	int       i;
	int res;

	arglist = PyTuple_New(2);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	size = PyObjC_SizeOfType(signature);
	if (size == -1) {
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SetItem(arglist, 0, PyString_FromString(signature));
	PyTuple_SetItem(arglist, 1, PyInt_FromLong(count));

	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	seq = PySequence_Fast(result, "Must return a sequence of length 2");
	if (seq == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	if (PySequence_Fast_GET_SIZE(seq) != 2) {
		Py_DECREF(seq);
		PyErr_SetString(PyExc_TypeError,
			"Must return a sequence of length 2");
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return;
	}

	if (PySequence_Fast_GET_ITEM(seq, 0) != Py_None) {
		PyErr_SetString(PyExc_TypeError,
			"returnvalue[0] must be Py_None");
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return;
	}

	values = PySequence_Fast_GET_ITEM(seq, 1);
	if (values == NULL) {
		PyErr_SetString(PyExc_TypeError,
			"returnvalue[1] must be a sequence");
		Py_DECREF(seq);
		PyObjCErr_ToObjC();
		return;
	}
	Py_DECREF(seq);

	if ((unsigned)PySequence_Fast_GET_SIZE(values) != count) {
		PyErr_SetString(PyExc_TypeError,
			"returnvalue[1] must be a of correct size");
		Py_DECREF(values);
		PyObjCErr_ToObjC();
		return;
	}


	for (i = 0; (unsigned)i < count; i++) {
		res = PyObjC_PythonToObjC(signature, 
			PySequence_Fast_GET_ITEM(values, i),
			((char*)buf)+(i*size));
		if (res == -1) {
			Py_DECREF(values);
			PyObjCErr_ToObjC();
		}
	}
	Py_DECREF(values);
}

int _pyobjc_install_NSCoder(void)
{
  Class classNSCoder = objc_lookUpClass("NSCoder");
  
  if (PyObjC_RegisterMethodMapping(
	 classNSCoder,
	 @selector(encodeArrayOfObjCType:count:at:),
	 call_NSCoder_encodeArrayOfObjCType_count_at_,
	 (IMP)imp_NSCoder_encodeArrayOfObjCType_count_at_) < 0) {
    NSLog(
    	@"Error occurred while installing NSCoder bridge method -encodeArrayOfObjCType:count:at:");
    return -1;
  }
  if (PyObjC_RegisterMethodMapping(
	 classNSCoder,
	 @selector(encodeValueOfObjCType:at:),
	 call_NSCoder_encodeValueOfObjCType_at_,
	 (IMP)imp_NSCoder_encodeValueOfObjCType_at_) < 0) {
    NSLog(@"Error occurred while installing NSCoder bridge method -encodeArrayOfObjCType:at:");
    return -1;
  }

  if (PyObjC_RegisterMethodMapping(
	 classNSCoder,
	 @selector(decodeArrayOfObjCType:count:at:),
	 call_NSCoder_decodeArrayOfObjCType_count_at_,
	 (IMP)imp_NSCoder_decodeArrayOfObjCType_count_at_) < 0) {
    NSLog(
    	@"Error occurred while installing NSCoder bridge method -encodeArrayOfObjCType:count:at:");
    return -1;
  }

  if (PyObjC_RegisterMethodMapping(
	 classNSCoder,
	 @selector(decodeValueOfObjCType:at:),
	 call_NSCoder_decodeValueOfObjCType_at_,
	 (IMP)imp_NSCoder_decodeValueOfObjCType_at_) < 0) {
    NSLog(@"Error occurred while installing NSCoder bridge method -decodeArrayOfObjCType:at:");
    return -1;
  }

  return 0;
}
