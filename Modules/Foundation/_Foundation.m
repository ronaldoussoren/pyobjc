/*
 * Mapping of static items in the Foundation kit, and custom wrappers for
 * "difficult" methods.
 */

#include <Python.h>
#import <Foundation/Foundation.h>
#import <Foundation/NSDebug.h>

#ifdef MACOSX
#include <pymactoolbox.h>

#else
/* GNUstep's Foundation.h doesn't include these while we do use them */
#import <Foundation/NSPropertyList.h>
#import <Foundation/NSKeyedArchiver.h>
#endif

#include "pyobjc-api.h"
#include "wrapper-const-table.h"

#include "NSAutoreleasePoolSupport.m"
#include "decimals.m"

#include "_Fnd_Functions.inc"
#include "_Fnd_Classes.inc"

#ifdef MACOSX


PyDoc_STRVAR(objc_NSFileTypeForHFSTypeCode_doc,
	"NSString *NSFileTypeForHFSTypeCode(OSType hfsTypeCode);");

static PyObject* 
objc_NSFileTypeForHFSTypeCode(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static	char* keywords[] = { "hfsTypeCode", NULL };
	PyObject*  result;
	NSString*  oc_result;
	OSType hfsTypeCode;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"i:NSFileTypeForHFSTypeCode",
			keywords, &hfsTypeCode)) {
		PyErr_Clear();
		if (!PyArg_ParseTupleAndKeywords(args, kwds, 
				"O&:NSFileTypeForHFSTypeCode",
				keywords, PyMac_GetOSType, &hfsTypeCode)) {
			return NULL;
		}
	}
	
	PyObjC_DURING
		oc_result = NSFileTypeForHFSTypeCode(hfsTypeCode);
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		oc_result = NULL;
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	result = PyObjC_IdToPython(oc_result);
	return result;
}

PyDoc_STRVAR(objc_NSHFSTypeCodeFromFileType_doc,
		"OSType NSHFSTypeCodeFromFileType(NSString *fileType);");

static PyObject* 
objc_NSHFSTypeCodeFromFileType(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
{
static	char* keywords[] = { "hfsTypeCode", NULL };
	NSString*  fileType;
	OSType hfsTypeCode;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"O&:NSHFSTypeCodeFromFileType",
			keywords, PyObjCObject_Convert, &fileType)) {
		return NULL;
	}
	
	PyObjC_DURING
		hfsTypeCode = NSHFSTypeCodeFromFileType(fileType);
	PyObjC_HANDLER
		hfsTypeCode = 0;
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

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

static PyObject* 
objc_NSDivideRect(
	PyObject* self __attribute__((__unused__)), 
	PyObject* args, 
	PyObject* kwds)
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

static inline int 
add_NSPoint(PyObject* d, char* name, NSPoint value)
{
        int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(NSPoint), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int 
add_NSTimeInterval(PyObject* d, char* name, NSTimeInterval value)
{
        int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(NSTimeInterval), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int 
add_NSSize(PyObject* d, char* name, NSSize value)
{
        int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(NSSize), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int 
add_NSRect(PyObject* d, char* name, NSRect value)
{
        int res;
	PyObject* v;

	v = PyObjC_ObjCToPython(@encode(NSRect), &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}


static PyObject* call_objWithObjects_count_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	PyObject* objectList;
	PyObject* objectCount;
	id* objects;
	int count;
	int arrayToken;
	id  res;

	if  (!PyArg_ParseTuple(arguments, "OO", &objectList, &objectCount)) {
		return NULL;
	}

	arrayToken = PyObjC_PythonToCArray(@encode(id),
			objectList, objectCount,
			(void**)&objects, &count);
	if (arrayToken == -1) {
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			res = ((id(*)(id,SEL,id*,int))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCObject_GetObject(self),
					PyObjCIMP_GetSelector(method),
					objects, count);
		} else {
			PyObjC_InitSuper(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCObject_GetObject(self));

			res = objc_msgSendSuper(&super,
				PyObjCSelector_GetSelector(method),
				objects, count);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	PyObjC_ENDHANDLER

	PyObjC_FreeCArray(arrayToken, objects);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	if (PyObjCObject_IsUninitialized(self)) {
		if (result != self) {
			PyObjCObject_ClearObject(self);
		}
	}

	return result;
}

static void 
imp_objWithObjects_count_(void* cif __attribute__((__unused__)), void* resp, void** args, void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	id* objects = *(id**)args[2];
	int count = *(int*)args[3];
	id* preturnValue = (id*)resp;

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v = NULL;
	PyGILState_STATE state;

	*preturnValue = nil;

	state = PyGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyObjC_CArrayToPython(@encode(id), objects, count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyInt_FromLong(count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 2,  v);

	result = PyObject_Call((PyObject*)callable, arglist, NULL); 
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	*preturnValue = PyObjC_PythonToId(result);
	Py_DECREF(result);
	if (PyErr_Occurred()) goto error;

	PyGILState_Release(state);
	return;

error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
	*preturnValue = nil;
}


static PyObject* call_clsWithObjects_count_(
		PyObject* method, PyObject* self, PyObject* arguments)
{
	PyObject* result;
	struct objc_super super;
	PyObject* objectList;
	PyObject* objectCount;
	id* objects;
	int count;
	int arrayToken;
	id  res;

	if  (!PyArg_ParseTuple(arguments, "OO", &objectList, &objectCount)) {
		return NULL;
	}

	arrayToken = PyObjC_PythonToCArray(
			@encode(id), 
			objectList, objectCount,
			(void**)&objects, &count);
	if (arrayToken == -1) {
		return NULL;
	}

	PyObjC_DURING
		if (PyObjCIMP_Check(method)) {
			res = ((id(*)(id,SEL,id*,int))
				(PyObjCIMP_GetIMP(method)))(
					PyObjCClass_GetClass(self),
					PyObjCIMP_GetSelector(method),
					objects, count);
		} else {
			PyObjC_InitSuperCls(&super, 
				PyObjCSelector_GetClass(method),
				PyObjCClass_GetClass(self));

			res = objc_msgSendSuper(&super,
					PyObjCSelector_GetSelector(method),
					objects, count);
		}
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
		res = nil;
	PyObjC_ENDHANDLER

	PyObjC_FreeCArray(arrayToken, objects);

	if (res == nil && PyErr_Occurred()) {
		return NULL;
	}
	
	result = PyObjC_IdToPython(res);

	return result;
}

static void 
imp_clsWithObjects_count_(void* cif __attribute__((__unused__)), void* resp, void** args, void* callable)
{
	id self = *(id*)args[0];
	//SEL _meth = *(SEL*)args[1];
	id* objects = *(id**)args[2];
	int count = *(int*)args[3];
	id* preturnValue = (id*)resp;

	PyObject* result = NULL;
	PyObject* arglist = NULL;
	PyObject* v = NULL;
	PyGILState_STATE state = PyGILState_Ensure();

	arglist = PyTuple_New(3);
	if (arglist == NULL) goto error;

	v = PyObjC_IdToPython(self);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 0, v);

	v = PyObjC_CArrayToPython(@encode(id), objects, count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 1, v);

	v = PyInt_FromLong(count);
	if (v == NULL) goto error;
	PyTuple_SET_ITEM(arglist, 2,  v);

	result = PyObject_Call((PyObject*)callable, arglist, NULL);
	Py_DECREF(arglist); arglist = NULL;
	if (result == NULL) goto error;

	*preturnValue = PyObjC_PythonToId(result);
	Py_DECREF(result);
	if (PyErr_Occurred()) goto error;
	PyGILState_Release(state);
	return;


error:
	Py_XDECREF(arglist);
	PyObjCErr_ToObjCWithGILState(&state);
	*preturnValue = nil;
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
#include "_FoundationMapping_NSDecimalNumber.m"
#include "_FoundationMapping_NSDictionary.m"
#include "_FoundationMapping_NSIndexSet.m"
#include "_FoundationMapping_NSMutableArray.m"
#include "_FoundationMapping_NSNetService.m"
#include "_FoundationMapping_NSScriptObjectSpecifier.m"
#include "_FoundationMapping_NSSet.m"
#include "_FoundationMapping_NSString.m"
#include "_FoundationMapping_NSStream.m"

static const char* NSPoint_name = "Foundation.NSPoint";
static const char* NSPoint_doc = "struct NSPoint(x, y)";
static const char* NSPoint_fields[] = {
	"x",
	"y"
};

static const char* NSSize_name = "Foundation.NSSize";
static const char* NSSize_doc = "struct NSSize(width, height)";
static const char* NSSize_fields[] = {
	"width",
	"height"
};

static const char* NSRange_name = "Foundation.NSRange";
static const char* NSRange_doc = "struct NSRange(location, length)";
static const char* NSRange_fields[] = {
	"location",
	"length"
};

static const char* NSRect_name = "Foundation.NSRect";
static const char* NSRect_doc = "struct NSRect(origin, size)";
static const char* NSRect_fields[] = {
	"origin",
	"size",
	NULL
};

/* A special init method for rects, this sets a different default value
 * for the fields, makes the type more convenient to use.
 */
static int 
NSRect_init(PyObject* self, PyObject* args, PyObject* kwds)
{
	PyObject* origin = NULL;
	PyObject* size  = NULL;
	int r;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OO", 
				(char**)NSRect_fields, &origin, &size)) {
		return -1;
	}

	if (origin == NULL) {
		NSPoint aPoint = { 0, 0 };
		origin = PyObjC_ObjCToPython(@encode(NSPoint), &aPoint);
		if (origin == NULL) return -1;
	} else {
		Py_INCREF(origin);
	}

	if (size == NULL) {
		NSSize aSize = { 0, 0 };
		size = PyObjC_ObjCToPython(@encode(NSSize), &aSize);
		if (size == NULL) {
			Py_DECREF(origin);
			return -1;
		}
	} else {
		Py_INCREF(size);
	}

	r = PyObject_SetAttrString(self, "origin", origin);
	if (r == -1)  {
		Py_DECREF(origin);
		Py_DECREF(size);
		return -1;
	}
	r = PyObject_SetAttrString(self, "size", size);
	if (r == -1)  {
		Py_DECREF(origin);
		Py_DECREF(size);
		return -1;
	}
	Py_DECREF(origin);
	Py_DECREF(size);

	return 0;
}

void init_Foundation(void);

void init_Foundation(void)
{
	PyObject *m, *d, *v;
	CFBundleRef bundle;
	const char** name;

	m = Py_InitModule4("_Foundation", foundation_methods, foundation_doc, 
			NULL, PYTHON_API_VERSION);
	d = PyModule_GetDict(m);

	if (PyObjC_ImportAPI(m) < 0) {
		printf("Importing objc failed\n");
		return;
	}

#ifdef MACOSX
	bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.Foundation"));
#else
	bundle = NULL;
#endif

	/* Register information in generated tables */
	if (register_ints(d, enum_table) < 0) return;
	if (register_variableList(d, bundle, string_table, (sizeof(string_table)/sizeof(string_table[0]))-1) < 0) return;

#ifdef 	NSUserDomainMask
	/* These are defines and not enums on GNUstep */
	{
	int v;

	v = NSUserDomainMask;
	PyModule_AddObject(m, "NSUserDomainMask", PyObjC_ObjCToPython(@encode(int), &v)); 

	v = NSLocalDomainMask;
	PyModule_AddObject(m, "NSLocalDomainMask", PyObjC_ObjCToPython(@encode(int), &v)); 

	v = NSNetworkDomainMask;
	PyModule_AddObject(m, "NSNetworkDomainMask", PyObjC_ObjCToPython(@encode(int), &v)); 

	v = NSSystemDomainMask;
	PyModule_AddObject(m, "NSSystemDomainMask", PyObjC_ObjCToPython(@encode(int), &v)); 

	v = NSAllDomainsMask;
	PyModule_AddObject(m, "NSAllDomainsMask", PyObjC_ObjCToPython(@encode(int), &v)); 
	}
#endif


#ifdef MACOSX
	CFRelease(bundle);
#endif


#	include "_Fnd_Var.inc"
    
	/* Add manual registrations below */
	v = PyObjC_RegisterStructType(@encode(NSPoint),
			NSPoint_name, NSPoint_doc, NULL, 2, NSPoint_fields);
	if (v == NULL) return;
	PyDict_SetItemString(d, "NSPoint", v);
	Py_DECREF(v);

	v = PyObjC_RegisterStructType(@encode(NSSize),
			NSSize_name, NSSize_doc, NULL, 2, NSSize_fields);
	if (v == NULL) return;
	PyDict_SetItemString(d, "NSSize", v);
	Py_DECREF(v);

	v = PyObjC_RegisterStructType(@encode(NSRange),
			NSRange_name, NSRange_doc, NULL, 2, NSRange_fields);
	if (v == NULL) return;
	PyDict_SetItemString(d, "NSRange", v);
	Py_DECREF(v);

	v = PyObjC_RegisterStructType(@encode(NSRect),
			NSRect_name, NSRect_doc, NSRect_init, 2, NSRect_fields);
	if (v == NULL) return;
	PyDict_SetItemString(d, "NSRect", v);
	Py_DECREF(v);

	/* Install wrappers for difficult methods */
#ifdef MACOSX
	/* XXX - check for OS X 10.2+ */
	if (_pyobjc_install_NSAppleEventDescriptor() != 0) return;
#endif
	if (_pyobjc_install_NSArray() != 0) return;
	if (_pyobjc_install_NSCoder() != 0) return;
	if (_pyobjc_install_NSData() != 0) return;
	if (_pyobjc_install_NSDecimalNumber() != 0) return;
	if (_pyobjc_install_NSDictionary() != 0) return;
	if (_pyobjc_install_NSIndexSet() != 0) return;
	if (_pyobjc_install_NSMutableArray() != 0) return;
	if (_pyobjc_install_NSNetService() != 0) return;
	if (_pyobjc_install_NSScriptObjectSpecifier() != 0) return;
	if (_pyobjc_install_NSSet() != 0) return;
	if (_pyobjc_install_NSString() != 0) return;
	if (_pyobjc_install_NSStream() != 0) return;
	if (install_decimal(m) != 0) return;

	/*
	 * On OSX finding the bundle/framework for a class is *very* expensive.
	 * We therefore have a cache of names of classes that are present in
	 * the Foundation framework. That way we don't have to ask for the 
	 * bundle/framework as often, which speeds up program initialization.
	 */
	v = PyString_FromString("Foundation");
	for (name = gClassNames; *name != NULL; name++) {
		PyObject* o;
		Class cls = objc_lookUpClass(*name);
		if (cls == NULL) continue;

		o = PyObjCClass_New(cls);
		if (o == NULL) return;

		PyObject_SetAttrString(o, "__module__", v);
		Py_DECREF(o);
	}
	Py_DECREF(v);
}
