/*
 * Mapping of static items in the Foundation kit, and custom wrappers for
 * "difficult" methods.
 */

#include <Python.h>
#import <Foundation/Foundation.h>
#import <Foundation/NSDebug.h>

#ifdef MACOSX
#import <CoreFoundation/CoreFoundation.h>
#include <pymactoolbox.h>
#endif

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

#include "_Fnd_Functions.inc"

#define NSLocalizedString_doc 0
static PyObject* objc_NSLocalizedString(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "key", "comment", NULL };
	PyObject*  result;
	NSString* oc_result;
	NSString* oc_key;
	NSString* oc_comment;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&O&:NSLocalizedString",
			keywords, PyObjCObject_Convert, &oc_key, 
			PyObjCObject_Convert, &oc_comment)) {
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
			PyObjCObject_Convert, &oc_tableName, 
			PyObjCObject_Convert, &oc_key, 
			PyObjCObject_Convert, &oc_comment)) {
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
			PyObjCObject_Convert, &oc_tableName, 
			PyObjCObject_Convert, &oc_key, 
			PyObjCObject_Convert, &oc_comment, 
			PyObjCObject_Convert, &oc_bundle)) {
		return NULL;
	}

	oc_result = NSLocalizedStringFromTableInBundle(
			oc_key, oc_tableName, oc_bundle, oc_comment);

	result = PyObjC_IdToPython(oc_result);
	return result;
}

#ifdef MACOSX


PyDoc_STRVAR(objc_NSFileTypeForHFSTypeCode_doc,
	"NSString *NSFileTypeForHFSTypeCode(OSType hfsTypeCode);");

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

PyDoc_STRVAR(objc_NSHFSTypeCodeFromFileType_doc,
		"OSType NSHFSTypeCodeFromFileType(NSString *fileType);");

static PyObject* objc_NSHFSTypeCodeFromFileType(PyObject* self __attribute__((__unused__)), 
		PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "hfsTypeCode", NULL };
	NSString*  fileType;
	OSType hfsTypeCode;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"O&:NSHFSTypeCodeFromFileType",
			keywords, PyObjCObject_Convert, &fileType)) {
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


static int
NSRect_Convert(PyObject* value, void* prect)
{
	int res = PyObjC_PythonToObjC(@encode(NSRect), 	value, prect);
	if (res == -1) {
		return 0;
	}
	return 1;
}

PyDoc_STRVAR(NSDivideRect_doc,
	"NSDivideRect(inRect, amount, edge) -> (slice, remainder)");

static PyObject* objc_NSDivideRect(PyObject* self __attribute__((__unused__)), 
		PyObject* args, PyObject* kwds)
{
static	char* keywords[] = { "inRect", "amount", "edge", NULL };
	NSRect inRect;
	NSRect slice;
	NSRect rem;
	float amount;
	NSRectEdge edge;
	PyObject* result;
	PyObject* v;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"O&fi:NSDivideRect",
			keywords, NSRect_Convert, &inRect,
			&amount, &edge)) {
		return NULL;
	}

	NSDivideRect(inRect, &slice, &rem, amount, edge);

	result = PyTuple_New(2);
	if (result == NULL) {
		return NULL;
	}

	v = PyObjC_ObjCToPython(@encode(NSRect), &slice);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	PyTuple_SET_ITEM(result, 0, v);

	v = PyObjC_ObjCToPython(@encode(NSRect), &rem);
	if (v == NULL) {
		Py_DECREF(result);
		return NULL;
	}
	PyTuple_SET_ITEM(result, 1, v);
	return result;
}

static PyMethodDef foundation_methods[] = {
#ifdef MACOSX
	{ 
		"NSFileTypeForHFSTypeCode", 
		(PyCFunction)objc_NSFileTypeForHFSTypeCode, 
		METH_VARARGS|METH_KEYWORDS, 
		objc_NSFileTypeForHFSTypeCode_doc
	},
	{ 
		"NSHFSFTypeCodeFromFileType", 
		(PyCFunction)objc_NSHFSTypeCodeFromFileType, 
		METH_VARARGS|METH_KEYWORDS, 
		objc_NSHFSTypeCodeFromFileType_doc 
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
	{
		"NSDivideRect",
		(PyCFunction)objc_NSDivideRect,
		METH_VARARGS|METH_KEYWORDS,
		NSDivideRect_doc
	},

	METHOD_TABLE_ENTRIES

	{ 0, 0, 0, 0 } /* sentinel */
};

PyDoc_STRVAR(foundation_doc,
"Foundation._Foundation defines constants, types and global functions used by "
"Foundation."
);

#include "_Fnd_Enum.inc"
#include "_Fnd_Str.inc"

static inline int add_NSPoint(PyObject* d, char* name, NSPoint value)
{
        int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(NSPoint), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_NSSize(PyObject* d, char* name, NSSize value)
{
        int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(NSSize), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_NSRect(PyObject* d, char* name, NSRect value)
{
        int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(NSRect), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

/*
 * Include the implementation of difficult methods.
 */
#ifdef MACOSX
#include "_FoundationMapping_NSAppleEventDescriptor.m"
#endif
#include "_FoundationMapping_NSArray.m"
#include "_FoundationMapping_NSCoder.m"
#include "_FoundationMapping_NSData.m"
#include "_FoundationMapping_NSDictionary.m"
#include "_FoundationMapping_NSIndexSet.m"
#include "_FoundationMapping_NSInputStream.m"
#include "_FoundationMapping_NSMutableArray.m"
#include "_FoundationMapping_NSNetService.m"
#include "_FoundationMapping_NSScriptObjectSpecifier.m"
#include "_FoundationMapping_NSSet.m"
#include "_FoundationMapping_NSString.m"


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

#ifdef MACOSX
	bundle = CFBundleCreate(NULL,
		(CFURLRef)[NSURL fileURLWithPath:@"/System/Library/Frameworks/Foundation.framework"]);
#else
	bundle = NULL;
#endif

	/* Register information in generated tables */
	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, (sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

#ifdef MACOSX
	CFRelease(bundle);
#endif


#	include "_Fnd_Var.inc"
    
	/* Add manual registrations below */


	/* Install wrappers for difficult methods */
#ifdef MACOSX
    /* XXX - check for OS X 10.2+ */
    if (_pyobjc_install_NSAppleEventDescriptor() != 0) return;
#endif
	if (_pyobjc_install_NSArray() != 0) return;
	if (_pyobjc_install_NSCoder() != 0) return;
	if (_pyobjc_install_NSData() != 0) return;
	if (_pyobjc_install_NSDictionary() != 0) return;
	if (_pyobjc_install_NSIndexSet() != 0) return;
	if (_pyobjc_install_NSInputStream() != 0) return;
	if (_pyobjc_install_NSMutableArray() != 0) return;
	if (_pyobjc_install_NSNetService() != 0) return;
	if (_pyobjc_install_NSScriptObjectSpecifier() != 0) return;
	if (_pyobjc_install_NSSet() != 0) return;
	if (_pyobjc_install_NSString() != 0) return;
}
