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

#import <GameplayKit/GameplayKit.h>
#import <MetalPerformanceShaders/MetalPerformanceShaders.h>
#import <ModelIO/ModelIO.h>

@interface OC_VectorCall : NSObject {
    PyObject* values;
}
@end

static PyObject* clsvalues = NULL;
@implementation  OC_VectorCall
- (instancetype)init
{
    self = [super init];
    if (self == nil) {
        return nil;
    }
    values = NULL;
    return self;
}

- (id _Nullable)storedvalue
{
    id result;

    PyObjC_BEGIN_WITH_GIL
        if (depythonify_python_object(values, &result)) {
            PyObjC_GIL_FORWARD_EXC();
        }

        Py_CLEAR(clsvalues);
    PyObjC_END_WITH_GIL
    return result;
}

+ (id _Nullable)storedvalue
{
    id result;

    PyObjC_BEGIN_WITH_GIL
        if (depythonify_python_object(clsvalues, &result)) {
            PyObjC_GIL_FORWARD_EXC();
        }

        Py_CLEAR(clsvalues);
    PyObjC_END_WITH_GIL
    return result;
}

- (simd_uchar16)v16C
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_uchar16){0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
}

+ (simd_uchar16)clsv16C
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_uchar16){0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
}

- (simd_double2)v2d
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_double2){0.0, 1.5};
}

+ (simd_double2)clsv2d
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_double2){0.0, 1.5};
}

- (simd_double2)v2dd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_double2){0.0, 1.5};
}

+ (simd_double2)clsv2dd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_double2){0.0, 1.5};
}

- (simd_float2)v2f
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float2){0.0, 1.5};
}

+ (simd_float2)clsv2f
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float2){0.0, 1.5};
}

- (simd_float2)v2fQ:(unsigned long long)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float2){0.0, 1.5};
}

+ (simd_float2)clsv2fQ:(unsigned long long)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float2){0.0, 1.5};
}

- (simd_float2)v2fd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float2){0.0, 1.5};
}

+ (simd_float2)clsv2fd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float2){0.0, 1.5};
}

- (simd_float2)v2fq:(long long)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float2){0.0, 1.5};
}

+ (simd_float2)clsv2fq:(long long)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float2){0.0, 1.5};
}

- (simd_int2)v2i
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_int2){0, 1};
}

+ (simd_int2)clsv2i
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_int2){0, 1};
}

- (simd_double3)v3dd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_double3){0.0, 1.5, 3.0};
}

+ (simd_double3)clsv3dd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_double3){0.0, 1.5, 3.0};
}

- (simd_float3)v3f
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

+ (simd_float3)clsv3f
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

- (simd_float3)v3fv2i:(simd_int2)arg0 v2i:(simd_int2)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

+ (simd_float3)clsv3fv2i:(simd_int2)arg0 v2i:(simd_int2)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

- (simd_float3)v3fv3f:(simd_float3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

+ (simd_float3)clsv3fv3f:(simd_float3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

- (simd_float3)v3fv3f:(simd_float3)arg0 id:(id)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

+ (simd_float3)clsv3fv3f:(simd_float3)arg0 id:(id)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

- (simd_float3)v3fv4i:(simd_int4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

+ (simd_float3)clsv3fv4i:(simd_int4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

- (simd_float3)v3fQ:(unsigned long long)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

+ (simd_float3)clsv3fQ:(unsigned long long)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

- (simd_float3)v3fd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

+ (simd_float3)clsv3fd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

- (simd_double4)v4dd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_double4){0.0, 1.5, 3.0, 4.5};
}

+ (simd_double4)clsv4dd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_double4){0.0, 1.5, 3.0, 4.5};
}

- (simd_float4)v4f
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float4){0.0, 1.5, 3.0, 4.5};
}

+ (simd_float4)clsv4f
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float4){0.0, 1.5, 3.0, 4.5};
}

- (simd_float4)v4fd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float4){0.0, 1.5, 3.0, 4.5};
}

+ (simd_float4)clsv4fd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float4){0.0, 1.5, 3.0, 4.5};
}

- (simd_int4)v4iv3f:(simd_float3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_int4){0, 1, 2, 3};
}

+ (simd_int4)clsv4iv3f:(simd_float3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_int4){0, 1, 2, 3};
}

- (id)idv2f:(simd_float2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv2f:(simd_float2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv2f:(simd_float2)arg0 v2I:(simd_uint2)arg1 q:(long long)arg2 id:(id)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv2f:(simd_float2)arg0 v2I:(simd_uint2)arg1 q:(long long)arg2 id:(id)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv2f:(simd_float2)arg0 v2f:(simd_float2)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv2f:(simd_float2)arg0 v2f:(simd_float2)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv2i:(simd_int2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv2i:(simd_int2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv2i:(simd_int2)arg0 i:(int)arg1 i:(int)arg2 Z:(BOOL)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv2i:(simd_int2)arg0 i:(int)arg1 i:(int)arg2 Z:(BOOL)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv2i:(simd_int2)arg0 i:(int)arg1 i:(int)arg2 Z:(BOOL)arg3 Class:(Class)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("#", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv2i:(simd_int2)arg0 i:(int)arg1 i:(int)arg2 Z:(BOOL)arg3 Class:(Class)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("#", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv3f:(simd_float3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv3f:(simd_float3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv3f:(simd_float3)arg0
        v2I:(simd_uint2)arg1
          Z:(BOOL)arg2
          Z:(BOOL)arg3
          Z:(BOOL)arg4
          q:(long long)arg5
         id:(id)arg6
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv3f:(simd_float3)arg0
           v2I:(simd_uint2)arg1
             Z:(BOOL)arg2
             Z:(BOOL)arg3
             Z:(BOOL)arg4
             q:(long long)arg5
            id:(id)arg6
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv3f:(simd_float3)arg0
        v2I:(simd_uint2)arg1
          Z:(BOOL)arg2
          Z:(BOOL)arg3
          q:(long long)arg4
         id:(id)arg5
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv3f:(simd_float3)arg0
           v2I:(simd_uint2)arg1
             Z:(BOOL)arg2
             Z:(BOOL)arg3
             q:(long long)arg4
            id:(id)arg5
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv3f:(simd_float3)arg0
        v2I:(simd_uint2)arg1
          Z:(BOOL)arg2
          q:(long long)arg3
         id:(id)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv3f:(simd_float3)arg0
           v2I:(simd_uint2)arg1
             Z:(BOOL)arg2
             q:(long long)arg3
            id:(id)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv3f:(simd_float3)arg0
        v2I:(simd_uint2)arg1
          i:(int)arg2
          Z:(BOOL)arg3
          q:(long long)arg4
         id:(id)arg5
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv3f:(simd_float3)arg0
           v2I:(simd_uint2)arg1
             i:(int)arg2
             Z:(BOOL)arg3
             q:(long long)arg4
            id:(id)arg5
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv3f:(simd_float3)arg0 v2I:(simd_uint2)arg1 q:(long long)arg2 id:(id)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv3f:(simd_float3)arg0 v2I:(simd_uint2)arg1 q:(long long)arg2 id:(id)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv3f:(simd_float3)arg0
        v3I:(simd_uint3)arg1
          Z:(BOOL)arg2
          q:(long long)arg3
         id:(id)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv3f:(simd_float3)arg0
           v3I:(simd_uint3)arg1
             Z:(BOOL)arg2
             q:(long long)arg3
            id:(id)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv3f:(simd_float3)arg0
        v3I:(simd_uint3)arg1
          q:(long long)arg2
          Z:(BOOL)arg3
         id:(id)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv3f:(simd_float3)arg0
           v3I:(simd_uint3)arg1
             q:(long long)arg2
             Z:(BOOL)arg3
            id:(id)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3I>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv3f:(simd_float3)arg0
          Q:(unsigned long long)arg1
          Q:(unsigned long long)arg2
          q:(long long)arg3
          Z:(BOOL)arg4
          Z:(BOOL)arg5
         id:(id)arg6
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv3f:(simd_float3)arg0
             Q:(unsigned long long)arg1
             Q:(unsigned long long)arg2
             q:(long long)arg3
             Z:(BOOL)arg4
             Z:(BOOL)arg5
            id:(id)arg6
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv3f:(simd_float3)arg0 Z:(BOOL)arg1 q:(long long)arg2 id:(id)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv3f:(simd_float3)arg0 Z:(BOOL)arg1 q:(long long)arg2 id:(id)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idv4f:(simd_float4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv4f:(simd_float4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0
       v2d:(simd_double2)arg1
       v2d:(simd_double2)arg2
       v2i:(simd_int2)arg3
         Z:(BOOL)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0
          v2d:(simd_double2)arg1
          v2d:(simd_double2)arg2
          v2i:(simd_int2)arg3
            Z:(BOOL)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 v2f:(simd_float2)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 v2f:(simd_float2)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 v3f:(simd_float3)arg1
{
    PyObject* items;
    PyObject* tmp;
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
    return @"hello";
}

+ (id)clsidid:(id)arg0 v3f:(simd_float3)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
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
    return @"hello";
}

- (id)idid:(id)arg0 v4f:(simd_float4)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 v4f:(simd_float4)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 id:(id)arg1 v2i:(simd_int2)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 id:(id)arg1 v2i:(simd_int2)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 id:(id)arg1 v2i:(simd_int2)arg2 f:(float)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 id:(id)arg1 v2i:(simd_int2)arg2 f:(float)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 Q:(unsigned long long)arg1 v2f:(simd_float2)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 Q:(unsigned long long)arg1 v2f:(simd_float2)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 Q:(unsigned long long)arg1 v3f:(simd_float3)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 Q:(unsigned long long)arg1 v3f:(simd_float3)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 Q:(unsigned long long)arg1 v4f:(simd_float4)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 Q:(unsigned long long)arg1 v4f:(simd_float4)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 Q:(unsigned long long)arg1 matrixfloat4x4:(matrix_float4x4)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 Q:(unsigned long long)arg1 matrixfloat4x4:(matrix_float4x4)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0
         Z:(BOOL)arg1
        id:(id)arg2
       v2i:(simd_int2)arg3
         q:(long long)arg4
         Q:(unsigned long long)arg5
         q:(long long)arg6
         Z:(BOOL)arg7
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg7);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0
            Z:(BOOL)arg1
           id:(id)arg2
          v2i:(simd_int2)arg3
            q:(long long)arg4
            Q:(unsigned long long)arg5
            q:(long long)arg6
            Z:(BOOL)arg7
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg7);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0
         q:(long long)arg1
       v2i:(simd_int2)arg2
         f:(float)arg3
         f:(float)arg4
         f:(float)arg5
         f:(float)arg6
{
    PyObject* items;
    PyObject* tmp;
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
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0
            q:(long long)arg1
          v2i:(simd_int2)arg2
            f:(float)arg3
            f:(float)arg4
            f:(float)arg5
            f:(float)arg6
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
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
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0
         q:(long long)arg1
       v2i:(simd_int2)arg2
         f:(float)arg3
         f:(float)arg4
         f:(float)arg5
         f:(float)arg6
         f:(float)arg7
{
    PyObject* items;
    PyObject* tmp;
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
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg7);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0
            q:(long long)arg1
          v2i:(simd_int2)arg2
            f:(float)arg3
            f:(float)arg4
            f:(float)arg5
            f:(float)arg6
            f:(float)arg7
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
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
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg7);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 GKBox:(GKBox)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKBox=<3f><3f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 GKBox:(GKBox)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKBox=<3f><3f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 GKQuad:(GKQuad)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKQuad=<2f><2f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 GKQuad:(GKQuad)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKQuad=<2f><2f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0
    MDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg1
                            f:(float)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_MDLAxisAlignedBoundingBox=<3f><3f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0
    MDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg1
                            f:(float)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_MDLAxisAlignedBoundingBox=<3f><3f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 matrixfloat2x2:(matrix_float2x2)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float2x2=[2<2f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 matrixfloat2x2:(matrix_float2x2)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float2x2=[2<2f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 matrixfloat3x3:(matrix_float3x3)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float3x3=[3<3f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 matrixfloat3x3:(matrix_float3x3)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float3x3=[3<3f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 matrixfloat4x4:(matrix_float4x4)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 matrixfloat4x4:(matrix_float4x4)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idCGColor:(CGColorRef)arg0 CGColor:(CGColorRef)arg1 id:(id)arg2 v2i:(simd_int2)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("^{CGColor=}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("^{CGColor=}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidCGColor:(CGColorRef)arg0
           CGColor:(CGColorRef)arg1
                id:(id)arg2
               v2i:(simd_int2)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("^{CGColor=}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("^{CGColor=}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idf:(float)arg0 v2f:(simd_float2)arg1 v2f:(simd_float2)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidf:(float)arg0 v2f:(simd_float2)arg1 v2f:(simd_float2)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idf:(float)arg0 v2f:(simd_float2)arg1 v2f:(simd_float2)arg2 Class:(Class)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("#", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidf:(float)arg0 v2f:(simd_float2)arg1 v2f:(simd_float2)arg2 Class:(Class)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("#", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idf:(float)arg0
      v2f:(simd_float2)arg1
        Q:(unsigned long long)arg2
        Q:(unsigned long long)arg3
        Q:(unsigned long long)arg4
        q:(long long)arg5
        Z:(BOOL)arg6
       id:(id)arg7
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
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
        tmp = PyObjC_ObjCToPython("Q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg7);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidf:(float)arg0
         v2f:(simd_float2)arg1
           Q:(unsigned long long)arg2
           Q:(unsigned long long)arg3
           Q:(unsigned long long)arg4
           q:(long long)arg5
           Z:(BOOL)arg6
          id:(id)arg7
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
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
        tmp = PyObjC_ObjCToPython("Q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg7);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idf:(float)arg0
      v2f:(simd_float2)arg1
        Q:(unsigned long long)arg2
        Q:(unsigned long long)arg3
        q:(long long)arg4
        Z:(BOOL)arg5
       id:(id)arg6
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
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
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidf:(float)arg0
         v2f:(simd_float2)arg1
           Q:(unsigned long long)arg2
           Q:(unsigned long long)arg3
           q:(long long)arg4
           Z:(BOOL)arg5
          id:(id)arg6
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
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
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idf:(float)arg0
       id:(id)arg1
      v2i:(simd_int2)arg2
        i:(int)arg3
        q:(long long)arg4
        Z:(BOOL)arg5
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidf:(float)arg0
          id:(id)arg1
         v2i:(simd_int2)arg2
           i:(int)arg3
           q:(long long)arg4
           Z:(BOOL)arg5
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idf:(float)arg0
         id:(id)arg1
        v2i:(simd_int2)arg2
          i:(int)arg3
          q:(long long)arg4
    CGColor:(CGColorRef)arg5
    CGColor:(CGColorRef)arg6
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("^{CGColor=}", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("^{CGColor=}", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidf:(float)arg0
          id:(id)arg1
         v2i:(simd_int2)arg2
           i:(int)arg3
           q:(long long)arg4
     CGColor:(CGColorRef)arg5
     CGColor:(CGColorRef)arg6
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("i", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("^{CGColor=}", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("^{CGColor=}", &arg6);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idf:(float)arg0 id:(id)arg1 v2i:(simd_int2)arg2 q:(long long)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
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

+ (id)clsidf:(float)arg0 id:(id)arg1 v2i:(simd_int2)arg2 q:(long long)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg2);
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

- (id)idf:(float)arg0 f:(float)arg1 id:(id)arg2 v2i:(simd_int2)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidf:(float)arg0 f:(float)arg1 id:(id)arg2 v2i:(simd_int2)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idGKBox:(GKBox)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKBox=<3f><3f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidGKBox:(GKBox)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKBox=<3f><3f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idGKBox:(GKBox)arg0 f:(float)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKBox=<3f><3f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidGKBox:(GKBox)arg0 f:(float)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKBox=<3f><3f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idGKQuad:(GKQuad)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKQuad=<2f><2f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidGKQuad:(GKQuad)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKQuad=<2f><2f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idGKQuad:(GKQuad)arg0 f:(float)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKQuad=<2f><2f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidGKQuad:(GKQuad)arg0 f:(float)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{GKQuad=<2f><2f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idMDLVoxelIndexExtent:(MDLVoxelIndexExtent)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_MDLVoxelIndexExtent=<4i><4i>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidMDLVoxelIndexExtent:(MDLVoxelIndexExtent)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_MDLVoxelIndexExtent=<4i><4i>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idmatrixfloat4x4:(matrix_float4x4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidmatrixfloat4x4:(matrix_float4x4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idmatrixfloat4x4:(matrix_float4x4)arg0 Z:(BOOL)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidmatrixfloat4x4:(matrix_float4x4)arg0 Z:(BOOL)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (BOOL)Zv2i:(simd_int2)arg0 id:(id)arg1 id:(id)arg2 id:(id)arg3 id:(id)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return NO;
}

+ (BOOL)clsZv2i:(simd_int2)arg0 id:(id)arg1 id:(id)arg2 id:(id)arg3 id:(id)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return NO;
}

- (BOOL)Zv2i:(simd_int2)arg0
           q:(long long)arg1
           f:(float)arg2
          id:(id)arg3
          id:(id)arg4
          id:(id)arg5
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return NO;
}

+ (BOOL)clsZv2i:(simd_int2)arg0
              q:(long long)arg1
              f:(float)arg2
             id:(id)arg3
             id:(id)arg4
             id:(id)arg5
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg5);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return NO;
}

- (BOOL)Zv4i:(simd_int4)arg0 Z:(BOOL)arg1 Z:(BOOL)arg2 Z:(BOOL)arg3 Z:(BOOL)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return NO;
}

+ (BOOL)clsZv4i:(simd_int4)arg0 Z:(BOOL)arg1 Z:(BOOL)arg2 Z:(BOOL)arg3 Z:(BOOL)arg4
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg3);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg4);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return NO;
}

- (CGColorRef)CGColorv3f:(simd_float3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (CGColorRef) @"color!";
}

+ (CGColorRef)clsCGColorv3f:(simd_float3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (CGColorRef) @"color!";
}

- (CGColorRef)CGColorv3f:(simd_float3)arg0 CGColorSpace:(CGColorSpaceRef)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("^{CGColorSpace=}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (CGColorRef) @"color!";
}

+ (CGColorRef)clsCGColorv3f:(simd_float3)arg0 CGColorSpace:(CGColorSpaceRef)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("^{CGColorSpace=}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (CGColorRef) @"color!";
}

- (float)fv2f:(simd_float2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return 2500000000.0;
}

+ (float)clsfv2f:(simd_float2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return 2500000000.0;
}

- (float)fv2i:(simd_int2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return 2500000000.0;
}

+ (float)clsfv2i:(simd_int2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return 2500000000.0;
}

- (void)vv2d:(simd_double2)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv2d:(simd_double2)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv2f:(simd_float2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv2f:(simd_float2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv2f:(simd_float2)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv2f:(simd_float2)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv3d:(simd_double3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3d>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv3d:(simd_double3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3d>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv3d:(simd_double3)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3d>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv3d:(simd_double3)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3d>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv3f:(simd_float3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv3f:(simd_float3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv3f:(simd_float3)arg0 v3f:(simd_float3)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
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
}

+ (void)clsvv3f:(simd_float3)arg0 v3f:(simd_float3)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
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
}

- (void)vv3f:(simd_float3)arg0 v3f:(simd_float3)arg1 v3f:(simd_float3)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv3f:(simd_float3)arg0 v3f:(simd_float3)arg1 v3f:(simd_float3)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv3f:(simd_float3)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv3f:(simd_float3)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<3f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv4d:(simd_double4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4d>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv4d:(simd_double4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4d>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv4f:(simd_float4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv4f:(simd_float4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv4f:(simd_float4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv4f:(simd_float4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4f>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv4i:(simd_int4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv4i:(simd_int4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vid:(id)arg0 v2f:(simd_float2)arg1 v2f:(simd_float2)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvid:(id)arg0 v2f:(simd_float2)arg1 v2f:(simd_float2)arg2
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vid:(id)arg0 v2f:(simd_float2)arg1 v2f:(simd_float2)arg2 q:(long long)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg2);
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
}

+ (void)clsvid:(id)arg0 v2f:(simd_float2)arg1 v2f:(simd_float2)arg2 q:(long long)arg3
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2f>", &arg2);
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
}

- (void)vf:(float)arg0 v2i:(simd_int2)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvf:(float)arg0 v2i:(simd_int2)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("f", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2i>", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vMDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_MDLAxisAlignedBoundingBox=<3f><3f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvMDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_MDLAxisAlignedBoundingBox=<3f><3f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vMDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg0 Z:(BOOL)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_MDLAxisAlignedBoundingBox=<3f><3f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvMDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg0 Z:(BOOL)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_MDLAxisAlignedBoundingBox=<3f><3f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vmatrixdouble4x4:(matrix_double4x4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_double4x4=[4<4d>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvmatrixdouble4x4:(matrix_double4x4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_double4x4=[4<4d>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vmatrixdouble4x4:(matrix_double4x4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_double4x4=[4<4d>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvmatrixdouble4x4:(matrix_double4x4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_double4x4=[4<4d>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vmatrixfloat2x2:(matrix_float2x2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float2x2=[2<2f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvmatrixfloat2x2:(matrix_float2x2)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float2x2=[2<2f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vmatrixfloat3x3:(matrix_float3x3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float3x3=[3<3f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvmatrixfloat3x3:(matrix_float3x3)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float3x3=[3<3f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vmatrixfloat4x4:(matrix_float4x4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvmatrixfloat4x4:(matrix_float4x4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vmatrixfloat4x4:(matrix_float4x4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvmatrixfloat4x4:(matrix_float4x4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_matrix_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vsimdfloat4x4:(simd_float4x4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvsimdfloat4x4:(simd_float4x4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vsimdquatd:(simd_quatd)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_quatd=<4d>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvsimdquatd:(simd_quatd)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_quatd=<4d>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vsimdquatf:(simd_quatf)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_quatf=<4f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvsimdquatf:(simd_quatf)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_quatf=<4f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vsimdquatf:(simd_quatf)arg0 v3f:(simd_float3)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_quatf=<4f>}", &arg0);
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
}

+ (void)clsvsimdquatf:(simd_quatf)arg0 v3f:(simd_float3)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_quatf=<4f>}", &arg0);
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
}

- (void)vsimdquatf:(simd_quatf)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_quatf=<4f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvsimdquatf:(simd_quatf)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_quatf=<4f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (GKBox)GKBox
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (GKBox){(vector_float3){1.0, 2.0, 3.0}, (vector_float3){4.0, 5.0, 6.0}};
}

+ (GKBox)clsGKBox
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (GKBox){(vector_float3){1.0, 2.0, 3.0}, (vector_float3){4.0, 5.0, 6.0}};
}

- (GKQuad)GKQuad
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (GKQuad){(vector_float2){9.0, 10.0}, (vector_float2){11.0, 12.0}};
}

+ (GKQuad)clsGKQuad
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (GKQuad){(vector_float2){9.0, 10.0}, (vector_float2){11.0, 12.0}};
}

- (GKTriangle)GKTriangleQ:(unsigned long long)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (GKTriangle){{(vector_float3){-18.5, -19.5, -110.5},
                         (vector_float3){-111.5, -112.5, -113.5},
                         (vector_float3){-17.5, 11.5, 122.5}}};
}

+ (GKTriangle)clsGKTriangleQ:(unsigned long long)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("Q", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (GKTriangle){{(vector_float3){-18.5, -19.5, -110.5},
                         (vector_float3){-111.5, -112.5, -113.5},
                         (vector_float3){-17.5, 11.5, 122.5}}};
}

- (MDLAxisAlignedBoundingBox)MDLAxisAlignedBoundingBox
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLAxisAlignedBoundingBox){(vector_float3){-8.0, -9.0, -10.0},
                                       (vector_float3){-11.0, -12.0, -13.0}};
}

+ (MDLAxisAlignedBoundingBox)clsMDLAxisAlignedBoundingBox
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLAxisAlignedBoundingBox){(vector_float3){-8.0, -9.0, -10.0},
                                       (vector_float3){-11.0, -12.0, -13.0}};
}

- (MDLAxisAlignedBoundingBox)MDLAxisAlignedBoundingBoxv4i:(simd_int4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLAxisAlignedBoundingBox){(vector_float3){-8.0, -9.0, -10.0},
                                       (vector_float3){-11.0, -12.0, -13.0}};
}

+ (MDLAxisAlignedBoundingBox)clsMDLAxisAlignedBoundingBoxv4i:(simd_int4)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<4i>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLAxisAlignedBoundingBox){(vector_float3){-8.0, -9.0, -10.0},
                                       (vector_float3){-11.0, -12.0, -13.0}};
}

- (MDLAxisAlignedBoundingBox)MDLAxisAlignedBoundingBoxd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLAxisAlignedBoundingBox){(vector_float3){-8.0, -9.0, -10.0},
                                       (vector_float3){-11.0, -12.0, -13.0}};
}

+ (MDLAxisAlignedBoundingBox)clsMDLAxisAlignedBoundingBoxd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLAxisAlignedBoundingBox){(vector_float3){-8.0, -9.0, -10.0},
                                       (vector_float3){-11.0, -12.0, -13.0}};
}

- (MDLVoxelIndexExtent)MDLVoxelIndexExtent
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLVoxelIndexExtent){(vector_int4){100, 101, 102, 103},
                                 (vector_int4){-20, -21, -22, -23}};
}

+ (MDLVoxelIndexExtent)clsMDLVoxelIndexExtent
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLVoxelIndexExtent){(vector_int4){100, 101, 102, 103},
                                 (vector_int4){-20, -21, -22, -23}};
}

- (MPSAxisAlignedBoundingBox)MPSAxisAlignedBoundingBox
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MPSAxisAlignedBoundingBox){(vector_float3){1.5, 2.5, 3.5},
                                       (vector_float3){4.5, 5.5, 6.5}};
}

+ (MPSAxisAlignedBoundingBox)clsMPSAxisAlignedBoundingBox
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MPSAxisAlignedBoundingBox){(vector_float3){1.5, 2.5, 3.5},
                                       (vector_float3){4.5, 5.5, 6.5}};
}

- (MPSImageHistogramInfo)MPSImageHistogramInfo
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MPSImageHistogramInfo){4398046511104, YES,
                                   (vector_float4){1.0, 2.0, 3.0, 4.0},
                                   (vector_float4){-1.0, -2.0, -3.0, -4.0}};
}

+ (MPSImageHistogramInfo)clsMPSImageHistogramInfo
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MPSImageHistogramInfo){4398046511104, YES,
                                   (vector_float4){1.0, 2.0, 3.0, 4.0},
                                   (vector_float4){-1.0, -2.0, -3.0, -4.0}};
}

- (matrix_double4x4)matrixdouble4x4
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_double4x4){
        {(vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5},
         (vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5}}};
}

+ (matrix_double4x4)clsmatrixdouble4x4
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_double4x4){
        {(vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5},
         (vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5}}};
}

- (matrix_double4x4)matrixdouble4x4d:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_double4x4){
        {(vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5},
         (vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5}}};
}

+ (matrix_double4x4)clsmatrixdouble4x4d:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_double4x4){
        {(vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5},
         (vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5}}};
}

- (matrix_float2x2)matrixfloat2x2
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_float2x2){{(vector_float2){0.0, 1.5}, (vector_float2){0.0, 1.5}}};
}

+ (matrix_float2x2)clsmatrixfloat2x2
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_float2x2){{(vector_float2){0.0, 1.5}, (vector_float2){0.0, 1.5}}};
}

- (matrix_float3x3)matrixfloat3x3
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_float3x3){{(vector_float3){0.0, 1.5, 3.0},
                              (vector_float3){0.0, 1.5, 3.0},
                              (vector_float3){0.0, 1.5, 3.0}}};
}

+ (matrix_float3x3)clsmatrixfloat3x3
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_float3x3){{(vector_float3){0.0, 1.5, 3.0},
                              (vector_float3){0.0, 1.5, 3.0},
                              (vector_float3){0.0, 1.5, 3.0}}};
}

- (matrix_float4x4)matrixfloat4x4
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

+ (matrix_float4x4)clsmatrixfloat4x4
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

- (matrix_float4x4)matrixfloat4x4id:(id)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

+ (matrix_float4x4)clsmatrixfloat4x4id:(id)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

- (matrix_float4x4)matrixfloat4x4d:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

+ (matrix_float4x4)clsmatrixfloat4x4d:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (matrix_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

- (simd_float4x4)simdfloat4x4
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

+ (simd_float4x4)clssimdfloat4x4
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

- (simd_float4x4)simdfloat4x4simdfloat4x4:(simd_float4x4)arg0 id:(id)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

+ (simd_float4x4)clssimdfloat4x4simdfloat4x4:(simd_float4x4)arg0 id:(id)arg1
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{_simd_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

- (simd_quatd)simdquatdd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_quatd){(vector_double4){0.0, 1.5, 3.0, 4.5}};
}

+ (simd_quatd)clssimdquatdd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_quatd){(vector_double4){0.0, 1.5, 3.0, 4.5}};
}

- (simd_quatf)simdquatf
{
    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_quatf){(vector_float4){0.0, 1.5, 3.0, 4.5}};
}

+ (simd_quatf)clssimdquatf
{
    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_quatf){(vector_float4){0.0, 1.5, 3.0, 4.5}};
}

- (simd_quatf)simdquatfd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_quatf){(vector_float4){0.0, 1.5, 3.0, 4.5}};
}

+ (simd_quatf)clssimdquatfd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;
    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("d", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_quatf){(vector_float4){0.0, 1.5, 3.0, 4.5}};
}

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "vectorcall", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_vectorcall(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_vectorcall(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_VectorCall", PyObjC_IdToPython([OC_VectorCall class]))
        < 0) {
        return NULL;
    }

    return m;
}
