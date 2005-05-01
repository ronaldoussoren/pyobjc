/*
 * Mapping of static items in the QTKit framework
 */
#include <Python.h>
#include "pymactoolbox.h"

#import <Cocoa/Cocoa.h>
#import <QTKit/QTKit.h>

#include "pyobjc-api.h"
#include "wrapper-const-table.h"



PyDoc_STRVAR(ib_doc,
"QTKit._QTKit defines constants, types and global functions used by "
"QTKit"
);


#include "_QTKit_Enum.inc"
#include "_QTKit_Str.inc"
#include "_QTKit_Functions.inc"

static PyMethodDef ib_methods[] = {

	METHOD_TABLE_ENTRIES

	{ 0, 0, 0, 0 }
};

void init_QTKit(void);

static const char* QTTime_fields[] = {
	"timeValue",
	"timeScale",
	"flags",
	NULL
};

static const char* QTTimeRange_fields[] = {
	"time",
	"duration",
	NULL
};

void init_QTKit(void)
{
	PyObject *m, *d, *v;
	CFBundleRef bundle;

	m = Py_InitModule4("_QTKit", ib_methods, 
		ib_doc, NULL, PYTHON_API_VERSION);
	if (!m) return;

	d = PyModule_GetDict(m);
	if (!d) return;

	if (PyObjC_ImportAPI(m) < 0) {
		return;
	}

#	include "_QTKit_Var.inc"

	v = PyObjC_RegisterStructType(@encode(QTTime),
		"QTKit.QTTime",
		"struct QTTime (timeValue, timeScale, flags )",
		NULL,
		3, QTTime_fields);
	if (v == NULL) return;
	PyDict_SetItemString(d, "QTTime", v);
	Py_DECREF(v);

	v = PyObjC_RegisterStructType(@encode(QTTimeRange),
		"QTKit.QTTimeRange",
		"struct QTTimeRange (time, duration)",
		NULL,
		2, QTTimeRange_fields);
	if (v == NULL) return;
	PyDict_SetItemString(d, "QTTimeRange", v);
	Py_DECREF(v);

	/* Convert pointers to/from QuickTime objects */
	if (PyObjCPointerWrapper_Register(
		@encode(Media),
		MediaObj_New,
		MediaObj_Convert) < 0) {

		return;
	}

	if (PyObjCPointerWrapper_Register(
		@encode(Movie),
		MovieObj_New,
		MovieObj_Convert) < 0) {

		return;
	}

	if (PyObjCPointerWrapper_Register(
		@encode(MovieController),
		MovieCtlObj_New,
		MovieCtlObj_Convert) < 0) {

		return;
	}

	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.QTKit"));

	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, 
		(sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

	//CFRelease(bundle);
}
