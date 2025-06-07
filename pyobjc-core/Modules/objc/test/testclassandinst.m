/*
 * NOTE: PyObjC_TestClassAndInstance is a class that can't be created
 *      from Python but ends up in some fun places like NSWindow
 */

#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>

#ifndef GNU_RUNTIME
#include <objc/objc-runtime.h>
#endif

@interface PyObjC_TestUnallocatable : NSObject {
}
@end

@implementation PyObjC_TestUnallocatable
+ (id)allocWithZone:(NSZone*)zone
{
    (void)&zone; /* Force use */
    return nil;
}
@end

@interface PyObjC_TestClassAndInstance : NSObject {
}

+ (BOOL)isInstance;
- (BOOL)isInstance;
@end

@implementation PyObjC_TestClassAndInstance
+ (BOOL)isInstance
{
    return NO;
}
- (BOOL)isInstance
{
    return YES;
}
@end

/* Python glue */
static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_EXCL_LINE
                "PyObjC_TestClassAndInstance",
                           PyObjC_IdToPython([PyObjC_TestClassAndInstance class]))
        < 0) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_EXCL_LINE
                "PyObjC_TestUnallocatable",
                           PyObjC_IdToPython([PyObjC_TestUnallocatable class]))
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
    .m_name = "testclassandinst",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_testclassandinst(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_testclassandinst(void)
{
    return PyModuleDef_Init(&mod_module);
}
