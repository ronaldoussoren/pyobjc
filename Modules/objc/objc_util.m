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
	PyObject*     v;
	char          buf[128];
	PyObject*     exc_type;
	PyObject*     exc_value;
	PyObject*     exc_traceback;

	exception = ObjCErr_PyExcForName([[localException name] cString]);

	userInfo = [localException userInfo];
	if (userInfo) {
		id val;

		val = [userInfo objectForKey:@"__pyobjc_exc__"];
		if (val) {
			PyObject* exc = [val pyObject];

			/* Create a new exception */
			if (PyInstance_Check(exc)) {
				PyErr_SetNone(
					(PyObject*)
					((PyInstanceObject*)exc)->in_class);
			} else {
				PyErr_SetNone((PyObject*)exc->ob_type);
			}

			/* And now replace the actual exception object by
			 * the object in 'userInfo'
			 */
			Py_INCREF(exc);
			PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);
			PyErr_Restore(exc_type, exc , exc_traceback);
			Py_XDECREF(exc_value);
			return;
		}
	}

	dict = PyDict_New();
	v = PyString_FromString([[localException name] cString]);
	PyDict_SetItemString(dict, "name", v);
	Py_DECREF(v);
	PyDict_SetItemString(dict, "reason",  v);
	Py_DECREF(v);
	if (userInfo) {
		v = ObjCObject_New(userInfo);
		if (v == NULL) {
			PyErr_Print();
			abort();
		}
		PyDict_SetItemString(dict, "userInfo", v);
		Py_DECREF(v);
	} else {
		PyDict_SetItemString(dict, "userInfo", Py_None);
	}

	snprintf(buf, sizeof(buf), "%s - %s", 
		[[localException name] cString],
		[[localException reason] cString]);

	PyErr_SetObject(exception, PyString_FromString(buf));
	PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);
	if (!exc_value || !PyObject_IsInstance(exc_value, exc_type)) {
		PyErr_NormalizeException(&exc_type, &exc_value, &exc_traceback);
	}
	PyObject_SetAttrString(exc_value, "_pyobjc_info_", dict);
	PyObject_SetAttrString(exc_value, "name", PyString_FromString(
		[[localException name] cString]));
#if 0	
	Py_DECREF(dict);
#endif
	PyErr_Restore(exc_type, exc_value, exc_traceback);
}

void ObjCErr_ToObjC(void)
{
	PyObject* exc_type;
	PyObject* exc_value;
	PyObject* exc_traceback;
	PyObject* args;
	PyObject* repr;
	NSException* val;
	NSDictionary* userInfo;

	PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);

	if (!exc_type) return;

	if (!PyObject_IsInstance(exc_value, exc_type)) {
		PyErr_NormalizeException(&exc_type, &exc_value, &exc_traceback);
	}

	args = PyObject_GetAttrString(exc_value, "_pyobjc_info_");
	if (args == NULL) {
		PyErr_Clear();
	} else {
		/* This may be an exception that started out in 
		 * Objective-C code.
		 */
		PyObject* v;
		char*     reason = NULL;
		char*     name = NULL;
		id        userInfo = nil;

		v = PyDict_GetItemString(args, "reason"); 
		if (v && PyString_Check(v)) {
			reason = PyString_AsString(v);
		} else {
			PyErr_Clear();
		}

		v = PyDict_GetItemString(args, "name"); 
		if (v && PyString_Check(v)) {
			name = PyString_AsString(v);
		} else {
			PyErr_Clear();
		}

		v = PyDict_GetItemString(args, "userInfo");
		if (v && ObjCObject_Check(v)) {
			userInfo = ObjCObject_GetObject(v);
		} else {
			PyErr_Clear();
		}

		if (name && reason) {
			id oc_name;
			id oc_reason;

			oc_name = [NSString stringWithCString:name];
			oc_reason = [NSString stringWithCString:reason];
			val = [NSException exceptionWithName:oc_name
				     reason:oc_reason
				     userInfo:userInfo];
			Py_DECREF(args);
			Py_DECREF(exc_type);
			if (exc_value)
			  Py_DECREF(exc_value);
			if (exc_traceback)
			  Py_DECREF(exc_traceback);

			[val raise];
		}
	}
	Py_XDECREF(args);

	repr = PyObject_Str(exc_value);
	userInfo = [NSDictionary 
			dictionaryWithObject:[
				OC_PythonObject newWithObject:exc_value]
			forKey:@"__pyobjc_exc__"
		   ];
	val = [NSException 
		exceptionWithName:@"OC_PythonException"
		reason:[NSString stringWithCString:PyString_AS_STRING(repr)]
		userInfo:userInfo];

	Py_DECREF(repr);
	Py_DECREF(exc_type);
	if (exc_value)
	  Py_DECREF(exc_value);
	if (exc_traceback)
	  Py_DECREF(exc_traceback);

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
				Py_DECREF(imp);
			} else {
				r = PyDict_SetItem(type_dict, name, imp);

				if (r < 0) return -1;

				Py_DECREF(imp);
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

