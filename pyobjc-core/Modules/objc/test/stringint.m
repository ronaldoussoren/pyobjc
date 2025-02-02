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

+ (NSString*)getCharactersOn:(NSString*)value
{
    unichar buffer[1024];

    if ([value length] > 1023) {
        return nil;
    }

    [value getCharacters:buffer];
    return [NSString stringWithCharacters:buffer length:[value length]];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "OC_StringInt", PyObjC_IdToPython([OC_StringInt class]))
        < 0) {
        return -1;
    }
    if (PyModule_AddObject(m, "OC_BadString", PyObjC_IdToPython([OC_BadString class]))
        < 0) {
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
    .m_name = "stringint",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_stringint(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_stringint(void)
{
    return PyModuleDef_Init(&mod_module);
}
