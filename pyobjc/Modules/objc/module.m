/*
 * This module implements an extension-class with a custom meta-class.
 *
 * The idea is to use a trick like this to perform our magic tasks with
 * Python subclasses of Objective-C classes.
 */
#include <Python.h>
#include "pyobjc.h"
#include <stddef.h>
#include <Foundation/NSAutoReleasePool.h>
#include "objc_support.h"

NSAutoreleasePool* ObjC_global_release_pool = nil;

PyDoc_STRVAR(objc_lookup_class_doc,
  "lookup_class(class_name) -> class\n"
  "\n"
  "Search for the named classes in the Objective-C runtime and return it.\n"
  "Raises noclass_error when the class doesn't exist.");

static PyObject* 
objc_lookup_class(PyObject* self, PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "class_name", NULL };
	char* class_name = NULL;
	Class objc_class;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "s:lookup_class",
			keywords, &class_name)) {
		return NULL;
	}

	objc_class = objc_lookUpClass(class_name);
	if (objc_class == NULL) {
		PyErr_SetString(objc_noclass_error, class_name);
		return NULL;
	}

	return ObjCClass_New(objc_class);
}

PyDoc_STRVAR(objc_recycle_autorelease_pool_doc,
  "recycle_autorelease_pool()\n"
  "\n"
  "This 'releases' the global autorelease pool and creates a new one.\n"
  "This method is for system use only\n");
static PyObject*
objc_recycle_autorelease_pool(PyObject* self, PyObject* args, PyObject* kwds)
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



static PyObject* 
objc_class_list(PyObject* self)
{
	return ObjC_GetClassList();
}

static PyObject* 
objc_set_signature_for_selector(PyObject* self, PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "class_name", "selector", "signature", NULL };
	char* class_name;
	char* selector;
	char* signature;
	SEL   sel;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "sss:set_signature_for_selector",
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


static PyMethodDef meta_methods[] = {
	{ "lookup_class", (PyCFunction)objc_lookup_class, METH_VARARGS|METH_KEYWORDS, objc_lookup_class_doc },
	{ "class_list", (PyCFunction)objc_class_list, METH_NOARGS, ""},
	{ "set_signature_for_selector", (PyCFunction)objc_set_signature_for_selector, METH_VARARGS|METH_KEYWORDS, "" },
	{ "recycle_autorelease_pool", (PyCFunction)objc_recycle_autorelease_pool, METH_VARARGS|METH_KEYWORDS, objc_recycle_autorelease_pool_doc },
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

void init_objc(void)
{
	PyObject *m, *d;

	/* Allocate an auto-release pool for our own use, this avoids numerous
	 * warnings during startup of a python script.
	 */
	ObjC_global_release_pool = [[NSAutoreleasePool alloc] init];

	PyType_Ready(&ObjCClass_Type); 
	PyType_Ready(&ObjCObject_Type);
	PyType_Ready(&ObjCSelector_Type); 
	PyType_Ready(&ObjCNativeSelector_Type);
	PyType_Ready(&ObjCPythonSelector_Type);
	PyType_Ready(&ObjCIvar_Type);
	PyType_Ready(&ObjCInformalProtocol_Type);

	m = Py_InitModule4("_objc", meta_methods, "metatest-doc", 
			NULL, PYTHON_API_VERSION);
	d = PyModule_GetDict(m);

	PyDict_SetItemString(d, "objc_class", (PyObject*)&ObjCClass_Type);
	PyDict_SetItemString(d, "objc_object", (PyObject*)&ObjCObject_Type);
	PyDict_SetItemString(d, "selector", (PyObject*)&ObjCSelector_Type);
	PyDict_SetItemString(d, "ivar", (PyObject*)&ObjCIvar_Type);
	PyDict_SetItemString(d, "informal_protocol", (PyObject*)&ObjCInformalProtocol_Type);

	convenience_dict = PyDict_New();
	if (convenience_dict == NULL) return;

	Py_INCREF(convenience_dict);
	PyDict_SetItemString(d, "CONVENIENCE_METHODS", convenience_dict);

	allocator_dict = PyDict_New();
	if (allocator_dict == NULL) return;

	Py_INCREF(allocator_dict);
	PyDict_SetItemString(d, "ALLOCATOR_METHODS", allocator_dict);

	if (ObjCUtil_Init(m) < 0) return;
	if (ObjCAPI_Register(d) < 0) return;
	if (ObjC_RegisterStdStubs(&objc_api) < 0) return;

	{
		struct objc_typestr_values* cur = objc_typestr_values;

		for (; cur->name != NULL; cur ++)  {
			PyDict_SetItemString(d, cur->name,
				PyString_FromStringAndSize(&cur->value, 1));
		}
	}

	PyDict_SetItemString(d, "__version__", 
		PyString_FromString(PYOBJC_VERSION));

}
