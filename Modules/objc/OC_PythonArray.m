#include "OC_PythonArray.h"
#include "pyobjc.h"
#include "objc_support.h"

@implementation OC_PythonArray 

+newWithPythonObject:(PyObject*)v;
{
	OC_PythonArray* res = 
		[[OC_PythonArray alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

-initWithPythonObject:(PyObject*)v;
{
	value = v;
	Py_INCREF(value);
	return self;
}

-(void)dealloc
{
	Py_XDECREF(value);
}

-(PyObject*)pyObject
{
	return value;
}


-(int)count
{
	return PySequence_Length([self pyObject]);
}

-objectAtIndex:(int)idx
{
	PyObject* v;
	id         result;
	const char* err;

	v = PySequence_GetItem([self pyObject], idx);
	if (v == NULL) {
		ObjCErr_ToObjC();
		return nil;
	}

	err = depythonify_c_value("@", v, &result);
	Py_DECREF(v);
	if (err != NULL) {
		ObjCErr_Set(PyExc_TypeError, "Cannot convert result: %s",
			err);
		ObjCErr_ToObjC();
		return nil;
	}

	return result;
}


-(void)replaceObjectAtIndex:(int)idx withObject:newValue;
{
	PyObject* v;

	v = pythonify_c_value("@", &newValue);
	if (v == NULL) {
		ObjCErr_ToObjC();
		return;
	}

	if (PySequence_SetItem([self pyObject], idx, v) < 0) {
		Py_DECREF(v);
		ObjCErr_ToObjC();
		return;
	}
	Py_DECREF(v);
}

@end 
