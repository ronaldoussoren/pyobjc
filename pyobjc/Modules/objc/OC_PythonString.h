#ifndef OC_PythonString_h
#define OC_PythonString_h

#import <CoreFoundation/CoreFoundation.h>
#import <Foundation/NSString.h>

/*
 * OC_PythonString - Objective-C proxy class for Python strings
 *
 * Instances of this class are used as proxies for Python strings 
 * when these are passed to Objective-C code. Because this class is
 * a subclass of NSString Python sequences can be used everywhere
 * where NSString is used.  Python strings are immutable.
 */

@interface OC_PythonString:NSString
{
    PyObject* value;
    PyObject* _internalRep;
    CFStringRef stringValue;
}

+newWithPythonObject:(PyObject*)value;
-initWithPythonObject:(PyObject*)value;
-(void)dealloc;
-(PyObject*)__pyobjc_PythonObject__;
@end
#endif
