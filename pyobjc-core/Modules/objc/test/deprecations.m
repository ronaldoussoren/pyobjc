#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface OCTestDeprecations : NSObject {
}
- (int)method1;
- (int)method2;
- (int)method3;
- (int)method4;
- (int)method5;
- (int)method6;
- (int)method7;
- (int)method8;
- (int)method9;
- (int)method10;
- (int)method11;

- (int)method1:(int*)value;
- (int)method2:(int*)value;
- (int)method3:(int*)value;
- (int)method4:(int*)value;
- (int)method5:(int*)value;
- (int)method6:(int*)value;
- (int)method7:(int*)value;
- (int)method8:(int*)value;
- (int)method9:(int*)value;
- (int)method10:(int*)value;
- (int)method11:(int*)value;
@end

@implementation OCTestDeprecations

- (int)method1
{
    return 1;
}
- (int)method2
{
    return 2;
}
- (int)method3
{
    return 3;
}
- (int)method4
{
    return 4;
}
- (int)method5
{
    return 5;
}
- (int)method6
{
    return 6;
}
- (int)method7
{
    return 7;
}
- (int)method8
{
    return 8;
}
- (int)method9
{
    return 9;
}

- (int)method10
{
    return 10;
}
- (int)method11
{
    return 11;
}

- (int)method1:(int*)value
{
    return 1 + *value;
}
- (int)method2:(int*)value
{
    return 2 + *value;
}
- (int)method3:(int*)value
{
    return 3 + *value;
}
- (int)method4:(int*)value
{
    return 4 + *value;
}
- (int)method5:(int*)value
{
    return 5 + *value;
}
- (int)method6:(int*)value
{
    return 6 + *value;
}
- (int)method7:(int*)value
{
    return 7 + *value;
}
- (int)method8:(int*)value
{
    return 8 + *value;
}
- (int)method9:(int*)value
{
    return 9 + *value;
}
- (int)method10:(int*)value
{
    return 10 + *value;
}
- (int)method11:(int*)value
{
    return 11 + *value;
}

@end

static int
func1(void)
{
    return 1;
}
static int
func2(void)
{
    return 2;
}
static int
func3(void)
{
    return 3;
}
static int
func4(void)
{
    return 4;
}
static int
func5(void)
{
    return 5;
}
static int
func6(void)
{
    return 6;
}
static int
func7(void)
{
    return 7;
}
static int
func8(void)
{
    return 8;
}
static int
func9(void)
{
    return 9;
}
static int
func10(void)
{
    return 10;
}
static int
func11(void)
{
    return 11;
}

typedef void (*F)(void);
static struct function {
    char* name;
    F     function;
} gFunctionMap[] = {{"func1", (F)func1},   {"func2", (F)func2},   {"func3", (F)func3},
                    {"func4", (F)func4},   {"func5", (F)func5},   {"func6", (F)func6},
                    {"func7", (F)func7},   {"func8", (F)func8},   {"func9", (F)func9},
                    {"func10", (F)func10}, {"func11", (F)func11}, {NULL, NULL}};

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1;                 // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "OCTestDeprecations",
                           PyObjC_IdToPython([OCTestDeprecations class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    PyObject* v = PyCapsule_New(gFunctionMap, "objc.__inline__", NULL);
    if (v == NULL) {
        return -1;
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "function_list", v)
        < 0) {
        return -1;
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
    .m_name     = "deprecations",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_deprecations(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_deprecations(void)
{
    return PyModuleDef_Init(&mod_module);
}
