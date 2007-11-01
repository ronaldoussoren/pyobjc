#include "pyobjc.h"

@implementation OC_PythonEnumerator

+newWithPythonObject:(PyObject*)object
{
	return [[self alloc] initWithPythonObject:object];
}

-initWithPythonObject:(PyObject*)object
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

-nextObject
{
	if (!valid) return nil;

	NSObject* result = nil;

	PyObjC_BEGIN_WITH_GIL
		PyObject* object = PyIter_Next(value);
		if (object == NULL) {
			if (PyErr_ExceptionMatches(PyExc_StopIteration)) {
				valid = NO;
				PyErr_Clear();
				PyObjC_GIL_RETURN(nil);
			}

			PyObjC_GIL_FORWARD_EXC();

		}
		result = PyObjC_PythonToId(object);
		if (result == nil) {
			PyObjC_GIL_FORWARD_EXC();
		}

	PyObjC_END_WITH_GIL

	return result;
}

-allObjects
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
