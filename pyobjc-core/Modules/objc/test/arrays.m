#include "Python.h"
#include "pyobjc-api.h"
#include <stdarg.h>

#import <Foundation/Foundation.h>

struct ArrayStruct {
    int first;
    int second;
};

typedef int                int_array_t[4];
typedef struct ArrayStruct struct_array_t[4];

@interface OC_ArrayTest : NSObject {
}
- (NSObject*)arrayOf4Ints:(int_array_t)array;
- (NSObject*)arrayOf4IntsIn:(in int_array_t)array;
- (NSObject*)arrayOf4IntsInOut:(inout int_array_t)array;
- (void)arrayOf4IntsOut:(out int_array_t)array;

- (NSObject*)arrayOf4Structs:(struct_array_t)array;
- (NSObject*)arrayOf4StructsIn:(in struct_array_t)array;
- (NSObject*)arrayOf4StructsInOut:(inout struct_array_t)array;
- (void)arrayOf4StructsOut:(out struct_array_t)array;

+ (NSObject*)callArrayOf4Ints:(OC_ArrayTest*)object;
+ (NSObject*)callArrayOf4IntsOut:(OC_ArrayTest*)object;
+ (NSObject*)callArrayOf4Structs:(OC_ArrayTest*)object;
+ (NSObject*)callArrayOf4StructsOut:(OC_ArrayTest*)object;
@end

@implementation OC_ArrayTest

- (NSObject*)arrayOf4Ints:(int_array_t)array
{
    return [NSArray arrayWithObjects:[NSNumber numberWithInt:array[0]],
                                     [NSNumber numberWithInt:array[1]],
                                     [NSNumber numberWithInt:array[2]],
                                     [NSNumber numberWithInt:array[3]], nil];
}
- (NSObject*)arrayOf4IntsIn:(in int_array_t)array
{
    return [NSArray arrayWithObjects:[NSNumber numberWithInt:array[0]],
                                     [NSNumber numberWithInt:array[1]],
                                     [NSNumber numberWithInt:array[2]],
                                     [NSNumber numberWithInt:array[3]], nil];
}
- (NSObject*)arrayOf4IntsInOut:(inout int_array_t)array
{
    NSObject* result = [NSArray arrayWithObjects:[NSNumber numberWithInt:array[0]],
                                                 [NSNumber numberWithInt:array[1]],
                                                 [NSNumber numberWithInt:array[2]],
                                                 [NSNumber numberWithInt:array[3]], nil];

    array[0] += 42;
    array[1] += 42;
    array[2] += 42;
    array[3] += 42;

    return result;
}
- (void)arrayOf4IntsOut:(out int_array_t)array
{
    array[0] = 99;
    array[1] = 100;
    array[2] = 102;
    array[3] = 110;
}

- (NSObject*)arrayOf4Structs:(struct_array_t)array
{
    return [NSArray
        arrayWithObjects:[NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[0].first],
                                              [NSNumber numberWithInt:array[0].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[1].first],
                                              [NSNumber numberWithInt:array[1].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[2].first],
                                              [NSNumber numberWithInt:array[2].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[3].first],
                                              [NSNumber numberWithInt:array[3].second],
                                              nil],
                         nil];
}
- (NSObject*)arrayOf4StructsIn:(in struct_array_t)array
{
    return [NSArray
        arrayWithObjects:[NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[0].first],
                                              [NSNumber numberWithInt:array[0].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[1].first],
                                              [NSNumber numberWithInt:array[1].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[2].first],
                                              [NSNumber numberWithInt:array[2].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[3].first],
                                              [NSNumber numberWithInt:array[3].second],
                                              nil],
                         nil];
}
- (NSObject*)arrayOf4StructsInOut:(inout struct_array_t)array
{
    NSObject* result = [NSArray
        arrayWithObjects:[NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[0].first],
                                              [NSNumber numberWithInt:array[0].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[1].first],
                                              [NSNumber numberWithInt:array[1].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[2].first],
                                              [NSNumber numberWithInt:array[2].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[3].first],
                                              [NSNumber numberWithInt:array[3].second],
                                              nil],
                         nil];

    int i;
    for (i = 0; i < 4; i++) {
        array[i].first += 42;
        array[i].second -= 42;
    }

    return result;
}
- (void)arrayOf4StructsOut:(out struct_array_t)array
{
    int i;
    for (i = 0; i < 4; i++) {
        array[i].first  = 1 + i * i;
        array[i].second = -4 - i * i * i;
    }
}

+ (NSObject*)callArrayOf4Ints:(OC_ArrayTest*)object
{
    int_array_t array = {1, 2, 3, 4};
    return [object arrayOf4Ints:array];
}

+ (NSObject*)callArrayOf4IntsOut:(OC_ArrayTest*)object
{
    int_array_t array;
    [object arrayOf4IntsOut:array];
    return [NSArray arrayWithObjects:[NSNumber numberWithInt:array[0]],
                                     [NSNumber numberWithInt:array[1]],
                                     [NSNumber numberWithInt:array[2]],
                                     [NSNumber numberWithInt:array[3]], nil];
}

+ (NSObject*)callArrayOf4Structs:(OC_ArrayTest*)object
{
    struct_array_t array = {{1, 2}, {3, 4}, {5, 6}, {7, 8}};
    return [object arrayOf4Structs:array];
}

+ (NSObject*)callArrayOf4StructsOut:(OC_ArrayTest*)object
{
    struct_array_t array;
    [object arrayOf4StructsOut:array];

    return [NSArray
        arrayWithObjects:[NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[0].first],
                                              [NSNumber numberWithInt:array[0].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[1].first],
                                              [NSNumber numberWithInt:array[1].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[2].first],
                                              [NSNumber numberWithInt:array[2].second],
                                              nil],
                         [NSArray
                             arrayWithObjects:[NSNumber numberWithInt:array[3].first],
                                              [NSNumber numberWithInt:array[3].second],
                                              nil],
                         nil];
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};


static int mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "OC_ArrayTest", PyObjC_IdToPython([OC_ArrayTest class]))
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
    .m_name = "arrays",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = mod_methods,
    .m_slots = mod_slots,
    .m_traverse = NULL,
    .m_clear = NULL,
    .m_free = NULL,
};

PyObject* PyInit_arrays(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_arrays(void)
{
    return PyModuleDef_Init(&mod_module);
}
