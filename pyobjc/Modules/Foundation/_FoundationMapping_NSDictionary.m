/*
 * Special wrappers for NSDictionary methods with 'difficult' arguments.
 *
 * -initWithObjects:forKeys:count:		[call ,imp]
 * +dictionaryWithObjects:forKeys:count:	[call, imp]
 *
 * Undocumented methods:
 * -getKeys:		
 * -getObjects:
 * -getObjects:andKeys:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject* call_NSDictionary_initWithObjects_forKeys_count_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	int err;
	struct objc_super super;
	PyObject* keyList;
	PyObject* keySeq;
	PyObject* objectList;
	PyObject* objectSeq;
	id* objects;
	id* keys;
	int count;
	int i;
	id  res;

	if  (!PyArg_ParseTuple(arguments, "OOi", &objectList, &keyList, &count) ) {
		return NULL;
	}

	keySeq = PySequence_Fast(keyList, "keys not a sequence");
	if (keySeq == NULL) {
		return NULL;
	}
	objectSeq = PySequence_Fast(objectList, "objects not a sequence");
	if (objectSeq == NULL) {
		Py_DECREF(keySeq);
		return NULL;
	}

	if (PySequence_Fast_GET_SIZE(keySeq) < count) {
		PyErr_SetString(PyExc_ValueError, "too few keys");
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		return NULL;
	}

	if (PySequence_Fast_GET_SIZE(objectSeq) < count) {
		PyErr_SetString(PyExc_ValueError, "too few objects");
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		return NULL;
	}

	keys = alloca(sizeof(id) * count);
	if (keys == NULL) {
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		PyErr_NoMemory();
		return NULL;
	}

	objects = alloca(sizeof(id) * count);
	if (objects == NULL) {
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = PyObjC_PythonToObjC(@encode(id), 
			PySequence_Fast_GET_ITEM(objectSeq, i), objects + i);
		if (err == -1) {
			Py_DECREF(keySeq);
			Py_DECREF(objectSeq);
			PyErr_NoMemory();
			return NULL;
		}

		err = PyObjC_PythonToObjC(@encode(id), 
			PySequence_Fast_GET_ITEM(keySeq, i), keys + i);
		if (err == -1) {
			Py_DECREF(keySeq);
			Py_DECREF(objectSeq);
			PyErr_NoMemory();
			return NULL;
		}
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		res = objc_msgSendSuper(&super,
				@selector(initWithObjects:forKeys:count:),
				objects, keys, count);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	NS_ENDHANDLER

	Py_DECREF(objectSeq);
	Py_DECREF(keySeq);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

static id imp_NSDictionary_initWithObjects_forKeys_count_(id self, SEL sel,
		id* objects, id* keys, int count)
{
	PyObject* result;
	PyObject* arglist;
	PyObject* v;
	int i;
	id  returnValue;

	arglist = PyTuple_New(4);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	v = PyObjC_IdToPython(self);
	if (v == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyTuple_New(count);
	if (v == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}
	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, PyObjC_IdToPython(objects[i]));
		if (PyTuple_GET_ITEM(v, i) == NULL) {
			Py_DECREF(v);
			Py_DECREF(arglist);
			PyObjCErr_ToObjC();
			return nil;
		}
	}
	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyTuple_New(count);
	if (v == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}
	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, PyObjC_IdToPython(keys[i]));
		if (PyTuple_GET_ITEM(v, i) == NULL) {
			Py_DECREF(v);
			Py_DECREF(arglist);
			PyObjCErr_ToObjC();
			return nil;
		}
	}
	PyTuple_SET_ITEM(arglist, 2, v);
	PyTuple_SET_ITEM(arglist, 3, PyInt_FromLong(count));
	if (PyTuple_GET_ITEM(arglist, 3) == NULL) {	
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

	returnValue = PyObjC_PythonToId(result);
	Py_DECREF(result);
	if (PyErr_Occurred()) {
		PyObjCErr_ToObjC();
		return nil;
	}
	return returnValue;
}

static PyObject* call_NSDictionary_dictionaryWithObjects_forKeys_count_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	int err;
	struct objc_super super;
	PyObject* keyList;
	PyObject* keySeq;
	PyObject* objectList;
	PyObject* objectSeq;
	id* objects;
	id* keys;
	int count;
	int i;
	id  res;

	if  (!PyArg_ParseTuple(arguments, "OOi", &objectList, &keyList, &count)) {
		return NULL;
	}

	keySeq = PySequence_Fast(keyList, "keys not a sequence");
	if (keySeq == NULL) {
		return NULL;
	}
	objectSeq = PySequence_Fast(objectList, "objects not a sequence");
	if (objectSeq == NULL) {
		Py_DECREF(keySeq);
		return NULL;
	}

	if (PySequence_Fast_GET_SIZE(keySeq) < count) {
		PyErr_SetString(PyExc_ValueError, "too few keys");
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		return NULL;
	}

	if (PySequence_Fast_GET_SIZE(objectSeq) < count) {
		PyErr_SetString(PyExc_ValueError, "too few objects");
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		return NULL;
	}

	keys = alloca(sizeof(id) * count);
	if (keys == NULL) {
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		PyErr_NoMemory();
		return NULL;
	}

	objects = alloca(sizeof(id) * count);
	if (objects == NULL) {
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = PyObjC_PythonToObjC(@encode(id), 
			PySequence_Fast_GET_ITEM(objectSeq, i), objects + i);
		if (err == -1) {
			Py_DECREF(keySeq);
			Py_DECREF(objectSeq);
			PyErr_NoMemory();
			return NULL;
		}

		err = PyObjC_PythonToObjC(@encode(id), 
			PySequence_Fast_GET_ITEM(keySeq, i), keys + i);
		if (err == -1) {
			Py_DECREF(keySeq);
			Py_DECREF(objectSeq);
			PyErr_NoMemory();
			return NULL;
		}
	}

	NS_DURING
		PyObjC_InitSuperCls(&super, 
			PyObjCSelector_GetClass(method), 
			PyObjCClass_GetClass(self));

			
		res = objc_msgSendSuper(&super,
				@selector(dictionaryWithObjects:forKeys:count:),
				objects, keys, count);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	NS_ENDHANDLER

	Py_DECREF(objectSeq);
	Py_DECREF(keySeq);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

static id imp_NSDictionary_dictionaryWithObjects_forKeys_count_(
	id self, SEL sel, id* objects, id* keys, int count)
{
	PyObject* result;
	PyObject* arglist;
	PyObject* v;
	int i;
	id  returnValue;

	arglist = PyTuple_New(4);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	v = PyObjC_IdToPython(self);
	if (v == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}

	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyTuple_New(count);
	if (v == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}
	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, PyObjC_IdToPython(objects[i]));
		if (PyTuple_GET_ITEM(v, i) == NULL) {
			Py_DECREF(v);
			Py_DECREF(arglist);
			PyObjCErr_ToObjC();
			return nil;
		}
	}
	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyTuple_New(count);
	if (v == NULL) {
		PyObjCErr_ToObjC();
		return nil;
	}
	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, PyObjC_IdToPython(keys[i]));
		if (PyTuple_GET_ITEM(v, i) == NULL) {
			Py_DECREF(v);
			Py_DECREF(arglist);
			PyObjCErr_ToObjC();
			return nil;
		}
	}
	PyTuple_SET_ITEM(arglist, 2, v);
	PyTuple_SET_ITEM(arglist, 3, PyInt_FromLong(count));
	if (PyTuple_GET_ITEM(arglist, 3) == NULL) {	
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

	returnValue = PyObjC_PythonToId(result);
	Py_DECREF(result);
	if (PyErr_Occurred()) {
		PyObjCErr_ToObjC();
		return nil;
	}
	return returnValue;
}

static int 
_pyobjc_install_NSDictionary(void)
{
	Class classNSDictionary = objc_lookUpClass("NSDictionary");

	if (PyObjC_RegisterMethodMapping(
		classNSDictionary,
		@selector(initWithObjects:forKeys:count:),
		call_NSDictionary_initWithObjects_forKeys_count_,
		(IMP)imp_NSDictionary_initWithObjects_forKeys_count_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSDictionary,
		@selector(dictionaryWithObjects:forKeys:count:),
		call_NSDictionary_dictionaryWithObjects_forKeys_count_,
		(IMP)imp_NSDictionary_dictionaryWithObjects_forKeys_count_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSDictionary,
		@selector(getKeys:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSDictionary,
		@selector(getObjects:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSDictionary,
		@selector(getObjects:andKeys:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
