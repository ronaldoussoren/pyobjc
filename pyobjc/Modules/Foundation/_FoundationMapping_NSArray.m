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
		if (PyObjCIMP_Check(method)) {
			res = ((id(*)(id,SEL, int(*)(id, id, void*), void*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					SortHelperFunc, realContext);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			
			res = objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method), 
					SortHelperFunc, realContext);
		}
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

static PyObject* 
call_NSArray_sortedArrayUsingFunction_context_hint_(
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
		if (PyObjCIMP_Check(method)) {
			res = ((id(*)(id,SEL, int(*)(id, id, void*), void*, id))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					SortHelperFunc, realContext, hint);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));
				
			res = objc_msgSendSuper(&super,
				 PyObjCSelector_GetSelector(method),
				 SortHelperFunc, realContext, hint);
		}
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

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	v = PyObjC_IdToPython(self);
	if (v == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	PyTuple_SET_ITEM(arglist, 0, v);

	v = sortFuncWrapper(func);
	if (v == NULL ){
		 Py_DECREF(arglist);
		 PyObjCErr_ToObjCWithGILState(&state);
		 return nil;
	}
	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyCObject_New(context, NULL);
	if (v == NULL) {
		Py_DECRF(arglist);
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}
	PyTuple_SET_ITEM(arglist, 2, v);

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	returnValue = PyObjC_PythonToId(result);
	Py_DECREF(result);
	if (PyErr_Occurred()) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}
	PyGILState_Release(state);
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


static int 
_pyobjc_install_NSArray(void)
{
	Class classNSArray = objc_lookUpClass("NSArray");
	if (classNSArray == NULL) return 0;

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
		call_objWithObjects_count_,
		imp_objWithObjects_count_) < 0) {

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
		call_clsWithObjects_count_,
		imp_clsWithObjects_count_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(initWithObjects:count:),
		call_objWithObjects_count_,
		imp_objWithObjects_count_)) {

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
