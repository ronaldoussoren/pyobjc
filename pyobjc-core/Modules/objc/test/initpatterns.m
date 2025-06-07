#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_InitPatterns : NSObject {
}
@end

@interface OC_InitReturnsSelf : NSObject {
}
@end

@implementation OC_InitReturnsSelf
- (instancetype)init
{
    return [super init];
}
@end


@interface OC_InitReturnsNil : NSObject {
}
@end

@implementation OC_InitReturnsNil
- (instancetype)init
{
    [self release];
    return nil;
}
@end


@interface OC_InitReturnsOther : NSObject {
}
@end

@implementation OC_InitReturnsOther
- (instancetype)init
{
    [self release];
    self = [OC_InitReturnsOther alloc];
    return [super init];
}
@end


@interface OC_AllocSingleton : NSObject {
}
@end

@implementation OC_AllocSingleton
static OC_AllocSingleton* singleton = nil;

+ (NSInteger)singletonRetainCount
{
    if (singleton == nil) {
        singleton = [super alloc];
    }
    return [singleton retainCount];
}

+ (instancetype)alloc
{

   if (singleton == nil) {
       singleton = [super alloc];
   }
   return [singleton retain];
}
+(instancetype) NS_RETURNS_RETAINED allocsuper
{
    return [super alloc];
}

- (instancetype)init
{
    [self release];
    self = [OC_AllocSingleton allocsuper];
    return [super init];
}
@end

@interface OC_AllocSingletonInitNil : NSObject {
}
@end

@implementation OC_AllocSingletonInitNil
static OC_AllocSingletonInitNil* singleton_nil = nil;

+ (NSInteger)singletonRetainCount
{
    if (singleton_nil == nil) {
        singleton_nil = [super alloc];
    }
    return [singleton_nil retainCount];
}

+ (instancetype)alloc
{

   if (singleton_nil == nil) {
       singleton_nil = [super alloc];
   }
   return [singleton_nil retain];
}
- (instancetype)init
{
    [self release];
    return nil;
}
@end

@implementation OC_InitPatterns
+(id)newValueFor:(Class)cls
{
    return [[cls alloc] init];
}

+(id)callInitOn:(id)value
{
    /* init steals a reference to self and returns a new reference */
    [value retain];
    return [[value init] autorelease];;
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_InitReturnsSelf", PyObjC_IdToPython([OC_InitReturnsSelf class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_InitReturnsNil", PyObjC_IdToPython([OC_InitReturnsNil class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_InitReturnsOther", PyObjC_IdToPython([OC_InitReturnsOther class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_AllocSingleton", PyObjC_IdToPython([OC_AllocSingleton class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_AllocSingletonInitNil", PyObjC_IdToPython([OC_AllocSingletonInitNil class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_InitPatterns", PyObjC_IdToPython([OC_InitPatterns class]))
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
    .m_name = "initpatterns",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_initpatterns(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_initpatterns(void)
{
    return PyModuleDef_Init(&mod_module);
}
