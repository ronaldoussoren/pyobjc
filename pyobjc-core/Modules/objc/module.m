/*
 * The module entry point for ``_objc``. This file contains ``init_objc``
 * and the implementation of a number of exported functions.
 */
#include "pyobjc.h"
#include "OC_NSBundleHack.h"
#include <objc/Protocol.h>
#include <objc/objc-sync.h>

#include <stddef.h>
#include <ctype.h>
#include <sys/socket.h>
#include <netinet/in.h>

#import <Foundation/NSAutoreleasePool.h>
#import <Foundation/NSBundle.h>
#import <Foundation/NSProcessInfo.h>
#import <Foundation/NSString.h>

#import <mach-o/dyld.h>
#import <mach-o/getsect.h>
#import <mach-o/loader.h>
#import <objc/Protocol.h>

int PyObjC_VerboseLevel = 0;
int PyObjC_HideProtected = 1;
BOOL PyObjC_useKVO = YES;
BOOL PyObjC_nativeProperties = NO;

PyObject* PyObjCClass_DefaultModule = NULL;
PyObject* PyObjC_NSNumberWrapper = NULL;
#if PY_MAJOR_VERSION == 2
PyObject* PyObjCStrBridgeWarning = NULL;
int PyObjC_StrBridgeEnabled = 1;
#endif


PyObject* PyObjC_TypeStr2CFTypeID = NULL;

static NSAutoreleasePool* global_release_pool = nil;

@interface OC_NSAutoreleasePoolCollector: NSObject
  /* 
   * This class is used to automaticly reset the
   * global pool when an outer autorelease pool is
   * recycled. This avoids problems when a python
   * plugin is loaded in an Objective-C program.
   */
{}
+(void)newAutoreleasePool;
+(void)targetForBecomingMultiThreaded:(id)sender;
@end
@implementation OC_NSAutoreleasePoolCollector
+(void)newAutoreleasePool
{
	self = [[self alloc] init];
	global_release_pool = [[NSAutoreleasePool alloc] init];
	(void)[self autorelease];
}

-(void)dealloc
{
	global_release_pool = nil;
	[super dealloc];
}

+(void)targetForBecomingMultiThreaded:(id)sender
{
    [sender self];
}

@end

PyDoc_STRVAR(pyobjc_id_doc,
  "pyobjc_id(obj) -> int\n"
  "\n"
  "Return the id of the underlying NSObject as an int."
);

static PyObject*
pyobjc_id(PyObject* self __attribute__((__unused__)), PyObject* args,
PyObject *kwds)
{
	static char* keywords[] = { "obj", NULL };
	PyObject *o;
	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O",
		keywords, &o)) {
		return NULL;
	}
	if (!PyObjCObject_Check(o)) {
		PyErr_SetString(PyExc_TypeError, "not an Objective-C object");
		return NULL;
	}
	return PyInt_FromLong((long)PyObjCObject_GetObject(o));
}


PyDoc_STRVAR(repythonify_doc,
  "repythonify(obj, type='@') -> object\n"
  "\n"
  "Put an object through the bridge by calling \n"
  "depythonify_c_value then pythonify_c_value.\n"
  "This is for internal use only."
);

static PyObject*
repythonify(PyObject* self __attribute__((__unused__)), PyObject* args,
PyObject *kwds)
{
	static char* keywords[] = { "obj", "type", NULL };
	const char *type = "@";
	PyObject *rval;
	void *datum;
	Py_ssize_t size;
	PyObject *o;
	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
				"O|"Py_ARG_BYTES,
		keywords, &o, &type)) {
		return NULL;
	}
	size = PyObjCRT_SizeOfType(type);
	if (size < 1) {
		PyErr_SetString(PyExc_ValueError, "Can not calculate size for type");
		return NULL;
	}
	datum = PyMem_Malloc(size);
	if (datum == NULL) {
		return PyErr_NoMemory();
	}
	if (depythonify_c_value(type, o, datum)) {
		PyMem_Free(datum);
		return NULL;
	}
	rval = pythonify_c_value(type, datum);
	PyMem_Free(datum);
	return rval;
}

#if PY_MAJOR_VERSION == 2
PyDoc_STRVAR(setStrBridgeEnabled_doc,
  "setStrBridgeEnabled(bool)\n"
  "\n"
  "False disables the transparent str bridge (default) \n"
  "True enables the transparent str bridge, note that \n"
  "this is discouraged.");

static PyObject*
setStrBridgeEnabled(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
	static char* keywords[] = { "enabled", NULL };
	PyObject *o;
	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:setStrBridgeEnabled",
		keywords, &o)) {
		return NULL;
	}
	PyObjC_StrBridgeEnabled = PyObject_IsTrue(o);
	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(getStrBridgeEnabled_doc,
	"getStrBridgeEnabled() -> bool\n"
	"\n"
	"Return the status of the transparent str bridge.");

static PyObject* 
getStrBridgeEnabled(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
	static char* keywords[] = { NULL };

	if (!PyArg_ParseTupleAndKeywords(args, kwds, ":getStrBridgeEnabled",
			keywords)) {
		return NULL;
	}

	return PyBool_FromLong(PyObjC_StrBridgeEnabled);
}
#endif /* !Py3k */

PyDoc_STRVAR(lookUpClass_doc,
  "lookUpClass(class_name) -> class\n"
  "\n"
  "Search for the named classes in the Objective-C runtime and return it.\n"
  "Raises noclass_error when the class doesn't exist.");

static PyObject* 
lookUpClass(PyObject* self __attribute__((__unused__)), 
	PyObject* args, PyObject* kwds)
{
	static 	char* keywords[] = { "class_name", NULL };
	char* class_name = NULL;
	Class objc_class;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "s:lookUpClass",
			keywords, &class_name)) {
		return NULL;
	}

	objc_class = objc_lookUpClass(class_name);
	if (objc_class == NULL) {
		PyErr_SetString(PyObjCExc_NoSuchClassError, class_name);
		return NULL;
	}
	return PyObjCClass_New(objc_class);
}


PyDoc_STRVAR(classAddMethods_doc,
	 "classAddMethods(targetClass, methodsArray)\n"
	 "\n"
	 "Adds methods in methodsArray to class. The effect is similar to how \n"
	 "categories work. If class already implements a method as defined in \n"
	 "methodsArray, the original implementation will be replaced by the \n"
	 "implementation from methodsArray.");

static PyObject*
classAddMethods(PyObject* self __attribute__((__unused__)), 
	PyObject* args, PyObject* keywds)
{
	static 	char* kwlist[] = { "targetClass", "methodsArray", NULL };
	PyObject* classObject = NULL;
	PyObject* methodsArray = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, keywds, 
			"OO:classAddMethods", kwlist,
			&classObject, &methodsArray)) {
		return NULL;
	}

	if (!PyObjCClass_Check(classObject)) {
		PyErr_SetString(PyExc_TypeError, "base class is not an Objective-C class");
		return NULL;
	}

	methodsArray = PySequence_Fast(
			methodsArray, "methodsArray must be a sequence");
	if (methodsArray == NULL) return NULL;
	
	int r = PyObjCClass_AddMethods(classObject, 
			PySequence_Fast_ITEMS(methodsArray),
			PySequence_Fast_GET_SIZE(methodsArray));
	Py_DECREF(methodsArray);

	if (r == -1) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}



PyDoc_STRVAR(remove_autorelease_pool_doc,
  "removeAutoreleasePool()\n"
  "\n"
  "This removes the global NSAutoreleasePool.  You should do this\n"
  "at the end of a plugin's initialization script.\n");
static PyObject*
remove_autorelease_pool(PyObject* self __attribute__((__unused__)),
	PyObject* args, PyObject* kwds)
{
	static char* keywords[] = { NULL };
	if (!PyArg_ParseTupleAndKeywords(args, kwds, "", keywords)) {
		return NULL;
	}

	PyObjC_DURING
		[global_release_pool release];
		global_release_pool = nil;
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(recycle_autorelease_pool_doc,
  "recycleAutoreleasePool()\n"
  "\n"
  "This 'releases' the global autorelease pool and creates a new one.\n"
  "This method is for system use only\n");
static PyObject*
recycle_autorelease_pool(PyObject* self __attribute__((__unused__)), 
	PyObject* args, PyObject* kwds)
{
	static	char* keywords[] = { NULL };

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "", keywords)) {
		return NULL;
	}

	if (global_release_pool != NULL) {

		PyObjC_DURING
			[global_release_pool release];
			[OC_NSAutoreleasePoolCollector newAutoreleasePool];
		PyObjC_HANDLER
			PyObjCErr_FromObjC(localException);
		PyObjC_ENDHANDLER

		if (PyErr_Occurred()) return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(set_class_extender_doc,
	"setClassExtender(func) -> None\n"
	"\n"
	"Register a function that will be called to update the class\n"
	"dict of new Objective-C classes and class-proxies. This will\n"
	"replace any existing callback.\n"
	"The function will be called like this:\n"
	"\tclass_extender(superclass, class_name, class_dict)\n"
	"superclass:\n"
	"  The superclass for the new class, or None if this is the top of\n"
	"  a class hierarchy.\n"
	"class_name:\n"
	"  Name of the new class\n"
	"class_dict:\n"
	"  The proposed class dictionary. The callback is supposed to update\n"
	"  this dictionary.\n"
	"");
static PyObject*
set_class_extender(PyObject* self __attribute__((__unused__)), 
	PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "callback", NULL };
	PyObject* callback;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:setClassExtender",
			keywords, &callback)) {
		return NULL;
	}

	if (!PyCallable_Check(callback)) {
		PyErr_SetString(PyExc_TypeError, "Expecting callable");
		return NULL;
	}
	
	Py_INCREF(callback);
	Py_XDECREF(PyObjC_ClassExtender);
	PyObjC_ClassExtender = callback;

	Py_INCREF(Py_None);
	return Py_None;
}


PyDoc_STRVAR(getClassList_doc,
  "getClassList() -> [ cls, ...] n"
  "\n"
  "Return a list with all Objective-C classes known to the runtime.\n"
);
static PyObject* 
getClassList(PyObject* self __attribute__((__unused__)))
{
	return PyObjC_GetClassList();
}

PyDoc_STRVAR(set_signature_for_selector_doc,
	"setSignatureForSelector(class_name, selector, signature) -> None\n"
	"\n"
	"Register a replacement signature for a specific selector. This \n"
	"can be used to provide a more exact signature for a method.\n"
	"\n"
	"This function is deprecated, use the new metadata machinery.\n"
	"");
static PyObject* 
set_signature_for_selector(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "class_name", "selector", "signature", NULL };
	char* class_name;
	char* selector;
	char* signature;
	SEL   sel;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sss:setSignatureForSelector",
			keywords, &class_name, &selector, &signature)) {
		return NULL;
	}

	if (PyErr_WarnEx(PyExc_DeprecationWarning,
		"Use the new metadata machinery", 1) < 0) {

		return NULL;
	}

	sel = sel_getUid(selector);
	
	if (ObjC_SignatureForSelector(class_name, sel, signature) < 0) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(setNSNumberWrapper_doc,
	"_setNSNumberWrapper(wrapper) -> None\n"
	"\n"
	"Set the NSNumber wrapper function to the new value."
);
static PyObject* 
setNSNumberWrapper(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "wrapper", NULL };
	PyObject* o;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &o)) {
		return NULL;
	}

	Py_XDECREF(PyObjC_NSNumberWrapper);
	Py_INCREF(o);
	PyObjC_NSNumberWrapper = o;

	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(getNSNumberWrapper_doc,
	"_getNSNumberWrapper() -> wrapper\n"
	"\n"
	"Get the current NSNumber wrapper function."
);
static PyObject* 
getNSNumberWrapper(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { NULL };

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "",
			keywords)) {
		return NULL;
	}

	if (PyObjC_NSNumberWrapper == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}
	Py_INCREF(PyObjC_NSNumberWrapper);
	return PyObjC_NSNumberWrapper;
}

PyDoc_STRVAR(setHideProtected_doc,
	"setHideProtected(bool) -> None\n"
	"\n"
	"If true methods whose name starts with an underscore will not "
	"visible for introspection using dir() or the class __dict__.");
static PyObject* 
setHideProtected(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "flag", NULL };
	PyObject* o;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O",
			keywords, &o)) {
		return NULL;
	}

	PyObjC_HideProtected = PyObject_IsTrue(o);

	Py_INCREF(Py_None);
	return Py_None;
}


PyDoc_STRVAR(setVerbose_doc,
	"setVerbose(bool) -> None\n"
	"\n"
	"Set verbosity to the new value."
);
static PyObject* 
setVerbose(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "level", NULL };
	PyObject* o;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:setVerbose",
			keywords, &o)) {
		return NULL;
	}

	PyObjC_VerboseLevel = PyObject_IsTrue(o);

	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(setUseKVOForSetattr_doc,
	"setUseKVOForSetattr(bool) -> bool\n"
	"\n"
	"Specify the default value for __useKVO__ on classes defined "
	"after this call. Returns the previous value."
);
static PyObject* 
setUseKVOForSetattr(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "value", NULL };
	PyObject* o;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &o)) {
		return NULL;
	}

	PyObject* result = PyBool_FromLong(PyObjC_useKVO);
	PyObjC_useKVO = PyObject_IsTrue(o);

	return result;
}

PyDoc_STRVAR(getVerbose_doc,
	"getVerbose() -> bool\n"
	"\n"
	"Return the verbosity value."
);
static PyObject* 
getVerbose(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { NULL };

	if (!PyArg_ParseTupleAndKeywords(args, kwds, ":getVerbose",
			keywords)) {
		return NULL;
	}

	return PyBool_FromLong(PyObjC_VerboseLevel);
}


PyDoc_STRVAR(allocateBuffer_doc,
	     "allocateBuffer(size) -> <r/w buffer>\n"
	     "\n"
	     "Allocate a buffer of memory of size. Buffer is \n"
	     "read/write."
	     );
static PyObject*
allocateBuffer(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
	static	char* keywords[] = { "length", 0 };
	Py_ssize_t length;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, Py_ARG_SIZE_T, 
				keywords, &length)) {
		return NULL;
	}

	if (length <= 0 ) {
		PyErr_SetString(PyExc_ValueError, 
			"Length must be greater than 0.");
		return NULL;
	}

#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION < 6
	return PyBuffer_New(length);
#else
	return PyByteArray_FromStringAndSize(NULL, length);
#endif
}

PyDoc_STRVAR(currentBundle_doc,
	"currentBundle() -> bundle\n"
	"\n"
	"Get the current bundle during module initialization.\n"
	"Works for plug-ins and applications.\n"
	"\n"
	"Note that this is the default bundle used by\n"
	"NibClassBuilder.extractClasses(...),\n"
	"so calling it explicitly is rarely useful.\n"
	"After module initialization, use\n"
	"NSBundle.bundleForClass_(ClassInYourBundle)."
);
static PyObject*
currentBundle(PyObject* self __attribute__((__unused__)))
{
	id rval;
	char *bundle_address = getenv("PYOBJC_BUNDLE_ADDRESS");
	if (!(bundle_address && sscanf(bundle_address, "%p", &rval) == 1)) {
		rval = [NSBundle mainBundle];
	}
	return pythonify_c_value(@encode(id), &rval);
}


PyDoc_STRVAR(loadBundle_doc,
	"loadBundle(module_name, module_globals, bundle_path=None, "
	"bundle_identifier=None) -> bundle\n"
	"\n"
	"Load the bundle identified by 'bundle_path' or 'bundle_identifier' \n"
	"and add the classes in the bundle to the 'module_globals'.\n"
	"\n"
	"If 'bundle_identifier' is specified the right bundle is located\n"
	"using NSBundle's +bundleWithIdentifier:.\n"
	"If 'bundle_path' is specified the right bundle is located using\n"
	"NSBundle's +bundleWithPath:. The path must be an absolute pathname\n"
);
static PyObject*
loadBundle(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { "module_name", "module_globals", "bundle_path", "bundle_identifier", "scan_classes", NULL };
static	Py_ssize_t	curClassCount = -1;
	NSBundle* bundle = nil;
	id bundle_identifier = nil;
	id bundle_path = nil;
	PyObject* module_name;
	PyObject* module_globals;
	PyObject* class_list;
	Py_ssize_t len, i;
	PyObject* scanClasses = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
#if PY_MAJOR_VERSION == 2
			"SO|O&O&O",
#else
			"UO|O&O&O",
#endif
			keywords, &module_name, &module_globals,
			PyObjCObject_Convert, &bundle_path, PyObjCObject_Convert, &bundle_identifier, &scanClasses)) {
		return NULL;
	}

	if (!bundle_path && !bundle_identifier) {
		PyErr_SetString(PyExc_ValueError,
			"Need to specify either bundle_path or "
			"bundle_identifier");
		return NULL;
	}
	if (bundle_path && bundle_identifier) {
		PyErr_SetString(PyExc_ValueError,
			"Need to specify either bundle_path or "
			"bundle_identifier");
		return NULL;
	}

	if (bundle_path) {
		if (![bundle_path isKindOfClass:[NSString class]]) {
			PyErr_SetString(PyExc_TypeError,
					"bundle_path is not a string");
			return NULL;
		}
		bundle = [NSBundle bundleWithPath:bundle_path];
	} else {
		if (![bundle_identifier isKindOfClass:[NSString class]]) {
			PyErr_SetString(PyExc_TypeError,
					"bundle_identifier is not a string");
			return NULL;
		}
		bundle = [NSBundle bundleWithIdentifier:bundle_identifier];
	}

	if (![bundle load]) {
		PyErr_SetString(PyExc_ImportError,
			"Bundle could not be loaded");
		return NULL;
	}

	/* 
	 * Scanning the class list is expensive and something to be avoided
	 * when possible.
	 */

	if (scanClasses != NULL && !PyObject_IsTrue(scanClasses)) {
		return pythonify_c_value(@encode(NSBundle*), &bundle);
	}

#if 0
	Py_ssize_t newClassCount = PyObjC_ClassCount();
	if (newClassCount == curClassCount) {
		/* Make use of the structure of wrapper modules to avoid
		 * scanning the class list when nothing has changed. 
		 *
		 * Bundle wrappers first 'from Dependency import *' and then
		 * load the wrapped framework. When that framework doesn't
		 * define new classes we don't actually have to add classes
		 * to the global dict.
		 */
		return pythonify_c_value(@encode(NSBundle*), &bundle);
	}
#endif


	class_list = PyObjC_GetClassList();
	if (class_list == NULL) {	
		return NULL;
	}

	curClassCount = len = PyTuple_GET_SIZE(class_list);
	for (i = 0; i < len; i++) {
		PyObject* item;
		const char*  nm;

		item = PyTuple_GET_ITEM(class_list, i);
		if (item == NULL) {
			continue;
		}

		nm = ((PyTypeObject*)item)->tp_name;

		if (nm[0] == '%') {
			/* skip, posed-as type */
		} else if (PyObjC_HideProtected && nm[0] == '_') {
			/* Skip private classes */
		} else if (strcmp(nm, "Object") == 0 
				|| strcmp(nm, "List") == 0
				|| strcmp(nm, "Protocol") == 0) {
			/* skip, these have been deprecated since OpenStep! */
		} else if (PyDict_SetItemString(module_globals, 
				((PyTypeObject*)item)->tp_name, item) == -1) {
			Py_DECREF(class_list); class_list = NULL;
			return NULL;
		}
	}
	Py_XDECREF(class_list); class_list = NULL;

	return pythonify_c_value(@encode(NSBundle*), &bundle);
}

PyDoc_STRVAR(objc_splitSignature_doc,
	"splitSignature(signature) -> list\n"
	"\n"
	"Split a signature string into a list of items."
);
static PyObject*
objc_splitSignature(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { "signature", NULL };
	const char* signature;
	const char* end;
	PyObject* result;
	PyObject* tuple;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			Py_ARG_BYTES,
			keywords, &signature)) {
		return NULL;
	}

	result = PyList_New(0);
	if (result == NULL) return NULL;
	
	while (signature && *signature != 0) {
		PyObject* str;
		const char* t;

		end = PyObjCRT_SkipTypeSpec(signature);
		if (end == NULL) {
			Py_DECREF(result);
			return NULL;
		}

		t = end-1;
		while (t != signature && isdigit(*t)) {
			t --;
		}
		t ++;

		str = PyBytes_FromStringAndSize(signature, t - signature);
		if (str == NULL) {
			Py_DECREF(result);
			return NULL;
		}

		if (PyList_Append(result, str) == -1) {
			Py_DECREF(result);
			return NULL;
		}

		signature = end;
	}	

	tuple = PyList_AsTuple(result);
	Py_DECREF(result);
	return tuple;
}


PyDoc_STRVAR(objc_splitStruct_doc,
	"_splitStruct(signature) -> fieldnames, types\n"
	"\n"
	"Split a struct signature string into a list of items."
);
static PyObject*
objc_splitStruct(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { "signature", NULL };
	const char* signature;
	const char* end;
	PyObject* result;
	PyObject* tuple;

	/* XXX */

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"s:splitStruct",
			keywords, &signature)) {
		return NULL;
	}

	result = PyList_New(0);
	if (result == NULL) return NULL;
	
	while (signature && *signature != 0) {
		PyObject* str;
		const char* t;

		end = PyObjCRT_SkipTypeSpec(signature);
		if (end == NULL) {
			Py_DECREF(result);
			return NULL;
		}

		t = end-1;
		while (t != signature && isdigit(*t)) {
			t --;
		}
		t ++;

		str = PyText_FromStringAndSize(signature, t - signature);
		if (str == NULL) {
			Py_DECREF(result);
			return NULL;
		}

		if (PyList_Append(result, str) == -1) {
			Py_DECREF(result);
			return NULL;
		}

		signature = end;
	}	

	tuple = PyList_AsTuple(result);
	Py_DECREF(result);
	return tuple;
}

PyDoc_STRVAR(PyObjC_loadBundleVariables_doc, 
	"loadBundleVariables(bundle, module_globals, variableInfo, "
	"skip_undefined=True)\n"
	"\n"
	"Load the specified variables in the bundle. If skip_undefined is \n"
	"True, variables that are not present in the bundle are skipped, \n"
	"otherwise this method raises objc.error when a variable cannot be \n"
	"found.\n"
	"\n"
	"variableInfo is a list of (name, type) pairs. The type is the \n"
	"Objective-C type specifier for the variable type.");
PyDoc_STRVAR(PyObjC_loadBundleFunctions_doc,
	"loadBundleFunctions(bundle, module_globals, functionInfo, "
	"skip_undefined=True)\n"
	"\n"
	"Load the specified functions in the bundle. If skip_undefined is \n"
	"True, variables that are not present in the bundle are skipped, \n"
	"otherwise this method raises objc.error when a variable cannot be \n"
	"found.\n"
	"\n"    
	"functionInfo is a list of (name, signature, doc [, methinfo]) triples. \n"
	"The signature is the Objective-C type specifier for the function \n"
	"signature.");
PyDoc_STRVAR(PyObjC_loadFunctionList_doc,
	"PRIVATE!\n"
	"_loadFunctionList(list, module_globals, functionInfo, "
	"skip_undefined=True)\n"
	"\n"
	"Load the specified functions. List should be a CObject contains\n"
	"print an array of { char*, funcion } \"tuples\".");
	


PyDoc_STRVAR(objc_CFToObject_doc,
	"CFToObject(cfObject) -> objCObject\n"
	"\n"
	"Convert a CoreFoundation object to an Objective-C object. \n"
	"Raises an exception if the conversion fails"
);
static PyObject*
objc_CFToObject(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { "value", 0 };
	PyObject* argument;
	id	  res;

	if (!PyArg_ParseTupleAndKeywords(args, kwds,
			"O:CFToObject", keywords,
			&argument)) {
		return NULL;
	}

	res = PyObjC_CFTypeToID(argument);
	if (res == 0) {
		PyErr_SetString(PyExc_TypeError, "not a CoreFoundation object");
		return NULL;
	}

	return pythonify_c_value(@encode(id), &res);
}

PyDoc_STRVAR(objc_ObjectToCF_doc,
	"ObjectToCF(objCObject) -> cfObject\n"
	"\n"
	"Convert an Objective-C object to a CoreFoundation object. \n"
	"Raises an exception if the conversion fails"
);
static PyObject*
objc_ObjectToCF(PyObject* self __attribute__((__unused__)), 
	PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "value", 0 };
	PyObject* argument;

	if (!PyArg_ParseTupleAndKeywords(args, kwds,
			"O:ObjectToCF", keywords,
			&argument)) {
		return NULL;
	}

	if (!PyObjCObject_Check(argument)) {
		PyErr_SetString(PyExc_TypeError, "not an Objective-C object");
		return NULL;
	}

	return PyObjC_IDToCFType(PyObjCObject_GetObject(argument));
}


PyDoc_STRVAR(protocolsForProcess_doc,
	"protocolsForProcess() -> [Protocols]\n"
	"\n"
	"Returns a list of Protocol objects that the class claims\n"
	"to implement directly."
);
static PyObject*
protocolsForProcess(PyObject* self __attribute__((__unused__)))
{
	PyObject *protocols;
	Protocol** protlist;
	unsigned int protCount;
	unsigned int i;

	protlist = objc_copyProtocolList(&protCount);
	if (protlist == NULL) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	protocols = PyList_New(protCount);
	if (protocols == NULL) {
		return NULL;
	}
	for (i = 0; i < protCount; i++) {
		PyObject *p = PyObjCFormalProtocol_ForProtocol(protlist[i]);
		if (p == NULL) {
			Py_DECREF(p);
			free(protlist);
			return NULL;
		}
		PyList_SET_ITEM(protocols, i, p);
	}
	free(protlist);
	return protocols;
}


PyDoc_STRVAR(protocolsForClass_doc,
	"protocolsForClass(cls) -> [Protocols]\n"
	"\n"
	"Returns a list of Protocol objects that the class claims\n"
	"to implement directly."
);
static PyObject*
protocolsForClass(PyObject* self __attribute__((__unused__)),
		PyObject* args,
		PyObject* kwds)
{
	static char* keywords[] = { "cls", NULL };
	Protocol** protocol_list;
	unsigned int protocol_count, i;
	PyObject *protocols;
	Class cls;
	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O&:protocolsForClass", keywords, 
			PyObjCClass_Convert, &cls)) {
		return NULL;
	}
	protocols = PyList_New(0);
	if (protocols == NULL) {
		return NULL;
	}
	protocol_list = class_copyProtocolList(cls, &protocol_count);
	for (i = 0; i < protocol_count; i++) {
		PyObject *protocol = PyObjCFormalProtocol_ForProtocol(protocol_list[i]);
		if (protocol == NULL) {
			free(protocol_list);
			Py_DECREF(protocols);
			return NULL;
		}
		PyList_Append(protocols, protocol);
		Py_DECREF(protocol);
	}
	free(protocol_list);
	return protocols;
}

PyDoc_STRVAR(createOpaquePointerType_doc,
	"createOpaquePointerType(name, typestr, doc) -> type\n"
	"\n"
	"Return a wrapper type for opaque pointers of the given type. The type \n"
	"will be registered with PyObjC and will be used to wrap pointers of the \n"
	"given type."
);
static PyObject*
createOpaquePointerType(PyObject* self __attribute__((__unused__)),
		PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "name", "typestr", "doc", NULL };
	char* name;
	char* typestr;
	char* docstr = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
				"s"Py_ARG_BYTES"|s", 
				keywords, 
				&name, &typestr, &docstr)) {
		return NULL;
	}

	return PyObjCCreateOpaquePointerType(name, typestr, docstr);
}

PyDoc_STRVAR(registerMetaData_doc,
	"registerMetaDataForSelector(class, selector, metaDataList) -> None\n"
	"\n"
	"XXX: work out documentation.");
static PyObject*
registerMetaData(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "class", "selector", "metadata", NULL };

	PyObject* class_name;
	PyObject* selector;
	PyObject* metadata;

	
	if (!PyArg_ParseTupleAndKeywords(args, kwds, "SSO", keywords, 
			&class_name, &selector, &metadata)) {
		return NULL;
	}

	if (PyObjC_registerMetaData(class_name, selector, metadata) < 0) {
		return NULL;
	
	} else {
		Py_INCREF(Py_None);
		return Py_None;
	}
}

PyDoc_STRVAR(registerStructAlias_doc,
	"registerStructAlias(typestr, structType)\n"
	"\n"
	"Registers 'typestr' as a type that should be mapped onto 'structType'\n"
	"'structType' must be created using 'createStructType' (or through \n"
	"a metadata file."
);
static PyObject*
registerStructAlias(PyObject* self __attribute__((__unused__)),
		                PyObject* args, PyObject* kwds)
{
	static char* keywords[] = { "typestr", "structType", NULL };
	char* typestr;
	PyObject* structType;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
				Py_ARG_BYTES "O",
				keywords, &typestr, &structType)) {
		return NULL;
	}

	if (PyObjC_RegisterStructAlias(typestr, structType) == -1) {
		return NULL;
	}
	Py_INCREF(Py_None);
	return Py_None;
}


PyDoc_STRVAR(createStructType_doc,
	"createStructType(name, typestr, fieldnames, doc) -> type\n"
	"\n"
	"Return a wrapper type for structs of the given type. The wrapper will \n"
	"registered with PyObjC and will be used to wrap structs of the given type.\n"
	"The field names can be ``None`` iff the typestr contains field names."
);
static PyObject*
createStructType(PyObject* self __attribute__((__unused__)),
		PyObject* args, PyObject* kwds)
{
static char* keywords[] = { "name", "typestr", "fieldnames", "doc", NULL };
	char* name;
	char* typestr;
	PyObject* pyfieldnames;
	char* docstr = NULL;
	PyObject* retval;
	char** fieldnames = NULL;
	Py_ssize_t i;
	Py_ssize_t field_count;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
				"s"Py_ARG_BYTES"O|s", 
				keywords, 
				&name, &typestr, &pyfieldnames, &docstr)) {
		return NULL;
	}

	name = PyObjCUtil_Strdup(name);
	typestr = PyObjCUtil_Strdup(typestr);
	if (docstr) {
		docstr = PyObjCUtil_Strdup(docstr);
	}

	if (pyfieldnames != Py_None) {
		pyfieldnames = PySequence_Fast(pyfieldnames, 
			"fieldnames must be a sequence of strings");

		if (pyfieldnames == NULL) goto error_cleanup;
		if (name == NULL || typestr == NULL) {
			PyErr_NoMemory();
			goto error_cleanup;
		}

		fieldnames = PyMem_Malloc(sizeof(char*) * PySequence_Fast_GET_SIZE(pyfieldnames));
		if (fieldnames == NULL) {
			PyErr_NoMemory();
			goto error_cleanup;
		}
		memset(fieldnames, 0, 
				sizeof(char*) * PySequence_Fast_GET_SIZE(pyfieldnames));
		for (i = 0; i < PySequence_Fast_GET_SIZE(pyfieldnames); i++) {
			PyObject* v = PySequence_Fast_GET_ITEM(pyfieldnames, i);
			if (PyUnicode_Check(v)) {
				PyObject* bytes = PyUnicode_AsEncodedString(v, NULL, NULL);
				if (bytes == NULL) {
					goto error_cleanup;
				}
				fieldnames[i] = PyObjCUtil_Strdup(PyBytes_AsString(bytes));
				Py_DECREF(bytes);
#if PY_MAJOR_VERSION == 2
			} else if (PyString_Check(v)) {
				fieldnames[i] = PyObjCUtil_Strdup(PyString_AS_STRING(v));
#endif
			} else {
				PyErr_SetString(PyExc_TypeError,
					"fieldnames must be a sequence of strings");
				goto error_cleanup;
			}
			if (fieldnames[i] == NULL) {
				PyErr_NoMemory();
				goto error_cleanup;
			}
		}
		field_count = PySequence_Fast_GET_SIZE(pyfieldnames);
	} else {
		field_count = -1;
		fieldnames = NULL;
	}


	retval = PyObjC_RegisterStructType(typestr, name, docstr, NULL,
			field_count, (const char**)fieldnames);
	if (retval == NULL) goto error_cleanup;
	Py_DECREF(pyfieldnames);

	return retval;

error_cleanup:
	if (name) PyMem_Free(name);
	if (typestr) PyMem_Free(typestr);
	if (docstr) PyMem_Free(docstr);
	if (fieldnames) {
		for (i = 0; i < PySequence_Fast_GET_SIZE(pyfieldnames); i++) {
			if (fieldnames[i]) PyMem_Free(fieldnames[i]);
		}
		PyMem_Free(fieldnames);
	}
	Py_XDECREF(pyfieldnames);

	return NULL;
}

PyDoc_STRVAR(PyObjCIvar_Info_doc, 
	"listInstanceVariables(classOrInstance) -> [ (name, typestr), ... ]\n"
	"\n"
	"Return information about all instance variables of an object or class\n"
);
PyDoc_STRVAR(PyObjCIvar_Get_doc, 
	"getInstanceVariable(object, name) -> value\n"
	"\n"
	"Return the value of an instance variable\n"
);
PyDoc_STRVAR(PyObjCIvar_Set_doc, 
	"setInstanceVariable(object, name, value [, updateRefCount])\n"
	"\n"
	"Modify an instance variable. If the instance variable is an object \n"
	"reference you must include the ``updateRefCount`` argument, otherwise it \n"
	"is ignored. If ``updateRefCount`` is true the reference counts of the \n"
	"old and new values are updated, otherwise they are not.\n"
	"\n"
	"NOTE: updating instance variables is dangerous, instance variables are \n"
	"private in Objective-C and classes might not expected that those values \n"
	"are changed by other code."
);

PyDoc_STRVAR(registerCFSignature_doc,
	"registerCFSignature(name, encoding, typeId [, tollfreeName]) -> type\n"
	"\n"
	"Register a CoreFoundation based type with the bridge. If \n"
	"tollFreeName is supplied the type is tollfree bridged to that class.");
static PyObject*
registerCFSignature(PyObject* self __attribute__((__unused__)),
		PyObject* args, PyObject* kwds)
{
	static char* keywords[] = { "name", "encoding", "typeId", "tollfreeName", NULL };
	char* name;
	char* encoding;
	PyObject* pTypeId;
	CFTypeID typeId;
	char* tollfreeName = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
		"s"Py_ARG_BYTES"O|s",
		keywords, &name, &encoding, &pTypeId, &tollfreeName)) {
		return NULL;
	}

	if (pTypeId == Py_None) {
		if (tollfreeName == NULL) {
			PyErr_SetString(PyExc_ValueError,
				"Must specify a typeid when not toll-free");
			return NULL;
		}
		typeId = (CFTypeID)-1;

	} else if (depythonify_c_value(@encode(CFTypeID), pTypeId, &typeId) == -1) {
		return NULL;

	} else {
		PyObject* v = PyInt_FromLong(typeId);
		int r = PyDict_SetItemString(PyObjC_TypeStr2CFTypeID, encoding, v);
		Py_DECREF(v);
		if (r == -1) {
			return NULL;
		}
	}

	if (tollfreeName) {
		Class cls = objc_lookUpClass(tollfreeName);
		if (cls == nil) {
			PyErr_SetString(PyObjCExc_NoSuchClassError,
					tollfreeName);
			return NULL;
		}
		if (PyObjCPointerWrapper_RegisterID(encoding) == -1) {
			return NULL;
		}

		/* Don't have to do anything with the cfTypeId: because
		 * the type is toll-free bridged automatic conversion will
		 * do the right thing.
		 */

		return PyObjCClass_New(cls);
	} else {
		return PyObjCCFType_New(name, encoding, typeId);
	}

	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(_updatingMetadata_doc,
	"PRIVATE:");
static PyObject*
_updatingMetadata(PyObject* self __attribute__((__unused__)),
		PyObject* args, PyObject* kwds)
{
	static char* keywords[] = { "flag", NULL };
	PyObject* flag;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", keywords, &flag)) {
		return NULL;
	}

	if (PyObject_IsTrue(flag)) {
		PyObjC_UpdatingMetaData = YES;

	} else {
		PyObjC_MappingCount ++;
		PyObjC_UpdatingMetaData = NO;

	}
	
	Py_INCREF(Py_None);
	return Py_None;
}

/* Support for locking */
static PyObject*
PyObjC_objc_sync_enter(PyObject* self __attribute__((__unused__)), PyObject* args)
{
	NSObject* object;
	int rv;

	if (!PyArg_ParseTuple(args, "O&", 
			PyObjCObject_Convert, &object)) {
		return NULL;
	}

	Py_BEGIN_ALLOW_THREADS
		rv = objc_sync_enter(object);
	
	Py_END_ALLOW_THREADS

	if (rv == OBJC_SYNC_SUCCESS) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyErr_Format(PyObjCExc_LockError, "objc_sync_enter failed: %d", rv);
	return NULL;
}

static PyObject*
PyObjC_objc_sync_exit(PyObject* self __attribute__((__unused__)), PyObject* args)
{
	NSObject* object;
	int rv;

	if (!PyArg_ParseTuple(args, "O&", 
			PyObjCObject_Convert, &object)) {
		return NULL;
	}

	Py_BEGIN_ALLOW_THREADS
		rv = objc_sync_exit(object);
	Py_END_ALLOW_THREADS
	if (rv == OBJC_SYNC_SUCCESS) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	PyErr_Format(PyObjCExc_LockError, "objc_sync_exit failed: %d", rv);
	return NULL;
}

PyDoc_STRVAR(parseBridgeSupport_doc,
 "parseBridgeSupport(xmldata, globals, framework [, dylib_path] [, inlineTab]) -> None\n"
 "\n"
 "Process the XML bridgesupport data. Constants and functions will be added\n"
 "to the `globals` dictionary. If `dylib_path` is present and not None it is\n"
 "the filesystem path for a dylib containing static inline definitions.");
static PyObject*
parseBridgeSupport(PyObject* self __attribute__((__unused__)),
		PyObject* args, PyObject* kwds)
{
	static char* keywords[] = { "xmldata", "globals", "framework", "dylib_path", "inlineTab", NULL };
	char* data;
	Py_ssize_t datalen;
	PyObject* globalDict;
	const char* framework;
	const char* dylibPath = NULL;
	PyObject* inlineTab = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "s#O!s|zO", keywords, 
			&data, &datalen, &PyDict_Type, &globalDict, 
			&framework, &dylibPath, &inlineTab)) {
		return NULL;
	}

	int r = PyObjC_ProcessXML(data, datalen, globalDict, dylibPath, framework, inlineTab);
	if (r == -1) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}


PyDoc_STRVAR(_makeClosure_doc,
  "_makeClosure(callable, closureFor, [argIndex]) -> closure\n"
  "\n"
  "Returns a closure object that can be used to call the function from\n"
  "C. This object has no useable interface from Python.\n"
 );
#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION < 7
static void _callback_cleanup(void* closure)
{
	PyObjCFFI_FreeIMP((IMP)closure);
}
#else
static void _callback_cleanup(PyObject* closure)
{
	PyObjCFFI_FreeIMP((IMP)PyCapsule_GetPointer(closure, "objc.__imp__"));
}
#endif

static PyObject*
_makeClosure(
	PyObject* self __attribute__((__unused__)),
	PyObject* args,
	PyObject* kwds)
{
static  char* keywords[] = { "callable", "closureFor", "argIndex", NULL };
	PyObject* callable;
	PyObject* closureFor;
	PyObjCMethodSignature* methinfo;
	Py_ssize_t argIndex;
	Py_ssize_t i;

	argIndex=-1;
	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO|" Py_ARG_SIZE_T ,
		keywords, &callable, &closureFor, &argIndex)) {
		return NULL;
	}

	if (!PyCallable_Check(callable)) {
		PyErr_SetString(PyExc_TypeError, "Callable isn't callable");
		return NULL;
	}

	if (PyObjCFunction_Check(closureFor)) {
		methinfo = (PyObjCMethodSignature*)PyObjCFunc_GetMethodSignature(closureFor);
		if (methinfo == NULL) {
			return NULL;
		}

	} else if (PyObjCSelector_Check(closureFor)) {
		methinfo = ((PyObjCSelector*)closureFor)->sel_methinfo;
		if (methinfo == NULL) {
			PyErr_SetString(PyExc_ValueError,
				"No signature??");
			return NULL;
		}

	} else {
		PyErr_Format(PyExc_TypeError, "Don't know how to create closure for instance of %s", 
				Py_TYPE(closureFor)->tp_name);
		return NULL;
	}

	if (argIndex == -1) {
		for (i = 0; i < Py_SIZE(methinfo); i++) {
			if (methinfo->argtype[i].callable != NULL) {
				argIndex = i;
				break;
			}
		}
		if (argIndex == -1) {
			PyErr_SetString(PyExc_ValueError,
				"No callback argument in the specified object");
			return NULL;
		}

	} else {
		if (argIndex < 0 || argIndex >= Py_SIZE(methinfo)) {
			PyErr_SetString(PyExc_IndexError,
				"No such argument");
			return NULL;
		}
		if (methinfo->argtype[argIndex].callable == NULL) {
			PyErr_Format(PyExc_ValueError,
				"Argument %" PY_FORMAT_SIZE_T "d is not callable", argIndex);
			return NULL;
		}
	}


	PyObjC_callback_function result;

	result = PyObjCFFI_MakeFunctionClosure(methinfo->argtype[argIndex].callable, callable);
	if (result == NULL) {
		return NULL;
	}

	PyObject* retval = PyCapsule_New(
		result, "objc.__imp__", _callback_cleanup);
	if (retval == NULL) {
		PyObjCFFI_FreeIMP((IMP)result);
		return NULL;
	}

	return retval;
}

static PyObject*
ivar_dict(PyObject* self __attribute__((__unused__)))
{
	Py_INCREF(PyObjCInstanceVariable_Type.tp_dict);
	return PyObjCInstanceVariable_Type.tp_dict;
}

PyObject* 
PyObjC_AdjustSelf(PyObject* object)
{
	if (PyType_Check(object) && PyType_IsSubtype((PyTypeObject*)object, &PyObjCClass_Type)) {
		PyObject* temp = PyObjCClass_ClassForMetaClass(object);
		Py_INCREF(temp);
		Py_DECREF(object);
		return temp;
	}
	return object;
}

static PyObject*
mod_propertiesForClass(PyObject* mod __attribute__((__unused__)), PyObject* object)
{
	return PyObjCClass_ListProperties(object);
}

static PyObject* 
mod_setClassSetupHook(PyObject* mod __attribute__((__unused__)), PyObject* hook)
{
	PyObject* curval = PyObjC_class_setup_hook;

	PyObjC_class_setup_hook = hook;
	Py_INCREF(hook);

	return curval;
}

/* 
 * Helper function for decoding XML metadata:
 *
 * This fixes an issue with metadata files: metadata files use
 * _C_BOOL to represent type 'BOOL', but that the string should
 * be used to represent 'bool' which has a different size on
 * PPC. Therefore swap usage of _C_BOOL and _C_NSBOOL in data
 * from metadata files.
 */
static void typecode2typecode(char* buf)
{
	/* Skip pointer declarations and anotations */
	for (;;) {
		switch(*buf) {
		case _C_PTR:
		case _C_IN:
		case _C_OUT:
		case _C_INOUT:
		case _C_ONEWAY:
		case _C_CONST:
			buf++;
			break;
		default:
		      goto exit;
		}
	}
exit:

	switch (*buf) {
	case _C_BOOL:
		*buf = _C_NSBOOL;
		break;
	case _C_NSBOOL:
		*buf = _C_BOOL;
		break;
        case _C_STRUCT_B:
		while (buf && *buf != _C_STRUCT_E && *buf && *buf++ != '=') {
		}
		while (buf && *buf && *buf != _C_STRUCT_E) {
			if (*buf == '"') {
				/* embedded field name */
				buf = strchr(buf+1, '"');
				if (buf == NULL) {
					return;
				}
				buf++;
			}
			typecode2typecode(buf);
			buf = (char*)PyObjCRT_SkipTypeSpec(buf);
		}
		break;
	
	case _C_UNION_B:
		while (buf && *buf != _C_UNION_E && *buf && *buf++ != '=') {
		}
		while (buf && *buf && *buf != _C_UNION_E) {
			if (*buf == '"') {
				/* embedded field name */
				buf = strchr(buf+1, '"');
				if (buf == NULL) {
					return;
				}
				buf++;
			}
			typecode2typecode(buf);
			buf = (char*)PyObjCRT_SkipTypeSpec(buf);
		}
		break;


	case _C_ARY_B:
		while (isdigit(*++buf));
		typecode2typecode(buf);
		break;
	}
}



static PyObject*
typestr2typestr(PyObject* args)
{
	char* s;
	char* buf;

	if (PyUnicode_Check(args)) {
		PyObject* bytes = PyUnicode_AsEncodedString(args, NULL, NULL);
		if (bytes == NULL) {
			return NULL;
		}
		buf = PyObjCUtil_Strdup(PyBytes_AsString(args));
		Py_DECREF(bytes);

	} else if (PyBytes_Check(args)) {
		buf = PyObjCUtil_Strdup(PyBytes_AsString(args));
	} else {
		PyErr_SetString(PyExc_TypeError, "expecing string");
		return NULL;
	}

	
	if (buf == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	s = buf;
	while (s && *s) {
		typecode2typecode(s);
		if (s && *s == '\"') {
			PyErr_Format(PyObjCExc_InternalError,
				"typecode2typecode: invalid typecode '%c' "
				"at \"%s\"", *s, s);
			*s = '\0';
			PyMem_Free(buf);
			return NULL;

		} else {
			s = (char*)PyObjCRT_SkipTypeSpec(s);
		}
	}

	PyObject* result = PyBytes_FromString(buf);
	PyMem_Free(buf);

	return result;
}



static PyObject*
_clear_intern(PyObject* self __attribute__((__unused__)))
{
	PyObjC_ClearIntern();
	Py_INCREF(Py_None);
	return Py_None;
}


static PyMethodDef mod_methods[] = {
	{
		"_setClassSetUpHook",
		(PyCFunction)mod_setClassSetupHook,
		METH_O,
		"Private: set hook used during subclass creation",
	},

	{
		"propertiesForClass",
	  	(PyCFunction)mod_propertiesForClass,
		METH_O,
		"Return information about properties from the runtim",
	},
	{
	  "splitSignature",
	  (PyCFunction)objc_splitSignature,
	  METH_VARARGS|METH_KEYWORDS,
	  objc_splitSignature_doc
	},
	{
	  "splitStruct",
	  (PyCFunction)objc_splitStruct,
	  METH_VARARGS|METH_KEYWORDS,
	  objc_splitStruct_doc,
	},
	{
	  "lookUpClass",
	  (PyCFunction)lookUpClass,
	  METH_VARARGS|METH_KEYWORDS,
	  lookUpClass_doc
	},
	{
	  "classAddMethods",
	  (PyCFunction)classAddMethods,
	  METH_VARARGS|METH_KEYWORDS,
	  classAddMethods_doc
	},
	{ "currentBundle", (PyCFunction)currentBundle, METH_NOARGS, currentBundle_doc },
	{ "getClassList", (PyCFunction)getClassList, METH_NOARGS, getClassList_doc },
	{ "_setClassExtender", (PyCFunction)set_class_extender, METH_VARARGS|METH_KEYWORDS, set_class_extender_doc  },
	{ "setSignatureForSelector", (PyCFunction)set_signature_for_selector, METH_VARARGS|METH_KEYWORDS, set_signature_for_selector_doc },
	{ "recycleAutoreleasePool", (PyCFunction)recycle_autorelease_pool, METH_VARARGS|METH_KEYWORDS, recycle_autorelease_pool_doc },
	{ "removeAutoreleasePool", (PyCFunction)remove_autorelease_pool, METH_VARARGS|METH_KEYWORDS, remove_autorelease_pool_doc },
	{ "_setNSNumberWrapper", (PyCFunction)setNSNumberWrapper, METH_VARARGS|METH_KEYWORDS, setNSNumberWrapper_doc },
	{ "_getNSNumberWrapper", (PyCFunction)getNSNumberWrapper, METH_VARARGS|METH_KEYWORDS, getNSNumberWrapper_doc },
	{ "setVerbose", (PyCFunction)setVerbose, METH_VARARGS|METH_KEYWORDS, setVerbose_doc },
	{ "setUseKVOForSetattr", (PyCFunction)setUseKVOForSetattr, METH_VARARGS|METH_KEYWORDS, setUseKVOForSetattr_doc },
	{ "setHideProtected", (PyCFunction)setHideProtected, METH_VARARGS|METH_KEYWORDS, setHideProtected_doc },
	{ "getVerbose", (PyCFunction)getVerbose, METH_VARARGS|METH_KEYWORDS, getVerbose_doc },
	{ "pyobjc_id", (PyCFunction)pyobjc_id, METH_VARARGS|METH_KEYWORDS, pyobjc_id_doc },
	{ "repythonify", (PyCFunction)repythonify, METH_VARARGS|METH_KEYWORDS, repythonify_doc },
#if PY_MAJOR_VERSION == 2
	{ "setStrBridgeEnabled", (PyCFunction)setStrBridgeEnabled, METH_VARARGS|METH_KEYWORDS, setStrBridgeEnabled_doc },
	{ "getStrBridgeEnabled", (PyCFunction)getStrBridgeEnabled, METH_VARARGS|METH_KEYWORDS, getStrBridgeEnabled_doc },
#endif
	{ "loadBundle", (PyCFunction)loadBundle, METH_VARARGS|METH_KEYWORDS, loadBundle_doc },
	{ "allocateBuffer", (PyCFunction)allocateBuffer, METH_VARARGS|METH_KEYWORDS, allocateBuffer_doc },
	{ "protocolsForClass", (PyCFunction)protocolsForClass, METH_VARARGS|METH_KEYWORDS, protocolsForClass_doc },
	{ "protocolsForProcess", (PyCFunction)protocolsForProcess, METH_NOARGS, protocolsForProcess_doc },
	{ "registerCFSignature", (PyCFunction)registerCFSignature, METH_VARARGS|METH_KEYWORDS, registerCFSignature_doc },
	{ "CFToObject", (PyCFunction)objc_CFToObject, METH_VARARGS|METH_KEYWORDS, objc_CFToObject_doc },
	{ "ObjectToCF", (PyCFunction)objc_ObjectToCF, METH_VARARGS|METH_KEYWORDS, objc_ObjectToCF_doc },
	{ "loadBundleVariables", (PyCFunction)PyObjC_loadBundleVariables,
		METH_VARARGS|METH_KEYWORDS, PyObjC_loadBundleVariables_doc },
	{ "loadSpecialVar", (PyCFunction)PyObjC_loadSpecialVar,
		METH_VARARGS|METH_KEYWORDS, NULL },
	{ "loadBundleFunctions", (PyCFunction)PyObjC_loadBundleFunctions,
		METH_VARARGS|METH_KEYWORDS, PyObjC_loadBundleFunctions_doc },
	{ "_loadFunctionList", (PyCFunction)PyObjC_loadFunctionList,
		METH_VARARGS|METH_KEYWORDS, PyObjC_loadFunctionList_doc },
	{ "listInstanceVariables", (PyCFunction)PyObjCIvar_Info, 
		METH_O, PyObjCIvar_Info_doc },
	{ "getInstanceVariable", (PyCFunction)PyObjCIvar_Get,
		METH_VARARGS|METH_KEYWORDS, PyObjCIvar_Get_doc },
	{ "setInstanceVariable", (PyCFunction)PyObjCIvar_Set,
		METH_VARARGS|METH_KEYWORDS, PyObjCIvar_Set_doc },
	{ "createOpaquePointerType", (PyCFunction)createOpaquePointerType,
		METH_VARARGS|METH_KEYWORDS, createOpaquePointerType_doc },
	{ "createStructType", (PyCFunction)createStructType,
		METH_VARARGS|METH_KEYWORDS, createStructType_doc },
	{ "registerStructAlias", (PyCFunction)registerStructAlias,
		METH_VARARGS|METH_KEYWORDS, registerStructAlias_doc },
	{ "registerMetaDataForSelector", (PyCFunction)registerMetaData,
		METH_VARARGS|METH_KEYWORDS, registerMetaData_doc },
	{ "_updatingMetadata", (PyCFunction)_updatingMetadata,
		METH_VARARGS|METH_KEYWORDS, _updatingMetadata_doc },
	{ "_makeClosure", (PyCFunction)_makeClosure,
		METH_VARARGS|METH_KEYWORDS, _makeClosure_doc },

	{ "_sockaddrFromPython", (PyCFunction)PyObjC_SockAddrFromPython,
		METH_VARARGS, "private function" },
	{ "_sockaddrToPython", (PyCFunction)PyObjC_SockAddrToPython,
		METH_VARARGS, "private function" },
	{ "parseBridgeSupport", (PyCFunction)parseBridgeSupport,
		METH_VARARGS|METH_KEYWORDS, parseBridgeSupport_doc },
	{ "_setSetupCFClasses", (PyCFunction)PyObjC_SetSetupCFClasses, 
		METH_O, "private function" },
	{ "_setStructConvenience", (PyCFunction)PyObjC_SetStructConvenience, 
		METH_O, "private function" },
	{ "_ivar_dict", (PyCFunction)ivar_dict, METH_NOARGS, "private functions" },

	{ "_objc_sync_enter", (PyCFunction)PyObjC_objc_sync_enter,
		METH_VARARGS, "acquire mutex for an object" },
	{ "_objc_sync_exit", (PyCFunction)PyObjC_objc_sync_exit,
		METH_VARARGS, "release mutex for an object" },
	{ "_block_call", (PyCFunction)PyObjCBlock_Call,
		METH_VARARGS,
		"_block_call(block, signature, args, kwds) -> retval" },

	{ "_typestr2typestr", (PyCFunction)typestr2typestr, 
		METH_O, "private function" },

	{ "_clear_intern", (PyCFunction)_clear_intern, METH_NOARGS,  NULL },


	{ 0, 0, 0, 0 } /* sentinel */
};

struct objc_typestr_values {
	char*	name;
	char    value;
} objc_typestr_values [] = {
	{ "_C_ID", _C_ID },
	{ "_C_CLASS", _C_CLASS },
	{ "_C_SEL", _C_SEL },
	{ "_C_CHR", _C_CHR },
	{ "_C_UCHR", _C_UCHR },
	{ "_C_SHT", _C_SHT },
	{ "_C_USHT", _C_USHT },
#ifdef _C_BOOL
	{ "_C_BOOL", _C_BOOL },
#endif
	{ "_C_INT", _C_INT },
	{ "_C_UINT", _C_UINT },
	{ "_C_LNG", _C_LNG },
	{ "_C_ULNG", _C_ULNG },
	{ "_C_LNG_LNG", _C_LNG_LNG },
	{ "_C_ULNG_LNG", _C_ULNG_LNG },
	{ "_C_FLT", _C_FLT },
	{ "_C_DBL", _C_DBL },
	{ "_C_BFLD", _C_BFLD },
	{ "_C_VOID", _C_VOID },                         
	{ "_C_UNDEF", _C_UNDEF },                          
	{ "_C_PTR", _C_PTR },
	{ "_C_CHARPTR", _C_CHARPTR },
	{ "_C_ARY_B", _C_ARY_B },
	{ "_C_ARY_E", _C_ARY_E },
	{ "_C_UNION_B", _C_UNION_B },
	{ "_C_UNION_E", _C_UNION_E },
	{ "_C_STRUCT_B", _C_STRUCT_B },
	{ "_C_STRUCT_E", _C_STRUCT_E },
	{ "_C_CONST", _C_CONST },
	{ "_C_IN", _C_IN },
	{ "_C_INOUT", _C_INOUT },
	{ "_C_OUT", _C_OUT },
	{ "_C_BYCOPY", _C_BYCOPY },
	{ "_C_ONEWAY", _C_ONEWAY },

	/* Compatibility: */
	{ "_C_LNGLNG", _C_LNG_LNG },
	{ "_C_ULNGLNG", _C_ULNG_LNG },

	/* PyObjC specific */
	{ "_C_NSBOOL",	_C_NSBOOL },
	{ "_C_UNICHAR", _C_UNICHAR },
	{ "_C_CHAR_AS_TEXT", _C_CHAR_AS_TEXT },
	{ "_C_CHAR_AS_INT", _C_CHAR_AS_INT },

	{ NULL, 0 }
};



PyObjC_MODULE_INIT(_objc)
{
	PyObject *m, *d, *v;

	PyObjC_SetupRuntimeCompat();
	if (PyErr_Occurred()) {
		PyObjC_INITERROR();
	}

	NSAutoreleasePool *initReleasePool = [[NSAutoreleasePool alloc] init];
	[OC_NSBundleHack installBundleHack];

	PyObjCClass_DefaultModule = PyText_FromString("objc");

	if (PyObjC_InitProxyRegistry() < 0) {
		PyObjC_INITERROR();
	}

	PyObjC_TypeStr2CFTypeID = PyDict_New();
	if (PyObjC_TypeStr2CFTypeID == NULL) {
		PyObjC_INITERROR();
	}

	if (PyObjCBlock_Setup() == -1) {
		PyObjC_INITERROR();
	}


	if (PyType_Ready(&PyObjCClass_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready((PyTypeObject*)&PyObjCObject_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjCSelector_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjCNativeSelector_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjCPythonSelector_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjCInstanceVariable_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjCInformalProtocol_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjCFormalProtocol_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjCUnicode_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjCIMP_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjCMethodAccessor_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjCMethodSignature_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjC_VarList_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjC_FSRefType) < 0) {
		PyObjC_INITERROR();
	}
	if (PyType_Ready(&PyObjC_FSSpecType) < 0) {
		PyObjC_INITERROR();
	}

	PyObjCSuper_Type.tp_doc = PySuper_Type.tp_doc;
	PyObjCSuper_Type.tp_init = PySuper_Type.tp_init;
	PyObjCSuper_Type.tp_alloc = PySuper_Type.tp_alloc;
	PyObjCSuper_Type.tp_new = PySuper_Type.tp_new;
	PyObjCSuper_Type.tp_dealloc = PySuper_Type.tp_dealloc;
	PyObjCSuper_Type.tp_free = PySuper_Type.tp_free;
	PyObjCSuper_Type.tp_traverse = PySuper_Type.tp_traverse;
	if (PyType_Ready(&PyObjCSuper_Type) < 0) {
		PyObjC_INITERROR();
	}

	if (PyObjCCFType_Setup() == -1) {
		PyObjC_INITERROR();
	}
	if (PyObjCXML_Init() == -1) {
		PyObjC_INITERROR();
	}

	m = PyObjC_MODULE_CREATE(_objc);
	if (m == 0) {
		PyObjC_INITERROR();
	}


	d = PyModule_GetDict(m);
	if (d == 0) {
		PyObjC_INITERROR();
	}
	/* use PyDict_SetItemString for the retain, non-heap types can't be dealloc'ed */

	if (PyDict_SetItemString(d, "objc_class", (PyObject*)&PyObjCClass_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "objc_object", (PyObject*)&PyObjCObject_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "pyobjc_unicode", (PyObject*)&PyObjCUnicode_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "selector", (PyObject*)&PyObjCSelector_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "FSRef", (PyObject*)&PyObjC_FSRefType) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "FSSpec", (PyObject*)&PyObjC_FSSpecType) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "ivar", (PyObject*)&PyObjCInstanceVariable_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "informal_protocol", (PyObject*)&PyObjCInformalProtocol_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "formal_protocol", (PyObject*)&PyObjCFormalProtocol_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "varlist", (PyObject*)&PyObjC_VarList_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "function", (PyObject*)&PyObjCFunc_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "IMP", (PyObject*)&PyObjCIMP_Type) < 0) {
		PyObjC_INITERROR();
	}
	if (PyDict_SetItemString(d, "super", (PyObject*)&PyObjCSuper_Type) < 0) {
		PyObjC_INITERROR();
	}

	v = PyObjCInitNULL();
	if (v == NULL) {
		PyObjC_INITERROR();
	}

	if (PyDict_SetItemString(d, "NULL", v) < 0) {
		Py_DECREF(v);
		PyObjC_INITERROR();
	}
	Py_DECREF(v);

	if (PyObjCUtil_Init(m) < 0) {
		PyObjC_INITERROR();
	}
	if (PyObjCAPI_Register(m) < 0) {
		PyObjC_INITERROR();
	}
	if (PyObjCIMP_SetUpMethodWrappers() < 0) {
		PyObjC_INITERROR();
	}

#if PY_MAJOR_VERSION == 2
	PyObjCStrBridgeWarning = PyErr_NewException("objc.PyObjCStrBridgeWarning", PyExc_DeprecationWarning, NULL);
	PyModule_AddObject(m, "PyObjCStrBridgeWarning", PyObjCStrBridgeWarning);
#endif

	{
		struct objc_typestr_values* cur = objc_typestr_values;

		for (; cur->name != NULL; cur ++)  {
			PyObject* t = PyBytes_FromStringAndSize(&cur->value, 1);
			if (t == NULL) {
				PyObjC_INITERROR();
			}
			if (PyModule_AddObject(m, cur->name, t)) {
				PyObjC_INITERROR();
			}
		}
	}

	/* Add _C_CFTYPEID to avoid hardcoding this in our python code */
	if (PyModule_AddObject(m, "_C_CFTYPEID", PyBytes_FromString(@encode(CFTypeID))) < 0) {
		PyObjC_INITERROR();
	}

	/* Likewise for _C_NSInteger and _C_NSUInteger */
	if (PyModule_AddObject(m, "_C_NSInteger", PyBytes_FromString(@encode(NSInteger))) < 0) {
		PyObjC_INITERROR();
	}
	if (PyModule_AddObject(m, "_C_NSUInteger", PyBytes_FromString(@encode(NSUInteger))) < 0) {
		PyObjC_INITERROR();
	}
	if (PyModule_AddObject(m, "_C_CFIndex", PyBytes_FromString(@encode(CFIndex))) < 0) {
		PyObjC_INITERROR();
	}
	if (PyModule_AddObject(m, "_C_CGFloat", PyBytes_FromString(@encode(CGFloat))) < 0) {
		PyObjC_INITERROR();
	}


	if (PyModule_AddIntConstant(m, "_size_sockaddr_ip4", sizeof(struct sockaddr_in)) < 0) {
		PyObjC_INITERROR();
	}
	if (PyModule_AddIntConstant(m, "_size_sockaddr_ip6", sizeof(struct sockaddr_in6)) < 0) {
		PyObjC_INITERROR();
	}


	if (PyModule_AddStringConstant(m, "__version__", OBJC_VERSION) < 0) {
		PyObjC_INITERROR();
	}

	if (PyModule_AddObject(m, "_sockaddr_type", PyBytes_FromString(@encode(struct sockaddr))) < 0) {
		PyObjC_INITERROR();
	}

	PyObjCPointerWrapper_Init();
	PyObjC_InstallAllocHack();

#ifdef MAC_OS_X_VERSION_MAX_ALLOWED
	/* An easy way to check for the MacOS X version we did build for */
	if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_MAX_ALLOWED", MAC_OS_X_VERSION_MAX_ALLOWED) < 0) {
		PyObjC_INITERROR();
	}
#endif /* MAC_OS_X_VERSION_MAX_ALLOWED */

#ifdef MAC_OS_X_VERSION_MIN_REQUIRED
	if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_MIN_REQUIRED", MAC_OS_X_VERSION_MAX_ALLOWED) < 0) {
		PyObjC_INITERROR();
	}
#endif /* MAC_OS_X_VERSION_MIN_REQUIRED */

#ifdef MAC_OS_X_VERSION_10_1
	if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_1", MAC_OS_X_VERSION_10_1) < 0) {
		PyObjC_INITERROR();
	}
#endif /* MAC_OS_X_VERSION_10_1 */

#ifdef MAC_OS_X_VERSION_10_2
	if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_2", MAC_OS_X_VERSION_10_2) < 0) {
		PyObjC_INITERROR();
	}
#endif /* MAC_OS_X_VERSION_10_2 */

#ifdef MAC_OS_X_VERSION_10_3
	if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_3", MAC_OS_X_VERSION_10_3) < 0) {
		PyObjC_INITERROR();
	}
#endif /* MAC_OS_X_VERSION_10_3 */

#ifdef MAC_OS_X_VERSION_10_4
	if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_4", MAC_OS_X_VERSION_10_4) < 0) {
		PyObjC_INITERROR();
	}
#endif /* MAC_OS_X_VERSION_10_4 */

#ifdef MAC_OS_X_VERSION_10_5
	if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_5", MAC_OS_X_VERSION_10_5) < 0) {
		PyObjC_INITERROR();
	}
#endif /* MAC_OS_X_VERSION_10_5 */

#ifdef MAC_OS_X_VERSION_10_6
	if (PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_6", MAC_OS_X_VERSION_10_6) < 0) {
		PyObjC_INITERROR();
	}
#endif /* MAC_OS_X_VERSION_10_6 */

	if (PyModule_AddStringConstant(m, "platform", "MACOSX") < 0) {
		PyObjC_INITERROR();
	}

	PyEval_InitThreads();
	if (![NSThread isMultiThreaded]) {
		[NSThread detachNewThreadSelector:@selector(targetForBecomingMultiThreaded:) toTarget:[OC_NSAutoreleasePoolCollector class] withObject:nil];
	}
	[initReleasePool release];
	/* Allocate an auto-release pool for our own use, this avoids numerous
	 * warnings during startup of a python script.
	 */
	global_release_pool = [[NSAutoreleasePool alloc] init];
	[OC_NSAutoreleasePoolCollector newAutoreleasePool];

#ifndef Py_ARG_BYTES
#error "No Py_ARG_BYTES"
#endif

#ifndef Py_ARG_NSInteger
#error "No Py_ARG_NSInteger"
#endif

#ifndef Py_ARG_NSUInteger
#error "No Py_ARG_NSUInteger"
#endif

	PyObjC_INITDONE();
}
