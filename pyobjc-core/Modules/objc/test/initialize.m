/*
 * This module is used in the unittests for object initialize.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

#if __has_feature(c_atomic)
static _Atomic int numUninitialized = 0;
#else
#error "Needs work"
static int numUninitialized = 0;
#endif

@interface OC_TestInitialize : NSObject {
    int isInitialized;
}
- (instancetype)init;
- (instancetype)retain;
- (void)release;
- (instancetype)autorelease;
- (int)isInitialized;
+ (int)numUninitialized;
- (id)dummy;
+ (id)makeInstance;

/* completely unrelated ... */
- (oneway void)onewayVoidMethod;

@end

@implementation OC_TestInitialize

- (instancetype)init
{
    self = [super init];
    if (!self)
        return self;

    isInitialized = 1;
    return self;
}

- (instancetype)retain
{
    if (!isInitialized) {
        numUninitialized++;
    }
    return [super retain];
}

- (void)release
{
    if (!isInitialized) {
        numUninitialized++;
    }
    [super release];
}

- (instancetype)autorelease
{
    if (!isInitialized) {
        numUninitialized++;
    }
    return [super autorelease];
}

- (int)isInitialized
{
    return isInitialized;
}

+ (int)numUninitialized
{
    return numUninitialized;
}

- (id)dummy
{
    return @"hello";
}

+ (id)makeInstance
{
    return [[[self alloc] init] autorelease];
}

- (oneway void)onewayVoidMethod
{
    isInitialized = -1;
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
                           "OC_TestInitialize",
                           PyObjC_IdToPython([OC_TestInitialize class]))
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
    .m_name     = "initialize",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_initialize(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_initialize(void)
{
    return PyModuleDef_Init(&mod_module);
}
