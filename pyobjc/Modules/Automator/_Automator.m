/*
 * Mapping of static items in the Automator framework
 */
#include <Python.h>

#import <Cocoa/Cocoa.h>
#import <Automator/Automator.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"Automator._Automator defines constants, types and global functions used by "
"Automator"
);


#include "_Automator_Enum.inc"
#include "_Automator_Str.inc"

void init_Automator(void);

void init_Automator(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_Automator", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.AutomatorFramework"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
