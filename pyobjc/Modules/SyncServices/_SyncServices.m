/*
 * Mapping of static items in the SyncServices framework
 */
#include <Python.h>

#import <SyncServices/SyncServices.h>
#import <CoreFoundation/CoreFoundation.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"SyncServices._SyncServices defines constants, types and global functions used by "
"SyncServices"
);


#include "_SyncServices_Enum.inc"
#include "_SyncServices_Str.inc"

void init_SyncServices(void);

void init_SyncServices(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_SyncServices", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.syncservices"));
	if (bundle == NULL) {
		PyErr_SetString(PyExc_RuntimeError, "cannot open SyncServices.framework");
		return;
	}

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
