/*
 * Special wrappers for NSView methods with 'difficult' arguments.
 *
 * -sortSubviewsUsingFunction:context:			[call]
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"


static PyObject* 
call_NSView_sortSubviewsUsingFunction_context_(
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

			
		res = objc_msgSendSuper(&super,
				@selector(sortSubviewsUsingFunction:context:),
				 SortHelperFunc, realContext);
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
call_NSView_getRectsBeingDrawn_count_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	PyObject* v;
	NSRect* rects;
	int count;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

			
		objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				&rects, &count);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	v = PyObjC_CArrayToPython(@encode(NSRect), rects, count);
	if (v == NULL) return NULL;

	result = Py_BuildValue("Oi", v, count);
	Py_XDECREF(v);

	return result;
}


static int 
_pyobjc_install_NSView(void)
{
	Class classNSView = objc_lookUpClass("NSView");

	if (PyObjC_RegisterMethodMapping(
		classNSView,
		@selector(sortSubviewsUsingFunction:context:),
		call_NSView_sortSubviewsUsingFunction_context_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSView,
		@selector(getRectsBeingDrawn:count:),
		call_NSView_getRectsBeingDrawn_count_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
