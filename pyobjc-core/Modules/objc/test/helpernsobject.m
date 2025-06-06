#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface OC_AllocRaises : NSObject {
}
@end

@implementation OC_AllocRaises
+ (instancetype)alloc
{
    @throw [NSException exceptionWithName:@"SomeException"
                                   reason:@"Some Reason"
                                 userInfo:nil];
}

+ (instancetype)invokeAlloc:(Class)cls  NS_RETURNS_RETAINED
{
    return [cls alloc];
}

+(void)invoke:(SEL)sel on:(NSObject*)object
{
    if (sel_isEqual(sel, @selector(retain))) {
        (void)[object retain];
    } else if (sel_isEqual(sel, @selector(release))) {
        (void)[object release];
    } else if (sel_isEqual(sel, @selector(dealloc))) {
        (void)[object dealloc];
    }
}

@end

@interface OC_RefcountRaises : NSObject {
    int scenario;
}
@end

@implementation OC_RefcountRaises
- (instancetype)init
{
    self = [super init];
    if (!self)
        return self;
    scenario = 0;
    return self;
}
- (void)setScenario:(int)value
{
    scenario = value;
}

- (instancetype)retain
{
    if (scenario == 1) {
        scenario = 0;
        @throw [NSException exceptionWithName:@"SomeException"
                                       reason:@"Some Reason"
                                     userInfo:nil];
    }
    return [super retain];
}

- (oneway void)release
{
    if (scenario == 2) {
        scenario = 0;
        @throw [NSException exceptionWithName:@"SomeException"
                                       reason:@"Some Reason"
                                     userInfo:nil];
    }
    [super release];
}

- (void)dealloc
{
    if (scenario == 3) {
        scenario = 0;
        @throw [NSException exceptionWithName:@"SomeException"
                                       reason:@"Some Reason"
                                     userInfo:nil];
    }
    if (self == nil)
        [super dealloc];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "OC_AllocRaises", PyObjC_IdToPython([OC_AllocRaises class]))
        < 0) {
        return -1;
    }
    if (PyModule_AddObject(m, "OC_RefcountRaises",
                           PyObjC_IdToPython([OC_RefcountRaises class]))
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
    .m_name = "helpernsobject",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_helpernsobject(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_helpernsobject(void)
{
    return PyModuleDef_Init(&mod_module);
}

NS_ASSUME_NONNULL_END
