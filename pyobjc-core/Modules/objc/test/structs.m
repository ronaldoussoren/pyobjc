/*
 * Helper methods struct tests (objc.test.test_struct)
 */
#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

struct FooStruct {
    int first;
    int second;
};

@interface OC_StructTest : NSObject {
}
+ (struct FooStruct)createWithFirst:(int)first andSecond:(int)second;
+ (int)sumFields:(struct FooStruct)foo;
- (NSObject*)arrayOf4Structs:(struct FooStruct[4])argument;

+ (NSObject*)callArrayOf4Structs:(OC_StructTest*)object;
@end

@implementation OC_StructTest
+ (struct FooStruct)createWithFirst:(int)first andSecond:(int)second
{
    struct FooStruct f;
    f.first  = first;
    f.second = second;
    return f;
}

+ (int)sumFields:(struct FooStruct)foo
{
    return foo.first + foo.second;
}

+ (NSObject*)callArrayOf4Structs:(OC_StructTest*)object
{
    static struct FooStruct structs[4] = {
        {1, 2},
        {3, 4},
        {5, 6},
        {7, 8},
    };

    return [object arrayOf4Structs:structs];
}
- (NSObject*)arrayOf4Structs:(struct FooStruct[4])argument
{
    return [NSData dataWithBytes:(void*)argument length:4 * sizeof(*argument)];
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                "OC_StructTest", PyObjC_IdToPython([OC_StructTest class]))
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
    .m_name = "structs",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_structs(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_structs(void)
{
    return PyModuleDef_Init(&mod_module);
}
