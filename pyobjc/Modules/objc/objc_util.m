/*
 * Some utility functions...
 *
 * TODO: Documentation
 */

#import <Foundation/NSString.h>
#import <Foundation/NSDictionary.h>
#include "objc_util.h"
#include "pyobjc.h"

PyObject* objc_error;
PyObject* objc_noclass_error;
PyObject* objc_internal_error;


int ObjCUtil_Init(PyObject* module)
{
#define NEW_EXC(identifier, name, base_class) \
	identifier = PyErr_NewException("objc."name, base_class, NULL); \
	if (identifier == NULL) return -1; \
	Py_INCREF(identifier); \
	if (PyModule_AddObject(module, name, identifier) < 0) return -1;

	NEW_EXC(objc_error, "error", NULL);
	NEW_EXC(objc_noclass_error, "nosuchclass_error", objc_error);
	NEW_EXC(objc_internal_error, "internal_error", objc_error);

	return 0;
}

void ObjCErr_Set(PyObject* exc, char* fmt, ...)
{
	char buf[1024];
	va_list ap;
	
	va_start(ap, fmt);
	vsnprintf(buf, sizeof(buf), fmt, ap);
	va_end(ap);

	PyErr_SetString(exc, buf);
}


static PyObject* 
ObjCErr_PyExcForName(const char* value)
{
	/* TODO: This table should be changeable from python */
	if (strcmp(value, "NSRangeException") == 0) {
		return PyExc_IndexError;
	}  else if (strcmp(value, "NSInvalidArgumentException") == 0) {
		return PyExc_ValueError;
	}  else if (strcmp(value, "NSMallocException") == 0) {
		return PyExc_MemoryError;
	} 

	return objc_error;
}
	

void ObjCErr_FromObjC(NSException* localException)
{
	NSDictionary* userInfo;
	PyObject*     dict;
	PyObject*     exception;

	NSLog(@"OBJC EXC: %@", localException);

	exception = ObjCErr_PyExcForName([[localException name] cString]);

	userInfo = [localException userInfo];
	if (userInfo) {
		id val;

		val = [userInfo objectForKey:@"__pyobjc_exc__"];
		if (val) {
			PyObject* exc = [val pyObject];
			PyErr_SetObject((PyObject*)exc->ob_type, exc);
		}
	}

	dict = PyDict_New();
	PyDict_SetItemString(dict, "name", PyString_FromString(
				[[localException name] cString]));
	PyDict_SetItemString(dict, "reason", PyString_FromString(
				[[localException reason] cString]));
	if (userInfo) {
		PyDict_SetItemString(dict, "userInfo",
			ObjCObject_New(userInfo));
	} else {
		Py_INCREF(Py_None);
		PyDict_SetItemString(dict, "userInfo", Py_None);
	}
	PyErr_SetObject(exception, dict);
	Py_DECREF(dict);
	PyErr_Print();
}

void ObjCErr_ToObjC(void)
{
	PyObject* exc = PyErr_Occurred();
	PyObject* repr;
	NSException* val;

	if (exc == NULL) return;

	repr = PyObject_Str(exc);


	printf("--Forwarding python exception:\n");
	PyErr_Print();
	printf("--DONE\n");

	/* TODO: save 'exc' in as userInfo */
	val = [NSException 
		exceptionWithName:@"OC_PythonException"
		reason:[NSString stringWithCString:PyString_AS_STRING(repr)]
		userInfo:nil];

	Py_DECREF(repr);

	[val raise];
}

PyObject* convenience_dict = NULL;

int ObjC_AddConvenienceMethods(Class cls, PyObject* type_dict)
{
	PyObject* values = NULL;
	int       i, len;

	values = PyDict_Values(type_dict);
	if (values == NULL) return -1;

	len = PySequence_Length(values);
	for (i = 0; i < len; i++) {
		PyObject* value;
		PyObject* mapping;

		value = PySequence_GetItem(values, i);
		if (value == NULL) {
			Py_DECREF(values);
			return -1;
		}

		if (!ObjCSelector_Check(value)) {
			Py_DECREF(value);
			continue;
		}

		mapping = PyDict_GetItemString(convenience_dict, 
			(char*)SELNAME(((ObjCSelector*)value)->sel_selector));
		if (mapping == NULL) {
			PyErr_Clear();
			Py_DECREF(value);
			continue;
		}
		Py_DECREF(value);

		if (PyString_Check(mapping)) {
			/* Default mapping */
			int r;
			r = PyDict_SetItem(type_dict, mapping, value);
			if (r < 0) return -1;

			Py_INCREF(mapping);
			Py_INCREF(value);
		} else if (!PySequence_Check(mapping) || PySequence_Length(mapping) != 2) {
			PyErr_SetString(PyExc_RuntimeError,
				"objc.CONVENIENCE_METHODS must contain 2-tuples");
		} else {
			/* (name, imp) */
			PyObject* name;
			PyObject* imp;
			int r;

			name = PySequence_GetItem(mapping, 0);
			imp = PySequence_GetItem(mapping, 1);

			if (name == NULL || imp == NULL) return -1;

			if (imp == Py_None) {
				/* Default mapping */
				r = PyDict_SetItem(type_dict, name, value);

				if (r < 0) return -1;
#if 0
				Py_INCREF(name);
				Py_INCREF(value);
#endif
				Py_INCREF(value);
				Py_DECREF(imp);
			} else {
				r = PyDict_SetItem(type_dict, name, imp);

				if (r < 0) return -1;

#if 0
				Py_INCREF(name);
				Py_INCREF(imp);
#endif
			}
		}
	}

	Py_DECREF(values);
	return 0;
}

char* ObjC_strdup(const char* value)
{
	int len;
	char* result;

	len = strlen(value);
	result = PyMem_Malloc(len+1);
	if (result == NULL) return NULL;

	memcpy(result, value, len);
	result[len] = 0;
	return result;
}

