/*
 * The default processing doesn't work for some calls to alloc. Therefore
 * we install custom handlers for these calls.
 */
#include "pyobjc.h"
#include "objc_support.h"

static PyObject*
call_NSObject_alloc(PyObject* method, PyObject* self, PyObject* arguments)
{
	id result = nil;

	if (PyArg_ParseTuple(arguments, "") < 0) {
		return NULL;
	}

	if (!PyObjCClass_Check(self)) {
		PyErr_SetString(PyExc_TypeError, "Expecting class");
		return NULL;
	}

	NS_DURING
		result = [PyObjCClass_GetClass(self) alloc];
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = nil;
	NS_ENDHANDLER;

	if (result == nil && PyErr_Occurred()) {
		return NULL;
	}

	if (PyObjC_HasPythonImplementation(result)) {
		return PyObjC_GetPythonImplementation(result);
	}
	return PyObjCObject_NewUnitialized(result);
}

static PyObject*
supercall_NSObject_alloc(PyObject* method, PyObject* self, PyObject* arguments)
{
	id result = nil;
	struct objc_super super;

	if (PyArg_ParseTuple(arguments, "") < 0) {
		return NULL;
	}

	if (!PyObjCClass_Check(self)) {
		PyErr_SetString(PyExc_TypeError, "Expecting class");
		return NULL;
	}

	/* XXX: Shouldn't we use method->sel_class here? */
	RECEIVER(super) = (id)PyObjCClass_GetClass(self);
	super.class = GETISA((Class)(RECEIVER(super)));

	NS_DURING
		result = objc_msgSendSuper(&super, @selector(alloc));
	NS_HANDLER
		ObjCErr_FromObjC(localException);
		result = nil;
	NS_ENDHANDLER;

	if (result == nil && PyErr_Occurred()) {
		return NULL;
	}

	if (PyObjC_HasPythonImplementation(result)) {
		return PyObjC_GetPythonImplementation(result);
	}
	return PyObjCObject_NewUnitialized(result);
}

static id 
imp_NSObject_alloc(id self, SEL sel)
{
	id objc_result;
	int err;
	PyObject* arglist;
	PyObject* result;

	arglist = PyTuple_New(0);
	if (arglist == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	result = PyObjC_CallPython(self, sel, arglist);
	if (result == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	err = depythonify_c_value("@", result, &objc_result);
	Py_DECREF(result);
	if (err == -1) {
		return NULL;
	}

	return objc_result;
}

int
PyObjC_InstallAllocHack(void)
{
	return ObjC_RegisterMethodMapping(
		objc_lookUpClass("NSObject"),
		@selector(alloc),
		call_NSObject_alloc,
		supercall_NSObject_alloc,
		(IMP)imp_NSObject_alloc);
}
