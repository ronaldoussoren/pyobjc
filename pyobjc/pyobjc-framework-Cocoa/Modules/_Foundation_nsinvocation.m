#include "Python.h"
#include "pyobjc-api.h"

#include <Foundation/Foundation.h>

static PyObject* 
call_NSInvocation_setArgument_atIndex_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	NSMethodSignature* signature;
	const char* tp;
	PyObject* py_value;
	Py_ssize_t index;
	void* buf;
	Py_ssize_t sz;

	if  (!PyArg_ParseTuple(arguments, "On", &py_value, &index)) {
		return NULL;
	}

	PyObjC_DURING
		signature = [(NSInvocation*)PyObjCObject_GetObject(self) methodSignature];

		tp = [signature getArgumentTypeAtIndex:index];
	
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		signature = NULL;

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	sz = PyObjCRT_SizeOfType(tp);
	if (sz == -1) {
		return NULL;
	}

	buf = PyMem_Malloc(sz);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	if (PyObjC_PythonToObjC(tp, py_value, buf) == -1) {
		PyMem_Free(buf);
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, void*, NSUInteger))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					buf, index);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					buf, index);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	PyMem_Free(buf);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* 
call_NSInvocation_setReturnValue_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	NSMethodSignature* signature;
	const char* tp;
	PyObject* py_value;
	void* buf;
	Py_ssize_t sz;

	if  (!PyArg_ParseTuple(arguments, "O", &py_value)) {
		return NULL;
	}

	PyObjC_DURING
		signature = [(NSInvocation*)PyObjCObject_GetObject(self) methodSignature];

		tp = [signature methodReturnType];
	
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		signature = NULL;

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	sz = PyObjCRT_SizeOfType(tp);
	if (sz == -1) {
		return NULL;
	}

	buf = PyMem_Malloc(sz);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	if (PyObjC_PythonToObjC(tp, py_value, buf) == -1) {
		PyMem_Free(buf);
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, void*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					buf);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					buf);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	PyMem_Free(buf);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject* 
call_NSInvocation_getArgument_atIndex_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	NSMethodSignature* signature;
	const char* tp;
	PyObject* py_value;
	Py_ssize_t index;
	void* buf;
	Py_ssize_t sz;

	if  (!PyArg_ParseTuple(arguments, "On", &py_value, &index)) {
		return NULL;
	}

	if (py_value != Py_None) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}

	PyObjC_DURING
		signature = [(NSInvocation*)PyObjCObject_GetObject(self) methodSignature];

		tp = [signature getArgumentTypeAtIndex:index];
	
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		signature = NULL;

	PyObjC_ENDHANDLER


	if (PyErr_Occurred()) {
		return NULL;
	}

	sz = PyObjCRT_SizeOfType(tp);
	if (sz == -1) {
		return NULL;
	}

	buf = PyMem_Malloc(sz);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}


	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, void*, NSUInteger))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					buf, index);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					buf, index);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER


	if (PyErr_Occurred()) {
		PyMem_Free(buf);
		return NULL;
	}

	py_value = PyObjC_ObjCToPython(tp, buf);
	PyMem_Free(buf);
	if (py_value == NULL) {
		return NULL;
	}

	return py_value;
}

static PyObject* 
call_NSInvocation_getReturnValue_(
	PyObject* method, PyObject* self, PyObject* arguments)
{
	struct objc_super super;
	NSMethodSignature* signature;
	const char* tp;
	PyObject* py_value;
	void* buf;
	Py_ssize_t sz;

	if  (!PyArg_ParseTuple(arguments, "O", &py_value)) {
		return NULL;
	}

	if (py_value != Py_None) {
		PyErr_SetString(PyExc_ValueError, "buffer must be None");
		return NULL;
	}

	PyObjC_DURING
		signature = [(NSInvocation*)PyObjCObject_GetObject(self) methodSignature];

		tp = [signature methodReturnType];
	
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		signature = NULL;

	PyObjC_ENDHANDLER


	if (PyErr_Occurred()) {
		return NULL;
	}

	sz = PyObjCRT_SizeOfType(tp);
	if (sz == -1) {
		return NULL;
	}

	buf = PyMem_Malloc(sz);
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}


	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			((void(*)(id,SEL, void*))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					buf);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			(void)objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					buf);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER


	if (PyErr_Occurred()) {
		PyMem_Free(buf);
		return NULL;
	}

	py_value = PyObjC_ObjCToPython(tp, buf);
	PyMem_Free(buf);
	if (py_value == NULL) {
		return NULL;
	}

	return py_value;
}


PyDoc_STRVAR(mod_doc, "");

static PyMethodDef mod_methods[] = {
	        { 0, 0, 0, 0 } /* sentinel */
};

void init_nsinvocation(void);

void
init_nsinvocation(void)
{
	PyObject* m = Py_InitModule4("_nsinvocation", mod_methods,
			mod_doc, NULL, PYTHON_API_VERSION);

	if (PyObjC_ImportAPI(m) < 0) { return; }

	Class classNSInvocation = objc_lookUpClass("NSInvocation");
  
	if (PyObjC_RegisterMethodMapping(
			classNSInvocation,
			@selector(setArgument:atIndex:),
			call_NSInvocation_setArgument_atIndex_,
			PyObjCUnsupportedMethod_IMP) < 0) {
		return;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSInvocation,
			@selector(setReturnValue:),
			call_NSInvocation_setReturnValue_,
			PyObjCUnsupportedMethod_IMP) < 0) {
		return;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSInvocation,
			@selector(getArgument:atIndex:),
			call_NSInvocation_getArgument_atIndex_,
			PyObjCUnsupportedMethod_IMP) < 0) {
		return;
	}

	if (PyObjC_RegisterMethodMapping(
			classNSInvocation,
			@selector(getReturnValue:),
			call_NSInvocation_getReturnValue_,
			PyObjCUnsupportedMethod_IMP) < 0) {
		return;
	}
}
