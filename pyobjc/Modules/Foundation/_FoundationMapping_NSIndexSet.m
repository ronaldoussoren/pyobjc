/*
 * Special wrappers for NSIndexSet methods with 'difficult' arguments.
 * 
 * -getIndexes:maxCount:inIndexRange:		[call]
 *
 * Undocumented methods:
 * -getValue:
 * -pointerValue:
 *
 * PLATFORM: MacOS X 10.3
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject*
call_NSIndexSet_getIndexes_maxCount_inIndexRange_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	NSRange range;
	int maxCount;
	unsigned int* buffer;
	unsigned int retval;
	struct objc_super super;
	PyObject* result;
	PyObject* v;
	unsigned int i;

	if (!PyArg_ParseTuple(arguments, "iO&", &maxCount, convert_NSRange, &range)) {
		return NULL;
	}

	buffer = malloc(maxCount * sizeof(unsigned int));
	if (buffer == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuper(&super,
			 PyObjCSelector_GetClass(method), 
			 PyObjCObject_GetObject(self));
		retval = (unsigned)objc_msgSendSuper(&super, 
				PyObjCSelector_GetSelector(method), 
				buffer, maxCount, range);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		retval = 0;
										        NS_ENDHANDLER

	if (retval == 0 && PyErr_Occurred()) {
		free(buffer);
		return NULL;
	}

	result = PyTuple_New(3);
	if (result == NULL) {
		free(buffer);
		return NULL;
	}

	v = PyObjC_ObjCToPython(@encode(unsigned int), &retval);
	if (v == NULL) {
		Py_DECREF(result);
		free(buffer);
		return NULL;
	}
	PyTuple_SET_ITEM(result, 0, v);

	v = PyTuple_New(retval);
	if (result == NULL) {
		Py_DECREF(result);
		free(buffer);
		return NULL;
	}
	PyTuple_SET_ITEM(result, 1, v);

	for (i = 0; i < retval; i++) {
		PyObject* o = PyObjC_ObjCToPython(@encode(unsigned int),
				buffer + i);
		if (o == NULL) {
			Py_DECREF(result);
			free(buffer);
			return NULL;
		}

		PyTuple_SET_ITEM(v, i, o);
	}

	v = PyObjC_ObjCToPython(@encode(NSRange), &range);
	if (result == NULL) {
		Py_DECREF(result);
		free(buffer);
		return NULL;
	}
	PyTuple_SET_ITEM(result, 2, v);

	free(buffer);
	return result;
}

static int 
_pyobjc_install_NSIndexSet(void)
{
	Class classNSIndexSet = objc_lookUpClass("NSIndexSet");
	if (classNSIndexSet == NULL) {
		return 0;
	}

	if (PyObjC_RegisterMethodMapping(
		classNSIndexSet,
		@selector(getIndexes:maxCount:inIndexRange:),
		call_NSIndexSet_getIndexes_maxCount_inIndexRange_,
		PyObjCUnsupportedMethod_IMP) < 0) {

		return -1;
	}

	return 0;
}
