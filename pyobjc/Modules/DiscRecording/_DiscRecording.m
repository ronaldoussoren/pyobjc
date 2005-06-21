/*
 * Mapping of static items in the DiscRecording framework
 */
#include <Python.h>

#import <DiscRecording/DiscRecording.h>
#import <CoreFoundation/CoreFoundation.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"DiscRecording._DiscRecording defines constants, types and global functions used by "
"DiscRecording"
);


#include "_DiscRecording_Enum.inc"
#include "_DiscRecording2_Enum.inc"
#include "_DiscRecording3_Enum.inc"
#include "_DiscRecording_Str.inc"
#include "_DiscRecording2_Str.inc"
#include "_DiscRecording3_Str.inc"

void init_DiscRecording(void);

void init_DiscRecording(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_DiscRecording", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.DiscRecording"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
