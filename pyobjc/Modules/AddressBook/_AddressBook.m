/*
 * Mapping of static items in the AddressBook framework
 * 
 * - constants 
 * - enumerations
 */
#include <Python.h>

#import <AddressBook/AddressBook.h>
#import <CoreFoundation/CoreFoundation.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef addressbook_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(addressbook_doc,
"Cocoa._AddressBook defines constants, types and global functions used by "
"Cocoa.AddressBook."
);


#include "_Addr_Enum.inc"
#include "_Addr_Str.inc"

void init_AddressBook(void);
void init_AddressBook(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_AddressBook", addressbook_methods, 
		addressbook_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleCreate(NULL,
		(CFURLRef)[NSURL fileURLWithPath:@"/System/Library/Frameworks/AddressBook.framework"]);


	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0])-1)) < 0) return;

	//CFRelease(bundle);
}
