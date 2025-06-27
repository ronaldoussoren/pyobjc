#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface OC_MutableDataHelper : NSMutableData {
    int scenario;
}
@end

@implementation OC_MutableDataHelper
+ (NSData* _Nullable)fetchBytesOf:(NSMutableData*)input
{
    const void* bytes = [input bytes];
    if (bytes == NULL) {
        return NULL;
    }
    return [NSData dataWithBytes:bytes length:[input length]];
}

+ (NSData* _Nullable)fetchMutableBytesOf:(NSMutableData*)input
{
    void* bytes = [input mutableBytes];
    if (bytes == NULL) {
        return NULL;
    }
    return [NSData dataWithBytes:bytes length:[input length]];
}

- (instancetype)initWithScenario:(int)value
{
    self = [super init];
    if (!self) {
        return nil;
    }
    scenario = value;
    return self;
}
- (NSString*)description
{
    return [NSString stringWithFormat:@"<OC_MutableDataHelper scenario=%d>", scenario];
}

- (NSUInteger)length
{
    return 0;
}

- (const void*)bytes
{
    switch (scenario) {
    case 0:
        return (void* _Nonnull)NULL;
    case 1:
        @throw [NSException exceptionWithName:@"SomeException"
                                       reason:@"Some Reason"
                                     userInfo:nil];
    default:
        abort();
    }
}

- (void*)mutableBytes
{
    switch (scenario) {
    case 0:
        return (void* _Nonnull)NULL;
    case 1:
        @throw [NSException exceptionWithName:@"SomeException"
                                       reason:@"Some Reason"
                                     userInfo:nil];
    default:
        abort();
    }
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
                           "OC_MutableDataHelper",
                           PyObjC_IdToPython([OC_MutableDataHelper class]))
        < 0) {
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
    .m_name     = "helpernsdata",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_helpernsdata(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_helpernsdata(void)
{
    return PyModuleDef_Init(&mod_module);
}

NS_ASSUME_NONNULL_END
