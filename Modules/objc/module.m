/*
 * The module entry point for ``_objc``. This file contains ``init_objc``
 * and the implementation of a number of exported functions.
 */
#include "pyobjc.h"
#include "OC_NSBundleHack.h"
#include <objc/Protocol.h>

#include <stddef.h>
#include <ctype.h>

#import <Foundation/NSAutoreleasePool.h>
#import <Foundation/NSBundle.h>
#import <Foundation/NSProcessInfo.h>
#import <Foundation/NSString.h>

#ifdef MACOSX

#include <AvailabilityMacros.h>
#include <mach-o/dyld.h>
#include <pthread.h>
#include "mach_inject.h"

#define PYJECT_MACH_THREAD_STACK_SIZE 64 * 1024
#define PYJECT_PTHREAD_STACK_SIZE 188 * 1024
#define PYJECT_LINKOPTIONS (NSLINKMODULE_OPTION_BINDNOW | \
	NSLINKMODULE_OPTION_RETURN_ON_ERROR | \
	NSLINKMODULE_OPTION_PRIVATE)

#endif /* MACOSX */

int PyObjC_VerboseLevel = 0;
PyObject* PyObjCClass_DefaultModule = NULL;
PyObject* PyObjC_NSNumberWrapper = NULL;
int PyObjC_StrBridgeEnabled = 1;

static NSAutoreleasePool* global_release_pool = nil;

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
	int size;
	PyObject *o;
	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O|s:repythonify",
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

	objc_class = PyObjCRT_LookUpClass(class_name);
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
	Class targetClass;
	int methodCount;
	int methodIndex;
	int r;
	struct objc_method_list *methodsToAdd;
	struct objc_method_list *classMethodsToAdd;
	PyObject* extraDict = NULL;

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
	
	targetClass  = PyObjCClass_GetClass(classObject);
	methodCount  = PySequence_Fast_GET_SIZE(methodsArray);

	if (methodCount == 0) {
		Py_INCREF(Py_None);
		return Py_None;
	}
	
	extraDict = PyDict_New();
	if (extraDict == NULL) {
		return NULL;
	}

	methodsToAdd = PyObjCRT_AllocMethodList(methodCount);
	if (methodsToAdd == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	classMethodsToAdd = PyObjCRT_AllocMethodList(methodCount);
	if (classMethodsToAdd == NULL) {
		free(methodsToAdd);
		PyErr_NoMemory();
		return NULL;
	}

	methodsToAdd->method_count = 0;
	classMethodsToAdd->method_count = 0;


	for (methodIndex = 0; methodIndex < methodCount; methodIndex++) {
		PyObject* aMethod = PySequence_Fast_GET_ITEM(
				methodsArray, methodIndex);
		PyObject* name;
		struct objc_method *objcMethod;

		aMethod = PyObjCSelector_FromFunction(
			NULL,
			aMethod,
			classObject,
			NULL);
		if (aMethod == NULL) {
			PyErr_SetString(PyExc_TypeError ,
			      "All objects in methodArray must be of "
			      "type <objc.selector>, <function>, "
			      " <method> or <classmethod>");
			goto cleanup_and_return_error;
		}

		/* install in methods to add */
		if (PyObjCSelector_IsClassMethod(aMethod)) {
			objcMethod = &classMethodsToAdd->method_list[
				classMethodsToAdd->method_count++];
		} else {
			objcMethod = &methodsToAdd->method_list[
				methodsToAdd->method_count++];
		}
		
		objcMethod->method_name = PyObjCSelector_GetSelector(aMethod);
		objcMethod->method_types = strdup(
				PyObjCSelector_Signature(aMethod));
		if (objcMethod->method_types == NULL) {
			goto cleanup_and_return_error;
		}
		objcMethod->method_imp = PyObjCFFI_MakeIMPForPyObjCSelector(
			(PyObjCSelector*)aMethod);
		
		name = PyObject_GetAttrString(aMethod, "__name__");
		r = PyDict_SetItem(extraDict, name, aMethod);
		Py_DECREF(name); name = NULL;
		Py_DECREF(aMethod); aMethod = NULL;
		if (r == -1) {
			goto cleanup_and_return_error;
		}
	}

	/* add the methods */
	if (methodsToAdd->method_count != 0) {
		PyObjCRT_ClassAddMethodList(targetClass, methodsToAdd);
	} else {
		free(methodsToAdd);
	}
	if (classMethodsToAdd->method_count != 0) {
		PyObjCRT_ClassAddMethodList(GETISA(targetClass),
				classMethodsToAdd);
	} else {
		free(classMethodsToAdd);
	}


	r = PyDict_Merge(((PyTypeObject*)classObject)->tp_dict, extraDict, 1);
	if (r == -1) goto cleanup_and_return_error;

	Py_DECREF(extraDict); extraDict = NULL;

	Py_INCREF(Py_None);
	return Py_None;

cleanup_and_return_error:
	if (extraDict) {
		Py_DECREF(extraDict);
	}
	if (methodsToAdd) free(methodsToAdd);
	if (classMethodsToAdd) free(classMethodsToAdd);
	return NULL;
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

	PyObjC_DURING
		[global_release_pool release];
		global_release_pool = [[NSAutoreleasePool alloc] init];
	PyObjC_HANDLER
		PyObjCErr_FromObjC(localException);
	PyObjC_ENDHANDLER

	if (PyErr_Occurred()) return NULL;

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

	sel = PyObjCRT_SELUID(selector);
	
	if (ObjC_SignatureForSelector(class_name, sel, signature) < 0) {
		return NULL;
	}

	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(setNSNumberWrapper_doc,
	"setNSNumberWrapper(wrapper) -> None\n"
	"\n"
	"Set the NSNumber wrapper function to the new value."
);
static PyObject* 
setNSNumberWrapper(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "wrapper", NULL };
	PyObject* o;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "O:setNSNumberWrapper",
			keywords, &o)) {
		return NULL;
	}

	Py_XDECREF(PyObjC_NSNumberWrapper);
	Py_INCREF(o);
	PyObjC_NSNumberWrapper = o;

	Py_INCREF(Py_None);
	return Py_None;
}

PyDoc_STRVAR(getNSNumberWrapper_doc,
	"getNSNumberWrapper() -> wrapper\n"
	"\n"
	"Return the verbosity value."
);
static PyObject* 
getNSNumberWrapper(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { NULL };

	if (!PyArg_ParseTupleAndKeywords(args, kwds, ":getNSNumberWrapper",
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
	int length;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "i", keywords, &length)) {
		return NULL;
	}

	if (length <= 0 ) {
		PyErr_SetString(PyExc_ValueError, 
			"Length must be greater than 0.");
		return NULL;
	}

	return PyBuffer_New(length);
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
static  char* keywords[] = { "module_name", "module_globals", "bundle_path", "bundle_identifier", NULL };
	NSBundle* bundle = nil;
	id bundle_identifier = nil;
	id bundle_path = nil;
	PyObject* module_name;
	PyObject* module_globals;
	PyObject* class_list;
	int       len, i;
	PyObject* module_key = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"SO|O&O&:loadBundle",
			keywords, &module_name, &module_globals,
            PyObjCObject_Convert, &bundle_path, PyObjCObject_Convert, &bundle_identifier)) {
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
#ifdef MACOSX
		if (![bundle_identifier isKindOfClass:[NSString class]]) {
			PyErr_SetString(PyExc_TypeError,
					"bundle_identifier is not a string");
			return NULL;
        }
		bundle = [NSBundle bundleWithIdentifier:bundle_identifier];
#else  /* !MACOSX */
		/* GNUstep doesn't seem to support ``bundleWithIdentifier:``
           but it could be emulated by enumerating allFrameworks and
           allBundles.. */
		PyErr_SetString(PyExc_RuntimeError,
			"The 'bundle_identifier' argument is only supported "
			"on MacOS X");
		return NULL;

#endif /* !MACOSX */
	}

	if (![bundle load]) {
		PyErr_SetString(PyExc_ImportError,
			"Bundle could not be loaded");
		return NULL;
	}

	class_list = PyObjC_GetClassList();
	if (class_list == NULL) {	
		return NULL;
	}

	module_key = PyString_FromString("__module__");
	if (module_key == NULL) {
		Py_DECREF(class_list);
		return NULL;
	}

	len = PyTuple_GET_SIZE(class_list);
	for (i = 0; i < len; i++) {
		PyObject* item;
		PyObject* mod;
		Class     cls;

		item = PyTuple_GET_ITEM(class_list, i);
		if (item == NULL) {
			continue;
		}

		cls = PyObjCClass_GetClass(item);
		if (cls == nil) {
			PyErr_Clear();
			continue;
		}

		mod = PyObject_GetAttr(item, module_key);
		if (mod == NULL) {
			PyErr_Clear();
			/* cls has just been loaded */
			if (PyObject_SetAttr(item, module_key, module_name) == -1) {
				Py_DECREF(module_key); module_key = NULL;
				Py_DECREF(class_list); class_list = NULL;
				return NULL;
			}
		}
		
		if (((PyTypeObject*)item)->tp_name[0] == '%') {
			/* skip, posed-as type */
		} else if (PyDict_SetItemString(module_globals, 
				((PyTypeObject*)item)->tp_name, item) == -1) {
			Py_DECREF(module_key); module_key = NULL;
			Py_DECREF(class_list); class_list = NULL;
			return NULL;
		}
	}
	Py_XDECREF(module_key); module_key = NULL;
	Py_XDECREF(class_list); class_list = NULL;

	return PyObjC_IdToPython(bundle);
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
			"s:splitSignature",
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

		str = PyString_FromStringAndSize(signature, t - signature);
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

#ifdef MACOSX

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
	"variableInfo is a list of (name, signature, doc) triples. \n"
	"The signature is the Objective-C type specifier for the function \n"
	"signature.");

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

#ifdef MAC_OS_X_VERSION_10_3
#if MAC_OS_X_VERSION_MAX_ALLOWED <= MAC_OS_X_VERSION_10_3
static void *
pyject_pthread_entry_point(void *param) {
	char *pathname = (char *)param;
	NSObjectFileImageReturnCode rc;
	NSObjectFileImage image;
	NSModule newModule;
	const char *errString;
	char errBuf[512];

	rc = NSCreateObjectFileImageFromFile(pathname, &image);
	switch(rc) {
		default:
		case NSObjectFileImageFailure:
		case NSObjectFileImageFormat:
			/* for these a message is printed on stderr by dyld */
			errString = "Can't create object file image";
		break;
		case NSObjectFileImageSuccess:
			errString = NULL;
			break;
		case NSObjectFileImageInappropriateFile:
			errString = "Inappropriate file type for dynamic loading";
			break;
		case NSObjectFileImageArch:
			errString = "Wrong CPU type in object file";
			break;
		case NSObjectFileImageAccess:
			errString = "Can't read object file (no access)";
			break;
	}
	if (errString == NULL) {
		newModule = NSLinkModule(image, pathname, PYJECT_LINKOPTIONS);
		if (newModule == NULL) {
			int errNo;
			const char *fileName, *moreErrorStr;
			NSLinkEditErrors c;
			NSLinkEditError( &c, &errNo, &fileName, &moreErrorStr );
			snprintf(errBuf, sizeof(errBuf), "Failure linking new module: %s: %s",
					fileName, moreErrorStr);
			errString = errBuf;
		}
	}
	if (errString) {
		printf("%s\n", errString);
	}
	return NULL;
}

static void
pyject_mach_entry_point(ptrdiff_t codeOffset, void *paramBlock, size_t paramSize __attribute__((__unused__))) {
	pthread_attr_t attr;
	pthread_t tid;
	pthread_attr_init(&attr);
	pthread_attr_setscope(&attr, PTHREAD_SCOPE_SYSTEM);
	pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);
	pthread_attr_setstacksize(&attr, PYJECT_PTHREAD_STACK_SIZE);
	pthread_create(&tid, &attr, (void*)((char*)&pyject_pthread_entry_point+codeOffset), (void *)paramBlock);
	pthread_attr_destroy(&attr);
	while (1) {
		sleep(3600);
	}
}

PyDoc_STRVAR(inject_doc,
"inject(pid, bundle)\n"
"\n"
"Loads the given MH_BUNDLE in the target process identified by pid\n");

static PyObject*
pyject_inject(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds) {
	static char *keywords[] = { "pid", "bundle", NULL };
	int pid;
	char *bundle;
	mach_error_t e;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "is:inject", keywords, &pid, &bundle)) {
		return NULL;
	}

	e = mach_inject(&pyject_mach_entry_point, bundle, strlen(bundle), pid, PYJECT_MACH_THREAD_STACK_SIZE);

	Py_INCREF(Py_None);
	return Py_None;
}

#endif /* MAC_OS_X_VERSION_MAX_ALLOWED <= MAC_OS_X_VERSION_10_3 */
#endif /* MAC_OS_X_VERSION_10_3 */
#endif /* MACOSX */


PyDoc_STRVAR(enableThreading_doc,
	"enableThreading() -> None\n"
	"\n"
	"This sets the interpreter up for multithreading (if that hasn't\n"
	"been done yet). This makes it possible to use the Cocoa threading\n"
	"API's to create new threads, even when those threads will run\n"
	"python code.");

static PyObject*
enableThreading(PyObject* self __attribute__((__unused__)))
{
	PyEval_InitThreads();
	Py_INCREF(Py_None);
	return Py_None;
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
	struct objc_protocol_list *protocol_list;
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
	protocol_list = cls->protocols;
	while (protocol_list != NULL) {
		int i;
		for (i = 0; i < protocol_list->count; i++) {
			PyObject *protocol = PyObjCObject_NewClassic(protocol_list->list[i]);
			if (protocol == NULL) {
				Py_DECREF(protocols);
				return NULL;
			}
			PyList_Append(protocols, protocol);
			Py_DECREF(protocol);
		}
		protocol_list = protocol_list->next;
	}
	return protocols;
}


static PyMethodDef mod_methods[] = {
	{
	  "splitSignature",
	  (PyCFunction)objc_splitSignature,
	  METH_VARARGS|METH_KEYWORDS,
	  objc_splitSignature_doc
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
	{ "setClassExtender", (PyCFunction)set_class_extender, METH_VARARGS|METH_KEYWORDS, set_class_extender_doc  },
	{ "setSignatureForSelector", (PyCFunction)set_signature_for_selector, METH_VARARGS|METH_KEYWORDS, set_signature_for_selector_doc },
	{ "recycleAutoreleasePool", (PyCFunction)recycle_autorelease_pool, METH_VARARGS|METH_KEYWORDS, recycle_autorelease_pool_doc },
	{ "setNSNumberWrapper", (PyCFunction)setNSNumberWrapper, METH_VARARGS|METH_KEYWORDS, setNSNumberWrapper_doc },
	{ "getNSNumberWrapper", (PyCFunction)getNSNumberWrapper, METH_VARARGS|METH_KEYWORDS, getNSNumberWrapper_doc },
	{ "setVerbose", (PyCFunction)setVerbose, METH_VARARGS|METH_KEYWORDS, setVerbose_doc },
	{ "getVerbose", (PyCFunction)getVerbose, METH_VARARGS|METH_KEYWORDS, getVerbose_doc },
	{ "repythonify", (PyCFunction)repythonify, METH_VARARGS|METH_KEYWORDS, repythonify_doc },
	{ "setStrBridgeEnabled", (PyCFunction)setStrBridgeEnabled, METH_VARARGS|METH_KEYWORDS, setStrBridgeEnabled_doc },
	{ "getStrBridgeEnabled", (PyCFunction)getStrBridgeEnabled, METH_VARARGS|METH_KEYWORDS, getStrBridgeEnabled_doc },
	{ "loadBundle", (PyCFunction)loadBundle, METH_VARARGS|METH_KEYWORDS, loadBundle_doc },
	{ "allocateBuffer", (PyCFunction)allocateBuffer, METH_VARARGS|METH_KEYWORDS, allocateBuffer_doc },
	{ "enableThreading", (PyCFunction)enableThreading, METH_NOARGS, enableThreading_doc },
	{ "protocolsForClass", (PyCFunction)protocolsForClass, METH_VARARGS|METH_KEYWORDS, protocolsForClass_doc },
#ifdef MACOSX
	{ "CFToObject", (PyCFunction)objc_CFToObject, METH_VARARGS|METH_KEYWORDS, objc_CFToObject_doc },
	{ "ObjectToCF", (PyCFunction)objc_ObjectToCF, METH_VARARGS|METH_KEYWORDS, objc_ObjectToCF_doc },
	{ "loadBundleVariables", (PyCFunction)PyObjC_loadBundleVariables,
		METH_VARARGS|METH_KEYWORDS, PyObjC_loadBundleVariables_doc },
	{ "loadBundleFunctions", (PyCFunction)PyObjC_loadBundleFunctions,
		METH_VARARGS|METH_KEYWORDS, PyObjC_loadBundleFunctions_doc },
#if MAC_OS_X_VERSION_MAX_ALLOWED <= MAC_OS_X_VERSION_10_3
	{ "inject", (PyCFunction)pyject_inject, METH_VARARGS|METH_KEYWORDS, inject_doc },
#endif /* MAC_OS_X_VERSION_MAX_ALLOWED <= MAC_OS_X_VERSION_10_3 */
#endif /* MACOSX */

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
	{ "_C_LNGLNG", _C_LNGLNG },
	{ "_C_ULNGLNG", _C_ULNGLNG },
	{ "_C_CONST", _C_CONST },
	{ "_C_IN", _C_IN },
	{ "_C_INOUT", _C_INOUT },
	{ "_C_OUT", _C_OUT },
	{ "_C_BYCOPY", _C_BYCOPY },
	{ "_C_ONEWAY", _C_ONEWAY },

	{ NULL, 0 }
};


void init_objc(void);

void 
init_objc(void)
{
	PyObject *m, *d;

	/* Allocate an auto-release pool for our own use, this avoids numerous
	 * warnings during startup of a python script.
	 */
	global_release_pool = [[NSAutoreleasePool alloc] init];
	[OC_NSBundleHack installBundleHack];

	PyObjCClass_DefaultModule = PyString_FromString("objc");

	if (PyObjC_InitProxyRegistry() < 0) {
		return;
	}

	PyType_Ready(&PyObjCClass_Type); 
	PyType_Ready((PyTypeObject*)&PyObjCObject_Type);
	PyType_Ready(&PyObjCSelector_Type); 
	PyType_Ready(&PyObjCNativeSelector_Type);
	PyType_Ready(&PyObjCPythonSelector_Type);
	PyType_Ready(&PyObjCInstanceVariable_Type);
	PyType_Ready(&PyObjCInformalProtocol_Type);
	PyType_Ready(&PyObjCUnicode_Type);
	PyType_Ready(&PyObjCInformalProtocol_Type);
	PyType_Ready(&PyObjCIMP_Type);
	PyType_Ready(&PyObjCMethodAccessor_Type);
	PyType_Ready(&PyObjCZoneWrapper_Type);

	m = Py_InitModule4("_objc", mod_methods, NULL,
			NULL, PYTHON_API_VERSION);

    d = PyModule_GetDict(m);
    /* use PyDict_SetItemString for the retain, non-heap types can't be dealloc'ed */
	PyDict_SetItemString(d, "objc_class", (PyObject*)&PyObjCClass_Type);
	PyDict_SetItemString(d, "objc_object", (PyObject*)&PyObjCObject_Type);
	PyDict_SetItemString(d, "pyobjc_unicode", (PyObject*)&PyObjCUnicode_Type);
	PyDict_SetItemString(d, "selector", (PyObject*)&PyObjCSelector_Type);
	PyDict_SetItemString(d, "ivar", (PyObject*)&PyObjCInstanceVariable_Type);
	PyDict_SetItemString(d, "informal_protocol", (PyObject*)&PyObjCInformalProtocol_Type);
	PyDict_SetItemString(d, "function", (PyObject*)&PyObjCFunc_Type);
	PyDict_SetItemString(d, "IMP", (PyObject*)&PyObjCIMP_Type);

	if (PyObjCUtil_Init(m) < 0) return;
	if (PyObjCAPI_Register(m) < 0) return;
	if (PyObjCIMP_SetUpMethodWrappers() < 0) return;

#if 1
	/* Python based plugin bundles currently use only PyObjClass_GetClass,
	 * add that seperately to avoid distributing pyobjc-api.h for now 
	 */
	{
		PyObject* v = PyCObject_FromVoidPtr((void*)(PyObjCClass_GetClass), NULL);
		if (v == NULL) return;

		PyModule_AddObject(m, "__C_GETCLASS__", v);
	}
#endif

	{
		struct objc_typestr_values* cur = objc_typestr_values;

		for (; cur->name != NULL; cur ++)  {
			PyModule_AddObject(m, cur->name,
				PyString_FromStringAndSize(&cur->value, 1));
		}
	}
	/* Add a _C_NSBOOL value, the actual type might vary acros platforms */
	PyModule_AddStringConstant(m, "_C_NSBOOL", @encode(BOOL));

	PyModule_AddStringConstant(m, "__version__", OBJC_VERSION);

	PyObjCPointerWrapper_Init();
	PyObjC_InstallAllocHack();

#ifdef MAC_OS_X_VERSION_MAX_ALLOWED
	/* An easy way to check for the MacOS X version we did build for */
	PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_MAX_ALLOWED", MAC_OS_X_VERSION_MAX_ALLOWED);
#endif /* MAC_OS_X_VERSION_MAX_ALLOWED */

#ifdef MAC_OS_X_VERSION_10_1
	PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_1", MAC_OS_X_VERSION_10_1);
#endif /* MAC_OS_X_VERSION_10_1 */

#ifdef MAC_OS_X_VERSION_10_2
	PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_2", MAC_OS_X_VERSION_10_2);
#endif /* MAC_OS_X_VERSION_10_2 */

#ifdef MAC_OS_X_VERSION_10_3
	PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_3", MAC_OS_X_VERSION_10_3);
#endif /* MAC_OS_X_VERSION_10_3 */

#ifdef MAC_OS_X_VERSION_10_4
	PyModule_AddIntConstant(m, "MAC_OS_X_VERSION_10_4", MAC_OS_X_VERSION_10_4);
#endif /* MAC_OS_X_VERSION_10_4 */

#ifdef MACOSX
	PyModule_AddStringConstant(m, "platform", "MACOSX");
#else
	PyModule_AddStringConstant(m, "platform", "GNUSTEP");
#endif /* MACOSX */

	PyEval_InitThreads();
}
