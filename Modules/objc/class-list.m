/*
 * Implements a function to fetch the list of objective-C classes known
 * in the runtime.
 */

#include "pyobjc.h"

#ifndef GNU_RUNTIME

	/* Implementation for MacOS X */

PyObject*
ObjC_GetClassList(void)
{
	PyObject* 	result = NULL;
	Class*		buffer = NULL;
	int		bufferLen = 0;
	int		neededLen = 0;
	int             i;

	neededLen = objc_getClassList(NULL, 0);
	while (bufferLen < neededLen) {
		Class*    newBuffer;
		bufferLen = neededLen;
		newBuffer = realloc(buffer, sizeof(Class) * bufferLen);
		if (newBuffer == NULL) {
			PyErr_SetString(PyExc_MemoryError, 
				"ObjC_GetClassList");
			goto error_cleanup;
		}
		buffer = newBuffer; newBuffer = NULL;
		neededLen = objc_getClassList(buffer, bufferLen);
	}
	bufferLen = neededLen;

	result = PyTuple_New(bufferLen);
	if (result == NULL) {
		goto error_cleanup;
	}

	for (i = 0; i < bufferLen; i++) {
		PyObject* pyclass;

		pyclass = ObjCClass_New(buffer[i]);
		if (pyclass == NULL) {
			goto error_cleanup;
		}
		if (PyTuple_SET_ITEM(result, i, pyclass) < 0) {
			Py_DECREF(pyclass);
			goto error_cleanup;
		}
	}

	free(buffer); buffer = NULL;
	return result;

error_cleanup:
	if (buffer) {
		free(buffer);
		buffer = NULL;
	}
	if (result) {
		Py_DECREF(result);
		result = NULL;
	}
	return NULL;
}

#else	 /* GNU_RUNTIME */

	/* This is completely untested (it will probably not compile either,
	 * I don't have access to a machine with the GNU runtime)
	 */

PyObject*
ObjC_GetClassList(void)
{
	PyObject* 	result = NULL;
	Class		classid;
	void*	        state = NULL;

	result = PyList_New(0);
	while (classid = objc_next_class(&state)) {
		PyObject* pyclass = ObjCClass_New(classid);
		if (pyclass == NULL) {
			goto error_cleanup;
		}
		if (PyList_Append(result, pyclass) < 0) {
			Py_DECREF(pyclass);
			goto error_cleanup;
		}
		Py_DECREF(pyclass);
	}

	return result;

error_cleanup:
	return NULL;
	if (result) {
		Py_DECREF(result);
		result = NULL;
	}
	return NULL;
}

#endif /* GNU_RUNTIME */
