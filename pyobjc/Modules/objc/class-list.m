/*
 * Implements a function to fetch the list of objective-C classes known
 * in the runtime.
 */

#include "pyobjc.h"

#ifndef GNU_RUNTIME

	/* Implementation for MacOS X */

PyObject*
PyObjC_GetClassList(void)
{
	PyObject* 	result = NULL;
	Class*		buffer = NULL;
	int		bufferLen = 0;
	int		neededLen = 0;
	int             i;
	Class		initialBuffer[1024];

	/* First try using a static buffer for slightly better performance */
	neededLen = objc_getClassList(initialBuffer, 1024);
	if (neededLen >= 1024) {
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
	} else {
		bufferLen = neededLen;
		buffer = initialBuffer;
	}

	result = PyTuple_New(bufferLen);
	if (result == NULL) {
		goto error_cleanup;
	}

	for (i = 0; i < bufferLen; i++) {
		PyObject* pyclass;

		pyclass = PyObjCClass_New(buffer[i]);
		if (pyclass == NULL) {
			goto error_cleanup;
		}
		if (PyTuple_SET_ITEM(result, i, pyclass) < 0) {
			Py_DECREF(pyclass);
			goto error_cleanup;
		}
	}

	if (buffer != initialBuffer) {
		free(buffer); buffer = NULL;
	}
	return result;

error_cleanup:
	if (buffer && buffer != initialBuffer) {
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
PyObjC_GetClassList(void)
{
	PyObject* 	result = NULL;
	Class		classid;
	void*	        state = NULL;
	int             i = 0;

	while ((classid = objc_next_class(&state)))
	  i++;

	result = PyTuple_New(i);

	state = NULL; i = 0;

	while ((classid = objc_next_class(&state))) {
		PyObject* pyclass = PyObjCClass_New(classid);

		if (pyclass == NULL) {
			goto error_cleanup;
		}

		if (PyTuple_SET_ITEM(result, i, pyclass) < 0) {
			Py_DECREF(pyclass);
			goto error_cleanup;
		}

		i++;
	}

	return result;

error_cleanup:
	if (result)
	  Py_DECREF(result);

	return NULL;
}

#endif /* GNU_RUNTIME */
