/*
 * Mapping of static items in the WebKit framework
 * 
 * - constants 
 * - enumerations
 */
#include <Python.h>

#import <WebKit/WebKit.h>
#import <CoreFoundation/CoreFoundation.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"WebKit._WebKit defines constants, types and global functions used by "
"WebKit"
);


#include "_WebKit_Enum.inc"
#include "_WebKit_Str.inc"

void init_WebKit(void);

void init_WebKit(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_WebKit", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleCreate(NULL,
		(CFURLRef)[NSURL fileURLWithPath:@"/System/Library/Frameworks/WebKit.framework"]);

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
