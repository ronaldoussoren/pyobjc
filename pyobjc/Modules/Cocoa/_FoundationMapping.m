/*
 * This module contains custom mapping functions for problematic methods
 *
 * TODO: I (Ronald) have now written mappings for two methods, and I'd say
 *       that we can do better...
 */

#include <Python.h>
#include <Foundation/Foundation.h>
#include <objc/objc-runtime.h>
#include "pyobjc-api.h"

#if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
#include "_Fnd_NSCoder.inc"
#include "_Fnd_NSData.inc"
#endif

PyDoc_STRVAR(mapping_doc,
	"This module registers some utility functions with the PyObjC core \n"
	"and is not used by 'normal' python code"
);

static PyMethodDef mapping_methods[] = {
	{ 0, 0, 0, 0 }
};

void init_FoundationMapping(void)
{
	PyObject *m, *d;

	m = Py_InitModule4("_FoundationMapping", mapping_methods, mapping_doc, 
		NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;
	
	if (ObjC_ImportModule(m) < 0) {
		return;
	}

	if (ObjC_RegisterMethodMapping(
			objc_lookUpClass("NSCoder"), 
			@selector(encodeArrayOfObjCType:count:at:),
			call_NSCoder_encodeArrayOfObjCType_count_at_,
			supercall_NSCoder_encodeArrayOfObjCType_count_at_,
			(IMP)imp_NSCoder_encodeArrayOfObjCType_count_at_) < 0) {

		printf("Python error1\n");
		PyErr_Print();
		return;
	}
	if (ObjC_RegisterMethodMapping(
			objc_lookUpClass("NSCoder"), 
			@selector(encodeValueOfObjCType:at:),
			call_NSCoder_encodeValueOfObjCType_at_,
			supercall_NSCoder_encodeValueOfObjCType_at_,
			(IMP)imp_NSCoder_encodeValueOfObjCType_at_) < 0) {

		printf("Python error1\n");
		PyErr_Print();
		return;
	}

	
	if (ObjC_RegisterMethodMapping(
			objc_lookUpClass("NSData"), 
			@selector(initWithBytes:length:),
			call_NSData_initWithBytes_length_,
			supercall_NSData_initWithBytes_length_,
			(IMP)imp_NSData_initWithBytes_length_) < 0 ) {

		printf("Python error1\n");
		PyErr_Print();
		return;
	}


	if (PyErr_Occurred()) {
		printf("Python error\n");
		PyErr_Print();
	}
}
