/*
 * Mapping of static items in the Foundation kit.
 */
#include <Python.h>
#import <Foundation/Foundation.h>
#import <Foundation/NSDebug.h>
#import <CoreFoundation/CoreFoundation.h>

#ifdef MACOSX
#include <pymactoolbox.h>
#endif

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

/** Functions */

#ifdef GNUSTEP
#include "_Fnd_Functions.GNUstep.inc"

#else /* !GNUSTEP */

#include "_Fnd_Functions.inc"

#endif /* !GNUSTEP */

/* The headings below refer to the reference pages on developer.apple.com */

/* 'Assertions' */
/*      All assertion-checking macros have not been wrapped. If needed 
 *      functions with simular functionality can be added as python code.
 */

/* 'Bundles' */

#define NSLocalizedString_doc 0
static PyObject* objc_NSLocalizedString(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "key", "comment", NULL };
	PyObject*  result;
	NSString* oc_result;
	NSString* oc_key;
	NSString* oc_comment;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSLocalizedString",
			keywords, convert_id, &oc_key, 
			convert_id, &oc_comment)) {
		return NULL;
	}

	oc_result = NSLocalizedString(oc_key, oc_comment);

	result = PyObjC_IdToPython(oc_result);
	return result;
}

#define NSLocalizedStringFromTable_doc 0
static PyObject* objc_NSLocalizedStringFromTable(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "key", "tableName", "comment", NULL };
	PyObject*  result;
	NSString* oc_result;
	NSString* oc_key;
	NSString* oc_tableName;
	NSString* oc_comment;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"O&O&O&:NSLocalizedStringFromTable",
			keywords, 
			convert_id, &oc_tableName, 
			convert_id, &oc_key, 
			convert_id, &oc_comment)) {
		return NULL;
	}

	oc_result = NSLocalizedStringFromTable(
		oc_key, oc_tableName, oc_comment);
	result = PyObjC_IdToPython(oc_result);
	return result;
}

#define NSLocalizedStringFromTableInBundle_doc 0
static PyObject* objc_NSLocalizedStringFromTableInBundle(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "key", "tableName", "comment", "bundle", NULL };
	PyObject* result;
	NSString* oc_result;
	NSString* oc_key;
	id        oc_bundle;
	NSString* oc_tableName;
	NSString* oc_comment;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"O&O&O&O:NSLocalizedStringFromTableInBundle",
			keywords, 
			convert_id, &oc_tableName, 
			convert_id, &oc_key, 
			convert_id, &oc_comment, 
			convert_id, &oc_bundle)) {
		return NULL;
	}

	oc_result = NSLocalizedStringFromTableInBundle(
			oc_key, oc_tableName, oc_bundle, oc_comment);

	result = PyObjC_IdToPython(oc_result);
	return result;
}

#ifdef MACOSX


/* NSString *NSFileTypeForHFSTypeCode(OSType hfsTypeCode); */

static PyObject* objc_NSFileTypeForHFSTypeCode(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "hfsTypeCode", NULL };
	PyObject*  result;
	NSString*  oc_result;
	OSType hfsTypeCode;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"O&:NSFileTypeForHFSTypeCode",
			keywords, PyMac_GetOSType, &hfsTypeCode)) {
		return NULL;
	}
	
	NS_DURING
		oc_result = NSFileTypeForHFSTypeCode(hfsTypeCode);
	NS_HANDLER
		PyObjCErr_FromObjC(localException);
		oc_result = NULL;
	NS_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	result = PyObjC_IdToPython(oc_result);
	return result;
}

/* OSType NSHFSTypeCodeFromFileType(NSString *fileType); */

static PyObject* objc_NSHFSTypeCodeFromFileType(PyObject* self __attribute__((__unused__)), 
		PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "hfsTypeCode", NULL };
	NSString*  fileType;
	OSType hfsTypeCode;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"O&:NSHFSTypeCodeFromFileType",
			keywords, convert_id, &fileType)) {
		return NULL;
	}
	
	NS_DURING
		hfsTypeCode = NSHFSTypeCodeFromFileType(fileType);
	NS_HANDLER
		hfsTypeCode = 0;
		PyObjCErr_FromObjC(localException);
	NS_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	return PyMac_BuildOSType(hfsTypeCode);
}


#endif /* MACOSX */


static PyMethodDef foundation_methods[] = {
#ifdef MACOSX
	{ 
		"NSFileTypeForHFSTypeCode", 
		(PyCFunction)objc_NSFileTypeForHFSTypeCode, 
		METH_VARARGS|METH_KEYWORDS, 
		NULL
	},
	{ 
		"NSHFSFTypeCodeFromFileType", 
		(PyCFunction)objc_NSHFSTypeCodeFromFileType, 
		METH_VARARGS|METH_KEYWORDS, 
		NULL
	},

#endif /* MACOSX */
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

#include "_Fnd_Enum.inc"
#include "_Fnd_Str.inc"

#endif  /* !GNUSTEP */

void init_Foundation(void);

void init_Foundation(void)
{
	PyObject *m, *d;
	CFBundleRef bundle;

	m = Py_InitModule4("_Foundation", foundation_methods, foundation_doc, 
			NULL, PYTHON_API_VERSION);
	d = PyModule_GetDict(m);

	if (PyObjC_ImportAPI(m) < 0) {
		printf("Importing objc failed\n");
		return;
	}

	bundle = CFBundleCreate(NULL,
		(CFURLRef)[NSURL fileURLWithPath:@"/System/Library/Frameworks/Foundation.framework"]);

	/* Register information in generated tables */
	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, (sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;
	
	//CFRelease(bundle);

#ifdef  GNUSTEP 
#	include "_Fnd_Var.GNUstep.inc"
#else /* !GNUSTEP */

#	include "_Fnd_Var.inc"

#endif /* !GNUSTEP */
    
	/* Add manual registrations below */
}
