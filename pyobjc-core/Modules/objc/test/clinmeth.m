/*
 * Helper classes for test_clinmeth
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

@interface PyObjC_ClsInst1 : NSObject {
}
- (int)instance;
- (int)both;
+ (int)both;
+ (int)clsmeth;
@end

@implementation PyObjC_ClsInst1

- (int)instance
{
    return 1;
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
@end

@interface PyObjC_ClsInst2 : PyObjC_ClsInst1 {
}
- (int)instance;
- (int)both;
+ (int)both;
+ (int)clsmeth;
@end

@implementation PyObjC_ClsInst2

- (int)instance
{
    return 10;
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
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};


static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "PyObjC_ClsInst1",
                           PyObjC_IdToPython([PyObjC_ClsInst1 class]))
        < 0) {
        return -1;
    }
    if (PyModule_AddObject(m, "PyObjC_ClsInst2",
                           PyObjC_IdToPython([PyObjC_ClsInst2 class]))
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
    .m_name = "clinmeth",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_clinmeth(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_clinmeth(void)
{
    return PyModuleDef_Init(&mod_module);
}
