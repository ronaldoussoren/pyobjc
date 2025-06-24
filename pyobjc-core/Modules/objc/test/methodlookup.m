/*
 * Helper classes for test_methodlookup
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface PyObjC_MethodLookup1 : NSObject {
}
- (int)instance;
- (int)instance2;
- (int)instance3;
- (int)instance4;
- (int)instance5;
- (int)both;
+ (int)both;
+ (int)clsmeth;
+ (int)clsmeth2;
+ (int)clsmeth3;
+ (int)clsmeth4;
+ (int)clsmeth5;

+ (id)OC_description;
- (id)OC_description;
- (int)pyobjc__instanceCount;
+ (int)pyobjc__classCount;
- (id)pyobjc_setObject:(id)o forKey:(id)k;
+ (id)pyobjc_setObject:(id)o forKey:(id)k;
@end

@implementation PyObjC_MethodLookup1

- (int)instance
{
    return 1;
}

- (int)instance2
{
    return -1;
}

- (int)instance3
{
    return -1;
}

- (int)instance4
{
    return -1;
}

- (int)instance5
{
    return -1;
}

- (int)both
{
    return 2;
}

+ (int)both
{
    return 3;
}

+ (int)clsmeth
{
    return 4;
}

+ (int)clsmeth2
{
    return 4;
}
+ (int)clsmeth3
{
    return 4;
}
+ (int)clsmeth4
{
    return 4;
}
+ (int)clsmeth5
{
    return 4;
}
+ (id)OC_description
{
    return @"class description";
}

- (id)OC_description
{
    return @"method description";
}

- (int)pyobjc__instanceCount
{
    return 42;
}

+ (int)pyobjc__classCount
{
    return 99;
}

- (id)pyobjc_setObject:(id)o forKey:(id)k
{
    return [NSArray arrayWithObjects:o, k, nil];
}

+ (id)pyobjc_setObject:(id)o forKey:(id)k
{
    return [NSArray arrayWithObjects:k, o, nil];
}

@end

@interface PyObjC_MethodLookup2 : PyObjC_MethodLookup1 {
}
- (int)instance;
- (int)instance3;
- (int)both;
+ (int)both;
+ (int)clsmeth;
+ (int)clsmeth3;
@end

@implementation PyObjC_MethodLookup2

- (int)instance
{
    return 10;
}

- (int)instance3
{
    return -10;
}

- (int)both
{
    return 20;
}

+ (int)both
{
    return 30;
}

+ (int)clsmeth
{
    return 40;
}

+ (int)clsmeth3
{
    return -40;
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
                           "PyObjC_MethodLookup1",
                           PyObjC_IdToPython([PyObjC_MethodLookup1 class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "PyObjC_MethodLookup2",
                           PyObjC_IdToPython([PyObjC_MethodLookup2 class]))
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
    .m_name     = "methodlookup",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_methodlookup(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_methodlookup(void)
{
    return PyModuleDef_Init(&mod_module);
}
