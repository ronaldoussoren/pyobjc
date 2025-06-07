/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface
NSObject (OC_CopyHelper)
- (void)modify;
@end

@interface OC_CopyFails : NSObject {
}
-(instancetype _Nullable)copy;
-(instancetype _Nullable)copyWithZone:(NSZone*)zone;
@end

@interface OC_CopyHelper : NSObject {
}
+ (NSObject<NSCopying>*)doCopySetup:(Class)aClass;
+ (NSObject*)newObjectOfClass:(Class)aClass;
@end

@implementation OC_CopyHelper
+ (NSObject<NSCopying>*)doCopySetup:(Class)aClass
{
    NSObject<NSCopying>* tmp;
    NSObject<NSCopying>* retval;

    tmp = (NSObject<NSCopying>*)[[aClass alloc] init];
    [tmp modify];

    retval = [tmp copyWithZone:nil];
    [tmp release];
    return [retval autorelease];
}

+ (NSObject*)newObjectOfClass:(Class)aClass
{
    return [[aClass alloc] init];
}
@end

@interface OC_CopyBase : NSObject <NSCopying> {
    int intVal;
}
- (instancetype)init;
- (instancetype)initWithInt:(int)intVal;
- (int)intVal;
- (void)setIntVal:(int)val;
- (instancetype)copyWithZone:(NSZone*)zone;
@end

@implementation OC_CopyBase
- (instancetype)init
{
    return [self initWithInt:0];
}

- (instancetype)initWithInt:(int)value
{
    self = [super init];
    if (self == nil) // LCOV_BR_EXCL_LINE
        return nil; // LCOV_EXCL_LINE

    intVal = value;
    return self;
}

- (int)intVal
{
    return intVal;
}

- (void)setIntVal:(int)val
{
    intVal = val;
}

#pragma GCC diagnostic   ignored "-Wdeprecated-declarations"
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

- (instancetype)copyWithZone:(NSZone*)zone
{
    return NSCopyObject(self, 0, zone);
}
@end

@implementation OC_CopyFails
-(instancetype _Nullable)copy
{
    return nil;
}

-(instancetype _Nullable)copyWithZone:(NSZone*)zone
{
    (void)&zone;
    return nil;
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_CopyHelper", PyObjC_IdToPython([OC_CopyHelper class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_CopyBase", PyObjC_IdToPython([OC_CopyBase class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_CopyFails", PyObjC_IdToPython([OC_CopyFails class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
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
    .m_name = "copying",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_copying(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_copying(void)
{
    return PyModuleDef_Init(&mod_module);
}
