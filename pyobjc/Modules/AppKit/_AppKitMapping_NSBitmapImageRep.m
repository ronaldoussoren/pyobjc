/*
 * NSBitmapImageRep mappings for difficult methods:
 *
 * -getTIFFCompressionTypes:count:	[call]
 *
 * TODO:
 * * Merge with _AppKitMapping_NSBitMap.m
 * -initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:
 */
#include <Python.h>
#include <Foundation/Foundation.h>
#include "pyobjc-api.h"

static PyObject* call_NSBitmapImageRep_getTIFFCompressionTypes_count_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	NSTIFFCompression* list;
	int numTypes;

	if  (!PyArg_ParseTuple(arguments, "")) {
		return NULL;
	}

	NS_DURING
		PyObjC_InitSuperCls(&super,
			PyObjCSelector_GetClass(method),
			PyObjCClass_GetClass(self));

		(void)objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				&list, &numTypes);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		list = NULL; numTypes = -1;
	NS_ENDHANDLER

	if (list == NULL && PyErr_Occurred()) {
		return NULL;
	}

	result = PyTuple_New(2);
	if (result == NULL) {
		return NULL;
	}

	PyTuple_SET_ITEM(result, 1, PyInt_FromLong(numTypes));
	if (PyTuple_GET_ITEM(result, 1) == NULL) {
		Py_DECREF(result);
		return NULL;
	}

	if (numTypes < 0) {
		PyTuple_SET_ITEM(result, 0, Py_None);
		Py_INCREF(Py_None);
	} else {
		int i;
		PyObject* v = PyTuple_New(numTypes);

		if (v == NULL) {
			Py_DECREF(result);
			return NULL;
		}

		PyTuple_SET_ITEM(result, 0, v);

		for (i = 0; i < numTypes; i++) {
			PyObject* o = PyObjC_ObjCToPython(
				@encode(NSTIFFCompression), 
				list + i);
			if (o == NULL) {
				Py_DECREF(result);
				return NULL;
			}
			PyTuple_SET_ITEM(v, i, o);
		}
	}

	return result;
}

static int 
_pyobjc_install_NSBitmapImageRep(void)
{
	Class class_NSBitmapImageRep = objc_lookUpClass("NSBitmapImageRep");

	if (PyObjC_RegisterMethodMapping(class_NSBitmapImageRep, 
		@selector(getTIFFCompressionTypes:count:),
		call_NSBitmapImageRep_getTIFFCompressionTypes_count_,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	if (PyObjC_RegisterMethodMapping(class_NSBitmapImageRep, 
		@selector(initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:),
		PyObjCUnsupportedMethod_Caller,
		PyObjCUnsupportedMethod_IMP) < 0 ) {

		return -1;
	}

	return 0;
}
