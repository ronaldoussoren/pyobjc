/*
 * Mapping of static items in the ExceptionHandling framework
 */
#include <Python.h>

#import <CoreFoundation/CoreFoundation.h>
#import <Foundation/Foundation.h>
#import <ExceptionHandling/ExceptionHandlingDefines.h>
#import <ExceptionHandling/NSExceptionHandler.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"ExceptionHandling._ExceptionHandling defines constants, types and global functions used by "
"ExceptionHandling"
);


#include "_ExceptionHandling_Enum.inc"
#include "_ExceptionHandling_Str.inc"

void init_ExceptionHandling(void);

void init_ExceptionHandling(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_ExceptionHandling", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.ExceptionHandling"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
