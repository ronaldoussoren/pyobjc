/*
 * Mapping of static items in the OSAKit framework
 */
#include <Python.h>
#include "pymactoolbox.h"

#import <Cocoa/Cocoa.h>
#import <OSAKit/OSAKit.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"



PyDoc_STRVAR(ib_doc,
"OSAKit._OSAKit defines constants, types and global functions used by "
"OSAKit"
);


#include "_OSAKit_Enum.inc"
#include "_OSAKit_Str.inc"

static PyMethodDef ib_methods[] = {

	{ 0, 0, 0, 0 }
};

void init_OSAKit(void);

void init_OSAKit(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_OSAKit", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.OSAKit"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
