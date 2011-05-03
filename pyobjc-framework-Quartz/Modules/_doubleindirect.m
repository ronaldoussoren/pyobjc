/*
 * Functions that return arrays by indirection, something that cannot be
 * described by the metadata.
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <ApplicationServices/ApplicationServices.h>

static PyObject*
m_CGWaitForScreenRefreshRects(PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	CGRect* rectArray = NULL;
	CGRectCount count = 0;
	CGError err;

	if (PyTuple_GET_SIZE(args) == 2) {
		if (PyTuple_GET_ITEM(args, 0) != Py_None) {
			PyErr_SetString(PyExc_ValueError, "pRectArray");
			return NULL;
		}
		if (PyTuple_GET_ITEM(args, 1) != Py_None) {
			PyErr_SetString(PyExc_ValueError, "pCount");
			return NULL;
		}
	}

	PyObjC_DURING
		err = CGWaitForScreenRefreshRects(&rectArray, &count);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (err == kCGErrorSuccess) {
		/* Build the array */
		PyObject* arr = PyObjC_CArrayToPython(
			@encode(CGRect), rectArray, count);
		if (arr == NULL) {
			return NULL;
		}

		/* Free the C-level array */
		CGReleaseScreenRefreshRects(rectArray);

		return Py_BuildValue("lNl", err, arr, count);
	}
	
	return Py_BuildValue("lOO", err, Py_None, Py_None);
}

static PyObject*
m_CGWaitForScreenUpdateRects(PyObject* self __attribute__((__unused__)),
		PyObject* args)
{
	CGRect* rectArray = NULL;
	size_t count = 0;
	CGScreenUpdateOperation requestedOperations;
	CGScreenUpdateOperation currentOperation;
	CGScreenUpdateMoveDelta delta;
	CGError err;
	PyObject* py_ops;

	if (!PyArg_ParseTuple(args, "O", &py_ops)) {
		PyObject* py_curop;
		PyObject* py_rectarr;
		PyObject* py_count;
		PyObject* py_delta;

		if (!PyArg_ParseTuple(args, "OOOOO", &py_ops, &py_curop, &py_rectarr, &py_count, &py_delta)) {
			return NULL;
		}

		if (py_curop != Py_None) {
			PyErr_SetString(PyExc_ValueError, "currentOperation != None");
			return NULL;
		}
		if (py_rectarr != Py_None) {
			PyErr_SetString(PyExc_ValueError, "pRectArray != None");
			return NULL;
		}
		if (py_count != Py_None) {
			PyErr_SetString(PyExc_ValueError, "pCount != None");
			return NULL;
		}
		if (py_delta != Py_None) {
			PyErr_SetString(PyExc_ValueError, "pDelta != None");
			return NULL;
		}
	}

	if (PyObjC_PythonToObjC(@encode(CGScreenUpdateOperation), py_ops, &requestedOperations) < 0) {
		return NULL;
	}

	PyObjC_DURING
		err = CGWaitForScreenUpdateRects(
				requestedOperations,
				&currentOperation,
				&rectArray, &count,
				&delta);

	PyObjC_HANDLER
		err = -1; /* Avoid compiler warning */
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		return NULL;
	}

	if (err == kCGErrorSuccess) {
		/* Build the array */
		PyObject* arr = PyObjC_CArrayToPython(
			@encode(CGRect), rectArray, count);
		if (arr == NULL) {
			return NULL;
		}
		PyObject* dlt = PyObjC_ObjCToPython(
				@encode(CGScreenUpdateMoveDelta), &delta);
		if (dlt == NULL) {
			return NULL;
		}

		/* Free the C-level array */
		CGReleaseScreenRefreshRects(rectArray);

		return Py_BuildValue("llNl", err, currentOperation, arr, count, dlt);
	}
	
	return Py_BuildValue("lOOOO", err, Py_None, Py_None, Py_None, Py_None);
}

static PyObject*
m_CGReleaseScreenRefreshRects(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* array;

	if (!PyArg_Parse(args, "O", &array)) {
		return NULL;
	}

	/* Do nothing, our wrappers for CGWaitForScreenRefreshRects and
	 * CGWaitForScreenUpdateRects have already released the real array.
	 */

	Py_INCREF(Py_None);
	return Py_None;
}


static PyMethodDef mod_methods[] = {
	{
		"CGWaitForScreenRefreshRects",
		(PyCFunction)m_CGWaitForScreenRefreshRects,
		METH_VARARGS,
		NULL
	},
	{
		"CGWaitForScreenUpdateRects",
		(PyCFunction)m_CGWaitForScreenUpdateRects,
		METH_VARARGS,
		NULL
	},
	{
		"CGReleaseScreenRefreshRects",
		(PyCFunction)m_CGReleaseScreenRefreshRects,
		METH_VARARGS,
		NULL
	},


	{ 0, 0, 0, 0 }
};

PyObjC_MODULE_INIT(_doubleindirect)
{
	PyObject* m = PyObjC_MODULE_CREATE(_doubleindirect);

	if (PyObjC_ImportAPI(m) < 0) PyObjC_INITERROR();

	PyObjC_INITDONE();
}
