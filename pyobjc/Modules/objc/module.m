/*
 * This module implements an extension-class with a custom meta-class.
 *
 * The idea is to use a trick like this to perform our magic tasks with
 * Python subclasses of Objective-C classes.
 */
#include "pyobjc.h"
#include <stddef.h>
#import <Foundation/NSAutoreleasePool.h>
#import <Foundation/NSBundle.h>
#import <Foundation/NSProcessInfo.h>
#import <Foundation/NSString.h>
#include "objc_support.h"

#include <ctype.h>

int ObjC_VerboseLevel = 0;
NSAutoreleasePool* ObjC_global_release_pool = nil;
PyObject* PyObjCClass_DefaultModule = NULL;

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
		PyErr_SetString(ObjCExc_noclass_error, class_name);
		return NULL;
	}

	return PyObjCClass_New(objc_class);
}


PyDoc_STRVAR(classAddMethods_doc,
	     "classAddMethods(targetClass, methodsArray)\n"
	     "\n"
	     "Adds methods in methodsArray to class.   The effect is similar to how categories work.   If class already implements a method as defined in methodsArray, the original implementation will be replaced by the implementation from methodsArray.");

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
	struct objc_method_list *methodsToAdd;

	if (!PyArg_ParseTupleAndKeywords(args, keywds, 
			"OO:classAddMethods", kwlist,
			&classObject, &methodsArray)) {
		return NULL;
	}

	targetClass  = PyObjCClass_GetClass(classObject);
	methodCount  = PyList_Size(methodsArray);

	if (methodCount == 0) {
		Py_INCREF(Py_None);
		return Py_None;
	}

	methodsToAdd = objc_allocMethodList(methodCount);
	if (methodsToAdd == NULL) {
		PyErr_NoMemory();
		return NULL;
	}

	methodsToAdd->method_count = methodCount;

	for (methodIndex = 0; methodIndex < methodCount; methodIndex++) {
		PyObject* aMethod = PyList_GetItem(methodsArray, methodIndex);
		struct objc_method *objcMethod;

		/* check
		 * FIXME: We should support functions here, just like with
		 * class definitions.
		 */
		if (!PyObjCSelector_Check(aMethod)) {
			PyErr_SetString(PyExc_TypeError ,
			      "All objects in methodArray must be of type "
			      "<objc.selector>.");
			goto cleanup_and_return_error;
		}

		/* install in methods to add */
		objcMethod = &methodsToAdd->method_list[methodIndex];
		objcMethod->method_name = PyObjCSelector_Selector(aMethod);

		objcMethod->method_types = strdup(PyObjCSelector_Signature(
			aMethod));
		objcMethod->method_imp = ObjC_MakeIMPForPyObjCSelector(
			(PyObjCSelector*)aMethod);
	}

	/* add the methods */
	class_addMethods(targetClass, methodsToAdd);

	/* This one shouldn't be necessary, but we get crashes without 
	 * the next line. The crashes happen when 'targetClass' is a Python
	 * class.
	class_addMethods(targetClass, NULL);
	 */

	Py_INCREF(Py_None);
	return Py_None;

cleanup_and_return_error:
	if (methodsToAdd) free(methodsToAdd);
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

	
	[ObjC_global_release_pool release];
	ObjC_global_release_pool = [[NSAutoreleasePool alloc] init];

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
	Py_XDECREF(ObjC_class_extender);
	ObjC_class_extender = callback;

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

	sel = SELUID(selector);
	
	if (ObjC_SignatureForSelector(class_name, sel, signature) < 0) {
		return NULL;
	}

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

	ObjC_VerboseLevel = PyObject_IsTrue(o);

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

	return PyObjCBool_FromLong(ObjC_VerboseLevel);
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


PyDoc_STRVAR(loadBundle_doc,
	"loadBundle(bundle, module_name, module_globals) -> None\n"
	"\n"
	"Find all classes defined in the 'bundle', set their __module__ to\n"
	"'module_name' and load them into 'module_globals'"
);
static PyObject*
loadBundle(PyObject* self __attribute__((__unused__)), PyObject* args, PyObject* kwds)
{
static  char* keywords[] = { "module_name", "module_globals", "bundle_path", "bundle_identifier", NULL };
	id        bundle;
	id        strval;
	int err;
	PyObject* bundle_identifier = NULL;
	PyObject* bundle_path = NULL;
	PyObject* module_name;
	PyObject* module_globals;
	PyObject* class_list;
	int       len, i;
	PyObject* module_key = NULL;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, 
			"SO|SS:loadBundle",
			keywords, &module_name, &module_globals,
			&bundle_path, &bundle_identifier)) {
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
		err = depythonify_c_value("@", bundle_path, &strval);
		if (err == -1) {
			return NULL;
		}
		bundle = [NSBundle bundleWithPath:strval];
	} else {
		err = depythonify_c_value("@", bundle_identifier, &strval);
		if (err == -1) {
			return NULL;
		}
		bundle = [NSBundle bundleWithIdentifier:strval];
	}

	//NSLog(@"loadBundle %@", strval);

	[bundle load];

	class_list = PyObjC_GetClassList();
	if (class_list == NULL) {	
		return NULL;
	}

	if (module_key == NULL) {
		module_key = PyString_FromString("__module__");
		if (module_key == NULL) {
			Py_DECREF(class_list);
			return NULL;
		}
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
		} else {
			int r, c;
			r = PyObject_Cmp(mod, module_name, &c);
			if (r == -1) {
				PyErr_Clear();
			} else if (c == 0) {
				if (PyDict_SetItemString(module_globals, 
						((PyTypeObject*)item)->tp_name, item) == -1) {
					Py_DECREF(module_key);
					Py_DECREF(class_list);
					return NULL;
				}
				continue;
			}
			r = PyObject_Cmp(mod, PyObjCClass_DefaultModule, &c);
			if (r == -1) {
				PyErr_Clear();
			} else if (c != 0) {
				/* Already assigned to a module, skip 
				 * expensive bundleForClass:
				 */
				continue;
			}
		}

		if ([NSBundle bundleForClass:cls] != bundle) {
			continue;
		}

		/* cls is located in bundle */
		if (PyObject_SetAttr(item, module_key, module_name) == -1) {
			Py_DECREF(module_key);
			Py_DECREF(class_list);
			return NULL;
		}

		if (PyDict_SetItemString(module_globals, 
				((PyTypeObject*)item)->tp_name, item) == -1) {
			Py_DECREF(module_key);
			Py_DECREF(class_list);
			return NULL;
		}
	}
	Py_XDECREF(module_key);
	Py_XDECREF(class_list);

	//NSLog(@"loadBundle %@ DONE", strval);

	Py_INCREF(Py_None);
	return Py_None;
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

	return pythonify_c_value("@", &res);
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


#endif /* MACOSX */

	



static PyMethodDef meta_methods[] = {
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
	{ "getClassList", (PyCFunction)getClassList, METH_NOARGS, getClassList_doc },
	{ "setClassExtender", (PyCFunction)set_class_extender, METH_VARARGS|METH_KEYWORDS, set_class_extender_doc  },
	{ "setSignatureForSelector", (PyCFunction)set_signature_for_selector, METH_VARARGS|METH_KEYWORDS, set_signature_for_selector_doc },
	{ "recyleAutoreleasePool", (PyCFunction)recycle_autorelease_pool, METH_VARARGS|METH_KEYWORDS, recycle_autorelease_pool_doc },
	{ "setVerbose", (PyCFunction)setVerbose, METH_VARARGS|METH_KEYWORDS, setVerbose_doc },
	{ "getVerbose", (PyCFunction)getVerbose, METH_VARARGS|METH_KEYWORDS, getVerbose_doc },
	{ "loadBundle", (PyCFunction)loadBundle, METH_VARARGS|METH_KEYWORDS, loadBundle_doc },
	{ "allocateBuffer", (PyCFunction)allocateBuffer, METH_VARARGS|METH_KEYWORDS, allocateBuffer_doc },

#ifdef MACOSX
	{ "CFToObject", (PyCFunction)objc_CFToObject, METH_VARARGS, objc_CFToObject_doc },
	{ "ObjectToCF", (PyCFunction)objc_ObjectToCF, METH_VARARGS, objc_ObjectToCF_doc },
#endif

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

void init_objc(void)
{
	PyObject *m, *d;

	//NSLog(@"initobjc");

	/* Allocate an auto-release pool for our own use, this avoids numerous
	 * warnings during startup of a python script.
	 */
	ObjC_global_release_pool = [[NSAutoreleasePool alloc] init];

	PyObjCClass_DefaultModule = PyString_FromString("objc");

	PyType_Ready(&PyObjCClass_Type); 
	PyType_Ready((PyTypeObject*)&PyObjCObject_Type);
	PyType_Ready(&PyObjCSelector_Type); 
	PyType_Ready(&ObjCNativeSelector_Type);
	PyType_Ready(&ObjCPythonSelector_Type);
	PyType_Ready(&PyObjCInstanceVariable_Type);
	PyType_Ready(&PyObjCInformalProtocol_Type);
	PyType_Ready(&PyObjCUnicode_Type);

	m = Py_InitModule4("_objc", meta_methods, NULL,
			NULL, PYTHON_API_VERSION);
	d = PyModule_GetDict(m);

	PyDict_SetItemString(d, "objc_class", (PyObject*)&PyObjCClass_Type);
	PyDict_SetItemString(d, "objc_object", (PyObject*)&PyObjCObject_Type);
	PyDict_SetItemString(d, "pyobjc_unicode", (PyObject*)&PyObjCUnicode_Type);
	PyDict_SetItemString(d, "selector", (PyObject*)&PyObjCSelector_Type);
	PyDict_SetItemString(d, "ivar", (PyObject*)&PyObjCInstanceVariable_Type);
	PyDict_SetItemString(d, "informal_protocol", (PyObject*)&PyObjCInformalProtocol_Type);
	PyDict_SetItemString(d, "YES", PyObjCBool_FromLong(1));
	PyDict_SetItemString(d, "NO", PyObjCBool_FromLong(0));

	if (ObjCUtil_Init(m) < 0) return;
	if (ObjCAPI_Register(d) < 0) return;

	{
		struct objc_typestr_values* cur = objc_typestr_values;

		for (; cur->name != NULL; cur ++)  {
			PyDict_SetItemString(d, cur->name,
				PyString_FromStringAndSize(&cur->value, 1));
		}
	}
	/* Add a _C_BOOL value, the actual type might vary acros platforms */
	PyDict_SetItemString(d, "_C_BOOL", PyString_FromString(@encode(BOOL)));

	PyDict_SetItemString(d, "__version__", 
		PyString_FromString(OBJC_VERSION));

	PyObjCPointerWrapper_Init();
	PyObjC_InstallAllocHack();
}
