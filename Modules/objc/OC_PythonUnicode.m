#include "pyobjc.h"
#import "OC_PythonUnicode.h"

@implementation OC_PythonUnicode 

+ newWithPythonObject:(PyObject*)v;
{
	OC_PythonUnicode* res;

	res = [[OC_PythonUnicode alloc] initWithPythonObject:v];
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

-(void)dealloc
{
	PyObjC_BEGIN_WITH_GIL
		PyObjC_UnregisterObjCProxy(value, self);
#ifndef PyObjC_UNICODE_FAST_PATH
		[realObject release];
#endif /* !PyObjC_UNICODE_FAST_PATH */
		Py_XDECREF(value);
	PyObjC_END_WITH_GIL

	[super dealloc];
}

#ifdef PyObjC_UNICODE_FAST_PATH

-(unsigned)length
{
	return (unsigned)PyUnicode_GET_SIZE(value);
}

-(unichar)characterAtIndex:(unsigned)anIndex
{
	if (anIndex >= (unsigned)PyUnicode_GET_SIZE(value)) {
		[NSException raise:@"NSRangeException" format:@"Range or index out of bounds"];
	}
	return PyUnicode_AS_UNICODE(value)[anIndex];
}

-(void)getCharacters:(unichar *)buffer range:(NSRange)aRange
{
	if (aRange.location + aRange.length > (unsigned)PyUnicode_GET_SIZE(value)) {
		[NSException raise:@"NSRangeException" format:@"Range or index out of bounds"];
	}
	memcpy(buffer, 
	       PyUnicode_AS_UNICODE(value) + aRange.location, 
	       sizeof(unichar) * aRange.length);
}

#else /* !PyObjC_UNICODE_FAST_PATH */

-(id)__realObject__
{
	if (!realObject) {
		PyObjC_BEGIN_WITH_GIL
			PyObject* utf8 = PyUnicode_AsUTF8String(value);
			if (!utf8) {
				NSLog(@"failed to encode unicode string to UTF8");
				PyErr_Clear();
			} else {
				realObject = [[NSString alloc]
					initWithBytes:PyString_AS_STRING(utf8)
					       length:(unsigned)PyString_GET_SIZE(value)
					     encoding:NSUTF8StringEncoding];
				Py_DECREF(utf8);
			}
		PyObjC_END_WITH_GIL
	}
	return realObject;
}
	
-(unsigned)length
{
	return [((NSString *)[self __realObject__]) length];
}

-(unichar)characterAtIndex:(unsigned)anIndex
{
	return [((NSString *)[self __realObject__]) characterAtIndex:anIndex];
}

-(void)getCharacters:(unichar *)buffer range:(NSRange)aRange
{
	[((NSString *)[self __realObject__]) getCharacters:buffer range:aRange];
}

#endif /* PyObjC_UNICODE_FAST_PATH */

@end /* implementation OC_PythonUnicode */
