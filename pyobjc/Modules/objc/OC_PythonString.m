#include "OC_PythonString.h"
#include "pyobjc.h"
#include "objc_support.h"

@implementation OC_PythonString
+newWithPythonObject:(PyObject*)v;
{
    OC_PythonString* res = [[OC_PythonString alloc] initWithPythonObject:v];
    [res autorelease];
    return res;
}

-initWithPythonObject:(PyObject*)v;
{
    value = v;

    if (PyString_Check(value)) {
	char *buffer;
	int length;
	int result;

	result = PyString_AsStringAndSize(value, &buffer, &length);
	if(result == -1) {
	    ObjCErr_ToObjC();
	    [self release];
	    return nil; // not reached
	}
	stringValue = CFStringCreateWithCStringNoCopy(NULL,
						      buffer,
						      kCFStringEncodingUTF8,
						      kCFAllocatorNull);
	_internalRep = NULL;
    } else if (PyUnicode_Check(value)) {
	char *buffer;
	int length;
	int result;
#warning Is there a way to determine what the encoding of value is and instantiate a CFString directly?
	_internalRep = PyUnicode_AsUTF8String(value);
	result = PyString_AsStringAndSize(_internalRep, &buffer, &length);
	if(result == -1) {
	    ObjCErr_ToObjC();
	    [self release];
	    return nil;
	}

	stringValue = CFStringCreateWithCStringNoCopy(NULL,
						      buffer,
						      kCFStringEncodingUTF8,
						      kCFAllocatorNull);
    }

    Py_INCREF(value);
    
    return self;
}

-(PyObject*)__pyobjc_PythonObject__
{
	Py_INCREF(value);
	return value;
}

-(void)dealloc
{
    CFRelease(stringValue);
    Py_XDECREF(value);
    Py_XDECREF(_internalRep);
    [super dealloc];
}

- (unsigned int)length;
{
    int result;
    result = CFStringGetLength(stringValue);
    return result;
}

- (unichar)characterAtIndex:(unsigned)index;
{
    UniChar result;
    result = CFStringGetCharacterAtIndex(stringValue, index);
    return result;
}
@end
