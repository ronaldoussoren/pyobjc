#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface PyObjC_TestCodingClass : NSObject {
    id returnObject;
}
- (void)encodeWithCoder:(NSCoder*)coder;
- (void)runThread:(id)object;
- (id)returnObject;

+ (int)fetchInt:(NSCoder*)coder;
+ (double)fetchDouble:(NSCoder*)coder;
+ (NSData*)fetchData:(NSCoder*)coder;
+ (NSArray*)fetchArray:(NSCoder*)coder;
@end

@interface
NSObject (IKnowWhatImDoing)
- (id)call;
@end

@implementation PyObjC_TestCodingClass
- (int)_privateMethodWithArg:(float)arg
{
    return (int)arg;
}

- (void)runThread:(id)object
{
    NSObject* pool = [[NSAutoreleasePool alloc] init];
    returnObject   = [object call];
    [returnObject retain];
    [pool release];
}

- (id)returnObject
{
    return returnObject;
}

- (void)encodeWithCoder:(NSCoder*)coder
{
    double d        = 1.5;
    int    iArray[] = {3, 4, 5, 6};
    [coder encodeValueOfObjCType:@encode(double) at:&d];
    [coder encodeArrayOfObjCType:@encode(int) count:4 at:iArray];
    [coder encodeBytes:"hello world" length:11];
}

+ (int)fetchInt:(NSCoder*)coder
{
    int i;
    [coder decodeValueOfObjCType:@encode(int) at:&i];
    return i;
}

+ (double)fetchDouble:(NSCoder*)coder
{
    double i;
    [coder decodeValueOfObjCType:@encode(double) at:&i];
    return i;
}

+ (NSData*)fetchData:(NSCoder*)coder
{
    void*      data;
    NSUInteger length;

    data = [coder decodeBytesWithReturnedLength:&length];
    return [NSData dataWithBytes:data length:length];
}

+ (NSArray*)fetchArray:(NSCoder*)coder
{
    int data[10];

    [coder decodeArrayOfObjCType:@encode(int) count:10 at:data];
    return [NSArray arrayWithObjects:[NSNumber numberWithInt:data[0]],
                                     [NSNumber numberWithInt:data[1]],
                                     [NSNumber numberWithInt:data[2]],
                                     [NSNumber numberWithInt:data[3]],
                                     [NSNumber numberWithInt:data[4]],
                                     [NSNumber numberWithInt:data[5]],
                                     [NSNumber numberWithInt:data[6]],
                                     [NSNumber numberWithInt:data[7]],
                                     [NSNumber numberWithInt:data[8]],
                                     [NSNumber numberWithInt:data[9]], nil];
}

+ (NSString*)fetchObjectDescription:(NSObject*)value
{
    return [value description];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "coding", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_coding(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_coding(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1) {
        return NULL;
    }

    if (PyModule_AddObject(m, "PyObjC_TestCodingClass",
                           PyObjC_IdToPython([PyObjC_TestCodingClass class]))
        == -1) {
        return NULL;
    }

    return m;
}
