#import "OC_PythonData.h"

@implementation OC_PythonData 

+ newWithPythonObject:(PyObject*)v;
{
	OC_PythonData* res;

	res = [[OC_PythonData alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

- initWithPythonObject:(PyObject*)v;
{
	self = [super init];
	if (!self) return nil;

	if (PyObject_AsReadBuffer(v, &buffer, ((int *)&buffer_len))) {
		[super dealloc];
		return nil;
	}

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

-(unsigned)length
{
	unsigned rval;
	PyObjC_BEGIN_WITH_GIL
		if (PyObject_AsReadBuffer(value, &buffer, ((int *)&buffer_len))) {
			PyErr_Clear();
			rval = 0;
		}
		rval = buffer_len;
	PyObjC_END_WITH_GIL
	return rval;
}

-(const void *)bytes
{
	const void *rval;
	PyObjC_BEGIN_WITH_GIL
		if (PyObject_AsReadBuffer(value, &buffer, ((int *)&buffer_len))) {
			PyErr_Clear();
			rval = NULL;
		}
		rval = buffer;
	PyObjC_END_WITH_GIL
	return rval;
}

@end /* implementation OC_PythonData */
