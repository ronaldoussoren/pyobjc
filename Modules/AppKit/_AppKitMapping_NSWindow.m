/*
 * Special wrappers for NSWindow methods with 'difficult' arguments.
 *
 * Note: WindowRef is the new name for WindowPtr, the old name is used in
 * the MacPython headers.
 *
 * -initWithWindowRef:
 * -windowRef
 *
 * NOTE: Requires MacPython for complete functionality.
 */
#include <Python.h>
#include <AppKit/AppKit.h>
#include "pyobjc-api.h"

#ifdef MACOSX

#include "pymactoolbox.h"

static PyObject* 
call_NSWindow_windowRef(
	PyObject* method, 
	PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     windowRef;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));


		windowRef = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method));

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
		windowRef = NULL;
	PyObjC_ENDHANDLER

	if (windowRef == NULL) {
		if (PyErr_Occurred()) return NULL;
		result = Py_None;
		Py_INCREF(result);
	} else {
		result = WinObj_New((WindowPtr)windowRef);
	}

	return result;
}

static void 
imp_NSWindow_windowRef(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	WindowPtr* pretval = (WindowPtr*)resp;

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

	WinObj_Convert(result, pretval);
	Py_DECREF(result);
	if (PyErr_Occurred()) goto error;

	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	*pretval = NULL;
	PyObjCErr_ToObjCWithGILState(&state);
}


static PyObject* 
call_NSWindow_initWithWindowRef_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     windowRef;
	id        objc_result;

	if  (!PyArg_ParseTuple(arguments, "O&", WinObj_Convert, &windowRef)) {
		return NULL;
	}

	PyObjC_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		objc_result = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method), windowRef);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		objc_result = nil;
		
	PyObjC_ENDHANDLER

	if (objc_result == nil && PyErr_Occurred()) return nil;

	result = PyObjC_IdToPython(objc_result);

	return result;
}

static void 
imp_NSWindow_initWithWindowRef_(
	void* cif __attribute__((__unused__)), 
	void* resp, 
	void** args, 
	void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	WindowPtr windowRef = *(WindowPtr*)args[2];
	id* pretval = (id*)resp;

	PyObject* result;
	PyObject* arglist = NULL;
	PyObject* v;

	PyGILState_STATE state = PyObjCGILState_Ensure();

	arglist = PyTuple_New(2);
	if (arglist == NULL) goto error;
	
	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 0, v);
	
	v = WinObj_New(windowRef);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 1, v); 

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	*pretval = PyObjC_PythonToId(result);
	if (*pretval == nil && PyErr_Occurred()) goto error;

	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	*pretval = nil;
	PyObjCErr_ToObjCWithGILState(&state);
}

#endif /* MACOSX */


static int 
_pyobjc_install_NSWindow(void)
{

#ifdef MACOSX 
	Class classNSWindow = objc_lookUpClass("NSWindow");

	if (PyObjC_RegisterMethodMapping(
		classNSWindow,
		@selector(initWithWindowRef:),
		call_NSWindow_initWithWindowRef_,
		imp_NSWindow_initWithWindowRef_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSWindow,
		@selector(windowRef),
		call_NSWindow_windowRef,
		imp_NSWindow_windowRef) < 0) {

		return -1;
	}
#endif /* MACOSX */

	return 0;
}
