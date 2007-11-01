#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"


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
			PyObjC_GIL_FORWARD_EXC();
		}
		Py_DECREF(r);

		PyObjC_GIL_RETURN(res);

	PyObjC_END_WITH_GIL

}


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



static PyMethodDef mod_methods[] = {
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_nsview(void);
void init_nsview(void)
{
	PyObject* m = Py_InitModule4("_nsview", mod_methods, "", NULL,
			PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);

	Class classNSView = objc_lookUpClass("NSView");

	if (PyObjC_RegisterMethodMapping(
		classNSView,
		@selector(sortSubviewsUsingFunction:context:),
		call_NSView_sortSubviewsUsingFunction_context_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSView,
		@selector(getRectsBeingDrawn:count:),
		call_NSView_getRectsBeingDrawn_count_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return;
	}
}
