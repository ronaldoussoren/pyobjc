/*
 * alloc_hack.m -- Implementation of alloc_hack.h
 */
#include "pyobjc.h"

static PyObject*
call_NSObject_alloc(PyObject* method, 
	PyObject* self, PyObject* arguments)
{
	id result = nil;
	struct objc_super super;
	PyThreadState *_save;
	IMP anIMP;
	Class aClass;
	SEL aSel;

	if (PyArg_ParseTuple(arguments, "") < 0) {
		return NULL;
	}

	if (!PyObjCClass_Check(self)) {
		PyErr_SetString(PyExc_TypeError, "Expecting class");
		return NULL;
	}

	if (PyObjCIMP_Check(method)) {
		anIMP = PyObjCIMP_GetIMP(method);
		aClass = PyObjCClass_GetClass(self);
		aSel = PyObjCIMP_GetSelector(method);
		Py_UNBLOCK_THREADS
		NS_DURING
			result = anIMP(aClass, aSel);
		NS_HANDLER
			PyObjCErr_FromObjC(localException);
			result = nil;
		NS_ENDHANDLER;
		Py_BLOCK_THREADS

	} else {
		RECEIVER(super) = (id)PyObjCClass_GetClass(self);
		super.class = PyObjCSelector_GetClass(method); 
		super.class = GETISA(super.class);
		aSel = PyObjCSelector_GetSelector(method);

		Py_UNBLOCK_THREADS
		NS_DURING
			result = objc_msgSendSuper(&super, aSel); 
		NS_HANDLER
			PyObjCErr_FromObjC(localException);
			result = nil;
		NS_ENDHANDLER;
		Py_BLOCK_THREADS
	}

	if (result == nil && PyErr_Occurred()) {
		return NULL;
	}

	return PyObjCObject_NewUnitialized(result);
}

static void 
imp_NSObject_alloc(
	ffi_cif* cif __attribute__((__unused__)), 
	void* resp, 
	void** args __attribute__((__unused__)), 
	void* callable)
{
	int err;
	PyObject* arglist = NULL;
	PyObject* v = NULL;
	PyObject* result = NULL;

	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(1);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(*(id*)args[0]);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 0, v);
	v = NULL;

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	if (result == NULL) goto error;

	Py_DECREF(arglist); arglist = NULL;

	err = depythonify_c_value("@", result, resp);
	Py_DECREF(result); result = NULL;
	if (err == -1) goto error;

	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
	return;
}

int
PyObjC_InstallAllocHack(void)
{
	int r;

	r = PyObjC_RegisterMethodMapping(
		PyObjCRT_LookUpClass("NSObject"),
		@selector(alloc),
		call_NSObject_alloc,
		imp_NSObject_alloc);
	if (r != 0) return r;

	return r;
}
