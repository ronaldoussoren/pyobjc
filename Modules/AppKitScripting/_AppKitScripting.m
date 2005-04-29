/*
 * Mapping of static items in the AppKitScripting framework
 */
#include <Python.h>

#import <AppKitScripting/AppKitScripting.h>
#import <CoreFoundation/CoreFoundation.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"AppKitScripting._AppKitScripting defines constants, types and global functions used by "
"AppKitScripting"
);


#include "_AppKitScripting_Enum.inc"
#include "_AppKitScripting_Str.inc"

void init_AppKitScripting(void);

void init_AppKitScripting(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_AppKitScripting", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.AppKitScripting"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
