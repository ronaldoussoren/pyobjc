#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

static PyObject*
mod_CFSetGetValues(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* pySet;
	PyObject* pyValues;
	CFSetRef set;
	void* values;
	CFIndex count;

	if (!PyArg_ParseTuple(args, "OO", &pySet, &pyValues)) {

		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFSetRef), pySet, &set) < 0) {
		return NULL;
	}

	if (pyValues == PyObjC_NULL) {
		values = NULL;
	} else if (pyValues == Py_None){
		count = CFSetGetCount(set);
		values = malloc(sizeof(void*) * count);
		if (values == NULL) {
			PyErr_NoMemory();
			return NULL;
		}
	} else {
		PyErr_SetString(PyExc_ValueError, "values must be None of NULL");
		return NULL;
	}


	PyObjC_DURING
		CFSetGetValues( set, values);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		if (values != NULL) {
			free(values);
		}
		return NULL;
	}

	if (values != NULL) {
		pyValues = PyObjC_CArrayToPython(@encode(id), values, count);
		free(values);
	} else {
		pyValues = Py_None;
		Py_INCREF(pyValues);
	}

	return pyValues;
}

static PyMethodDef mod_methods[] = {
        {
		"CFSetGetValues",
		(PyCFunction)mod_CFSetGetValues,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};

void init_CFSet(void);
void init_CFSet(void)
{
	PyObject* m = Py_InitModule4("_CFSet", mod_methods, "", NULL,
	PYTHON_API_VERSION);

	PyObjC_ImportAPI(m);
}
