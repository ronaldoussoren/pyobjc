#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
#include <objc/objc.h>

@interface OC_MethodCategories : NSObject {
}
@end

@implementation OC_MethodCategories

- (NSArray*)newWithInt:(int)value
{
    NSMutableArray* a = [[NSMutableArray alloc] init];
    for (int i = 0; i < value; i++) {
        [a addObject:@(value)];
    }
    return a;
}

+ (NSArray*)newWithFloat:(float)value
{
    return [[NSArray alloc] initWithObjects:[NSNumber numberWithFloat:value], nil];
}

- (NSObject*)newerValue
{
    return [[[NSObject alloc] init] autorelease];
}

+ (NSObject*)newerValue
{
    return [[[NSObject alloc] init] autorelease];
}

- (NSArray*)newAsCF __attribute__((cf_returns_retained))
{
    NSArray* value = [[NSArray alloc] init];
    CFRetain(value);
    [value release];
    return value;
}

- (NSArray*)newNotRetained __attribute__((ns_returns_not_retained))
{
    NSArray* value = [[[NSArray alloc] init] autorelease];
    return value;
}

- (CFArrayRef)newCFWithInt:(int)value
{
    NSMutableArray* a = [[NSMutableArray alloc] init];
    for (int i = 0; i < value; i++) {
        [a addObject:@(value)];
    }
    CFRetain(a);
    [a release];

    return (CFArrayRef)a;
}

+ (CFArrayRef)newCFWithFloat:(float)value
{
    NSArray* result =
        [[NSArray alloc] initWithObjects:[NSNumber numberWithFloat:value], nil];
    CFRetain(result);
    [result release];
    return (CFArrayRef)result;
}

- (CFArrayRef)newerCFValue
{
    return (CFArrayRef)[[[NSArray alloc] init] autorelease];
}

+ (CFArrayRef)newerCFValue
{
    return (CFArrayRef)[[[NSArray alloc] init] autorelease];
}

- (CFArrayRef)newAsOC
{
    NSArray* value = [[NSArray alloc] init];
    return (CFArrayRef)value;
}

- (CFArrayRef)newCFNotRetained __attribute__((cf_returns_not_retained))
{
    NSArray* value = [[[NSArray alloc] init] autorelease];
    return (CFArrayRef)value;
}

- (NSArray*)copyWithInt:(int)value
{
    NSMutableArray* a = [[NSMutableArray alloc] init];
    for (int i = 0; i < value; i++) {
        [a addObject:@(value)];
    }
    return a;
}

+ (NSArray*)copyWithFloat:(float)value
{
    return [[NSArray alloc] initWithObjects:[NSNumber numberWithFloat:value], nil];
}

- (NSObject*)copyingValue
{
    return [[[NSObject alloc] init] autorelease];
}

+ (NSObject*)copyingValue
{
    return [[[NSObject alloc] init] autorelease];
}

- (NSArray*)copyAsCF __attribute__((cf_returns_retained))
{
    NSArray* value = [[NSArray alloc] init];
    CFRetain(value);
    [value release];
    return value;
}

- (NSArray*)copyNotRetained __attribute__((ns_returns_not_retained))
{
    NSArray* value = [[[NSArray alloc] init] autorelease];
    return value;
}

- (CFArrayRef)copyCFWithInt:(int)value
{
    NSMutableArray* a = [[NSMutableArray alloc] init];
    for (int i = 0; i < value; i++) {
        [a addObject:@(value)];
    }
    CFRetain(a);
    [a release];

    return (CFArrayRef)a;
}

+ (CFArrayRef)copyCFWithFloat:(float)value
{
    NSArray* result =
        [[NSArray alloc] initWithObjects:[NSNumber numberWithFloat:value], nil];
    CFRetain(result);
    [result release];
    return (CFArrayRef)result;
}

- (CFArrayRef)copyingCFValue
{
    return (CFArrayRef)[[[NSArray alloc] init] autorelease];
}

+ (CFArrayRef)copyingCFValue
{
    return (CFArrayRef)[[[NSArray alloc] init] autorelease];
}

- (CFArrayRef)copyAsOC
{
    NSArray* value = [[NSArray alloc] init];
    return (CFArrayRef)value;
}

- (CFArrayRef)copyCFNotRetained __attribute__((cf_returns_not_retained))
{
    NSArray* value = [[[NSArray alloc] init] autorelease];
    return (CFArrayRef)value;
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
                           "OC_MethodCategories",
                           PyObjC_IdToPython([OC_MethodCategories class]))
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
    .m_name     = "methcat",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_methcat(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_methcat(void)
{
    return PyModuleDef_Init(&mod_module);
}
