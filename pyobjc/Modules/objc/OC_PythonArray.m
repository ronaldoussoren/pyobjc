#import "OC_PythonArray.h"

static void
nsmaptable_python_retain(NSMapTable *table __attribute__((__unused__)), const void *datum) {
	Py_INCREF((PyObject *)datum);
}

static void
nsmaptable_python_release(NSMapTable *table __attribute__((__unused__)), void *datum) {
	Py_DECREF((PyObject *)datum);
}

static void
nsmaptable_objc_retain(NSMapTable *table __attribute__((__unused__)), const void *datum) {
	[(id)datum retain];
}

static void
nsmaptable_objc_release(NSMapTable *table __attribute__((__unused__)), void *datum) {
	[(id)datum release];
}

static
NSMapTableKeyCallBacks PyObjC_ObjectToIdTable_KeyCallBacks = {
	NULL, // use pointer value for hash
	NULL, // use pointer value for equality
	&nsmaptable_python_retain,
	&nsmaptable_python_release,
	NULL, // generic description
	NULL // not a key
};

static
NSMapTableValueCallBacks PyObjC_ObjectToIdTable_ValueCallBacks = {
	&nsmaptable_objc_retain,
	&nsmaptable_objc_release,
	NULL  // generic description
};

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
	if (table) {
		NSResetMapTable(table);
	} else {
		table = NSCreateMapTable(PyObjC_ObjectToIdTable_KeyCallBacks, PyObjC_ObjectToIdTable_ValueCallBacks, [self count]);
	}
    NSMapInsert(table, (const void *)Py_None, (const void *)[NSNull null]);
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
		if (table) {
			NSFreeMapTable(table);
		}
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

		if ((result = (id)NSMapGet(table, (const void *)v))) {
			Py_DECREF(v);
		} else {
			err = depythonify_c_value(@encode(id), v, &result);
			if (err == -1) {
				PyObjC_GIL_FORWARD_EXC();
			} else {
				NSMapInsert(table, (const void *)v, (const void *)result);
				Py_DECREF(v);
			}
		}
	
	PyObjC_END_WITH_GIL

	return result;
}


-(void)replaceObjectAtIndex:(int)idx withObject:newValue;
{
	PyObject* v;

	PyObjC_BEGIN_WITH_GIL
		v = pythonify_c_value(@encode(id), &newValue);
		if (v == NULL) {
			PyObjC_GIL_FORWARD_EXC();
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
		v = pythonify_c_value(@encode(id), &anObject);
		if (v == NULL) {
			PyObjC_GIL_FORWARD_EXC();
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
		v = pythonify_c_value(@encode(id), &anObject);
		if (v == NULL) {
			PyObjC_GIL_FORWARD_EXC();
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
