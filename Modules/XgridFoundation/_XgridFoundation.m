/*
 * Mapping of static items in the XgridFoundation framework
 */
#include <Python.h>

#import <XgridFoundation/XgridFoundation.h>
#import <CoreFoundation/CoreFoundation.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"XgridFoundation._XgridFoundation defines constants, types and global functions used by "
"XgridFoundation"
);


#include "_XgridFoundation_Enum.inc"
#include "_XgridFoundation_Str.inc"

void init_XgridFoundation(void);

void init_XgridFoundation(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_XgridFoundation", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.xgrid.foundation"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
