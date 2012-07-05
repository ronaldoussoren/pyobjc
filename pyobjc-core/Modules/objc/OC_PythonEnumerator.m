#include "pyobjc.h"

@implementation OC_PythonEnumerator

+(instancetype)enumeratorWithPythonObject:(PyObject*)object
{
	return [[[self alloc] initWithPythonObject:object] autorelease];
}

-(id)initWithPythonObject:(PyObject*)object
{
	self = [super init];
	if (self == nil) return nil;

	Py_INCREF(object);
	Py_XDECREF(value);
	value = object;
	valid = YES;

	return self;
}

-(void)dealloc
{
	Py_XDECREF(value);
	[super dealloc];
}

-(id)nextObject
{
	if (!valid) {
		return nil;
	}

	NSObject* result = nil;

	PyObjC_BEGIN_WITH_GIL
		PyObject* object = PyIter_Next(value);
		if (object == NULL) {
			if (!PyErr_Occurred()) {
				valid = NO;
				PyErr_Clear();
				PyObjC_GIL_RETURN(nil);
			} else {
				PyObjC_GIL_FORWARD_EXC();
			}

		}
		result = PyObjC_PythonToId(object);
		if (result == nil) {
			if (PyErr_Occurred()) {
				PyObjC_GIL_FORWARD_EXC();
			} else {
				PyObjC_GIL_RETURN([NSNull null]);
			}
		}

	PyObjC_END_WITH_GIL

	return result;
}

-(NSArray*)allObjects
{
	NSMutableArray* array;
	NSObject* cur;

	array = [NSMutableArray array];
	if (array == nil) 
		return nil;

	while ((cur = [self nextObject]) != nil) {
		[array addObject:cur];
	}

	return array;
}

@end
