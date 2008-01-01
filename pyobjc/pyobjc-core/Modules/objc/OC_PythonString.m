#include "pyobjc.h"
#import "OC_PythonString.h"

@implementation OC_PythonString 

+ newWithPythonObject:(PyObject*)v;
{
	OC_PythonString* res;

	res = [[OC_PythonString alloc] initWithPythonObject:v];
	[res autorelease];
	return res;
}

- initWithPythonObject:(PyObject*)v;
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
		[realObject release];
		Py_XDECREF(value);
	PyObjC_END_WITH_GIL

	[super dealloc];
}

-(id)__realObject__
{
	static int supportsNoCopy = -1;
	if (supportsNoCopy == -1) {
		supportsNoCopy = (int)[NSString instancesRespondToSelector:@selector(initWithBytesNoCopy:length:encoding:freeWhenDone:)];
	}
	if (!realObject) {
#if defined(__LP64__) || MAC_OS_X_VERSION_MIN_REQUIRED >= MAC_OS_X_VERSION_10_3
		realObject = [[NSString alloc]
			initWithBytesNoCopy:PyString_AS_STRING(value)
			length:(NSUInteger)PyString_GET_SIZE(value)
			encoding:[NSString defaultCStringEncoding]
			freeWhenDone:NO];

#else
		if (supportsNoCopy) {
			// Mac OS X 10.3+
			realObject = [[NSString alloc]
				initWithBytesNoCopy:PyString_AS_STRING(value)
				length:(NSUInteger)PyString_GET_SIZE(value)
				encoding:[NSString defaultCStringEncoding]
				freeWhenDone:NO];
		} else {
			// Mac OS X 10.2
			realObject = [[NSString alloc]
				initWithBytes:PyString_AS_STRING(value)
				length:(NSUInteger)PyString_GET_SIZE(value)
				encoding:[NSString defaultCStringEncoding]];
		}
#endif
	}
	return realObject;
}

-(NSUInteger)length
{
	return [((NSString *)[self __realObject__]) length];
}

-(unichar)characterAtIndex:(NSUInteger)anIndex
{
	return [((NSString *)[self __realObject__]) characterAtIndex:anIndex];
}

-(void)getCharacters:(unichar *)buffer range:(NSRange)aRange
{
	[((NSString *)[self __realObject__]) getCharacters:buffer range:aRange];
}

@end /* implementation OC_PythonString */
