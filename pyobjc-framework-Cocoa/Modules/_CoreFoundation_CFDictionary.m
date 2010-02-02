#include <Python.h>
#include "pyobjc-api.h"

#import <CoreFoundation/CoreFoundation.h>

static PyObject*
mod_CFDictionaryGetKeysAndValues(
	PyObject* self __attribute__((__unused__)),
	PyObject* args)
{
	PyObject* pyDict;
	PyObject* pyKeys;
	PyObject* pyValues;
	PyObject* result;
	CFDictionaryRef dict;
	void* keys;
	void* values;
	CFIndex count;

	if (!PyArg_ParseTuple(args, "OOO", &pyDict, &pyKeys, &pyValues)) {

		return NULL;
	}

	if (PyObjC_PythonToObjC(@encode(CFDictionaryRef), pyDict, &dict) < 0) {
		return NULL;
	}

	count = -1;
	if (pyKeys == PyObjC_NULL) {
		keys = NULL;
	} else if (pyKeys == Py_None){
		count = CFDictionaryGetCount(dict);
		keys = malloc(sizeof(void*) * count);
		if (keys == NULL) {
			PyErr_NoMemory();
			return NULL;
		}
	} else {
		PyErr_SetString(PyExc_ValueError, "keys must be None of NULL");
		return NULL;
	}

	if (pyValues == PyObjC_NULL) {
		values = NULL;
	} else if (pyValues == Py_None){
		if (count == -1) {
			count = CFDictionaryGetCount(dict);
		}
		values = malloc(sizeof(void*) * count);
		if (values == NULL) {
			if (keys != NULL) {
				free(keys);
			}
			PyErr_NoMemory();
			return NULL;
		}
	} else {
		PyErr_SetString(PyExc_ValueError, "values must be None of NULL");
		return NULL;
	}


	PyObjC_DURING
		CFDictionaryGetKeysAndValues(
			dict, keys, values);

	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);

	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) {
		if (keys != NULL) {
			free(keys);
		}
		if (values != NULL) {
			free(values);
		}
		return NULL;
	}

	if (keys != NULL) {
		pyKeys = PyObjC_CArrayToPython(@encode(id), keys, count);
		free(keys);
	} else {
		pyKeys = Py_None;
		Py_INCREF(pyKeys);
	}

	if (values != NULL) {
		pyValues = PyObjC_CArrayToPython(@encode(id), values, count);
		free(values);
	} else {
		pyValues = Py_None;
		Py_INCREF(pyValues);
	}

	result = Py_BuildValue("NN", pyKeys, pyValues);
	return result;
}

static PyMethodDef mod_methods[] = {
        {
		"CFDictionaryGetKeysAndValues",
		(PyCFunction)mod_CFDictionaryGetKeysAndValues,
		METH_VARARGS,
		NULL
	},
	{ 0, 0, 0, 0 } /* sentinel */
};


/* Python glue */
#if PY_VERSION_HEX >= 0x03000000

static struct PyModuleDef mod_module = {
        PyModuleDef_HEAD_INIT,
	"_CFDictionary",
	NULL,
	0,
	mod_methods,
	NULL,
	NULL,
	NULL,
	NULL
};

#define INITERROR() return NULL
#define INITDONE() return m

PyObject* PyInit__CFDictionary(void);

PyObject*
PyInit__CFDictionary(void)

#else

#define INITERROR() return
#define INITDONE() return

void init_CFDictionary(void);

void
init_CFDictionary(void)
#endif
{
	PyObject* m;
#if PY_VERSION_HEX >= 0x03000000
	m = PyModule_Create(&mod_module);
#else
	m = Py_InitModule4("_CFDictionary", mod_methods,
		NULL, NULL, PYTHON_API_VERSION);
#endif
	if (!m) { 
		INITERROR();
	}

	if (PyObjC_ImportAPI(m) == -1) INITERROR();

	INITDONE();
}
