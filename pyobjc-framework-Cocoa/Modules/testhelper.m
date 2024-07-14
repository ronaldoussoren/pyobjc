#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface PyObjC_TestClass3 : NSObject {
}
+ createAHostWithAddress:(NSString*)address;
+ makeACopy:source;
+ makeDataWithBytes:(Class)cls method:(int)i;
+ makeDictFromClass:(Class)cls method:(int)i;
+ getBytes:(NSData*)data;
+ keyValue:(int)idx forObject:value key:id;
+ (void)setKeyValue:(int)idx forObject:object key:key value:value;
@end

@implementation PyObjC_TestClass3

+ createAHostWithAddress:(NSString*)address
{
    return [NSHost hostWithAddress:address];
}

+ getBytes:(NSData*)data
{
    const void* bytes = [data bytes];

    if (bytes == NULL) {
        return nil;
    } else {
        return [NSData dataWithBytes:bytes length:[data length]];
    }
}

+ makeDataWithBytes:(Class)cls method:(int)i
{
    if (i == 0) {
        return [cls dataWithBytes:"hello world" length:sizeof("hello world") - 1];
    } else {
        id o = [cls alloc];
        return [o initWithBytes:"hello world" length:sizeof("hello world") - 1];
    }
}

+ makeDictFromClass:(Class)cls method:(int)i
{
    id objects[4];
    id keys[4];

    objects[0] = [[NSObject alloc] init];
    objects[1] = [[NSObject alloc] init];
    objects[2] = [[NSObject alloc] init];
    objects[3] = [[NSObject alloc] init];

    keys[0] = [[NSObject alloc] init];
    keys[1] = [[NSObject alloc] init];
    keys[2] = [[NSObject alloc] init];
    keys[3] = [[NSObject alloc] init];

    if (i == 0) {
        return [cls dictionaryWithObjects:objects forKeys:keys count:4];
    } else {
        return [[cls alloc] initWithObjects:objects forKeys:keys count:4];
    }
}

+ makeACopy:source
{
    id theCopy;
    id pool;

    /* Copy the source, bracketed by the creation and
     * destruction of an autorelease pool. This should
     * cause a core-dump if the copy is not a 'new'
     * object.
     */
    pool    = [[NSAutoreleasePool alloc] init];
    theCopy = [source copy];
    [pool release];
    pool = nil;

    return theCopy;
}

+ keyValue:(int)idx forObject:object key:key
{
    switch (idx) {
    case 0:
        return [object valueForKey:key];
    case 1:
        return [object valueForKeyPath:key];
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
    case 2:
        return [object storedValueForKey:key];
    case 3:
        return [object valuesForKeys:key];
#pragma clang diagnostic pop
    }
    return nil;
}

+ (void)setKeyValue:(int)idx forObject:object key:key value:value
{
    switch (idx) {
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
    case 0:
        [object takeValue:value forKey:key];
        break;
    case 1:
        [object takeValue:value forKeyPath:key];
        break;
    case 2:
        [object takeStoredValue:value forKey:key];
        break;
    case 3:
        [object takeValuesFromDictionary:value];
        break;
    case 4:
        [object setValue:value forKey:key];
        break;
    case 5:
        [object setValue:value forKeyPath:key];
        break;
    case 6:
        [object setValuesForKeysWithDictionary:value];
        break;
    }
}

+ (NSObject*)createObservedOfClass:(Class)class
                          observer:(NSObject*)obj
                           keyPath:(NSString*)path
{
    NSObject* o = [[class alloc] init];
    [o addObserver:obj
        forKeyPath:path
           options:NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld
           context:0];
    return o;
}
@end

@interface PyObjC_TestClass4 : NSObject {
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
- call;
@end

@implementation PyObjC_TestClass4
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

- (id)returnObject;
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



static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) == -1)
        return -1;

    if (PyModule_AddObject(m, "PyObjC_TestClass3",
                       PyObjC_IdToPython([PyObjC_TestClass3 class])) < 0) {
        return -1;
    if (PyModule_AddObject(m, "PyObjC_TestClass4",
                       PyObjC_IdToPython([PyObjC_TestClass4 class])) < 0) {
        return -1;
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {
        .slot = Py_mod_exec,
        .value = (void*)mod_exec_module
    },
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        /* The code in this extension should be safe to use without the GIL */
        .slot = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {  /* Sentinel */
        .slot = 0,
        .value = 0
    }
};

static struct PyModuleDef mod_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "testhelper",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_testhelper(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_testhelper(void)
{
    return PyModuleDef_Init(&mod_module);
}
