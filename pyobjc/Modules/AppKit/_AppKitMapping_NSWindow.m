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

#include "pymactoolbox.h"

static PyObject* call_NSWindow_windowRef(
		PyObject* method, 
		PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     windowRef;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));


		windowRef = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method));
		if (windowRef == NULL) {
			result = Py_None;
			Py_INCREF(result);
		} else {
			result = WinObj_New((WindowPtr)windowRef);
		}

	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static void* imp_NSWindow_windowRef(id self, SEL sel)
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

	WinObj_Convert(result, (WindowPtr*)&objc_result); 
	Py_DECREF(result);

	if (PyErr_Occurred()) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	PyGILState_Release(state);
	return objc_result;
}


static PyObject* call_NSWindow_initWithWindowRef_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	void*     windowRef;
	id        objc_result;

	if  (!PyArg_ParseTuple(arguments, "O&", WinObj_Convert, &windowRef)) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super, 
			PyObjCSelector_GetClass(method),
			PyObjCObject_GetObject(self));

		objc_result = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method), windowRef);
		result = PyObjC_IdToPython(objc_result);

	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		result = NULL;
	NS_ENDHANDLER

	return result;
}

static id imp_NSWindow_initWithWindowRef_(id self, SEL sel, void* windowRef)
{
	PyObject* result;
	PyObject* arglist;
	id        objc_result;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}
	
	PyTuple_SET_ITEM(arglist, 0, WinObj_New(windowRef));
	if (PyErr_Occurred()) {
		Py_DECREF(arglist);
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist, NULL);
	Py_DECREF(arglist);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	objc_result = PyObjC_PythonToId(result);

	if (PyErr_Occurred()) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	PyGILState_Release(state);
	return objc_result;
}


static int 
_pyobjc_install_NSWindow(void)
{
	Class classNSWindow = objc_lookUpClass("NSWindow");

	if (PyObjC_RegisterMethodMapping(
		classNSWindow,
		@selector(initWithWindowRef:),
		call_NSWindow_initWithWindowRef_,
		(IMP)imp_NSWindow_initWithWindowRef_) < 0) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSWindow,
		@selector(windowRef),
		call_NSWindow_windowRef,
		(IMP)imp_NSWindow_windowRef) < 0) {

		return -1;
	}

	return 0;
}
