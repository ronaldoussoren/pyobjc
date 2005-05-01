/*
 * Mapping of static items in the CoreData framework
 */
#include <Python.h>

#import <CoreData/CoreData.h>
#import <CoreFoundation/CoreFoundation.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"CoreData._CoreData defines constants, types and global functions used by "
"CoreData"
);


#include "_CoreData_Enum.inc"
#include "_CoreData_Str.inc"

void init_CoreData(void);

void init_CoreData(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_CoreData", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

#	include "_CoreData_Var.inc"	

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.CoreData"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
