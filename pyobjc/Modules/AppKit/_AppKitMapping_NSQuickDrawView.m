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

#ifdef MACOSX

static PyObject* 
call_NSQuickDrawView_qdport(
		PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     port;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));


		port = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method));

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		port = NULL;
	
	PyObjC_ENDHANDLER

	if (port == NULL) {
		if (PyErr_Occurred()) return NULL;
		result = Py_None;
		Py_INCREF(result);
	} else {
		result = GrafObj_New((GrafPtr)port);
	}

	return result;
}

static void 
imp_NSQuickDrawView_qdport(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	GrafPtr* pretval = (GrafPtr*)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 0, v);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	GrafObj_Convert(result, pretval);
	Py_DECREF(result);

	if (PyErr_Occurred()) goto error;

	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	*pretval = NULL;
	PyObjCErr_ToObjCWithGILState(&state);
}

#endif /* MACOSX */

static int 
_pyobjc_install_NSQuickDrawView(void)
{

#ifdef MACOSX 
	Class classNSQuickDrawView = objc_lookUpClass("NSQuickDrawView");

	if (PyObjC_RegisterMethodMapping(
		classNSQuickDrawView,
		@selector(qdport),
		call_NSQuickDrawView_qdport,
		imp_NSQuickDrawView_qdport) < 0) {

		return -1;
	}
#endif /* MACOSX */

	return 0;
}
