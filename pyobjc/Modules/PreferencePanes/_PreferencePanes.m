/*
 * Mapping of static items in the PreferencePanes framework
 * 
 * - constants 
 * - enumerations
 */
#include <Python.h>

#import <PreferencePanes/PreferencePanes.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef prefpanes_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(prefpanes_doc,
"Cocoa._AddressBook defines constants, types and global functions used by "
"Cocoa.AddressBook."
);


#include "_PreferencePanes_Enum.inc"
#include "_PreferencePanes_Str.inc"

void init_PreferencePanes(void);

void init_PreferencePanes(void)
{
	PyObject *m, *d;

	m = Py_InitModule4("_PreferencePanes", prefpanes_methods, 
		prefpanes_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (ObjC_ImportModule(m) < 0) {
		return;
	}

	if (register_ints(d, enum_table) < 0) return;
	if (register_strings(d, string_table) < 0) return;
}
