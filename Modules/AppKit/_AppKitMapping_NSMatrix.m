/*
 * Special wrappers for NSMatrix methods with 'difficult' arguments.
 *
 * -sortUsingFunction:context:			[call]
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"

/*
 * Helper function for sortUsingFunction:context:
 */
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
call_NSMatrix_sortUsingFunction_context_(
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
				@selector(sortUsingFunction:context:),
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

#if 0

static PyObject* 
sortFuncWrapper(id (*func)(id, id, void*))
{
	/* Return an object that behaves like a callable and calls func */
}

static id 
imp_NSMatrix_sortUsingFunction_context_(id self, SEL sel,
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

#endif


static int 
_pyobjc_install_NSMatrix(void)
{
	Class classNSMatrix = objc_lookUpClass("NSMatrix");

	if (PyObjC_RegisterMethodMapping(
		classNSMatrix,
		@selector(sortUsingFunction:context:),
		call_NSMatrix_sortUsingFunction_context_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
