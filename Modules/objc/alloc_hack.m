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
	IMP anIMP;
	Class aClass;
	SEL volatile aSel;

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

		PyObjC_DURING
			result = anIMP(aClass, aSel);

		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);
			result = nil;

		PyObjC_ENDHANDLER;

	} else {
		RECEIVER(super) = (id)PyObjCClass_GetClass(self);
		super.class = PyObjCSelector_GetClass(method); 
		super.class = GETISA(super.class);
		aSel = PyObjCSelector_GetSelector(method);

		PyObjC_DURING
			result = objc_msgSendSuper(&super, aSel); 

		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);
			result = nil;

		PyObjC_ENDHANDLER;
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

	PyObjC_BEGIN_WITH_GIL

		arglist = PyTuple_New(1);
		if (arglist == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		v = PyObjC_IdToPython(*(id*)args[0]);
		if (v == NULL) {
			Py_DECREF(arglist);
			PyObjC_GIL_FORWARD_EXC();
		}

		PyTuple_SET_ITEM(arglist, 0, v);
		v = NULL;

		result = PyObject_Call((PyObject*)callable, arglist, NULL);
		if (result == NULL) {
			Py_DECREF(arglist);
			PyObjC_GIL_FORWARD_EXC();
		}

		Py_DECREF(arglist); 

		err = depythonify_c_value(@encode(id), result, resp);
		Py_DECREF(result); 
		if (err == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL
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
