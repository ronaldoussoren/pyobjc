/*
 * Mapping of static items in the Quartz framework
 */
#include <Python.h>

#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"Quartz._Quartz defines constants, types and global functions used by "
"Quartz"
);


#include "_Quartz_Enum.inc"
#include "_Quartz2_Enum.inc"
#include "_Quartz3_Enum.inc"
#include "_Quartz_Str.inc"
#include "_Quartz2_Str.inc"
#include "_Quartz3_Str.inc"

void init_Quartz(void);

void init_Quartz(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_Quartz", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.quartzframework"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
