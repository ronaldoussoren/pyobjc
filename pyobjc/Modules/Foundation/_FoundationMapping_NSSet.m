/*
 * Special wrappers for NSSet methods with 'difficult' arguments.
 *
 * -initWithObjects:count:		[call, imp]
 * +setWithObjects:count:		[call, imp]
 *
 * Unsupported methods:
 * -initWithObjects:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject* call_NSSet_setWithObjects_count_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	int err;
	struct objc_super super;
	PyObject* objectList;
	PyObject* objectSeq;
	id* objects;
	int count;
	int i;
	id  res;

	if  (PyArg_ParseTuple(arguments, "Oi", &objectList, &count) < 0) {
		return NULL;
	}

	objectSeq = PySequence_Fast(objectList, "objects not a sequence");
	if (objectSeq == NULL) {
		return NULL;
	}

	if (PySequence_Fast_GET_SIZE(objectSeq) < count) {
		PyErr_SetString(PyExc_ValueError, "too few objects");
		Py_DECREF(objectSeq);
		return NULL;
	}

	objects = alloca(sizeof(id) * count);
	if (objects == NULL) {
		Py_DECREF(objectSeq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = PyObjC_PythonToObjC(@encode(id), 
			PySequence_Fast_GET_ITEM(objectSeq, i), objects + i);
		if (err == -1) {
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
				@selector(setWithObjects:count:),
				objects, count);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	NS_ENDHANDLER

	Py_DECREF(objectSeq);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

static id imp_NSSet_setWithObjects_count_(id self, SEL sel,
		id* objects, int count)
{
	PyObject* result;
	PyObject* arglist;
	PyObject* v;
	int i;
	id  returnValue;

	arglist = PyTuple_New(3);
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

	v = PyInt_FromLong(count);
	if (v == NULL) {	
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return nil;
	}
	PyTuple_SET_ITEM(arglist, 2,  v);

	result = PyObjC_CallPython(self, sel, arglist);
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

static PyObject* call_NSSet_initWithObjects_count_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	int err;
	struct objc_super super;
	PyObject* objectList;
	PyObject* objectSeq;
	id* objects;
	int count;
	int i;
	id  res;

	if  (PyArg_ParseTuple(arguments, "Oi", &objectList, &count) < 0) {
		return NULL;
	}

	objectSeq = PySequence_Fast(objectList, "objects not a sequence");
	if (objectSeq == NULL) {
		return NULL;
	}

	if (PySequence_Fast_GET_SIZE(objectSeq) < count) {
		PyErr_SetString(PyExc_ValueError, "too few objects");
		Py_DECREF(objectSeq);
		return NULL;
	}

	objects = alloca(sizeof(id) * count);
	if (objects == NULL) {
		Py_DECREF(objectSeq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = PyObjC_PythonToObjC(@encode(id), 
			PySequence_Fast_GET_ITEM(objectSeq, i), objects + i);
		if (err == -1) {
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
				@selector(initWithObjects:count:),
				objects, count);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	NS_ENDHANDLER

	Py_DECREF(objectSeq);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

static id imp_NSSet_initWithObjects_count_(id self, SEL sel,
		id* objects, int count)
{
	PyObject* result;
	PyObject* arglist;
	PyObject* v;
	int i;
	id  returnValue;

	arglist = PyTuple_New(3);
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

	v = PyInt_FromLong(count);
	if (v == NULL) {	
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return nil;
	}
	PyTuple_SET_ITEM(arglist, 2,  v);

	result = PyObjC_CallPython(self, sel, arglist);
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
_pyobjc_install_NSSet(void)
{
	Class classNSSet = objc_lookUpClass("NSSet");

	if (PyObjC_RegisterMethodMapping(
		classNSSet,
                @selector(initWithObjects:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSSet,
                @selector(setWithObjects:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSSet,
		@selector(setWithObjects:count:),
		call_NSSet_setWithObjects_count_,
		(IMP)imp_NSSet_setWithObjects_count_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSSet,
		@selector(initWithObjects:count:),
		call_NSSet_initWithObjects_count_,
		(IMP)imp_NSSet_initWithObjects_count_) < 0) {

		return -1;
	}

	return 0;
}
