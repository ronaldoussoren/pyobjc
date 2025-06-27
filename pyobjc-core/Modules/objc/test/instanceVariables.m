/*
 * This module is used in the unittests for object identity.
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

@interface ClassWithVariables : NSObject {
    int       intValue;
    double    floatValue;
    char      charValue;
    char*     strValue;
    NSRect    rectValue;
    NSObject* nilValue;
    PyObject* pyValue;
    NSObject* objValue;
}
- (instancetype)init;
- (void)dealloc;
@end

@implementation ClassWithVariables
- (instancetype)init
{
    self = [super init];
    if (self == nil) // LCOV_BR_EXCL_LINE
        return nil;  // LCOV_EXCL_LINE

    intValue   = 42;
    floatValue = -10.055;
    charValue  = 'a';
    strValue   = "hello world";
    rectValue  = NSMakeRect(1, 2, 3, 4);
    nilValue   = nil;
    PyObjC_BEGIN_WITH_GIL
        pyValue =
            PySlice_New(PyLong_FromLong(1), PyLong_FromLong(10), PyLong_FromLong(4));
    PyObjC_END_WITH_GIL
    objValue = [[NSObject alloc] init];
    return self;
}

- (void)dealloc
{
    PyObjC_BEGIN_WITH_GIL
        Py_XDECREF(pyValue);
    PyObjC_END_WITH_GIL
    [objValue release];
    [nilValue release];
    [super dealloc];
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
                           "ClassWithVariables",
                           PyObjC_IdToPython([ClassWithVariables class]))
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
    .m_name     = "instanceVariables",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_instanceVariables(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_instanceVariables(
    void)
{
    return PyModuleDef_Init(&mod_module);
}
