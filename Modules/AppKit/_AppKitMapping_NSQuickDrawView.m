/*
 * Special wrappers for NSQuickDrawView methods with 'difficult' arguments.
 *
 * -qdPort		[call, imp]
 *
 * NOTE: Requires MacPython for complete functionality.
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"


static PyObject* call_NSQuickDrawView_qdport(
		PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     port;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));


		port = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method));
		if (port == NULL) {
			result = Py_None;
			Py_INCREF(result);
		} else {
			result = GrafObj_New((GrafPtr)port);
		}

	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void* imp_NSQuickDrawView_qdport(id self, SEL sel)
{
	PyObject* result;
	PyObject* arglist;
	void*    objc_result;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(0);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	GrafObj_Convert(result, (GrafPtr*)&objc_result); 
	Py_DECREF(result);

	if (PyErr_Occurred()) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	PyGILState_Release(state);
	return objc_result;
}


static int 
_pyobjc_install_NSQuickDrawView(void)
{
	Class classNSQuickDrawView = objc_lookUpClass("NSQuickDrawView");

	if (PyObjC_RegisterMethodMapping(
		classNSQuickDrawView,
		@selector(qdport),
		call_NSQuickDrawView_qdport,
		(IMP)imp_NSQuickDrawView_qdport) < 0) {

		return -1;
	}

	return 0;
}
