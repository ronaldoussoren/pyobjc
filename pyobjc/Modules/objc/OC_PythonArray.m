#import "OC_PythonArray.h"

@implementation OC_PythonArray 

+ newWithPythonObject:(PyObject*)v;
{
	OC_PythonArray* res;

	res = [[OC_PythonArray alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

- initWithPythonObject:(PyObject*)v;
{
	self = [super init];
	if (!self) return nil;


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
	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(value, self);
		Py_XDECREF(value);

	PyObjC_END_WITH_GIL

	[super dealloc];
}

-(int)count
{
	int result;

	PyObjC_BEGIN_WITH_GIL
		result = PySequence_Length(value);

	PyObjC_END_WITH_GIL

	return result;
}

-objectAtIndex:(int)idx
{
	PyObject* v;
	id result;
	int err;

	PyObjC_BEGIN_WITH_GIL

		v = PySequence_GetItem(value, idx);
		if (v == NULL) {
			PyObjC_GIL_FORWARD_EXC();
		}

		err = depythonify_c_value(@encode(id), v, &result);
		if (err == -1) {
			PyObjC_GIL_FORWARD_EXC();
		} else {
			Py_DECREF(v);
		}
	
	PyObjC_END_WITH_GIL

	return result;
}


-(void)replaceObjectAtIndex:(int)idx withObject:newValue;
{
	PyObject* v;

	PyObjC_BEGIN_WITH_GIL
		if (newValue == [NSNull null]) {
			Py_INCREF(Py_None);
			v = Py_None;
		} else {
			v = PyObjC_IdToPython(newValue);
			if (v == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		if (PySequence_SetItem(value, idx, v) < 0) {
			Py_DECREF(v);
			PyObjC_GIL_FORWARD_EXC();
		}
		Py_DECREF(v);

	PyObjC_END_WITH_GIL;
}

-(void)getObjects:(id*)buffer inRange:(NSRange)range
{
	unsigned int i;

	for (i = 0; i < range.length; i++) {
		buffer[i] = [self objectAtIndex:i+range.location];
	}
}

-(void)addObject:(id)anObject
{
	PyObject* v;
	PyObject* w;

	PyObjC_BEGIN_WITH_GIL
		if (anObject == [NSNull null]) {
			Py_INCREF(Py_None);
			v = Py_None;
		} else {
			v = PyObjC_IdToPython(anObject);
			if (v == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		w = PyObject_CallMethod(value, "append", "O", v);
		if (w == NULL) {
			Py_DECREF(v);
			PyObjC_GIL_FORWARD_EXC();
		}
		Py_DECREF(v);
		Py_DECREF(w);

	PyObjC_END_WITH_GIL;
}

-(void)insertObject:(id)anObject atIndex:(unsigned)idx
{
	PyObject* v;
	PyObject* w;

	PyObjC_BEGIN_WITH_GIL
		if (anObject == [NSNull null]) {
			Py_INCREF(Py_None);
			v = Py_None;
		} else {
			v = PyObjC_IdToPython(anObject);
			if (v == NULL) {
				PyObjC_GIL_FORWARD_EXC();
			}
		}

		w = PyObject_CallMethod(value, "insert", "iO", idx, v);
		if (w == NULL) {
			Py_DECREF(v);
			PyObjC_GIL_FORWARD_EXC();
		}
		Py_DECREF(v);
		Py_DECREF(w);

	PyObjC_END_WITH_GIL;
}

-(void)removeLastObject
{
	int r;
	int idx;

	PyObjC_BEGIN_WITH_GIL
		idx = PySequence_Length(value);
		if (idx == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}

		if (idx == 0) {
			PyErr_SetString(PyExc_ValueError, "pop empty sequence");
			PyObjC_GIL_FORWARD_EXC();
		}

		r = PySequence_DelItem(value, idx-1);
		if (r == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL;
}

-(void)removeObjectAtIndex:(unsigned)idx;
{
	int r;

	PyObjC_BEGIN_WITH_GIL
		if (idx > INT_MAX) {
			PyErr_SetString(PyExc_IndexError, "No such index");
			PyObjC_GIL_FORWARD_EXC();
		}

		r = PySequence_DelItem(value, (int)idx);
		if (r == -1) {
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL;
}

@end /* implementation OC_PythonArray */
