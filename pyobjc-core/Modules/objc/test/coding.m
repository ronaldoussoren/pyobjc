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
+ (int)fetchInt:(NSCoder*)coder size:(NSUInteger)size;
+ (double)fetchDouble:(NSCoder*)coder;
+ (NSObject*)fetchData:(NSCoder*)coder;
+ (NSArray*)fetchArray:(NSCoder*)coder;
@end

@interface NSObject (IKnowWhatImDoing)
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
    [coder encodeBytes:(void*)"message" length:4 forKey:@"random-key"];
}

+ (int)fetchInt:(NSCoder*)coder
{
    int i;
    [[clang::suppress]] [coder decodeValueOfObjCType:@encode(int) at:&i];
    return i;
}

+ (int)fetchInt:(NSCoder*)coder size:(NSUInteger)size
{
    int i;

    if (@available(macOS 10.13, *)) {
        [[clang::suppress]] [coder decodeValueOfObjCType:@encode(int) at:&i size:size];
    } else {
        [[clang::suppress]] [coder decodeValueOfObjCType:@encode(int) at:&i];
    }
    return i;
}

+ (double)fetchDouble:(NSCoder*)coder
{
    double i;
    [[clang::suppress]] [coder decodeValueOfObjCType:@encode(double) at:&i];
    return i;
}

+ (NSObject*)fetchData:(NSCoder*)coder forKey:(NSString*)key
{
    const void* data;
    NSUInteger  length;

    data = [coder decodeBytesForKey:key returnedLength:&length];
    if (data == NULL) {
        return [NSArray arrayWithObjects:[NSNull null], @(length), nil];
    }
    return [NSData dataWithBytes:data length:length];
}

+ (NSObject*)fetchData:(NSCoder*)coder
{
    void*      data;
    NSUInteger length;

    data = [coder decodeBytesWithReturnedLength:&length];
    if (data == NULL) {
        return [NSArray arrayWithObjects:[NSNull null], @(length), nil];
    }
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

@interface OC_RaisingCoder : NSCoder {
}
@end

@implementation OC_RaisingCoder
- (void)encodeArrayOfObjCType:(const char*)type
                        count:(NSUInteger)count
                           at:(const void*)array
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}

- (void)encodeBytes:(const void*)byteaddr length:(NSUInteger)length
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}

- (void)encodeBytes:(const uint8_t*)bytes length:(NSUInteger)length forKey:(NSString*)key
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}

- (void)encodeValueOfObjCType:(const char*)type at:(const void*)addr
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}

- (void)encodeValuesOfObjCTypes:(const char*)types, ...
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}

- (void)decodeValueOfObjCType:(const char*)type at:(void*)data
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}

- (void)decodeValueOfObjCType:(const char*)type at:(void*)data size:(NSUInteger)size
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}

- (void)decodeValuesOfObjCTypes:(const char*)types, ...
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}

- (void)decodeArrayOfObjCType:(const char*)itemType
                        count:(NSUInteger)count
                           at:(void*)array
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}

- (nullable void*)decodeBytesWithReturnedLength:(NSUInteger*)lengthp
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}

- (nullable const uint8_t*)decodeBytesForKey:(NSString*)key
                              returnedLength:(nullable NSUInteger*)lengthp
{
    @throw [NSException exceptionWithName:@"raising coder" reason:nil userInfo:nil];
}
@end

@interface OC_NilBytes : NSCoder {
}
@end

@implementation OC_NilBytes
- (nullable void*)decodeBytesWithReturnedLength:(NSUInteger*)lengthp
{
    *lengthp = 42;
    return NULL;
}

- (nullable const uint8_t*)decodeBytesForKey:(NSString*)key
                              returnedLength:(nullable NSUInteger*)lengthp
{
    if (lengthp) {
        *lengthp = 21;
    }
    return NULL;
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "PyObjC_TestCodingClass",
                           PyObjC_IdToPython([PyObjC_TestCodingClass class]))
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_RaisingCoder", PyObjC_IdToPython([OC_RaisingCoder class]))
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_NilBytes", PyObjC_IdToPython([OC_NilBytes class]))
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
    return 0;
}

static struct PyModuleDef_Slot mod_slots[] = {
    {.slot = Py_mod_exec, .value = (void*)mod_exec_module},
#if PY_VERSION_HEX >= 0x030c0000
    {
        /* This extension does not use the CPython API other than initializing
         * the module, hence is safe with subinterpreters and per-interpreter
         * GILs
         */
        .slot  = Py_mod_multiple_interpreters,
        .value = Py_MOD_PER_INTERPRETER_GIL_SUPPORTED,
    },
#endif
#if PY_VERSION_HEX >= 0x030d0000
    {
        .slot  = Py_mod_gil,
        .value = Py_MOD_GIL_NOT_USED,
    },
#endif
    {/* Sentinel */
     .slot  = 0,
     .value = 0}};

static struct PyModuleDef mod_module = {
    .m_base     = PyModuleDef_HEAD_INIT,
    .m_name     = "coding",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_coding(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_coding(void)
{
    return PyModuleDef_Init(&mod_module);
}
