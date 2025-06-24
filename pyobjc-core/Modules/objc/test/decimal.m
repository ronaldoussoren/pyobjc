#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface OC_TestDecimal : NSObject {
}
- (int)getDecimal:(out NSDecimal*)value;
- (id)stringFromDecimal:(in NSDecimal*)value;
- (void)doubleDecimal:(inout NSDecimal*)value;

@end

@implementation OC_TestDecimal

- (int)getDecimal:(out NSDecimal*)value
{
    NSDecimalNumber* num = [NSDecimalNumber decimalNumberWithString:@"2.5"];
    *value               = [num decimalValue];
    return 1;
}

- (id)stringFromDecimal:(in NSDecimal*)value
{
    return NSDecimalString(value, nil);
}

- (void)doubleDecimal:(inout NSDecimal*)value
{
    NSDecimal tmp;
    NSDecimalAdd(&tmp, value, value, NSRoundPlain);
    *value = tmp;
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
                           "OC_TestDecimal", PyObjC_IdToPython([OC_TestDecimal class]))
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
    .m_name     = "decimal",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_decimal(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_decimal(void)
{
    return PyModuleDef_Init(&mod_module);
}
