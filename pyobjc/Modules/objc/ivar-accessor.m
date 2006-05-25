/*
 */
#include "pyobjc.h"

static Ivar
find_ivar(NSObject* base, char* name)
{
	Class cur = GETISA((id)base);
	Ivar ivar;

	while (cur != nil) {
		ivar = class_getInstanceVariable(cur, name);
		if (ivar != nil) {
			return ivar;
		}
		cur = cur->super_class;
	}
	return nil;
}

PyObject*
PyObjCIvar_Info(PyObject* self __attribute__((__unused__)), PyObject* object)
{
	Class cur;

	if (PyObjCObject_Check(object)) {
		cur = GETISA((id)PyObjCObject_GetObject(object));
	} else if (PyObjCClass_Check(object)) {
		cur = PyObjCClass_GetClass(object);
	} else {
		PyErr_Format(PyExc_TypeError, "not a class or object");
		return NULL;
	}

	PyObject* result;

	result = PyList_New(0);
	if (result == NULL) {
		return result;
	}

	while (cur != nil) {
		Py_ssize_t i, len;
		Ivar ivar;
		PyObject* v;
		int r;

		if (cur->ivars != NULL) {
			len = cur->ivars->ivar_count;
			for (i = 0; i < len; i++) {
				ivar = cur->ivars->ivar_list + i;

				v = Py_BuildValue("(ss)", 
						ivar->ivar_name, 
						ivar->ivar_type);
				if (v == NULL) {
					Py_DECREF(result);
					return NULL;
				}
				r = PyList_Append(result, v);
				Py_DECREF(v);
				if (r == -1) {
					Py_DECREF(result);
					return NULL;
				}
			}
		}

		cur = cur->super_class;
	}
	return result;
}

PyObject*
PyObjCIvar_Get(PyObject* self __attribute__((__unused__)), 
		PyObject* args, PyObject* kwds)
{
static char* keywords[] = {"obj", "name", NULL };
	PyObject* anObject;
	char*     name;
	Ivar	  ivar;
	NSObject* objcValue;
	PyObject* result;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "Os", keywords, &anObject, &name)) {
		return NULL;
	}

	if (!PyObjCObject_Check(anObject)) {
		PyErr_Format(PyExc_TypeError,
			"Expecting an Objective-C object, got instance of %s",
			anObject->ob_type->tp_name);
		return NULL;
	}

	objcValue = PyObjCObject_GetObject(anObject);

	ivar = find_ivar(objcValue, name);
	if (ivar == NULL) {
		PyErr_Format(PyExc_AttributeError, "%s", name);
		return NULL;
	}

	if (strcmp(ivar->ivar_type, @encode(PyObject*)) == 0) {
		result = *(PyObject**)(((char*)(objcValue)) + ivar->ivar_offset);
		Py_XINCREF(result);
	} else {
		result = pythonify_c_value(ivar->ivar_type, 
			((char*)(objcValue)) + ivar->ivar_offset);
	}

	return result;
}

PyObject*
PyObjCIvar_Set(PyObject* self __attribute__((__unused__)), 
		PyObject* args, PyObject* kwds)
{
static char* keywords[] = {"obj", "name", "value", "updateRefCounts", NULL };
	PyObject* anObject;
	char*     name;
	Ivar	  ivar;
	PyObject* value;
	PyObject* updateRefCounts = NULL;
	NSObject* objcValue;
	int       result;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OsO|O", keywords, &anObject, 
				&name, &value, &updateRefCounts)) {
		return NULL;
	}

	if (!PyObjCObject_Check(anObject)) {
		PyErr_Format(PyExc_TypeError,
			"Expecting an Objective-C object, got instance of %s",
			anObject->ob_type->tp_name);
		return NULL;
	}

	objcValue = PyObjCObject_GetObject(anObject);

	ivar = find_ivar(objcValue, name);
	if (ivar == NULL) {
		PyErr_Format(PyExc_AttributeError, "%s", name);
		return NULL;
	}

	if (strcmp(ivar->ivar_type, @encode(PyObject*)) == 0) {
		Py_XINCREF(value);
		Py_XDECREF(*(PyObject**)(((char*)(objcValue)) + ivar->ivar_offset)); 
		*(PyObject**)(((char*)(objcValue)) + ivar->ivar_offset) = value; 

	} else if (ivar->ivar_type[0] == _C_ID) {
		NSObject* tmpValue;

		if (updateRefCounts == NULL) {
			PyErr_SetString(PyExc_TypeError,
				"Instance variable is an object, "
				"updateRefCounts argument is required");
			return NULL;
		}

		result = depythonify_c_value(ivar->ivar_type, value, &tmpValue);
		if (result != 0) {
			return NULL;
		}
			
		if (PyObject_IsTrue(updateRefCounts)) {
			[tmpValue retain];
			[*(NSObject**)(((char*)(objcValue)) + ivar->ivar_offset) autorelease];
		}
		*(NSObject**)(((char*)(objcValue)) + ivar->ivar_offset) = tmpValue;
	} else if (ivar->ivar_type[0] == _C_CLASS && strcmp(name, "isa") == 0) {
		/* We're changing the class of the ObjC value, also update the
		 * class of the python proxy.
		 */
		PyObject* cls;

		result = depythonify_c_value(ivar->ivar_type, value,
			((char*)(objcValue)) + ivar->ivar_offset);
		if (result != 0) {
			return NULL;
		}

		cls = PyObjCClass_New(GETISA((id)objcValue));
		if (cls == NULL) {
			return NULL;
		}

		Py_INCREF(cls);
		Py_DECREF((PyObject*)(anObject->ob_type));
		anObject->ob_type = (PyTypeObject*)cls;

	} else {
		result = depythonify_c_value(ivar->ivar_type, value,
			((char*)(objcValue)) + ivar->ivar_offset);
		if (result != 0) {
			return NULL;
		}
	}
	Py_INCREF(Py_None);
	return Py_None;
}
