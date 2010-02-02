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

#define COREFOUNDATION_DICTIONARY_METHODS \
        {	\
		"CFDictionaryGetKeysAndValues",	\
		(PyCFunction)mod_CFDictionaryGetKeysAndValues,	\
		METH_VARARGS,	\
		NULL	\
	},
