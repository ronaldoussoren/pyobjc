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

static PyObject* 
call_NSDictionary_initWithObjects_forKeys_count_(
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

	keys = PyMem_Malloc(sizeof(id) * count);
	if (keys == NULL) {
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		PyErr_NoMemory();
		return NULL;
	}

	objects = PyMem_Malloc(sizeof(id) * count);
	if (objects == NULL) {
		PyMem_Free(keys);
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = PyObjC_PythonToObjC(@encode(id), 
			PySequence_Fast_GET_ITEM(objectSeq, i), objects + i);
		if (err == -1) {
			PyMem_Free(keys);
			PyMem_Free(objects);
			Py_DECREF(keySeq);
			Py_DECREF(objectSeq);
			PyErr_NoMemory();
			return NULL;
		}

		err = PyObjC_PythonToObjC(@encode(id), 
			PySequence_Fast_GET_ITEM(keySeq, i), keys + i);
		if (err == -1) {
			PyMem_Free(keys);
			PyMem_Free(objects);
			Py_DECREF(keySeq);
			Py_DECREF(objectSeq);
			PyErr_NoMemory();
			return NULL;
		}
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		res = objc_msgSendSuper(&super,
				@selector(initWithObjects:forKeys:count:),
				objects, keys, count);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	PyObjC_ENDHANDLER

	PyMem_Free(keys);
	PyMem_Free(objects);
	Py_DECREF(objectSeq);
	Py_DECREF(keySeq);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

static void 
imp_NSDictionary_initWithObjects_forKeys_count_(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	id* objects = *(id**)args[2];
	id* keys = *(id**)args[3];
	int count = *(int*)args[4];
	id* pretval = (id*)resp;

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v;
	int i;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(4);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyTuple_New(count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 1, v);

	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, PyObjC_IdToPython(objects[i]));
		if (PyTuple_GET_ITEM(v, i) == NULL) goto error;
	}

	v = PyTuple_New(count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 2, v);

	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, PyObjC_IdToPython(keys[i]));
		if (PyTuple_GET_ITEM(v, i) == NULL) goto error;
	}

	v = PyInt_FromLong(count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 3, v);

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
	*pretval = nil;
	PyObjCErr_ToObjCWithGILState(&state);
}

static PyObject* 
call_NSDictionary_dictionaryWithObjects_forKeys_count_(
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

	keys = PyMem_Malloc(sizeof(id) * count);
	if (keys == NULL) {
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		PyErr_NoMemory();
		return NULL;
	}

	objects = PyMem_Malloc(sizeof(id) * count);
	if (objects == NULL) {
		PyMem_Free(keys);
		Py_DECREF(keySeq);
		Py_DECREF(objectSeq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = PyObjC_PythonToObjC(@encode(id), 
			PySequence_Fast_GET_ITEM(objectSeq, i), objects + i);
		if (err == -1) {
			PyMem_Free(keys);
			PyMem_Free(objects);
			Py_DECREF(keySeq);
			Py_DECREF(objectSeq);
			PyErr_NoMemory();
			return NULL;
		}

		err = PyObjC_PythonToObjC(@encode(id), 
			PySequence_Fast_GET_ITEM(keySeq, i), keys + i);
		if (err == -1) {
			PyMem_Free(keys);
			PyMem_Free(objects);
			Py_DECREF(keySeq);
			Py_DECREF(objectSeq);
			PyErr_NoMemory();
			return NULL;
		}
	}

	PyObjC_DURING
		PyObjC_InitSuperCls(&super, 
			PyObjCSelector_GetClass(method), 
			PyObjCClass_GetClass(self));

			
		res = objc_msgSendSuper(&super,
				@selector(dictionaryWithObjects:forKeys:count:),
				objects, keys, count);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	PyObjC_ENDHANDLER

	PyMem_Free(keys);
	PyMem_Free(objects);
	Py_DECREF(objectSeq);
	Py_DECREF(keySeq);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

static void 
imp_NSDictionary_dictionaryWithObjects_forKeys_count_(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	id* objects = *(id**)args[2];
	id* keys = *(id**)args[3];
	int count = *(int*)args[4];
	id* pretval = (id*)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;
	int i;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(4);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyTuple_New(count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 1, v);

	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, PyObjC_IdToPython(objects[i]));
		if (PyTuple_GET_ITEM(v, i) == NULL) goto error;
	}

	v = PyTuple_New(count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 2, v);
	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, PyObjC_IdToPython(keys[i]));
		if (PyTuple_GET_ITEM(v, i) == NULL) goto error;
	}

	v = PyInt_FromLong(count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 3, v); 

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
	*pretval = nil;
	PyObjCErr_ToObjCWithGILState(&state);
}

static int 
_pyobjc_install_NSDictionary(void)
{
	Class classNSDictionary = objc_lookUpClass("NSDictionary");
	if (classNSDictionary == NULL) return 0;

	if (PyObjC_RegisterMethodMapping(
		classNSDictionary,
		@selector(initWithObjects:forKeys:count:),
		call_NSDictionary_initWithObjects_forKeys_count_,
		imp_NSDictionary_initWithObjects_forKeys_count_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSDictionary,
		@selector(dictionaryWithObjects:forKeys:count:),
		call_NSDictionary_dictionaryWithObjects_forKeys_count_,
		imp_NSDictionary_dictionaryWithObjects_forKeys_count_) < 0) {

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
