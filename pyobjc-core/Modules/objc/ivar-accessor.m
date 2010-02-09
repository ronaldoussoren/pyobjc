/*
 */
#include "pyobjc.h"

static Ivar
find_ivar(NSObject* base, char* name)
{
	Class cur = object_getClass((id)base);
	Ivar ivar;

	while (cur != nil) {
		ivar = class_getInstanceVariable(cur, name);
		if (ivar != nil) {
			return ivar;
		}
		cur = class_getSuperclass(cur);
	}
	return nil;
}

PyObject*
PyObjCIvar_Info(PyObject* self __attribute__((__unused__)), PyObject* object)
{
	Class cur;
	PyObject* v;
	PyObject* result;
	int r;

	if (PyObjCObject_Check(object)) {
		cur = object_getClass((id)PyObjCObject_GetObject(object));
	} else if (PyObjCClass_Check(object)) {
		cur = PyObjCClass_GetClass(object);
	} else {
		PyErr_Format(PyExc_TypeError, "not a class or object");
		return NULL;
	}


	result = PyList_New(0);
	if (result == NULL) {
		return result;
	}

	/* Handle 'isa' specially, due to Objective-C 2.0 weirdness */
	v = Py_BuildValue(
			"(s"Py_ARG_BYTES")", 
			"isa", @encode(Class));
	if (v == NULL) {
		Py_DECREF(result);
		return result;
	}

	r = PyList_Append(result, v);
	Py_DECREF(v);
	if  (r == -1) {
		Py_DECREF(result);
		return result;
	}



	while (cur != nil) {
		Ivar ivar;
		Ivar* ivarList;
		unsigned i, ivarCount;

		ivarList = class_copyIvarList(cur, &ivarCount);
		if (ivarList == NULL) {
			PyErr_SetString(PyExc_SystemError, "copyIvarList failed");
			Py_DECREF(result);
			return NULL;
		}

		for (i = 0; i < ivarCount; i++) {
			ivar = ivarList[i];
			const char* ivar_name = ivar_getName(ivar);

			if (ivar == NULL) continue;

			if (strcmp(ivar_name, "isa") == 0) {
				/* See comment above */
				continue;
			}

			v = Py_BuildValue(
				"(s"Py_ARG_BYTES")", 
				ivar_name,
				ivar_getTypeEncoding(ivar));
			if (v == NULL) {
				free(ivarList);
				Py_DECREF(result);
				return NULL;
			}
			r = PyList_Append(result, v);
			Py_DECREF(v);
			if (r == -1) {
				free(ivarList);
				Py_DECREF(result);
				return NULL;
			}
		}

		free(ivarList);

		cur = class_getSuperclass(cur);
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
	const char* ivar_type;
	ptrdiff_t ivar_offset;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "Os", keywords, &anObject, &name)) {
		return NULL;
	}

	if (!PyObjCObject_Check(anObject)) {
		PyErr_Format(PyExc_TypeError,
			"Expecting an Objective-C object, got instance of %s",
			Py_TYPE(anObject)->tp_name);
		return NULL;
	}


	objcValue = PyObjCObject_GetObject(anObject);

	/* Shortcut for isa, mostly due to Objective-C 2.0 weirdness */
	if (strcmp(name, "isa") == 0) {
		Class cls = object_getClass(objcValue);
		return pythonify_c_value(@encode(Class), &cls);
	}

	ivar = find_ivar(objcValue, name);
	if (ivar == NULL) {
		PyErr_Format(PyExc_AttributeError, "%s", name);
		return NULL;
	}

	ivar_type = ivar_getTypeEncoding(ivar);
	ivar_offset = ivar_getOffset(ivar);

	if (strcmp(ivar_type, @encode(PyObject*)) == 0) {
		result = *(PyObject**)(((char*)(objcValue)) + ivar_offset);
		Py_XINCREF(result);
	} else {
		result = pythonify_c_value(ivar_type,
			((char*)(objcValue)) + ivar_offset);
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
	const char* ivar_type;
	ptrdiff_t ivar_offset;

	if (!PyArg_ParseTupleAndKeywords(args, kwds, "OsO|O", 
			keywords, &anObject, &name, &value, &updateRefCounts)) {
		return NULL;
	}

	if (!PyObjCObject_Check(anObject)) {
		PyErr_Format(PyExc_TypeError,
			"Expecting an Objective-C object, got instance of %s",
			Py_TYPE(anObject)->tp_name);
		return NULL;
	}

	objcValue = PyObjCObject_GetObject(anObject);

	if (strcmp(name, "isa") == 0) {
		/* 
		 * Change the class of the object, this means we'll have to
		 * update the python proxy object as well.
		 */
		Class cls;
		PyObject* pycls;

		result = depythonify_c_value(@encode(Class), value, &cls);
		if (result == -1) {
			return NULL;
		}

		(void)object_setClass(objcValue, cls);

		pycls = PyObjCClass_New(cls);
		if (pycls == NULL) {
			return NULL;
		}

		Py_DECREF((PyObject*)(Py_TYPE(anObject)));
		Py_TYPE(anObject) = (PyTypeObject*)pycls;
		Py_INCREF(Py_None);
		return Py_None;
	}


	ivar = find_ivar(objcValue, name);
	if (ivar == NULL) {
		PyErr_Format(PyExc_AttributeError, "%s", name);
		return NULL;
	}

	ivar_type = ivar_getTypeEncoding(ivar);
	ivar_offset = ivar_getOffset(ivar);


	if (strcmp(ivar_type, @encode(PyObject*)) == 0) {
		/* 
		 * Python object, need to handle refcounts
		 */
		Py_XINCREF(value);
		Py_XDECREF(*(PyObject**)(((char*)(objcValue)) + ivar_offset));
		*(PyObject**)(((char*)(objcValue)) + ivar_offset) = value; 

	} else if (ivar_type[0] == _C_ID) {
		/*
		 * Objective-C object, need to handle refcounts.
		 */
	
		NSObject* tmpValue;

		if (updateRefCounts == NULL) {
			PyErr_SetString(PyExc_TypeError,
				"Instance variable is an object, "
				"updateRefCounts argument is required");
			return NULL;
		}

		result = depythonify_c_value(ivar_type, value, &tmpValue);
		if (result != 0) {
			return NULL;
		}
			
		if (PyObject_IsTrue(updateRefCounts)) {
			[tmpValue retain];

			id v = object_getIvar(objcValue, ivar);
			[v release];
		}
		object_setIvar(objcValue, ivar, tmpValue);

	} else {
		/* A simple value */

		result = depythonify_c_value(ivar_type, value,
			((char*)(objcValue)) + ivar_offset);
		if (result != 0) {
			return NULL;
		}
	}
	Py_INCREF(Py_None);
	return Py_None;
}
