/*
 * Special wrappers for NSArray methods with 'difficult' arguments.
 *
 * -initWithObjects:count:		[call, imp]
 * -arrayByAddingObjects:count:		[call, imp]
 * +arrayWithObjects:count:		[call, imp]
 *
 * -sortedArrayUsingFunction:context:			[call]
 * -sortedArrayUsingFunction:context:hint:		[call]
 *
 * Unsupported methods: (The usual access methods are good enough)
 * -getObjects:
 * -getObjects:range:
 *
 * Undocumented methods:
 * -apply:context:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

/*
 * Helper function for sortedArrayUsing...
 */
static int
SortHelperFunc(id arg1, id arg2, void* opaque)
{
	PyObject* func = PyTuple_GetItem((PyObject*)opaque, 0);
	PyObject* context = PyTuple_GetItem((PyObject*)opaque, 1);
	PyObject* a1;
	PyObject* a2;
	PyObject* r;
	int res;

	if (func == NULL || context == NULL) {
		PyObjCErr_ToObjC();
		return NSOrderedSame;
	}
	
	a1 = PyObjC_IdToPython(arg1);
	if (a1 == NULL) {
		PyObjCErr_ToObjC();
		return NSOrderedSame;
	}

	a2 = PyObjC_IdToPython(arg2);
	if (a2 == NULL) {
		Py_DECREF(a1);
		PyObjCErr_ToObjC();
		return NSOrderedSame;
	}

	r = PyObject_CallFunction(func, "OOO", a1, a2, context);
	Py_DECREF(a1);
	Py_DECREF(a2);
	if (r == NULL) {
		PyObjCErr_ToObjC();
		return NSOrderedSame;
	}

	if (PyObjC_PythonToObjC(@encode(int), r, &res) < 0) {
		Py_DECREF(r);
		PyObjCErr_ToObjC();
		return NSOrderedSame;
	}
	Py_DECREF(r);

	return res;
}

static PyObject* 
call_NSArray_sortedArrayUsingFunction_context_(
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

			
		res = objc_msgSendSuper(&super,
				@selector(sortedArrayUsingFunction:context:),
				 SortHelperFunc, realContext);
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

static PyObject* call_NSArray_sortedArrayUsingFunction_context_hint_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	PyObject* sortFunc;
	PyObject* context;
	id hint = nil;
	PyObject* realContext;
	id  res;

	if  (!PyArg_ParseTuple(arguments, "OOO&", &sortFunc, &context,
			PyObjCObject_Convert, &hint)) {
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

			
		res = objc_msgSendSuper(&super,
			@selector(sortedArrayUsingFunction:context:hint:),
			 SortHelperFunc, realContext, hint);
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
imp_NSArray_sortedArrayUsingFunction_context_(id self, SEL sel,
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

static id 
imp_NSArray_sortedArrayUsingFunction_context_hint_(id self, SEL sel,
		id (*func)(id, id, void*), void* context, id hint)
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

	v = PyObjC_IdToPython(hint);
	if (v == NULL) {
		Py_DECRF(arglist);
		PyObjCErr_ToObjC();
		return nil;
	}
	PyTuple_SET_ITEM(arglist, 3, v);

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
#endif

static PyObject* call_NSArray_arrayWithObjects_count_(
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

	if  (!PyArg_ParseTuple(arguments, "Oi", &objectList, &count)) {
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
				@selector(arrayWithObjects:count:),
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

static id imp_NSArray_arrayWithObjects_count_(id self, SEL sel,
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

static PyObject* call_NSArray_arrayByAddingObjects_count_(
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

	if  (!PyArg_ParseTuple(arguments, "Oi", &objectList, &count)) {
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
				@selector(arrayByAddingObjects:count:),
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

static id imp_NSArray_arrayByAddingObjects_count_(id self, SEL sel,
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

static PyObject* call_NSArray_initWithObjects_count_(
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

	if  (!PyArg_ParseTuple(arguments, "Oi", &objectList, &count)) {
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

static id imp_NSArray_initWithObjects_count_(id self, SEL sel,
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
_pyobjc_install_NSArray(void)
{
	Class classNSArray = objc_lookUpClass("NSArray");

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(apply:context:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(arrayByAddingObjects:count:),
		call_NSArray_arrayByAddingObjects_count_,
		(IMP)imp_NSArray_arrayByAddingObjects_count_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(getObjects:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(getObjects:range:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(initWithObjects:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(arrayWithObjects:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(arrayWithObjects:count:),
		call_NSArray_arrayWithObjects_count_,
		(IMP)imp_NSArray_arrayWithObjects_count_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(initWithObjects:count:),
		call_NSArray_initWithObjects_count_,
		(IMP)imp_NSArray_initWithObjects_count_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(sortedArrayUsingFunction:context:),
		call_NSArray_sortedArrayUsingFunction_context_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(sortedArrayUsingFunction:context:hint:),
		call_NSArray_sortedArrayUsingFunction_context_hint_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
