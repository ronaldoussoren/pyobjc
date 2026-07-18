/*
 * This file is generated using Tools/generate-helpers-vector.py
 *
 *     ** DO NOT EDIT **
 */
#include "Python.h"
#include "pyobjc-api.h"
#import <simd/simd.h>
#include <stdarg.h>

#import <Foundation/Foundation.h>

#import <AppKit/AppKit.h>

#if PyObjC_BUILD_RELEASE >= 1011
#import <GameplayKit/GameplayKit.h>
#import <ModelIO/ModelIO.h>
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1013
#import <MetalPerformanceShaders/MetalPerformanceShaders.h>
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BULD_RELEASE < 1013
#define simd_uchar16 vector_uchar16
#define simd_float2 vector_float2
#define simd_float3 vector_float3
#define simd_float4 vector_float4
#define simd_double2 vector_double2
#define simd_double3 vector_double3
#define simd_double4 vector_double4
#define simd_uint2 vector_uint2
#define simd_uint3 vector_uint3
#define simd_int2 vector_int2
#define simd_int4 vector_int4
#define simd_float2x2 matrix_float2x2
#define simd_float3x3 matrix_float3x3
#define simd_float4x4 matrix_float4x4
#define simd_double4x4 matrix_double4x4
#endif /*  PyObjC_BULD_RELEASE < 1013 */

static PyObject* values      = NULL;
static BOOL      shouldRaise = NO;

static BOOL
f_shouldRaise(void)
{
    return shouldRaise;
}

static void
f_clearRaise(void)
{
    shouldRaise = NO;
}

static void
f_setRaise(void)
{
    shouldRaise = YES;
}

static id _Nullable f_storedvalue(void)
{
    id result;

    PyObjC_BEGIN_WITH_GIL
        if (depythonify_python_object(values, &result)) {
            PyObjC_GIL_FORWARD_EXC();
        }

        Py_CLEAR(values);
    PyObjC_END_WITH_GIL
    return result;
}

static simd_float3
v3fid_(id arg0)
{
    PyObject* items;
    PyObject* tmp;

    if (shouldRaise) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

static id
idsimdfloat4x4_(simd_float4x4 arg0)
{
    PyObject* items;
    PyObject* tmp;

    if (shouldRaise) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

static id
idsimdfloat4x4_f_f_q_(simd_float4x4 arg0, float arg1, float arg2, long long arg3)
{
    PyObject* items;
    PyObject* tmp;

    if (shouldRaise) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

static bool
Bid_v3f_(id arg0, simd_float3 arg1)
{
    PyObject* items;
    PyObject* tmp;

    if (shouldRaise) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return YES;
}

static simd_float3x3
simdfloat3x3id_(id arg0)
{
    PyObject* items;
    PyObject* tmp;

    if (shouldRaise) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float3x3){{(vector_float3){0.0, 1.5, 3.0},
                            (vector_float3){0.0, 1.5, 3.0},
                            (vector_float3){0.0, 1.5, 3.0}}};
}

static simd_float4x4
simdfloat4x4id_(id arg0)
{
    PyObject* items;
    PyObject* tmp;

    if (shouldRaise) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

static simd_float4x4
simdfloat4x4id_q_(id arg0, long long arg1)
{
    PyObject* items;
    PyObject* tmp;

    if (shouldRaise) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

static CGPoint
CGPointv2f_CGRect_Q_Q_(simd_float2 arg0, CGRect arg1, unsigned long long arg2,
                       unsigned long long arg3)
{
    PyObject* items;
    PyObject* tmp;

    if (shouldRaise) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{CGRect={CGPoint=dd}{CGSize=dd}}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (CGPoint){1.0, 2.0};
}

typedef void (*F)(void);
static struct function {
    char* name;
    F     function;
} gFunctionMap[] = {{"shouldRaise", (F)f_shouldRaise},
                    {"clearRaise", (F)f_clearRaise},
                    {"setRaise", (F)f_setRaise},
                    {"storedvalue", (F)f_storedvalue},

                    {"v3fid_", (F)v3fid_},
                    {"idsimdfloat4x4_", (F)idsimdfloat4x4_},
                    {"idsimdfloat4x4_f_f_q_", (F)idsimdfloat4x4_f_f_q_},
                    {"Bid_v3f_", (F)Bid_v3f_},
                    {"simdfloat3x3id_", (F)simdfloat3x3id_},
                    {"simdfloat4x4id_", (F)simdfloat4x4id_},
                    {"simdfloat4x4id_q_", (F)simdfloat4x4id_q_},
                    {"CGPointv2f_CGRect_Q_Q_", (F)CGPointv2f_CGRect_Q_Q_},
                    {NULL, NULL}};

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    PyObject* v = PyCapsule_New(gFunctionMap, "objc.__inline__", NULL);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        return -1;   // LCOV_EXCL_LINE
    }

    if (PyModule_AddObject(m, // LCOV_BR_EXCL_LINE
                           "function_list", v)
        == -1) {
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
    .m_name     = "vectorfunccall",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_vectorfunccall(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_vectorfunccall(void)
{
    return PyModuleDef_Init(&mod_module);
}
