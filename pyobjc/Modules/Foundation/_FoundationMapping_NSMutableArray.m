/*
 * Special wrappers for NSMutableArray methods with 'difficult' arguments.
 *
 * -removeObjectsFromIndices:numIndices:	[call, imp]
 * -replaceObjectsInRange:withObjects:count:	[call, imp]
 * -sortUsingFunction:context:			[call]
 * -sortUsingFunction:context:range:		[call]
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject* call_NSMutableArray_sortUsingFunction_context_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	PyObject* sortFunc;
	PyObject* context;
	PyObject* realContext;
	id  res;

	if  (!PyArg_ParseTuple(arguments, "OO", &sortFunc, &context)) {
		return NULL;
	}

	realContext = PyTuple_New(2);
	if (realContext == NULL) {
		return NULL;
	}
	PyTuple_SET_ITEM(realContext, 0, sortFunc);
	Py_INCREF(sortFunc);
	PyTuple_SET_ITEM(realContext, 1, context);
	Py_INCREF(context);

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

			
		(void)objc_msgSendSuper(&super,
				@selector(sortUsingFunction:context:),
				 SortHelperFunc, realContext);
		res = nil;
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	NS_ENDHANDLER

	Py_DECREF(realContext);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

static PyObject* call_NSMutableArray_sortUsingFunction_context_range_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	PyObject* sortFunc;
	PyObject* context;
	PyObject* rangeObj;
	NSRange range;
	PyObject* realContext;
	id  res;

	if  (!PyArg_ParseTuple(arguments, "OOO", &sortFunc, &context,
			 &rangeObj)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSRange), rangeObj, &range) < 0) {
		return NULL;
	}

	realContext = PyTuple_New(2);
	if (realContext == NULL) {
		return NULL;
	}
	PyTuple_SET_ITEM(realContext, 0, sortFunc);
	Py_INCREF(sortFunc);
	PyTuple_SET_ITEM(realContext, 1, context);
	Py_INCREF(context);

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

			
		(void)objc_msgSendSuper(&super,
			@selector(sortUsingFunction:context:range:),
			 SortHelperFunc, realContext, range);
		res = nil;
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	NS_ENDHANDLER

	Py_DECREF(realContext);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

#if 0

static PyObject* 
sortFuncWrapper(id (*func)(id, id, void*))
{
	/* Return an object that behaves like a callable and calls func */
}

static id 
imp_NSMutableArray_sortUsingFunction_context_(id self, SEL sel,
		id (*func)(id, id, void*), void* context)
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

	v = sortFuncWrapper(func);
	if (v == NULL ){
		 Py_DECREF(arglist);
		 PyObjCErr_ToObjC();
		 return nil;
	}
	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyCObject_New(context, NULL);
	if (v == NULL) {
		Py_DECRF(arglist);
		PyObjCErr_ToObjC();
		return nil;
	}
	PyTuple_SET_ITEM(arglist, 2, v);

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

static id 
imp_NSMutableArray_sortUsingFunction_context_range(id self, SEL sel,
		id (*func)(id, id, void*), void* context, NSRange range)
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

	v = sortFuncWrapper(func);
	if (v == NULL ){
		 Py_DECREF(arglist);
		 PyObjCErr_ToObjC();
		 return nil;
	}
	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyCObject_New(context, NULL);
	if (v == NULL) {
		Py_DECRF(arglist);
		PyObjCErr_ToObjC();
		return nil;
	}
	PyTuple_SET_ITEM(arglist, 2, v);

	v = PyObjC_ObjCToPython(@encode(NSRange), &range);
	if (v == NULL) {
		Py_DECRF(arglist);
		PyObjCErr_ToObjC();
		return nil;
	}
	PyTuple_SET_ITEM(arglist, 3, v);

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
#endif

static PyObject* call_NSMutableArray_removeObjectsFromIndices_numIndices_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	int err;
	struct objc_super super;
	PyObject* indicesList;
	PyObject* indicesSeq;
	unsigned* indices;
	int count;
	int i;

	if (!PyArg_ParseTuple(arguments, "Oi", &indicesList, &count)) {
		return NULL;
	}

	indicesSeq = PySequence_Fast(indicesList, "indices not a sequence");
	if (indicesSeq == NULL) {
		return NULL;
	}

	if (PySequence_Fast_GET_SIZE(indicesSeq) < count) {
		PyErr_SetString(PyExc_ValueError, "too few indices");
		Py_DECREF(indicesSeq);
		return NULL;
	}

	indices = alloca(sizeof(unsigned) * count);
	if (indices == NULL) {
		Py_DECREF(indicesSeq);
		PyErr_NoMemory();
		return NULL;
	}

	for (i = 0; i < count; i++) {
		err = PyObjC_PythonToObjC(@encode(unsigned), 
			PySequence_Fast_GET_ITEM(indicesSeq, i), indices + i);
		if (err == -1) {
			Py_DECREF(indicesSeq);
			PyErr_NoMemory();
			return NULL;
		}
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));
			
		objc_msgSendSuper(&super,
				@selector(removeObjectsFromIndices:numIndices:),
				indices, count);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	Py_DECREF(indicesSeq);

	if (PyErr_Occurred()) {
		return NULL;
	}
	
	result = Py_None;
	Py_INCREF(Py_None);
	return result;
}

static void imp_NSMutableArray_removeObjectsFromIndices_numIndices_(id self, 
	SEL sel, unsigned* indices, int count)
{
	PyObject* result;
	PyObject* arglist;
	PyObject* v;
	int i;

	arglist = PyTuple_New(3);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	v = PyObjC_IdToPython(self);
	if (v == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyTuple_New(count);
	if (v == NULL) {
		PyObjCErr_ToObjC();
		return;
	}
	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, PyObjC_ObjCToPython(@encode(unsigned),
				indices + i));
		if (PyTuple_GET_ITEM(v, i) == NULL) {
			Py_DECREF(v);
			Py_DECREF(arglist);
			PyObjCErr_ToObjC();
			return;
		}
	}
	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyInt_FromLong(count);
	if (v == NULL) {	
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}
	PyTuple_SET_ITEM(arglist, 2,  v);

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	Py_DECREF(result);
}

static PyObject* call_NSMutableArray_replaceObjectsInRange_withObjects_count_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	int err;
	struct objc_super super;
	PyObject* objectList;
	PyObject* objectSeq;
	PyObject* rangeObj;
	NSRange range;
	id* objects;
	int count;
	int i;

	if  (!PyArg_ParseTuple(arguments, "OOi", &rangeObj, &objectList, &count)) {
		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(NSRange), rangeObj, &range) < 0) {
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

			
		(void)objc_msgSendSuper(&super,
			@selector(replaceObjectsInRange:withObjects:count:),
			range, objects, count);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	Py_DECREF(objectSeq);

	if (PyErr_Occurred()) {
		return NULL;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}

static void imp_NSMutableArray_replaceObjectsInRange_withObjects_count_(
	id self, SEL sel, NSRange range, id* objects, int count)
{
	PyObject* result;
	PyObject* arglist;
	PyObject* v;
	int i;

	arglist = PyTuple_New(4);
	if (arglist == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	v = PyObjC_IdToPython(self);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyObjC_ObjCToPython(@encode(NSRange), &range);
	if (v == NULL) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}

	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyTuple_New(count);
	if (v == NULL) {
		PyObjCErr_ToObjC();
		return;
	}
	for (i = 0; i < count; i++) {
		PyTuple_SET_ITEM(v, i, PyObjC_IdToPython(objects[i]));
		if (PyTuple_GET_ITEM(v, i) == NULL) {
			Py_DECREF(v);
			Py_DECREF(arglist);
			PyObjCErr_ToObjC();
			return;
		}
	}
	PyTuple_SET_ITEM(arglist, 2, v);

	v = PyInt_FromLong(count);
	if (v == NULL) {	
		Py_DECREF(arglist);
		PyObjCErr_ToObjC();
		return;
	}
	PyTuple_SET_ITEM(arglist, 3,  v);

	result = PyObjC_CallPython(self, sel, arglist);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjC();
		return;
	}

	Py_DECREF(result);
}


static int 
_pyobjc_install_NSMutableArray(void)
{
	Class classNSMutableArray = objc_lookUpClass("NSMutableArray");

	if (PyObjC_RegisterMethodMapping(
		classNSMutableArray,
		@selector(sortUsingFunction:context:),
		call_NSMutableArray_sortUsingFunction_context_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSMutableArray,
		@selector(sortUsingFunction:context:range:),
		call_NSMutableArray_sortUsingFunction_context_range_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSMutableArray,
		@selector(removeObjectsFromIndices:numIndices:),
		call_NSMutableArray_removeObjectsFromIndices_numIndices_,
		(IMP)imp_NSMutableArray_removeObjectsFromIndices_numIndices_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSMutableArray,
		@selector(replaceObjectsInRange:withObjects:count:),
		call_NSMutableArray_replaceObjectsInRange_withObjects_count_,
		(IMP)imp_NSMutableArray_replaceObjectsInRange_withObjects_count_) < 0) {

		return -1;
	}

	return 0;
}
