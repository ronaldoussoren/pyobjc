#include "OC_PythonDictionary.h"
#include "OC_PythonArray.h"
#include "pyobjc.h"
#include "objc_support.h"

#if PY_MAJOR_VERSION == 2 && PY_MINOR_VERSION == 2 && PY_MICRO_VERSION == 0

/* Python 2.2.0 contains incorrect definitions for PyMapping_DelItem
 * and PyMapping_DelItemString
 */
#   undef PyMapping_DelItem
#   undef PyMapping_DelItemString

#   define PyMapping_DelItem(O,K) PyDict_DelItem((O),(K))
#   define PyMapping_DelItemString(O,K) PyDict_DelItemString((O),(K))

#endif /* Python 2.2.0 */


@implementation OC_PythonDictionary 

+newWithPythonObject:(PyObject*)v;
{
	OC_PythonArray* res = 
		[[OC_PythonDictionary alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

-initWithPythonObject:(PyObject*)v;
{
	value = v;
	Py_INCREF(v);
	return self;
}

-dealloc
{
	Py_XDECREF(value);
}

-(PyObject*)pyObject
{
	return value;
}


-(int)count
{
	return PyMapping_Length([self pyObject]);
}

-objectForKey:key
{
	PyObject* v;
	PyObject* k;
	id         result;
	const char* err;

	k = pythonify_c_value("@", &key);
	if (k == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

#if 0
	v = PyMapping_GetItem([self pyObject], k);
#else
	v = PyDict_GetItem([self pyObject], k);
#endif

	err = depythonify_c_value("@", v, &result);
	Py_DECREF(v);
	Py_DECREF(k);
	if (err != NULL) {
		ObjCErr_Set(PyExc_TypeError, "Cannot convert result: %s",
			err);
		ObjCErr_ToObjC();
		return nil;
	}
	return result;
}


-(void)setObject:val forKey:key
{
	PyObject* v;
	PyObject* k;

	v = pythonify_c_value("@", &val);
	if (v == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	k = pythonify_c_value("@", &key);
	if (k == NULL) {
		Py_DECREF(v);
		ObjCErr_ToObjC();
		return;
	}

	if (PyDict_SetItem([self pyObject], k, v) < 0) {
		Py_DECREF(v);
		Py_DECREF(k);
		ObjCErr_ToObjC();
		return;
	}
	Py_DECREF(v);
	Py_DECREF(k);
}

-(void)removeObjectForKey:key
{
	PyObject* k;

	k = pythonify_c_value("@", &key);
	if (k == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	if (PyMapping_DelItem([self pyObject], k) < 0) {
		Py_DECREF(k);
		ObjCErr_ToObjC();
		return;
	}
	Py_DECREF(k);
}

-keyEnumerator
{
	PyObject* keys = PyMapping_Keys([self pyObject]);
	id result = [OC_PythonArray newWithPythonObject:keys];
	Py_DECREF(keys);
	[result retain];

	return [result objectEnumerator];
}

@end 
