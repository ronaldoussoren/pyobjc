#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_GenericNew : NSObject {
    NSObject* value;
}
@end
@interface OC_GenericNewChild : OC_GenericNew {
}
@end
@interface OC_GenericNewChild2 : OC_GenericNewChild {
}
@end
@interface OC_GenericNewChild3 : OC_GenericNew {
}
@end

@implementation OC_GenericNew
- (NSObject*)value
{
    return value;
}

- (instancetype)init
{
    self = [super init];
    if (!self)
        return nil;

    value = nil;
    return self;
}

+ (instancetype)valueWithAddress:(NSObject*)address
{
    OC_GenericNew* value = [[OC_GenericNew alloc] init];
    value->value         = [address retain];
    return [value autorelease];
}

- (instancetype)initWithValue:(NSObject*)v
{
    self = [super init];
    if (!self)
        return nil;

    value = [v retain];
    return self;
}

- (instancetype)initWithURL:(NSObject*)v
{
    self = [super init];
    if (!self)
        return nil;

    value = [v retain];
    return self;
}

- (instancetype)initWithFirst:(NSObject*)first second:(NSObject*)second
{
    self = [super init];
    if (!self)
        return nil;

    value = [[NSArray alloc] initWithObjects:@"first-second", first, second, nil];
    return self;
}
@end

@implementation OC_GenericNewChild

- (instancetype)initWithX:(NSObject*)x y:(NSObject*)y
{
    self = [super init];
    if (!self)
        return nil;

    value = [[NSArray alloc] initWithObjects:@"x-y", x, y, nil];
    return self;
}
@end

@implementation OC_GenericNewChild2

- (instancetype)initWithX:(NSObject*)x y:(NSObject*)y z:(NSObject*)z
{
    self = [super init];
    if (!self)
        return nil;

    value = [[NSArray alloc] initWithObjects:@"x-y-z", x, y, z, nil];
    return self;
}
@end

@implementation OC_GenericNewChild3
+ (instancetype)valueWithA:(NSObject*)a b:(NSObject*)b
{
    OC_GenericNewChild3* result = [[super alloc] init];
    result->value               = [[NSArray alloc] initWithObjects:@"A-B", a, b, nil];
    return [result autorelease];
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
                           "OC_GenericNew", PyObjC_IdToPython([OC_GenericNew class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_GenericNewChild",
                           PyObjC_IdToPython([OC_GenericNewChild class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_GenericNewChild2",
                           PyObjC_IdToPython([OC_GenericNewChild2 class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OC_GenericNewChild3",
                           PyObjC_IdToPython([OC_GenericNewChild3 class]))
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
    .m_name     = "genericnew",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_genericnew(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_genericnew(void)
{
    return PyModuleDef_Init(&mod_module);
}
