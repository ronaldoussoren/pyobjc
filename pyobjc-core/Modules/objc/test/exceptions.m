/*
 * This module is used in test_exceptions
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

static NSString*
addSomeUnicode(NSString* input)
{
    return [NSString stringWithFormat:@"%@%C%C", input, (short)0x1234, (short)0x2049];
}

@interface PyObjCTestExceptions : NSObject {
}
- (void)raiseSimple;
- (void)raiseSimpleWithInfo;
- (void)raiseUnicodeName;
- (void)raiseUnicodeReason;
- (void)raiseUnicodeWithInfo;
- (void)raiseAString;
- (void)raiseWithString:(NSString*)name;
@end

@implementation PyObjCTestExceptions

- (void)raiseSimple
{
    [NSException raise:@"SimpleException" format:@"hello world"];
}

- (void)raiseWithString:(NSString*)name
{
    [NSException raise:name format:@"raised %@", name];
}

- (void)raiseSimpleWithInfo
{
    [[NSException
        exceptionWithName:@"InfoException"
                   reason:@"Reason string"
                 userInfo:[NSDictionary dictionaryWithObjectsAndKeys:@"value1", @"key1",
                                                                     @"value2", @"key2",
                                                                     NULL]] raise];
}

- (void)raiseUnicodeName
{
    [NSException raise:addSomeUnicode(@"SimpleException") format:@"hello world"];
}

- (void)raiseUnicodeReason
{
    [NSException raise:@"SimpleException" format:@"%@", addSomeUnicode(@"hello world")];
}

- (void)raiseUnicodeWithInfo
{
    [[NSException
        exceptionWithName:addSomeUnicode(@"InfoException")
                   reason:addSomeUnicode(@"Reason string")
                 userInfo:[NSDictionary
                              dictionaryWithObjectsAndKeys:addSomeUnicode(@"value1"),
                                                           addSomeUnicode(@"key1"),
                                                           addSomeUnicode(@"value2"),
                                                           addSomeUnicode(@"key2"), NULL]]
        raise];
}

- (void)raiseAString
{
    @throw @"thrown string";
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }
    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "PyObjCTestExceptions",
                           PyObjC_IdToPython([PyObjCTestExceptions class]))
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
    .m_name = "exceptions",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_exceptions(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_exceptions(void)
{
    return PyModuleDef_Init(&mod_module);
}
