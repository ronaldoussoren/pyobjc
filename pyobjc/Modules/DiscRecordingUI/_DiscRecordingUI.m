/*
 * Mapping of static items in the DiscRecordingUI framework
 */
#include <Python.h>

#import <DiscRecordingUI/DiscRecordingUI.h>
#import <CoreFoundation/CoreFoundation.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

static PyMethodDef ib_methods[] = {
	{ 0, 0, 0, 0 }
};


PyDoc_STRVAR(ib_doc,
"DiscRecordingUI._DiscRecordingUI defines constants, types and global functions used by "
"DiscRecordingUI"
);


#include "_DiscRecordingUI_Enum.inc"
#include "_DiscRecordingUI_Str.inc"

void init_DiscRecordingUI(void);

void init_DiscRecordingUI(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_DiscRecordingUI", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.DiscRecordingUI"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
