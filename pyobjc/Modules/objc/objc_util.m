/*
 * Some utility functions...
 *
 * TODO: Documentation
 */

#import <Foundation/NSString.h>
#import <Foundation/NSDictionary.h>
#include "objc_util.h"
#include "pyobjc.h"

PyObject* ObjCExc_error;
PyObject* ObjCExc_noclass_error;
PyObject* ObjCExc_internal_error;

PyObject* PyObjCExc_ProtocolWarning;


int ObjCUtil_Init(PyObject* module)
{
#define NEW_EXC(identifier, name, base_class) \
	identifier = PyErr_NewException("objc."name, base_class, NULL); \
	if (identifier == NULL) return -1; \
	Py_INCREF(identifier); \
	if (PyModule_AddObject(module, name, identifier) < 0) return -1;

	NEW_EXC(ObjCExc_error, "error", NULL);
	NEW_EXC(ObjCExc_noclass_error, "nosuchclass_error", ObjCExc_error);
	NEW_EXC(ObjCExc_internal_error, "internal_error", ObjCExc_error);

	NEW_EXC(PyObjCExc_ProtocolWarning, "ProtocolWarning", PyExc_Warning);

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

	return ObjCExc_error;
}
	

void PyObjCErr_FromObjC(NSException* localException)
{
	NSDictionary* userInfo;
	PyObject*     dict;
	PyObject*     exception;
	PyObject*     v;
	char          buf[256];
	PyObject*     exc_type;
	PyObject*     exc_value;
	PyObject*     exc_traceback;

	exception = ObjCErr_PyExcForName([[localException name] cString]);

	userInfo = [localException userInfo];
	if (userInfo) {
		id val;

		val = [userInfo objectForKey:@"__pyobjc_exc_type__"];
		if (val) {
			exc_type = [val  pyObject];
			exc_value = [[userInfo objectForKey:@"__pyobjc_exc_value__"]  pyObject];
			exc_traceback = [[userInfo objectForKey:@"__pyobjc_exc_traceback__"]  pyObject];

			/* -pyObject returns a borrowed reference and 
			 * PyErr_Restore steals one from us.
			 */
			Py_INCREF(exc_type);
			Py_XINCREF(exc_value);
			Py_XINCREF(exc_traceback);

			PyErr_Restore(exc_type, exc_value , exc_traceback);
			return;
		}
	}

	dict = PyDict_New();
	v = PyString_FromString([[localException name] cString]);
	PyDict_SetItemString(dict, "name", v);
	v = PyString_FromString([[localException reason] cString]);
	PyDict_SetItemString(dict, "reason",  v);
	Py_DECREF(v);
	if (userInfo) {
		v = PyObjCObject_New(userInfo);
		if (v != NULL) {
			PyDict_SetItemString(dict, "userInfo", v);
			Py_DECREF(v);
		} else { 
			PyErr_Clear();
		}
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
	PyErr_Restore(exc_type, exc_value, exc_traceback);
}


void PyObjCErr_ToObjC(void)
{
	PyObject* exc_type;
	PyObject* exc_value;
	PyObject* exc_traceback;
	PyObject* args;
	PyObject* repr;
	NSException* val;
	NSMutableDictionary* userInfo;

	PyErr_Fetch(&exc_type, &exc_value, &exc_traceback);
	if (!exc_type)
		return;

	PyErr_NormalizeException(&exc_type, &exc_value, &exc_traceback);

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
		if (v && PyObjCObject_Check(v)) {
			userInfo = PyObjCObject_GetObject(v);
		} else {
			userInfo = nil;
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
			Py_XDECREF(exc_type);
			Py_XDECREF(exc_value);
			Py_XDECREF(exc_traceback);
			[val raise];
		}
	}
	Py_XDECREF(args);

	repr = PyObject_Str(exc_value);
	userInfo = [NSMutableDictionary dictionaryWithCapacity: 3];
	[userInfo setObject:
		[OC_PythonObject newWithObject:exc_type]
		forKey:@"__pyobjc_exc_type__"];
	if (exc_value != NULL)
		[userInfo setObject:
			[OC_PythonObject newWithObject:exc_value]
			forKey:@"__pyobjc_exc_value__"];
	if (exc_traceback != NULL)
		[userInfo setObject:
			[OC_PythonObject newWithObject:exc_traceback]
			forKey:@"__pyobjc_exc_traceback__"];

	val = [NSException 
		exceptionWithName:@"OC_PythonException"
		reason:[NSString stringWithCString:PyString_AS_STRING(repr)]
		userInfo:userInfo];

	Py_DECREF(repr);

	if (ObjC_VerboseLevel) {
		PyErr_Restore(exc_type, exc_value , exc_traceback);
		NSLog(@"PyObjC: Converting exception to Objective-C:");
		PyErr_Print();
	} else {
		Py_DECREF(exc_type);
		Py_XDECREF(exc_value);
		Py_XDECREF(exc_traceback);
	}
	[val raise];
}

PyObject* ObjC_class_extender = NULL;

int ObjC_AddConvenienceMethods(Class cls, PyObject* type_dict)
{
	PyObject* super_class;
	PyObject* name;
	PyObject* res;
	PyObject* args;

	if (ObjC_class_extender == NULL || cls == nil) return 0;

	if (cls->super_class == nil) {
		super_class = Py_None;
		Py_INCREF(super_class);
	} else {
		super_class = PyObjCClass_New(cls->super_class);
		if (super_class == NULL) {
			return -1;
		}
	}

	name = PyString_FromString(cls->name);
	if (name == NULL) {
		Py_DECREF(super_class);
		return -1;
	}

	args = PyTuple_New(3);
	if (args == NULL) {
		Py_DECREF(super_class);
		Py_DECREF(name);
		return -1;
	}

	PyTuple_SET_ITEM(args, 0, super_class);
	PyTuple_SET_ITEM(args, 1, name);
	PyTuple_SET_ITEM(args, 2, type_dict);
	Py_INCREF(type_dict);

	res = PyObject_CallObject(ObjC_class_extender, args);
	Py_DECREF(args);
	if (res == NULL) {
		return -1;
	}
	Py_DECREF(res);

	return 0;
}

/* 
 * Update the convenience methods. We can't just change the type dict here,
 * because the type doesn't pick up new '__' methods  (like __getitem__) 
 * that way.
 */
int ObjC_UpdateConvenienceMethods(PyObject* cls)
{
	PyObject* super_class;
	PyObject* name;
	PyObject* res;
	PyObject* args;
	Class     objc_cls;
	PyObject* dict;
	PyObject* keys;
	int       i, len;
	

	if (ObjC_class_extender == NULL || cls == NULL) return 0;

	objc_cls = PyObjCClass_GetClass(cls);

	if (objc_cls->super_class == nil) {
		super_class = Py_None;
		Py_INCREF(super_class);
	} else {
		super_class = PyObjCClass_New(objc_cls->super_class);
		if (super_class == NULL) {
			return -1;
		}
	}

	name = PyString_FromString(objc_cls->name);
	if (name == NULL) {
		Py_DECREF(super_class);
		return -1;
	}

	dict = /*PyDict_Copy*/(((PyTypeObject*)cls)->tp_dict);
	Py_INCREF(dict);
	if (dict == NULL) {
		Py_DECREF(super_class);
		Py_DECREF(name);
		return -1;
	}

	args = PyTuple_New(3);
	if (args == NULL) {
		Py_DECREF(super_class);
		Py_DECREF(name);
		Py_DECREF(dict);
		return -1;
	}

	PyTuple_SET_ITEM(args, 0, super_class);
	PyTuple_SET_ITEM(args, 1, name);
	PyTuple_SET_ITEM(args, 2, dict);

	res = PyObject_CallObject(ObjC_class_extender, args);
	if (res == NULL) {
		Py_DECREF(args);
		return -1;
	}
	Py_DECREF(res);

	keys = PyDict_Keys(dict);
	if (keys == NULL) {
		Py_DECREF(args);
		return -1;
	}

	len = PySequence_Length(keys);
	if (len == -1) {
		Py_DECREF(keys);
		Py_DECREF(args);
		return -1;
	}
	for (i = 0; i < len; i++) {
		PyObject* k = PySequence_GetItem(keys, i);
		PyObject* v;
		char*     n;
		
		if (k == NULL) {
			PyErr_Clear();
			continue;
		}

		if (!PyString_Check(k)) {
			Py_DECREF(k);
			continue;
		}
		n = PyString_AS_STRING(k);
		if (n[0] != '_' || n[1] != '_') {
			Py_DECREF(k);
			continue;
		}
		if (	   strcmp(n, "__dict__") == 0 
			|| strcmp(n, "__bases__") == 0) {

			Py_DECREF(k);
			continue;
		}

		v = PyDict_GetItem(dict, k);
		if (v == NULL) {
			Py_DECREF(k);
			continue;
		}
		if (PyObject_SetAttr(cls, k, v) == -1) {
			Py_DECREF(k);
			continue;
		}
		Py_DECREF(k);
	}	


	Py_DECREF(args);

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

NSMapTableKeyCallBacks ObjC_PointerKeyCallBacks = {
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
	NULL,
};

NSMapTableValueCallBacks ObjC_PointerValueCallBacks = {
	NULL,
	NULL,
	NULL,
};

static void pyobj_retain(NSMapTable* table __attribute__((__unused__)), const void* v)
{
	Py_XINCREF((PyObject*)v);
}

static void pyobj_release(NSMapTable* table __attribute__((__unused__)), void* v)
{
	Py_XDECREF((PyObject*)v);
}

NSMapTableKeyCallBacks ObjC_PyObjectKeyCallBacks = {
	NULL,
	NULL,
	pyobj_retain,
	pyobj_release,
	NULL,
	NULL,
};

NSMapTableValueCallBacks ObjC_PyObjectValueCallBacks = {
	pyobj_retain,
	pyobj_release,
	NULL,
};
