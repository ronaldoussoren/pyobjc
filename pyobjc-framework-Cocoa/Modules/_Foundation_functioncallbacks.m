/*
 * Wrappers for methods with callback functions.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

static int
SortHelperFunc(id arg1, id arg2, void* opaque)
{
	PyObjC_BEGIN_WITH_GIL

		PyObject* func = PyTuple_GetItem((PyObject*)opaque, 0);
		PyObject* context = PyTuple_GetItem((PyObject*)opaque, 1);
		PyObject* a1;
		PyObject* a2;
		PyObject* r;
		int res;

		if (func == NULL || context == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}
	
		a1 = PyObjC_IdToPython(arg1);
		if (a1 == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		a2 = PyObjC_IdToPython(arg2);
		if (a2 == NULL) {
			Py_DECREF(a1);
			PyObjC_GIL_FORWARD_EXC();
		}

		r = PyObject_CallFunction(func, "OOO", a1, a2, context);
		Py_DECREF(a1);
		Py_DECREF(a2);
		if (r == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		if (PyObjC_PythonToObjC(@encode(int), r, &res) < 0) {
			Py_DECREF(r);
			PyObjC_GIL_FORWARD_EXC();
		}
		Py_DECREF(r);

		PyObjC_GIL_RETURN(res);
	PyObjC_END_WITH_GIL

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

	PyObjC_DURING
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
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	PyObjC_ENDHANDLER

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

	PyObjC_DURING
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
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	PyObjC_ENDHANDLER

	Py_DECREF(realContext);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}


static PyObject* 
call_NSMutableArray_sortUsingFunction_context_(
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

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

			
		(void)objc_msgSendSuper(&super,
				@selector(sortUsingFunction:context:),
				 SortHelperFunc, realContext);
		res = nil;
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	PyObjC_ENDHANDLER

	Py_DECREF(realContext);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

static PyObject* 
call_NSMutableArray_sortUsingFunction_context_range_(
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

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

			
		(void)objc_msgSendSuper(&super,
			@selector(sortUsingFunction:context:range:),
			 SortHelperFunc, realContext, range);
		res = nil;
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	PyObjC_ENDHANDLER

	Py_DECREF(realContext);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

PyDoc_STRVAR(mod_doc, "");

static PyMethodDef mod_methods[] = {
        { 0, 0, 0, 0 } /* sentinel */
};



void init_functioncallbacks(void);

void
init_functioncallbacks(void)
{
	PyObject* m = Py_InitModule4("_functioncallbacks", mod_methods, 
		mod_doc, NULL, PYTHON_API_VERSION);

	if (PyObjC_ImportAPI(m) < 0) { return; }

	Class classNSArray = objc_lookUpClass("NSArray");

	/* XXX: this one is mostly here because I'd like to add support someday
	 */
	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(apply:context:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(sortedArrayUsingFunction:context:),
		call_NSArray_sortedArrayUsingFunction_context_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSArray,
		@selector(sortedArrayUsingFunction:context:hint:),
		call_NSArray_sortedArrayUsingFunction_context_hint_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}



	Class classNSMutableArray = objc_lookUpClass("NSMutableArray");

	if (PyObjC_RegisterMethodMapping(
		classNSMutableArray,
		@selector(sortUsingFunction:context:),
		call_NSMutableArray_sortUsingFunction_context_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSMutableArray,
		@selector(sortUsingFunction:context:range:),
		call_NSMutableArray_sortUsingFunction_context_range_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}
}
