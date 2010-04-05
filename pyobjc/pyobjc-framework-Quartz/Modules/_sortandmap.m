/*
 * Functions with a callback argument that isn't "retained"
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>




static void
m_CGPDFDictionaryApplierFunction(
	const char *key,
	CGPDFObjectRef value,
	void* _info)
{
	PyObject* info = (PyObject*)_info;

	PyGILState_STATE   state = PyGILState_Ensure();

	PyObject* args = PyTuple_New(3);
	if (args == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}

	PyTuple_SET_ITEM(args, 0, PyBytes_FromString(key));
	if (PyTuple_GET_ITEM(args, 0) == NULL) {
		Py_DECREF(args);
		PyObjCErr_ToObjCWithGILState(&state);
	}
	
	PyTuple_SET_ITEM(args, 1, PyObjC_ObjCToPython(@encode(CGPDFObjectRef),
				value));
	if (PyTuple_GET_ITEM(args, 1) == NULL) {
		Py_DECREF(args);
		PyObjCErr_ToObjCWithGILState(&state);
	}

	PyTuple_SET_ITEM(args, 2, PyTuple_GET_ITEM(info, 1));
	Py_INCREF(PyTuple_GET_ITEM(args, 2));

	PyObject* result = PyObject_Call(PyTuple_GET_ITEM(info, 0), args, NULL);
	Py_DECREF(args);

	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}


	Py_DECREF(result);
	PyGILState_Release(state);
}

static PyObject*
m_CGPDFDictionaryApplyFunction(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* d;
	PyObject* f;
	PyObject* i;
	CGPDFDictionaryRef dictionary;

	if (!PyArg_ParseTuple(args, "OOO", &d, &f, &i)) {
		return NULL;
	}
	if (!PyCallable_Check(f)) {
		PyErr_SetString(PyExc_TypeError, "callback not callable");
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CGPDFDictionaryRef), d, &dictionary)<0){
		return NULL;
	}

	PyObject* real_info = Py_BuildValue("OO", f, i);
	if (real_info == NULL) {
		return NULL;
	}

	PyObjC_DURING
		CGPDFDictionaryApplyFunction(
			dictionary,
			m_CGPDFDictionaryApplierFunction,
			(void*)real_info);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF(real_info);
	if (PyErr_Occurred()) {
		return NULL;
	}
	Py_INCREF(Py_None);
	return Py_None;
}

/*
 * CGPathApply
 */

static PyObject* gCGPathElement = NULL;

static void
m_CGPathApplierFunction(void* _info, const CGPathElement* element)
{
	PyObject* info = (PyObject*)_info;

	PyGILState_STATE   state = PyGILState_Ensure();

#if 0
	PyObject* element = PyObjC_ObjCToPython(@encode(CGPathElement), 
			(void*)element);
	if (element == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
#endif
	PyObject* py_element = PyObject_CallFunction(gCGPathElement, 
		"lN", 
		element->type, 
		PyObjC_VarList_New(@encode(CGPoint), element->points));
	if (element == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}

	PyObject* result = PyObject_CallFunction(
		PyTuple_GET_ITEM(info, 0),
		"ON", PyTuple_GET_ITEM(info, 1), py_element);
	if (result == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(result);
	PyGILState_Release(state);
}

static PyObject*
setCGPathElement(PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	PyObject* v;

	if (!PyArg_ParseTuple(args, "O", &v)) {
		return NULL;
	}

	Py_XDECREF(gCGPathElement);
	Py_INCREF(v);
	gCGPathElement=v;

	Py_INCREF(Py_None);
	return Py_None;
}

static PyObject*
m_CGPathApply(PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	PyObject* py_path;
	PyObject* callback;
	PyObject* info;
	CGPathRef path;

	if (!PyArg_ParseTuple(args, "OOO", &py_path, &info, &callback)) {
		return NULL;
	}
	if (!PyCallable_Check(callback)) {
		PyErr_SetString(PyExc_TypeError, "callback not callable");
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CGPathRef), py_path, &path) < 0) {
		return NULL;
	}

	PyObject* real_info = Py_BuildValue("OO", callback, info);
	if (real_info == NULL) {
		return NULL;
	}

	PyObjC_DURING
		CGPathApply(path, real_info, m_CGPathApplierFunction);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF(real_info);

	if (PyErr_Occurred()) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}

static PyMethodDef mod_methods[] = {
	{
		"CGPDFDictionaryApplyFunction",
		(PyCFunction)m_CGPDFDictionaryApplyFunction,
		METH_VARARGS,
		NULL,
	},
	{
		"CGPathApply",
		(PyCFunction)m_CGPathApply,
		METH_VARARGS,
		NULL,
	},
	{
		"setCGPathElement",
		(PyCFunction)setCGPathElement,
		METH_VARARGS,
		NULL,
	},

	{ 0, 0, 0, 0 }
};


PyObjC_MODULE_INIT(_sortandmap)
{
	PyObject* m = PyObjC_MODULE_CREATE(_sortandmap);

	if (PyObjC_ImportAPI(m) < 0) PyObjC_INITERROR();

	PyObjC_INITDONE();
}
