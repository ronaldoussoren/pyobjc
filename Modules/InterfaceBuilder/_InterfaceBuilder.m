/*
 * Mapping of static items in the InterfaceBuilder framework
 * 
 * - constants 
 * - enumerations
 */
#include <Python.h>

#import <InterfaceBuilder/InterfaceBuilder.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"Cocoa._AddressBook defines constants, types and global functions used by "
"Cocoa.AddressBook."
);


#include "_InterfaceBuilder_Enum.inc"
#include "_InterfaceBuilder_Str.inc"

void init_InterfaceBuilder(void);

void init_InterfaceBuilder(void)
{
	PyObject *m, *d;

	m = Py_InitModule4("_InterfaceBuilder", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	if (register_ints(d, enum_table) < 0) return;
	if (register_strings(d, string_table) < 0) return;
}
