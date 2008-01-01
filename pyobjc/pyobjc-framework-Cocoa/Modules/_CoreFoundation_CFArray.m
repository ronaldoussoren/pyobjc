/*
 * Manual wrapper a callback function for CFArray
 *
 * XXX: this module should be unnecessary, but the general mechanism causes
 * crash. This is a temporary workaround
 */
#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

static CFComparisonResult
mod_CFComparatorFunction(const void* val1, const void* val2, void* context)
{
	CFComparisonResult result;
	PyGILState_STATE state = PyGILState_Ensure();
	PyObject* info = (PyObject*)context;

	PyObject* rv = PyObject_CallFunction(
		PyTuple_GET_ITEM(info, 0),
		"NNO", 
		PyObjC_ObjCToPython(@encode(NSObject*), &val1),
		PyObjC_ObjCToPython(@encode(NSObject*), &val2),
		PyTuple_GET_ITEM(info, 1));
	if (rv == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
	}

	if (PyObjC_PythonToObjC(@encode(CFComparisonResult), rv, &result)) {
		Py_DECREF(rv);
		PyObjCErr_ToObjCWithGILState(&state);
	}
	Py_DECREF(rv);

	PyGILState_Release(state);
	return result;
}

static PyObject*
mod_CFArrayBSearchValues(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	CFArrayRef array;
	CFRange    range;
	NSObject*  value;
	PyObject*  py_array;
	PyObject*  py_range;
	PyObject*  py_value;
	PyObject*  comparator;
	PyObject*  context;
	CFIndex    index;

	if (!PyArg_ParseTuple(args, "OOOOO", &py_array, &py_range, &py_value,
		&comparator, &context)) {

		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFArrayRef), py_array, &array) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(CFRange), py_range, &range) < 0) {
		return NULL;
	}
	if (PyObjC_PythonToObjC(@encode(NSObject*), py_value, &value) < 0) {
		return NULL;
	}
	index = -1;
	PyObject* real_info = Py_BuildValue("OO", comparator, context);
	PyObjC_DURING
		index = CFArrayBSearchValues(
			array, range, value, mod_CFComparatorFunction,
			real_info);

	PyObjC_HANDLER
		index = -1;
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	Py_DECREF(real_info);
	if (PyErr_Occurred()) {
		return NULL;
	}

	return PyObjC_ObjCToPython(@encode(CFIndex), &index);
}

static PyMethodDef mod_methods[] = {
        {
		"CFArrayBSearchValues",
		(PyCFunction)mod_CFArrayBSearchValues,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_CFArray(void);
void init_CFArray(void)
{
	PyObject* m = Py_InitModule4("_CFArray", mod_methods, "", NULL,
	PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
}
