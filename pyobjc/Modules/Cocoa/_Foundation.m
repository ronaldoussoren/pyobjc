/*
 * Mapping of static items in the Foundation kit:
 * - constants
 * - notification
 * - data types (TODO)
 * - enumerations (TODO)
 * - exceptions (TODO)
 * - global functions (TODO)
 */
#include <Python.h>
#import <Foundation/Foundation.h>
#import <Foundation/NSDebug.h>
#include "pyobjc-api.h"
#include "objc_support.h"
#include "const-table.h"

/** Functions */

/* The headings below refer to the reference pages on developer.apple.com */

/* 'Assertions' */
/*      All assertion-checking macros have not been wrapped. If needed 
 *      functions with simular functionality can be added as python code.
 */

/* 'Bundles' */

#define NSLocalizedString_doc 0
PyObject* objc_NSLocalizedString(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "key", "comment", NULL };
	char* key;
	char* comment;
	PyObject*  result;
	NSString* oc_result;
	NSString* oc_key;
	NSString* oc_comment;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "ss:NSLocalizedString",
			keywords, &key, &comment)) {
		return NULL;
	}

	oc_key = [NSString stringWithCString:key];
	oc_comment = [NSString stringWithCString:comment];
	oc_result = NSLocalizedString(oc_key, oc_comment);
	[oc_key release];
	[oc_comment release];

	result = ObjC_IdToPython(oc_result);
	[oc_result release];
	return result;
}

#define NSLocalizedStringFromTable_doc 0
PyObject* objc_NSLocalizedStringFromTable(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "key", "tableName", "comment", NULL };
	char* key;
	char* tableName;
	char* comment;
	PyObject*  result;
	NSString* oc_result;
	NSString* oc_key;
	NSString* oc_tableName;
	NSString* oc_comment;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sss:NSLocalizedString",
			keywords, &tableName, &key, &comment)) {
		return NULL;
	}

	oc_key = [NSString stringWithCString:key];
	oc_tableName = [NSString stringWithCString:tableName];
	oc_comment = [NSString stringWithCString:comment];
	oc_result = NSLocalizedStringFromTable(oc_key, oc_tableName, oc_comment);
	[oc_key release];
	[oc_tableName release];
	[oc_comment release];

	result = ObjC_IdToPython(oc_result);
	[oc_result release];
	return result;
}

#define NSLocalizedStringFromTableInBundle_doc 0
PyObject* objc_NSLocalizedStringFromTableInBundle(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "key", "tableName", "comment", "bundle", NULL };
	char* key;
	char* tableName;
	char* comment;
	PyObject* bundle;
	PyObject*  result;
	NSString* oc_result;
	NSString* oc_key;
	id        oc_bundle;
	NSString* oc_tableName;
	NSString* oc_comment;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sssO:NSLocalizedString",
			keywords, &tableName, &key, &comment, &bundle)) {
		return NULL;
	}
	if (!ObjCObject_Check(bundle)) {
		PyErr_SetString(PyExc_TypeError,
			"expecting NSBundle for bundle");
		return NULL;
	}

	oc_key = [NSString stringWithCString:key];
	oc_tableName = [NSString stringWithCString:tableName];
	oc_comment = [NSString stringWithCString:comment];
	oc_bundle = ObjCObject_GetObject(bundle);
	oc_result = NSLocalizedStringFromTableInBundle(
			oc_key, oc_tableName, oc_bundle, oc_comment);
	[oc_key release];
	[oc_tableName release];
	[oc_comment release];

	result = ObjC_IdToPython(oc_result);
	[oc_result release];
	return result;
}

#define NSLog_doc "NSLog(str) -> None"
PyObject* objc_NSLog(PyObject* self, PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "value", NULL };
	char* value;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "s:NSLog",
			keywords, &value)) {
		return NULL;
	}
	NSLog(@"%s", value);

	Py_INCREF(Py_None);
	return Py_None;
}

#ifdef GNUSTEP
#include "_Fnd_Functions.GNUstep.inc"

#else /* !GNUSTEP */

#if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
#include "_Fnd_Functions.inc"
#endif

#endif /* !GNUSTEP */

static PyMethodDef foundation_methods[] = {
	{ 
		"NSLocalizedString", 
		(PyCFunction)objc_NSLocalizedString, 
		METH_VARARGS|METH_KEYWORDS, 
		NSLocalizedString_doc 
	},
	{ 
		"NSLocalizedStringFromTable", 
		(PyCFunction)objc_NSLocalizedStringFromTable, 
		METH_VARARGS|METH_KEYWORDS, 
		NSLocalizedStringFromTable_doc 
	},
	{ 
		"NSLocalizedStringFromTableInBundle", 
		(PyCFunction)objc_NSLocalizedStringFromTableInBundle, 
		METH_VARARGS|METH_KEYWORDS, 
		NSLocalizedStringFromTable_doc 
	},
	{ 
		"NSLog", 
		(PyCFunction)objc_NSLog, 
		METH_VARARGS|METH_KEYWORDS, 
		NSLog_doc
	},

	METHOD_TABLE_ENTRIES

	{ 0, 0, 0, 0 } /* sentinel */
};

PyDoc_STRVAR(foundation_doc,
"Cocoa._Foundation defines constants, types and global functions used by "
"Cocoa.Foundation."
);

#ifdef  GNUSTEP 
#include "_Fnd_Enum.GNUstep.inc"
#include "_Fnd_Str.GNUstep.inc"
#else  /* !GNUSTEP */
#if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
#include "_Fnd_Enum.inc"
#include "_Fnd_Str.inc"
#endif
#endif  /* !GNUSTEP */

void init_Foundation(void)
{
	PyObject *m, *d;

	//	printf("Init _Foundation\n");

	m = Py_InitModule4("_Foundation", foundation_methods, foundation_doc, 
			NULL, PYTHON_API_VERSION);
	d = PyModule_GetDict(m);

	if (ObjC_ImportModule(m) < 0) {
		printf("Importing objc failed\n");
		return;
	}

	/* Register information in generated tables */
	if (register_ints(d, enum_table) < 0) return;
	if (register_strings(d, string_table) < 0) return;
#ifdef  GNUSTEP 
#	include "_Fnd_Var.GNUstep.inc"
#else /* !GNUSTEP */
#if MAC_OS_X_VERSION_10_2 <= MAC_OS_X_VERSION_MAX_ALLOWED
#	include "_Fnd_Var.inc"
#endif
#endif /* !GNUSTEP */
    
	/* Add manual registrations below */
}
