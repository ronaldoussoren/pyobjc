#include "pyobjc.h"
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
	if (unlikely(self == nil)) return nil;

	if (unlikely(PyObject_AsReadBuffer(v, &buffer, &buffer_len) == -1)) {
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

-(void)release
{
	/* See comment in OC_PythonUnicode */
	PyObjC_BEGIN_WITH_GIL
		[super release];
	PyObjC_END_WITH_GIL
}
        


-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(value, self);
		Py_XDECREF(value);

	PyObjC_END_WITH_GIL

	[super dealloc];
}

-(NSUInteger)length
{
	NSUInteger rval;
	
	PyObjC_BEGIN_WITH_GIL
		if (unlikely(PyObject_AsReadBuffer(value, &buffer, &buffer_len) == -1)) {
			PyErr_Clear();
			rval = 0;
		}
		if ((unsigned)buffer_len > NSUIntegerMax) {
			rval = NSUIntegerMax;
		} else {
			rval = buffer_len;
		}
	PyObjC_END_WITH_GIL
	return rval;
}

-(const void *)bytes
{
	const void *rval;
	PyObjC_BEGIN_WITH_GIL
		if (unlikely(PyObject_AsReadBuffer(value, &buffer, &buffer_len) == -1)) {
			PyErr_Clear();
			rval = NULL;
		}
		rval = buffer;
	PyObjC_END_WITH_GIL
	return rval;
}

@end /* implementation OC_PythonData */
