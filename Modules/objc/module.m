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

PyDoc_STRVAR(objc_lookup_class_doc,
"lookup_class(class_name) -> class\n\
\n\
Search for the named classes in the Objective-C runtime and return it.\n\
Raises noclass_error when the class doesn't exist.\
");

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

static PyObject* 
objc_class_list(PyObject* self)
{
	return ObjC_GetClassList();
}

/*
 * The 'is' operator for wrapped objective-C objects. The 'is' operator 
 * doesn't work here because it compares the wrappers instead of the actual
 * objects.
 * XXX: This is on the todo list, it would be nice if every objective-C object
 *      had at most 1 wrapper.
 */
PyDoc_STRVAR(objc_same_object_doc,
"same_object(obj1, objc2) -> bool\n"
"The 'is' operator for wrapped objective-C objects.");

static PyObject* 
objc_same_object(PyObject* self, PyObject* args, PyObject* kwds)
{
static 	char* keywords[] = { "first", "second", NULL };
	PyObject* first;
	PyObject* second;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OO:same_object",
			keywords, &first, &second)) {
		return NULL;
	}

	if (!ObjCObject_Check(first) && first != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Need two objective-C objects, or None");
		return NULL;
	}
	if (!ObjCObject_Check(second) && second != Py_None) {
		PyErr_SetString(PyExc_TypeError, "Need two objective-C objects, or None");
		return NULL;
	}

	if (first == second) return PyBool_FromLong(1);
	if (first == Py_None || second == Py_None) return PyBool_FromLong(0);

	return PyBool_FromLong(ObjCObject_GetObject(first) == ObjCObject_GetObject(second));
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
	{ "same_object", (PyCFunction)objc_same_object, METH_VARARGS|METH_KEYWORDS, objc_same_object_doc },
	{ "set_signature_for_selector", (PyCFunction)objc_set_signature_for_selector, METH_VARARGS|METH_KEYWORDS, "" },
	{ 0, 0, 0, 0 } /* sentinel */
};

struct objc_typestr_values {
	char*	name;
	char    value;
} objc_typestr_values [] = {
	{ "_C_ID", '@' },
	{ "_C_CLASS", '#' },
	{ "_C_SEL", ':' },
	{ "_C_CHR", 'c' },
	{ "_C_UCHR", 'C' },
	{ "_C_SHT", 's' },
	{ "_C_USHT", 'S' },
	{ "_C_INT", 'i' },
	{ "_C_UINT", 'I' },
	{ "_C_LNG", 'l' },
	{ "_C_ULNG", 'L' },
	{ "_C_FLT", 'f' },
	{ "_C_DBL", 'd' },
	{ "_C_BFLD", 'b' },
	{ "_C_VOID", 'v' },                         
	{ "_C_UNDEF", '?' },                          
	{ "_C_PTR", '^' },
	{ "_C_CHARPTR", '*' },
	{ "_C_ARY_B", '[' },
	{ "_C_ARY_E", ']' },
	{ "_C_UNION_B", '(' },
	{ "_C_UNION_E", ')' },
	{ "_C_STRUCT_B", '{' },
	{ "_C_STRUCT_E", '}' },
	{ "_C_LNGLNG", 'q' },
	{ "_C_ULNGLNG", 'Q' },
	{ "_C_CONST", 'r' },
	{ "_C_IN", 'n' },
	{ "_C_INOUT", 'N' },
	{ "_C_OUT", 'o' },
	{ "_C_BYCOPY", 'O' },
	{ "_C_ONEWAY", 'V' },

	{ NULL, 0 }
};

void init_objc(void)
{
	PyObject *m, *d;

	/* Allocate an auto-release pool for our own use, this avoids numerous
	 * warnings during startup of a python script.
	 */
	[[NSAutoreleasePool alloc] init];

	PyType_Ready(&ObjCClass_Type); 
	PyType_Ready(&ObjCObject_Type);
	PyType_Ready(&ObjCSelector_Type); 
	PyType_Ready(&ObjCNativeSelector_Type);
	PyType_Ready(&ObjCPythonSelector_Type);
	PyType_Ready(&ObjCIvar_Type);

	m = Py_InitModule4("_objc", meta_methods, "metatest-doc", 
			NULL, PYTHON_API_VERSION);
	d = PyModule_GetDict(m);

	PyDict_SetItemString(d, "objc_class", (PyObject*)&ObjCClass_Type);
	PyDict_SetItemString(d, "objc_object", (PyObject*)&ObjCObject_Type);
	PyDict_SetItemString(d, "selector", (PyObject*)&ObjCSelector_Type);
	PyDict_SetItemString(d, "ivar", (PyObject*)&ObjCIvar_Type);

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
}
