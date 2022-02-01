#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_BadString : NSString {
}
@end

@implementation OC_BadString
- (NSUInteger)length
{
    return 2;
}
- (unichar)characterAtIndex:(NSUInteger)index
{
    if (index == 0) {
        return (unichar)'a';
    }
    @throw [NSException exceptionWithName:@"SomeException"
                                   reason:@"Some Reason"
                                 userInfo:nil];
}
@end

@interface OC_StringInt : NSObject {
}
@end

@implementation OC_StringInt

+ (NSString*)getLowSurrogate
{
    return [NSString stringWithFormat:@"%C", 0xdccc];
}

+ (NSString*)getHighSurrogate
{
    return [NSString stringWithFormat:@"%C", 0xdbbb];
}

+ (NSString*)getBadPair
{
    return [NSString stringWithFormat:@"%C%C", 0xdc0b, 0xdb0b];
}

+ (NSString*)getCorrectPair
{
    return [NSString stringWithFormat:@"%C%C", 0xdb0b, 0xdc0b];
}

+ (NSString*)getExtremePair
{
    return [NSString stringWithFormat:@"%C%C", 0xdbff, 0xdfff];
}

+ (id)createNonUTF8WithClass:(Class)stringClass
{
#define BYTES "hello world"
    return [[[stringClass alloc] initWithBytes:BYTES
                                        length:sizeof(BYTES) - 1
                                      encoding:NSASCIIStringEncoding] autorelease];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "stringint", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_stringint(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_stringint(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_StringInt", PyObjC_IdToPython([OC_StringInt class]))
        < 0) {
        return NULL;
    }
    if (PyModule_AddObject(m, "OC_BadString", PyObjC_IdToPython([OC_BadString class]))
        < 0) {
        return NULL;
    }

    return m;
}
