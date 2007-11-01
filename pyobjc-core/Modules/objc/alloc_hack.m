/*
 * alloc_hack.m -- Implementation of alloc_hack.h
 */
#include "pyobjc.h"

static PyObject*
call_NSObject_alloc(PyObject* method, 
	PyObject* self, PyObject* arguments)
{
	id result = nil;
	struct objc_super spr;
	IMP anIMP;
	Class aClass;
	SEL volatile aSel;

	if (unlikely(PyArg_ParseTuple(arguments, "") < 0)) {
		return NULL;
	}

	if (unlikely(!PyObjCClass_Check(self))) {
		PyErr_Format(PyExc_TypeError, "Expecting Objective-C class, got instance of '%s'", self->ob_type->tp_name);
		return NULL;
	}

	if (unlikely(PyObjCIMP_Check(method))) {
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
		objc_superSetReceiver(spr, (id)PyObjCClass_GetClass(self));
		objc_superSetClass(spr, object_getClass(PyObjCSelector_GetClass(method)));
		aSel = PyObjCSelector_GetSelector(method);

		PyObjC_DURING
			result = objc_msgSendSuper(&spr, aSel); 

		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);
			result = nil;

		PyObjC_ENDHANDLER;
	}

	if (unlikely(result == nil && PyErr_Occurred())) {
		return NULL;
	}

	return PyObjCObject_New(result, PyObjCObject_kUNINITIALIZED, NO);
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
		if (unlikely(arglist == NULL)) {
			PyObjC_GIL_FORWARD_EXC();
		}

		v = PyObjC_IdToPython(*(id*)args[0]);
		if (unlikely(v == NULL)) {
			Py_DECREF(arglist);
			PyObjC_GIL_FORWARD_EXC();
		}
		v = PyObjC_AdjustSelf(v);
		if (unlikely(v == NULL)) {
			Py_DECREF(arglist);
			PyObjC_GIL_FORWARD_EXC();
		}

		PyTuple_SET_ITEM(arglist, 0, v);
		v = NULL;

		result = PyObject_Call((PyObject*)callable, arglist, NULL);
		if (unlikely(result == NULL)) {
			Py_DECREF(arglist);
			PyObjC_GIL_FORWARD_EXC();
		}

		Py_DECREF(arglist); 

		err = depythonify_c_value(@encode(id), result, resp);
		Py_DECREF(result); 
		if (unlikely(err == -1)) {
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL
}

static PyObject*
call_NSObject_dealloc(PyObject* method, 
	PyObject* self, PyObject* arguments)
{
	struct objc_super spr;
	IMP anIMP;
	Class aClass;
	SEL volatile aSel;

	if (unlikely(PyArg_ParseTuple(arguments, "") < 0)) {
		return NULL;
	}

	if (unlikely(!PyObjCObject_Check(self))) {
		PyErr_Format(PyExc_TypeError, 
			"[dealloc] Expecting Objective-C instance, got instance of '%s'",
			self->ob_type->tp_name);
		return NULL;
	}

	if (unlikely(PyObjCIMP_Check(method))) {
		anIMP = PyObjCIMP_GetIMP(method);
		aClass = PyObjCClass_GetClass(self);
		aSel = PyObjCIMP_GetSelector(method);

		PyObjC_DURING
			(void)anIMP(aClass, aSel);

		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);

		PyObjC_ENDHANDLER;

	} else {
		objc_superSetReceiver(spr, PyObjCObject_GetObject(self));
		objc_superSetClass(spr, PyObjCSelector_GetClass(method)); 
		aSel = PyObjCSelector_GetSelector(method);

		PyObjC_DURING
			(void)objc_msgSendSuper(&spr, aSel); 

		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);

		PyObjC_ENDHANDLER;
	}

	PyObjCObject_ClearObject(self);

	if (unlikely(PyErr_Occurred())) {
		return NULL;
	}


	Py_INCREF(Py_None);
	return Py_None;
}

static void 
imp_NSObject_dealloc(
	ffi_cif* cif __attribute__((__unused__)), 
	void* resp __attribute__((__unused__)),  
	void** args __attribute__((__unused__)), 
	void* callable)
{
	PyObject* arglist = NULL;
	PyObject* v = NULL;
	PyObject* result = NULL;

	PyObjC_BEGIN_WITH_GIL

		arglist = PyTuple_New(1);
		if (unlikely(arglist == NULL)) {
			PyObjC_GIL_FORWARD_EXC();
		}

		v = PyObjC_IdToPython(*(id*)args[0]);
		if (unlikely(v == NULL)) {
			Py_DECREF(arglist);
			PyObjC_GIL_FORWARD_EXC();
		}

		PyTuple_SET_ITEM(arglist, 0, v);
		v = NULL;

		result = PyObject_Call((PyObject*)callable, arglist, NULL);
		if (unlikely(result == NULL)) {
			Py_DECREF(arglist);
			PyObjC_GIL_FORWARD_EXC();
		}

		Py_DECREF(arglist); 

		if (unlikely(result != Py_None)) {
			PyErr_Format(PyExc_TypeError,
				"dealloc should return None, returned instance"
				" of %s", result->ob_type->tp_name);
			PyObjC_GIL_FORWARD_EXC();
		}

		Py_DECREF(result);

	PyObjC_END_WITH_GIL
}

static PyObject*
call_NSObject_release(PyObject* method, 
	PyObject* self, PyObject* arguments)
{
	struct objc_super spr;
	IMP anIMP;
	Class aClass;
	SEL volatile aSel;

	if (unlikely(PyArg_ParseTuple(arguments, "") < 0)) {
		return NULL;
	}

	if (unlikely(!PyObjCObject_Check(self))) {
		PyErr_Format(PyExc_TypeError, 
			"[release] Expecting Objective-C instance, got instance of '%s'",
			self->ob_type->tp_name);
		return NULL;
	}

	if (unlikely(PyObjCIMP_Check(method))) {
		anIMP = PyObjCIMP_GetIMP(method);
		aClass = PyObjCClass_GetClass(self);
		aSel = PyObjCIMP_GetSelector(method);

		PyObjC_DURING
			(void)anIMP(aClass, aSel);

		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);

		PyObjC_ENDHANDLER;

	} else {
		objc_superSetReceiver(spr, PyObjCObject_GetObject(self));
		objc_superSetClass(spr, PyObjCSelector_GetClass(method)); 
		aSel = PyObjCSelector_GetSelector(method);

		PyObjC_DURING
			(void)objc_msgSendSuper(&spr, aSel); 

		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);

		PyObjC_ENDHANDLER;
	}

	if (unlikely(PyErr_Occurred())) {
		return NULL;
	}


	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject*
call_NSObject_retain(PyObject* method, 
	PyObject* self, PyObject* arguments)
{
	struct objc_super spr;
	IMP anIMP;
	Class aClass;
	SEL volatile aSel;
	volatile id retval = nil;

	if (unlikely(PyArg_ParseTuple(arguments, "") < 0)) {
		return NULL;
	}

	if (!PyObjCObject_Check(self)) {
		PyErr_Format(PyExc_TypeError, 
			"[retain] Expecting Objective-C instance, got instance of '%s'",
			self->ob_type->tp_name);
		return NULL;
	}

	if (PyObjCIMP_Check(method)) {
		anIMP = PyObjCIMP_GetIMP(method);
		aClass = PyObjCClass_GetClass(self);
		aSel = PyObjCIMP_GetSelector(method);

		PyObjC_DURING
			retval = anIMP(aClass, aSel);

		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);

		PyObjC_ENDHANDLER;

	} else {
		objc_superSetReceiver(spr, PyObjCObject_GetObject(self));
		objc_superSetClass(spr, PyObjCSelector_GetClass(method));
		aSel = PyObjCSelector_GetSelector(method);

		PyObjC_DURING
			retval = objc_msgSendSuper(&spr, aSel); 

		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);

		PyObjC_ENDHANDLER;
	}

	if (PyErr_Occurred()) {
		return NULL;
	}

	return PyObjC_IdToPython(retval);
}

static void 
imp_NSObject_release(
	ffi_cif* cif __attribute__((__unused__)), 
	void* resp __attribute__((__unused__)),  
	void** args __attribute__((__unused__)), 
	void* callable)
{
	PyObject* arglist = NULL;
	PyObject* result = NULL;
	PyObject* pyself;
	int cookie;

	PyObjC_BEGIN_WITH_GIL

		arglist = PyTuple_New(1);
		if (arglist == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		pyself = PyObjCObject_NewTransient(*(id*)args[0], &cookie);
		if (pyself == NULL) {
			Py_DECREF(arglist);
			PyObjC_GIL_FORWARD_EXC();
		}

		PyTuple_SET_ITEM(arglist, 0, pyself);
		Py_INCREF(pyself);

		result = PyObject_Call((PyObject*)callable, arglist, NULL);
		if (result == NULL) {
			Py_DECREF(arglist);
			PyObjCObject_ReleaseTransient(pyself, cookie);
			PyObjC_GIL_FORWARD_EXC();
		}

		Py_DECREF(arglist); 
		PyObjCObject_ReleaseTransient(pyself, cookie);

		if (result != Py_None) {
			PyErr_Format(PyExc_TypeError,
				"release should return None, returned instance"
				" of %s", result->ob_type->tp_name);
			PyObjC_GIL_FORWARD_EXC();
		}

		Py_DECREF(result);

	PyObjC_END_WITH_GIL
}

static void 
imp_NSObject_retain(
	ffi_cif* cif __attribute__((__unused__)), 
	void* resp __attribute__((__unused__)),  
	void** args __attribute__((__unused__)), 
	void* callable)
{
	PyObject* arglist = NULL;
	PyObject* result = NULL;
	PyObject* pyself;
	int cookie;
	int err;

	PyObjC_BEGIN_WITH_GIL

		arglist = PyTuple_New(1);
		if (arglist == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		pyself = PyObjCObject_NewTransient(*(id*)args[0], &cookie);
		if (pyself == NULL) {
			Py_DECREF(arglist);
			PyObjC_GIL_FORWARD_EXC();
		}

		PyTuple_SET_ITEM(arglist, 0, pyself);
		Py_INCREF(pyself);

		result = PyObject_Call((PyObject*)callable, arglist, NULL);
		if (result == NULL) {
			Py_DECREF(arglist);
			PyObjCObject_ReleaseTransient(pyself, cookie);
			PyObjC_GIL_FORWARD_EXC();
		}

		Py_DECREF(arglist); 

		err = depythonify_c_value(@encode(id), result, resp);
		Py_DECREF(result); 
		PyObjCObject_ReleaseTransient(pyself, cookie);
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
		objc_lookUpClass("NSObject"),
		@selector(alloc),
		call_NSObject_alloc,
		imp_NSObject_alloc);
	if (r != 0) return r;

	r = PyObjC_RegisterMethodMapping(
		objc_lookUpClass("NSObject"),
		@selector(dealloc),
		call_NSObject_dealloc,
		imp_NSObject_dealloc);
	if (r != 0) return r;

	r = PyObjC_RegisterMethodMapping(
		objc_lookUpClass("NSObject"),
		@selector(retain),
		call_NSObject_retain,
		imp_NSObject_retain);
	if (r != 0) return r;

	r = PyObjC_RegisterMethodMapping(
		objc_lookUpClass("NSObject"),
		@selector(release),
		call_NSObject_release,
		imp_NSObject_release);
	if (r != 0) return r;

	r = PyObjC_RegisterMethodMapping(
		objc_lookUpClass("NSObject"),
		@selector(autorelease),
		call_NSObject_release,
		imp_NSObject_release);
	if (r != 0) return r;

	return r;
}
