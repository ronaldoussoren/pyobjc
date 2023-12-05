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





@interface OC_VectorCall : NSObject {
    PyObject* values;
}
@end

static PyObject* clsvalues   = NULL;
static BOOL      shouldRaise = NO;

@implementation OC_VectorCall
- (instancetype)init
{
    self = [super init];
    if (self == nil) {
        return nil;
    }
    values = NULL;
    return self;
}

- (BOOL)shouldRaise
{
    return shouldRaise;
}
+ (BOOL)shouldRaise
{
    return shouldRaise;
}

+ (void)clearRaise
{
    shouldRaise = NO;
}

+ (void)setRaise
{
    shouldRaise = YES;
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

- (simd_double2)v2d
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_double2){0.0, 1.5};
}

+ (simd_double2)clsv2d
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float2){0.0, 1.5};
}

+ (simd_float2)clsv2f
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_int2){0, 1};
}

+ (simd_int2)clsv2i
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float3){0.0, 1.5, 3.0};
}

+ (simd_float3)clsv3f
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_float4){0.0, 1.5, 3.0, 4.5};
}

+ (simd_float4)clsv4f
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

- (id)idv2d:(simd_double2)arg0 id:(id)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg0);
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
    return @"hello";
}

+ (id)clsidv2d:(simd_double2)arg0 id:(id)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg0);
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
    return @"hello";
}

- (id)idv2d:(simd_double2)arg0 q:(long long)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg0);
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
    return @"hello";
}

+ (id)clsidv2d:(simd_double2)arg0 q:(long long)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg0);
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
    return @"hello";
}

- (id)idv2f:(simd_float2)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidv2f:(simd_float2)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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
    return @"hello";
}

+ (id)clsidid:(id)arg0 v3f:(simd_float3)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

- (id)idid:(id)arg0 Q:(unsigned long long)arg1 simdfloat4x4:(simd_float4x4)arg2
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("Q", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 Q:(unsigned long long)arg1 simdfloat4x4:(simd_float4x4)arg2
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
        tmp = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &arg2);
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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

#if PyObjC_BUILD_RELEASE >= 1012
- (id)idid:(id)arg0 GKBox:(GKBox)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("{GKBox=<3f><3f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)clsidid:(id)arg0 GKBox:(GKBox)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
- (id)idid:(id)arg0 GKQuad:(GKQuad)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("{GKQuad=<2f><2f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)clsidid:(id)arg0 GKQuad:(GKQuad)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
- (id)idid:(id)arg0
    MDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg1
                            f:(float)arg2
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("{MDLAxisAlignedBoundingBox=<3f><3f>}", &arg1);
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
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (id)clsidid:(id)arg0
    MDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg1
                            f:(float)arg2
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{MDLAxisAlignedBoundingBox=<3f><3f>}", &arg1);
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
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

- (id)idid:(id)arg0 simdfloat2x2:(simd_float2x2)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("{simd_float2x2=[2<2f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 simdfloat2x2:(simd_float2x2)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float2x2=[2<2f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 simdfloat3x3:(simd_float3x3)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("{simd_float3x3=[3<3f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 simdfloat3x3:(simd_float3x3)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float3x3=[3<3f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

- (id)idid:(id)arg0 simdfloat4x4:(simd_float4x4)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidid:(id)arg0 simdfloat4x4:(simd_float4x4)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

#if PyObjC_BUILD_RELEASE >= 1013
- (id)idid:(id)arg0 simdquatf:(simd_quatf)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (id)clsidid:(id)arg0 simdquatf:(simd_quatf)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
- (id)idid:(id)arg0 simdquatf:(simd_quatf)arg1 id:(id)arg2
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (id)clsidid:(id)arg0 simdquatf:(simd_quatf)arg1 id:(id)arg2
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("@", &arg2);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

- (id)idCGColor:(CGColorRef)arg0 CGColor:(CGColorRef)arg1 id:(id)arg2 v2i:(simd_int2)arg3
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

#if PyObjC_BUILD_RELEASE >= 1012
- (id)idGKBox:(GKBox)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)clsidGKBox:(GKBox)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
- (id)idGKBox:(GKBox)arg0 f:(float)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)clsidGKBox:(GKBox)arg0 f:(float)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
- (id)idGKQuad:(GKQuad)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)clsidGKQuad:(GKQuad)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
- (id)idGKQuad:(GKQuad)arg0 f:(float)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)clsidGKQuad:(GKQuad)arg0 f:(float)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
- (id)idMDLVoxelIndexExtent:(MDLVoxelIndexExtent)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{MDLVoxelIndexExtent=<4i><4i>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (id)clsidMDLVoxelIndexExtent:(MDLVoxelIndexExtent)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{MDLVoxelIndexExtent=<4i><4i>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

- (id)idsimdfloat4x4:(simd_float4x4)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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

+ (id)clsidsimdfloat4x4:(simd_float4x4)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
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

- (id)idsimdfloat4x4:(simd_float4x4)arg0 Z:(BOOL)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("Z", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return @"hello";
}

+ (id)clsidsimdfloat4x4:(simd_float4x4)arg0 Z:(BOOL)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &arg0);
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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
    PyObjC_END_WITH_GIL
    return 2500000000.0;
}

+ (float)clsfv2f:(simd_float2)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

- (void)vv2d:(simd_double2)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvv2d:(simd_double2)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("<2d>", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vv2d:(simd_double2)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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
    PyObjC_END_WITH_GIL
}

+ (void)clsvv2f:(simd_float2)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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

#if PyObjC_BUILD_RELEASE >= 1011
- (void)vMDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{MDLAxisAlignedBoundingBox=<3f><3f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (void)clsvMDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{MDLAxisAlignedBoundingBox=<3f><3f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
- (void)vMDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg0 Z:(BOOL)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{MDLAxisAlignedBoundingBox=<3f><3f>}", &arg0);
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
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (void)clsvMDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox)arg0 Z:(BOOL)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{MDLAxisAlignedBoundingBox=<3f><3f>}", &arg0);
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
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

- (void)vsimddouble4x4:(simd_double4x4)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_double4x4=[4<4d>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvsimddouble4x4:(simd_double4x4)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_double4x4=[4<4d>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vsimddouble4x4:(simd_double4x4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_double4x4=[4<4d>]}", &arg0);
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

+ (void)clsvsimddouble4x4:(simd_double4x4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_double4x4=[4<4d>]}", &arg0);
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

- (void)vsimdfloat2x2:(simd_float2x2)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float2x2=[2<2f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvsimdfloat2x2:(simd_float2x2)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float2x2=[2<2f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vsimdfloat3x3:(simd_float3x3)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float3x3=[3<3f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvsimdfloat3x3:(simd_float3x3)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float3x3=[3<3f>]}", &arg0);
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

    if ([self shouldRaise]) {
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
}

+ (void)clsvsimdfloat4x4:(simd_float4x4)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

- (void)vsimdfloat4x4:(simd_float4x4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}

+ (void)clsvsimdfloat4x4:(simd_float4x4)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &arg0);
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

#if PyObjC_BUILD_RELEASE >= 1013
- (void)vsimdquatd:(simd_quatd)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_quatd=<4d>}", &arg0);
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
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (void)clsvsimdquatd:(simd_quatd)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_quatd=<4d>}", &arg0);
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
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
- (void)vsimdquatf:(simd_quatf)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (void)clsvsimdquatf:(simd_quatf)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &arg0);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
- (void)vsimdquatf:(simd_quatf)arg0 v3f:(simd_float3)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &arg0);
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
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (void)clsvsimdquatf:(simd_quatf)arg0 v3f:(simd_float3)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &arg0);
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
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
- (void)vsimdquatf:(simd_quatf)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = values = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &arg0);
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
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (void)clsvsimdquatf:(simd_quatf)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &arg0);
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
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1012
- (GKBox)GKBox
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (GKBox){(vector_float3){1.0, 2.0, 3.0}, (vector_float3){4.0, 5.0, 6.0}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (GKBox)clsGKBox
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (GKBox){(vector_float3){1.0, 2.0, 3.0}, (vector_float3){4.0, 5.0, 6.0}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
- (GKQuad)GKQuad
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (GKQuad){(vector_float2){9.0, 10.0}, (vector_float2){11.0, 12.0}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (GKQuad)clsGKQuad
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (GKQuad){(vector_float2){9.0, 10.0}, (vector_float2){11.0, 12.0}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
- (GKTriangle)GKTriangleQ:(unsigned long long)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (GKTriangle)clsGKTriangleQ:(unsigned long long)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
- (MDLAxisAlignedBoundingBox)MDLAxisAlignedBoundingBox
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLAxisAlignedBoundingBox){(vector_float3){-8.0, -9.0, -10.0},
                                       (vector_float3){-11.0, -12.0, -13.0}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (MDLAxisAlignedBoundingBox)clsMDLAxisAlignedBoundingBox
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLAxisAlignedBoundingBox){(vector_float3){-8.0, -9.0, -10.0},
                                       (vector_float3){-11.0, -12.0, -13.0}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
- (MDLAxisAlignedBoundingBox)MDLAxisAlignedBoundingBoxv4i:(simd_int4)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (MDLAxisAlignedBoundingBox)clsMDLAxisAlignedBoundingBoxv4i:(simd_int4)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
- (MDLAxisAlignedBoundingBox)MDLAxisAlignedBoundingBoxd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (MDLAxisAlignedBoundingBox)clsMDLAxisAlignedBoundingBoxd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
- (MDLVoxelIndexExtent)MDLVoxelIndexExtent
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLVoxelIndexExtent){(vector_int4){100, 101, 102, 103},
                                 (vector_int4){-20, -21, -22, -23}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (MDLVoxelIndexExtent)clsMDLVoxelIndexExtent
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MDLVoxelIndexExtent){(vector_int4){100, 101, 102, 103},
                                 (vector_int4){-20, -21, -22, -23}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

- (simd_double4x4)simddouble4x4
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_double4x4){
        {(vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5},
         (vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5}}};
}

+ (simd_double4x4)clssimddouble4x4
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_double4x4){
        {(vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5},
         (vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5}}};
}

- (simd_double4x4)simddouble4x4d:(double)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
    return (simd_double4x4){
        {(vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5},
         (vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5}}};
}

+ (simd_double4x4)clssimddouble4x4d:(double)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
    return (simd_double4x4){
        {(vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5},
         (vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5}}};
}

- (simd_float2x2)simdfloat2x2
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float2x2){{(vector_float2){0.0, 1.5}, (vector_float2){0.0, 1.5}}};
}

+ (simd_float2x2)clssimdfloat2x2
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float2x2){{(vector_float2){0.0, 1.5}, (vector_float2){0.0, 1.5}}};
}

- (simd_float3x3)simdfloat3x3
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float3x3){{(vector_float3){0.0, 1.5, 3.0},
                            (vector_float3){0.0, 1.5, 3.0},
                            (vector_float3){0.0, 1.5, 3.0}}};
}

+ (simd_float3x3)clssimdfloat3x3
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float3x3){{(vector_float3){0.0, 1.5, 3.0},
                            (vector_float3){0.0, 1.5, 3.0},
                            (vector_float3){0.0, 1.5, 3.0}}};
}

- (simd_float4x4)simdfloat4x4
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

- (simd_float4x4)simdfloat4x4id:(id)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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
        tmp = PyObjC_ObjCToPython("d", &arg1);
        if (tmp == NULL)
            PyObjC_GIL_FORWARD_EXC();
        if (PyList_Append(items, tmp) == -1)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

+ (simd_float4x4)clssimdfloat4x4id:(id)arg0 d:(double)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

- (simd_float4x4)simdfloat4x4d:(double)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

+ (simd_float4x4)clssimdfloat4x4d:(double)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
    return (simd_float4x4){
        {(vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
         (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5}}};
}

- (simd_float4x4)simdfloat4x4simdfloat4x4:(simd_float4x4)arg0 id:(id)arg1
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
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

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        items = clsvalues = PyList_New(0);
        if (items == NULL)
            PyObjC_GIL_FORWARD_EXC();
        tmp = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &arg0);
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

#if PyObjC_BUILD_RELEASE >= 1013
- (simd_quatd)simdquatdd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (simd_quatd)clssimdquatdd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
- (simd_quatf)simdquatf
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_quatf){(vector_float4){0.0, 1.5, 3.0, 4.5}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (simd_quatf)clssimdquatf
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (simd_quatf){(vector_float4){0.0, 1.5, 3.0, 4.5}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
- (simd_quatf)simdquatfd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (simd_quatf)clssimdquatfd:(double)arg0
{
    PyObject* items;
    PyObject* tmp;

    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

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
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

- (simd_uchar16)v16C
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_uchar16){0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
}

+ (simd_uchar16)clsv16C
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (vector_uchar16){0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
}

#if PyObjC_BUILD_RELEASE >= 1013
- (MPSImageHistogramInfo)MPSImageHistogramInfo
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MPSImageHistogramInfo){4398046511104, YES,
                                   (vector_float4){1.0, 2.0, 3.0, 4.0},
                                   (vector_float4){-1.0, -2.0, -3.0, -4.0}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (MPSImageHistogramInfo)clsMPSImageHistogramInfo
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MPSImageHistogramInfo){4398046511104, YES,
                                   (vector_float4){1.0, 2.0, 3.0, 4.0},
                                   (vector_float4){-1.0, -2.0, -3.0, -4.0}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1014
- (MPSAxisAlignedBoundingBox)MPSAxisAlignedBoundingBox
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        values = PyList_New(0);
        if (values == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MPSAxisAlignedBoundingBox){(vector_float3){1.5, 2.5, 3.5},
                                       (vector_float3){4.5, 5.5, 6.5}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1014 */

#if PyObjC_BUILD_RELEASE >= 1014
+ (MPSAxisAlignedBoundingBox)clsMPSAxisAlignedBoundingBox
{
    if ([self shouldRaise]) {
        shouldRaise = NO;
        [NSException raise:@"SimpleException" format:@"hello world"];
    }

    PyObjC_BEGIN_WITH_GIL
        clsvalues = PyList_New(0);
        if (clsvalues == NULL)
            PyObjC_GIL_FORWARD_EXC();
    PyObjC_END_WITH_GIL
    return (MPSAxisAlignedBoundingBox){(vector_float3){1.5, 2.5, 3.5},
                                       (vector_float3){4.5, 5.5, 6.5}};
}
#endif /* PyObjC_BUILD_RELEASE >= 1014 */

@end

@interface OC_VectorCallInvoke : NSObject {
}
@end

@implementation OC_VectorCallInvoke

+ (id)v2dOn:(OC_VectorCall*)value
{
    id           cinter;
    simd_double2 result = [value v2d];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<2d>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v2ddOn:(OC_VectorCall*)value
{
    simd_double2 result = [value v2dd:-557000000000.0];
    id           cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<2d>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v2fOn:(OC_VectorCall*)value
{
    id          cinter;
    simd_float2 result = [value v2f];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<2f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v2fQOn:(OC_VectorCall*)value
{
    simd_float2 result = [value v2fQ:35184372088832];
    id          cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<2f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v2fdOn:(OC_VectorCall*)value
{
    simd_float2 result = [value v2fd:-557000000000.0];
    id          cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<2f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v2fqOn:(OC_VectorCall*)value
{
    simd_float2 result = [value v2fq:-17592186044416];
    id          cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<2f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v2iOn:(OC_VectorCall*)value
{
    id        cinter;
    simd_int2 result = [value v2i];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<2i>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v3ddOn:(OC_VectorCall*)value
{
    simd_double3 result = [value v3dd:-557000000000.0];
    id           cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<3d>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v3fOn:(OC_VectorCall*)value
{
    id          cinter;
    simd_float3 result = [value v3f];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<3f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v3fv2iv2iOn:(OC_VectorCall*)value
{
    simd_float3 result = [value v3fv2i:(vector_int2){0, 1} v2i:(vector_int2){0, 1}];
    id          cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<3f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v3fv3fOn:(OC_VectorCall*)value
{
    simd_float3 result = [value v3fv3f:(vector_float3){0.0, 1.5, 3.0}];
    id          cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<3f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v3fv3fidOn:(OC_VectorCall*)value
{
    simd_float3 result = [value v3fv3f:(vector_float3){0.0, 1.5, 3.0} id:@"hello"];
    id          cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<3f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v3fv4iOn:(OC_VectorCall*)value
{
    simd_float3 result = [value v3fv4i:(vector_int4){0, 1, 2, 3}];
    id          cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<3f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v3fQOn:(OC_VectorCall*)value
{
    simd_float3 result = [value v3fQ:35184372088832];
    id          cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<3f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v3fdOn:(OC_VectorCall*)value
{
    simd_float3 result = [value v3fd:-557000000000.0];
    id          cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<3f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v4ddOn:(OC_VectorCall*)value
{
    simd_double4 result = [value v4dd:-557000000000.0];
    id           cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<4d>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v4fOn:(OC_VectorCall*)value
{
    id          cinter;
    simd_float4 result = [value v4f];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<4f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v4fdOn:(OC_VectorCall*)value
{
    simd_float4 result = [value v4fd:-557000000000.0];
    id          cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<4f>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)v4iv3fOn:(OC_VectorCall*)value
{
    simd_int4 result = [value v4iv3f:(vector_float3){0.0, 1.5, 3.0}];
    id        cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<4i>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv2didOn:(OC_VectorCall*)value
{
    id result = [value idv2d:(vector_double2){0.0, 1.5} id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv2dqOn:(OC_VectorCall*)value
{
    id result = [value idv2d:(vector_double2){0.0, 1.5} q:-17592186044416];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv2fOn:(OC_VectorCall*)value
{
    id result = [value idv2f:(vector_float2){0.0, 1.5}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv2fv2IqidOn:(OC_VectorCall*)value
{
    id result = [value idv2f:(vector_float2){0.0, 1.5}
                         v2I:(vector_uint2){0, 1}
                           q:-17592186044416
                          id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv2fv2fOn:(OC_VectorCall*)value
{
    id result = [value idv2f:(vector_float2){0.0, 1.5} v2f:(vector_float2){0.0, 1.5}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv2iOn:(OC_VectorCall*)value
{
    id result = [value idv2i:(vector_int2){0, 1}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv2iiiZOn:(OC_VectorCall*)value
{
    id result = [value idv2i:(vector_int2){0, 1} i:-42 i:-42 Z:NO];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv2iiiZClassOn:(OC_VectorCall*)value
{
    id result = [value idv2i:(vector_int2){0, 1} i:-42 i:-42 Z:NO Class:[NSObject class]];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv3fOn:(OC_VectorCall*)value
{
    id result = [value idv3f:(vector_float3){0.0, 1.5, 3.0}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv3fv2IZZZqidOn:(OC_VectorCall*)value
{
    id result = [value idv3f:(vector_float3){0.0, 1.5, 3.0}
                         v2I:(vector_uint2){0, 1}
                           Z:NO
                           Z:NO
                           Z:NO
                           q:-17592186044416
                          id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv3fv2IZZqidOn:(OC_VectorCall*)value
{
    id result = [value idv3f:(vector_float3){0.0, 1.5, 3.0}
                         v2I:(vector_uint2){0, 1}
                           Z:NO
                           Z:NO
                           q:-17592186044416
                          id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv3fv2IZqidOn:(OC_VectorCall*)value
{
    id result = [value idv3f:(vector_float3){0.0, 1.5, 3.0}
                         v2I:(vector_uint2){0, 1}
                           Z:NO
                           q:-17592186044416
                          id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv3fv2IiZqidOn:(OC_VectorCall*)value
{
    id result = [value idv3f:(vector_float3){0.0, 1.5, 3.0}
                         v2I:(vector_uint2){0, 1}
                           i:-42
                           Z:NO
                           q:-17592186044416
                          id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv3fv2IqidOn:(OC_VectorCall*)value
{
    id result = [value idv3f:(vector_float3){0.0, 1.5, 3.0}
                         v2I:(vector_uint2){0, 1}
                           q:-17592186044416
                          id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv3fv3IZqidOn:(OC_VectorCall*)value
{
    id result = [value idv3f:(vector_float3){0.0, 1.5, 3.0}
                         v3I:(vector_uint3){0, 1, 2}
                           Z:NO
                           q:-17592186044416
                          id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv3fv3IqZidOn:(OC_VectorCall*)value
{
    id result = [value idv3f:(vector_float3){0.0, 1.5, 3.0}
                         v3I:(vector_uint3){0, 1, 2}
                           q:-17592186044416
                           Z:NO
                          id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv3fQQqZZidOn:(OC_VectorCall*)value
{
    id result = [value idv3f:(vector_float3){0.0, 1.5, 3.0}
                           Q:35184372088832
                           Q:35184372088832
                           q:-17592186044416
                           Z:NO
                           Z:NO
                          id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv3fZqidOn:(OC_VectorCall*)value
{
    id result = [value idv3f:(vector_float3){0.0, 1.5, 3.0}
                           Z:NO
                           q:-17592186044416
                          id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idv4fOn:(OC_VectorCall*)value
{
    id result = [value idv4f:(vector_float4){0.0, 1.5, 3.0, 4.5}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididv2dv2dv2iZOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
                        v2d:(vector_double2){0.0, 1.5}
                        v2d:(vector_double2){0.0, 1.5}
                        v2i:(vector_int2){0, 1}
                          Z:NO];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididv2fOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello" v2f:(vector_float2){0.0, 1.5}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididv3fOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello" v3f:(vector_float3){0.0, 1.5, 3.0}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididv4fOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello" v4f:(vector_float4){0.0, 1.5, 3.0, 4.5}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idididv2iOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello" id:@"hello" v2i:(vector_int2){0, 1}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idididv2ifOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello" id:@"hello" v2i:(vector_int2){0, 1} f:2500000000.0];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididQv2fOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello" Q:35184372088832 v2f:(vector_float2){0.0, 1.5}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididQv3fOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello" Q:35184372088832 v3f:(vector_float3){0.0, 1.5, 3.0}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididQv4fOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
                          Q:35184372088832
                        v4f:(vector_float4){0.0, 1.5, 3.0, 4.5}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididQsimdfloat4x4On:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
                          Q:35184372088832
               simdfloat4x4:(simd_float4x4){{(vector_float4){0.0, 1.5, 3.0, 4.5},
                                             (vector_float4){0.0, 1.5, 3.0, 4.5},
                                             (vector_float4){0.0, 1.5, 3.0, 4.5},
                                             (vector_float4){0.0, 1.5, 3.0, 4.5}}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididZidv2iqQqZOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
                          Z:NO
                         id:@"hello"
                        v2i:(vector_int2){0, 1}
                          q:-17592186044416
                          Q:35184372088832
                          q:-17592186044416
                          Z:NO];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididqv2iffffOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
                          q:-17592186044416
                        v2i:(vector_int2){0, 1}
                          f:2500000000.0
                          f:2500000000.0
                          f:2500000000.0
                          f:2500000000.0];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididqv2ifffffOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
                          q:-17592186044416
                        v2i:(vector_int2){0, 1}
                          f:2500000000.0
                          f:2500000000.0
                          f:2500000000.0
                          f:2500000000.0
                          f:2500000000.0];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)ididGKBoxOn:(OC_VectorCall*)value
{
    id result = [value
         idid:@"hello"
        GKBox:(GKBox){(vector_float3){1.0, 2.0, 3.0}, (vector_float3){4.0, 5.0, 6.0}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)ididGKQuadOn:(OC_VectorCall*)value
{
    id result =
        [value idid:@"hello"
             GKQuad:(GKQuad){(vector_float2){9.0, 10.0}, (vector_float2){11.0, 12.0}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (id)ididMDLAxisAlignedBoundingBoxfOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
        MDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox) {
            (vector_float3){-8.0, -9.0, -10.0}, (vector_float3) { -11.0, -12.0, -13.0 }
        }
                                f:2500000000.0];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

+ (id)ididsimdfloat2x2On:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
               simdfloat2x2:(simd_float2x2){
                                {(vector_float2){0.0, 1.5}, (vector_float2){0.0, 1.5}}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididsimdfloat3x3On:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
               simdfloat3x3:(simd_float3x3){{(vector_float3){0.0, 1.5, 3.0},
                                             (vector_float3){0.0, 1.5, 3.0},
                                             (vector_float3){0.0, 1.5, 3.0}}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)ididsimdfloat4x4On:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
               simdfloat4x4:(simd_float4x4){{(vector_float4){0.0, 1.5, 3.0, 4.5},
                                             (vector_float4){0.0, 1.5, 3.0, 4.5},
                                             (vector_float4){0.0, 1.5, 3.0, 4.5},
                                             (vector_float4){0.0, 1.5, 3.0, 4.5}}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

#if PyObjC_BUILD_RELEASE >= 1013
+ (id)ididsimdquatfOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
                  simdquatf:(simd_quatf){(vector_float4){0.0, 1.5, 3.0, 4.5}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (id)ididsimdquatfidOn:(OC_VectorCall*)value
{
    id result = [value idid:@"hello"
                  simdquatf:(simd_quatf) {
                      (vector_float4) { 0.0, 1.5, 3.0, 4.5 }
                  }
                         id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

+ (id)idCGColorCGColoridv2iOn:(OC_VectorCall*)value
{
    id result = [value idCGColor:(CGColorRef) @"color!"
                         CGColor:(CGColorRef) @"color!"
                              id:@"hello"
                             v2i:(vector_int2){0, 1}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idfv2fv2fOn:(OC_VectorCall*)value
{
    id result = [value idf:2500000000.0
                       v2f:(vector_float2){0.0, 1.5}
                       v2f:(vector_float2){0.0, 1.5}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idfv2fv2fClassOn:(OC_VectorCall*)value
{
    id result = [value idf:2500000000.0
                       v2f:(vector_float2){0.0, 1.5}
                       v2f:(vector_float2){0.0, 1.5}
                     Class:[NSObject class]];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idfv2fQQQqZidOn:(OC_VectorCall*)value
{
    id result = [value idf:2500000000.0
                       v2f:(vector_float2){0.0, 1.5}
                         Q:35184372088832
                         Q:35184372088832
                         Q:35184372088832
                         q:-17592186044416
                         Z:NO
                        id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idfv2fQQqZidOn:(OC_VectorCall*)value
{
    id result = [value idf:2500000000.0
                       v2f:(vector_float2){0.0, 1.5}
                         Q:35184372088832
                         Q:35184372088832
                         q:-17592186044416
                         Z:NO
                        id:@"hello"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idfidv2iiqZOn:(OC_VectorCall*)value
{
    id result = [value idf:2500000000.0
                        id:@"hello"
                       v2i:(vector_int2){0, 1}
                         i:-42
                         q:-17592186044416
                         Z:NO];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idfidv2iiqCGColorCGColorOn:(OC_VectorCall*)value
{
    id result = [value idf:2500000000.0
                        id:@"hello"
                       v2i:(vector_int2){0, 1}
                         i:-42
                         q:-17592186044416
                   CGColor:(CGColorRef) @"color!"
                   CGColor:(CGColorRef) @"color!"];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idfidv2iqOn:(OC_VectorCall*)value
{
    id result = [value idf:2500000000.0
                        id:@"hello"
                       v2i:(vector_int2){0, 1}
                         q:-17592186044416];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idffidv2iOn:(OC_VectorCall*)value
{
    id result = [value idf:2500000000.0
                         f:2500000000.0
                        id:@"hello"
                       v2i:(vector_int2){0, 1}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)idGKBoxOn:(OC_VectorCall*)value
{
    id result = [value
        idGKBox:(GKBox){(vector_float3){1.0, 2.0, 3.0}, (vector_float3){4.0, 5.0, 6.0}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)idGKBoxfOn:(OC_VectorCall*)value
{
    id result = [value idGKBox:(GKBox) {
        (vector_float3){1.0, 2.0, 3.0}, (vector_float3) { 4.0, 5.0, 6.0 }
    }
                             f:2500000000.0];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)idGKQuadOn:(OC_VectorCall*)value
{
    id result = [value
        idGKQuad:(GKQuad){(vector_float2){9.0, 10.0}, (vector_float2){11.0, 12.0}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)idGKQuadfOn:(OC_VectorCall*)value
{
    id result = [value idGKQuad:(GKQuad) {
        (vector_float2){9.0, 10.0}, (vector_float2) { 11.0, 12.0 }
    }
                              f:2500000000.0];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (id)idMDLVoxelIndexExtentOn:(OC_VectorCall*)value
{
    id result = [value
        idMDLVoxelIndexExtent:(MDLVoxelIndexExtent){(vector_int4){100, 101, 102, 103},
                                                    (vector_int4){-20, -21, -22, -23}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

+ (id)idsimdfloat4x4On:(OC_VectorCall*)value
{
    id result =
        [value idsimdfloat4x4:(simd_float4x4){{(vector_float4){0.0, 1.5, 3.0, 4.5},
                                               (vector_float4){0.0, 1.5, 3.0, 4.5},
                                               (vector_float4){0.0, 1.5, 3.0, 4.5},
                                               (vector_float4){0.0, 1.5, 3.0, 4.5}}}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)idsimdfloat4x4ZOn:(OC_VectorCall*)value
{
    id result = [value idsimdfloat4x4:(simd_float4x4) {
        {
            (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
                (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4)
            {
                0.0, 1.5, 3.0, 4.5
            }
        }
    }
                                    Z:NO];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("@", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)Zv2iididididOn:(OC_VectorCall*)value
{
    BOOL result = [value Zv2i:(vector_int2){0, 1}
                           id:@"hello"
                           id:@"hello"
                           id:@"hello"
                           id:@"hello"];
    id   cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("Z", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)Zv2iqfidididOn:(OC_VectorCall*)value
{
    BOOL result = [value Zv2i:(vector_int2){0, 1}
                            q:-17592186044416
                            f:2500000000.0
                           id:@"hello"
                           id:@"hello"
                           id:@"hello"];
    id   cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("Z", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)Zv4iZZZZOn:(OC_VectorCall*)value
{
    BOOL result = [value Zv4i:(vector_int4){0, 1, 2, 3} Z:NO Z:NO Z:NO Z:NO];
    id   cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("Z", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)CGColorv3fOn:(OC_VectorCall*)value
{
    CGColorRef result = [value CGColorv3f:(vector_float3){0.0, 1.5, 3.0}];
    id         cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("^{CGColor=}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)CGColorv3fCGColorSpaceOn:(OC_VectorCall*)value
{
    CGColorRef result = [value CGColorv3f:(vector_float3){0.0, 1.5, 3.0}
                             CGColorSpace:(CGColorSpaceRef) @"colorspace!"];
    id         cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("^{CGColor=}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)fv2fOn:(OC_VectorCall*)value
{
    float result = [value fv2f:(vector_float2){0.0, 1.5}];
    id    cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("f", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)fv2iOn:(OC_VectorCall*)value
{
    float result = [value fv2i:(vector_int2){0, 1}];
    id    cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("f", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (void)vv2dOn:(OC_VectorCall*)value
{
    [value vv2d:(vector_double2){0.0, 1.5}];
}

+ (void)vv2ddOn:(OC_VectorCall*)value
{
    [value vv2d:(vector_double2){0.0, 1.5} d:-557000000000.0];
}

+ (void)vv2fOn:(OC_VectorCall*)value
{
    [value vv2f:(vector_float2){0.0, 1.5}];
}

+ (void)vv2fdOn:(OC_VectorCall*)value
{
    [value vv2f:(vector_float2){0.0, 1.5} d:-557000000000.0];
}

+ (void)vv3dOn:(OC_VectorCall*)value
{
    [value vv3d:(vector_double3){0.0, 1.5, 3.0}];
}

+ (void)vv3ddOn:(OC_VectorCall*)value
{
    [value vv3d:(vector_double3){0.0, 1.5, 3.0} d:-557000000000.0];
}

+ (void)vv3fOn:(OC_VectorCall*)value
{
    [value vv3f:(vector_float3){0.0, 1.5, 3.0}];
}

+ (void)vv3fv3fOn:(OC_VectorCall*)value
{
    [value vv3f:(vector_float3){0.0, 1.5, 3.0} v3f:(vector_float3){0.0, 1.5, 3.0}];
}

+ (void)vv3fv3fv3fOn:(OC_VectorCall*)value
{
    [value vv3f:(vector_float3){0.0, 1.5, 3.0}
            v3f:(vector_float3){0.0, 1.5, 3.0}
            v3f:(vector_float3){0.0, 1.5, 3.0}];
}

+ (void)vv3fdOn:(OC_VectorCall*)value
{
    [value vv3f:(vector_float3){0.0, 1.5, 3.0} d:-557000000000.0];
}

+ (void)vv4ddOn:(OC_VectorCall*)value
{
    [value vv4d:(vector_double4){0.0, 1.5, 3.0, 4.5} d:-557000000000.0];
}

+ (void)vv4fOn:(OC_VectorCall*)value
{
    [value vv4f:(vector_float4){0.0, 1.5, 3.0, 4.5}];
}

+ (void)vv4fdOn:(OC_VectorCall*)value
{
    [value vv4f:(vector_float4){0.0, 1.5, 3.0, 4.5} d:-557000000000.0];
}

+ (void)vv4iOn:(OC_VectorCall*)value
{
    [value vv4i:(vector_int4){0, 1, 2, 3}];
}

+ (void)vidv2fv2fOn:(OC_VectorCall*)value
{
    [value vid:@"hello" v2f:(vector_float2){0.0, 1.5} v2f:(vector_float2){0.0, 1.5}];
}

+ (void)vidv2fv2fqOn:(OC_VectorCall*)value
{
    [value vid:@"hello"
           v2f:(vector_float2){0.0, 1.5}
           v2f:(vector_float2){0.0, 1.5}
             q:-17592186044416];
}

+ (void)vfv2iOn:(OC_VectorCall*)value
{
    [value vf:2500000000.0 v2i:(vector_int2){0, 1}];
}

#if PyObjC_BUILD_RELEASE >= 1011
+ (void)vMDLAxisAlignedBoundingBoxOn:(OC_VectorCall*)value
{
    [value vMDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox){
                                          (vector_float3){-8.0, -9.0, -10.0},
                                          (vector_float3){-11.0, -12.0, -13.0}}];
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (void)vMDLAxisAlignedBoundingBoxZOn:(OC_VectorCall*)value
{
    [value vMDLAxisAlignedBoundingBox:(MDLAxisAlignedBoundingBox) {
        (vector_float3){-8.0, -9.0, -10.0}, (vector_float3) { -11.0, -12.0, -13.0 }
    }
                                    Z:NO];
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

+ (void)vsimddouble4x4On:(OC_VectorCall*)value
{
    [value vsimddouble4x4:(simd_double4x4){{(vector_double4){0.0, 1.5, 3.0, 4.5},
                                            (vector_double4){0.0, 1.5, 3.0, 4.5},
                                            (vector_double4){0.0, 1.5, 3.0, 4.5},
                                            (vector_double4){0.0, 1.5, 3.0, 4.5}}}];
}

+ (void)vsimddouble4x4dOn:(OC_VectorCall*)value
{
    [value vsimddouble4x4:(simd_double4x4) {
        {
            (vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4){0.0, 1.5, 3.0, 4.5},
                (vector_double4){0.0, 1.5, 3.0, 4.5}, (vector_double4)
            {
                0.0, 1.5, 3.0, 4.5
            }
        }
    }
                        d:-557000000000.0];
}

+ (void)vsimdfloat2x2On:(OC_VectorCall*)value
{
    [value vsimdfloat2x2:(simd_float2x2){
                             {(vector_float2){0.0, 1.5}, (vector_float2){0.0, 1.5}}}];
}

+ (void)vsimdfloat3x3On:(OC_VectorCall*)value
{
    [value vsimdfloat3x3:(simd_float3x3){{(vector_float3){0.0, 1.5, 3.0},
                                          (vector_float3){0.0, 1.5, 3.0},
                                          (vector_float3){0.0, 1.5, 3.0}}}];
}

+ (void)vsimdfloat4x4On:(OC_VectorCall*)value
{
    [value vsimdfloat4x4:(simd_float4x4){{(vector_float4){0.0, 1.5, 3.0, 4.5},
                                          (vector_float4){0.0, 1.5, 3.0, 4.5},
                                          (vector_float4){0.0, 1.5, 3.0, 4.5},
                                          (vector_float4){0.0, 1.5, 3.0, 4.5}}}];
}

+ (void)vsimdfloat4x4dOn:(OC_VectorCall*)value
{
    [value vsimdfloat4x4:(simd_float4x4) {
        {
            (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
                (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4)
            {
                0.0, 1.5, 3.0, 4.5
            }
        }
    }
                       d:-557000000000.0];
}

#if PyObjC_BUILD_RELEASE >= 1013
+ (void)vsimdquatddOn:(OC_VectorCall*)value
{
    [value vsimdquatd:(simd_quatd) {
        (vector_double4) { 0.0, 1.5, 3.0, 4.5 }
    }
                    d:-557000000000.0];
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (void)vsimdquatfOn:(OC_VectorCall*)value
{
    [value vsimdquatf:(simd_quatf){(vector_float4){0.0, 1.5, 3.0, 4.5}}];
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (void)vsimdquatfv3fOn:(OC_VectorCall*)value
{
    [value vsimdquatf:(simd_quatf) {
        (vector_float4) { 0.0, 1.5, 3.0, 4.5 }
    }
                  v3f:(vector_float3){0.0, 1.5, 3.0}];
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (void)vsimdquatfdOn:(OC_VectorCall*)value
{
    [value vsimdquatf:(simd_quatf) {
        (vector_float4) { 0.0, 1.5, 3.0, 4.5 }
    }
                    d:-557000000000.0];
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)GKBoxOn:(OC_VectorCall*)value
{
    id    cinter;
    GKBox result = [value GKBox];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{GKBox=<3f><3f>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)GKQuadOn:(OC_VectorCall*)value
{
    id     cinter;
    GKQuad result = [value GKQuad];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{GKQuad=<2f><2f>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
+ (id)GKTriangleQOn:(OC_VectorCall*)value
{
    GKTriangle result = [value GKTriangleQ:35184372088832];
    id         cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{GKTriangle=[3<3f>]}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (id)MDLAxisAlignedBoundingBoxOn:(OC_VectorCall*)value
{
    id                        cinter;
    MDLAxisAlignedBoundingBox result = [value MDLAxisAlignedBoundingBox];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter =
            PyObjC_ObjCToPython("{MDLAxisAlignedBoundingBox=<3f><3f>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (id)MDLAxisAlignedBoundingBoxv4iOn:(OC_VectorCall*)value
{
    MDLAxisAlignedBoundingBox result =
        [value MDLAxisAlignedBoundingBoxv4i:(vector_int4){0, 1, 2, 3}];
    id cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter =
            PyObjC_ObjCToPython("{MDLAxisAlignedBoundingBox=<3f><3f>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (id)MDLAxisAlignedBoundingBoxdOn:(OC_VectorCall*)value
{
    MDLAxisAlignedBoundingBox result = [value MDLAxisAlignedBoundingBoxd:-557000000000.0];
    id                        cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter =
            PyObjC_ObjCToPython("{MDLAxisAlignedBoundingBox=<3f><3f>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
+ (id)MDLVoxelIndexExtentOn:(OC_VectorCall*)value
{
    id                  cinter;
    MDLVoxelIndexExtent result = [value MDLVoxelIndexExtent];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{MDLVoxelIndexExtent=<4i><4i>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

+ (id)simddouble4x4On:(OC_VectorCall*)value
{
    id             cinter;
    simd_double4x4 result = [value simddouble4x4];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_double4x4=[4<4d>]}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)simddouble4x4dOn:(OC_VectorCall*)value
{
    simd_double4x4 result = [value simddouble4x4d:-557000000000.0];
    id             cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_double4x4=[4<4d>]}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)simdfloat2x2On:(OC_VectorCall*)value
{
    id            cinter;
    simd_float2x2 result = [value simdfloat2x2];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_float2x2=[2<2f>]}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)simdfloat3x3On:(OC_VectorCall*)value
{
    id            cinter;
    simd_float3x3 result = [value simdfloat3x3];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_float3x3=[3<3f>]}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)simdfloat4x4On:(OC_VectorCall*)value
{
    id            cinter;
    simd_float4x4 result = [value simdfloat4x4];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)simdfloat4x4iddOn:(OC_VectorCall*)value
{
    simd_float4x4 result = [value simdfloat4x4id:@"hello" d:-557000000000.0];
    id            cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)simdfloat4x4dOn:(OC_VectorCall*)value
{
    simd_float4x4 result = [value simdfloat4x4d:-557000000000.0];
    id            cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

+ (id)simdfloat4x4simdfloat4x4idOn:(OC_VectorCall*)value
{
    simd_float4x4 result = [value simdfloat4x4simdfloat4x4:(simd_float4x4) {
        {
            (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4){0.0, 1.5, 3.0, 4.5},
                (vector_float4){0.0, 1.5, 3.0, 4.5}, (vector_float4)
            {
                0.0, 1.5, 3.0, 4.5
            }
        }
    }
                                                        id:@"hello"];
    id            cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_float4x4=[4<4f>]}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

#if PyObjC_BUILD_RELEASE >= 1013
+ (id)simdquatddOn:(OC_VectorCall*)value
{
    simd_quatd result = [value simdquatdd:-557000000000.0];
    id         cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_quatd=<4d>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (id)simdquatfOn:(OC_VectorCall*)value
{
    id         cinter;
    simd_quatf result = [value simdquatf];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
+ (id)simdquatfdOn:(OC_VectorCall*)value
{
    simd_quatf result = [value simdquatfd:-557000000000.0];
    id         cinter;
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("{simd_quatf=<4f>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

+ (id)v16COn:(OC_VectorCall*)value
{
    id           cinter;
    simd_uchar16 result = [value v16C];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter = PyObjC_ObjCToPython("<16C>", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}

#if PyObjC_BUILD_RELEASE >= 1013
+ (id)MPSImageHistogramInfoOn:(OC_VectorCall*)value
{
    id                    cinter;
    MPSImageHistogramInfo result = [value MPSImageHistogramInfo];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter =
            PyObjC_ObjCToPython("{MPSImageHistogramInfo=QZ<4f><4f>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1014
+ (id)MPSAxisAlignedBoundingBoxOn:(OC_VectorCall*)value
{
    id                        cinter;
    MPSAxisAlignedBoundingBox result = [value MPSAxisAlignedBoundingBox];
    PyObjC_BEGIN_WITH_GIL
        PyObject* inter =
            PyObjC_ObjCToPython("{_MPSAxisAlignedBoundingBox=<3f><3f>}", &result);
        if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {
            PyObjC_GIL_FORWARD_EXC();
        }
    PyObjC_END_WITH_GIL
    return cinter;
}
#endif /* PyObjC_BUILD_RELEASE >= 1014 */

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
    if (PyModule_AddObject(m, "OC_VectorCallInvoke",
                           PyObjC_IdToPython([OC_VectorCallInvoke class]))
        < 0) {
        return NULL;
    }

    return m;
}
