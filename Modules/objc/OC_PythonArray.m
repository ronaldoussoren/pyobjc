#include "pyobjc.h"

@implementation OC_PythonArray 

+newWithPythonObject:(PyObject*)v;
{
	OC_PythonArray* res;

	res = [[OC_PythonArray alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

-initWithPythonObject:(PyObject*)v;
{
	Py_INCREF(v);
	Py_XDECREF(value);
	value = v;
	return self;
}

-(PyObject*)__pyobjc_PythonObject__
{
	Py_INCREF(value);
	return value;
}

-(void)dealloc
{
	PyGILState_STATE state = PyGILState_Ensure();

	Py_XDECREF(value);

	PyGILState_Release(state);
}

-(int)count
{
	int result;
	PyGILState_STATE state = PyGILState_Ensure();

	result = PySequence_Length(value);

	PyGILState_Release(state);
	return result;
}

-objectAtIndex:(int)idx
{
	PyObject* v;
	id  result;
	int err;
	PyGILState_STATE state = PyGILState_Ensure();

	v = PySequence_GetItem(value, idx);
	if (v == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	err = depythonify_c_value("@", v, &result);
	Py_DECREF(v);
	if (err == -1) {
		PyObjCErr_ToObjCWithGILState(&state);
		return nil;
	}

	PyGILState_Release(state);
	return result;
}


-(void)replaceObjectAtIndex:(int)idx withObject:newValue;
{
	PyObject* v;
	PyGILState_STATE state = PyGILState_Ensure();

	v = pythonify_c_value("@", &newValue);
	if (v == NULL) {
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}

	if (PySequence_SetItem(value, idx, v) < 0) {
		Py_DECREF(v);
		PyObjCErr_ToObjCWithGILState(&state);
		return;
	}
	Py_DECREF(v);
	PyGILState_Release(state);
}

@end /* implementation OC_PythonArray */
