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
#endif /*  PyObjC_BULD_RELEASE < 1013 */

@interface OC_Vector : NSObject {
    PyObject* values;
}
@end

@implementation OC_Vector
- (instancetype)init
{
    self = [super init];
    if (self == nil) {
        return nil;
    }
    values = NULL;
    return self;
}

- (id)getAndResetValues
{
    if (values == NULL) {
        return nil;
    }

    id result;
    PyObjC_BEGIN_WITH_GIL
        if (PyObjC_PythonToObjC(@encode(id), values, &result) == -1) {
            PyErr_Clear();
            result = nil;
        }
        Py_CLEAR(values);
    PyObjC_END_WITH_GIL
    return result;
}
- (void)dealloc
{
    PyObjC_BEGIN_WITH_GIL
        if (values) {
            Py_CLEAR(values);
        }
    PyObjC_END_WITH_GIL
    [super dealloc];
}

#define SET_VALUE(name, type, encoding)                                                  \
    -(void)name : (type)value                                                            \
    {                                                                                    \
        PyObjC_BEGIN_WITH_GIL                                                            \
            Py_CLEAR(values);                                                            \
            values = PyObjC_ObjCToPython(encoding, &value);                              \
        PyObjC_END_WITH_GIL                                                              \
    }

#define SET_VALUE_VALUE(name, name2, type1, encoding1, type2, encoding2)                 \
    -(void)name : (type1)value1 name2 : (type2)value2                                    \
    {                                                                                    \
        PyObjC_BEGIN_WITH_GIL                                                            \
            Py_CLEAR(values);                                                            \
        PyObjC_END_WITH_GIL                                                              \
        values = Py_BuildValue("(NN)", PyObjC_ObjCToPython(encoding1, &value1),          \
                               PyObjC_ObjCToPython(encoding2, &value2));                 \
    }

#define CALC_VALUE_VALUE(name, name2, type1, encoding1, type2, encoding2)                \
    -(id)name : (type1)value1 name2 : (type2)value2                                      \
    {                                                                                    \
        id result;                                                                       \
        PyObjC_BEGIN_WITH_GIL                                                            \
            PyObject* temp =                                                             \
                Py_BuildValue("(NN)", PyObjC_ObjCToPython(encoding1, &value1),           \
                              PyObjC_ObjCToPython(encoding2, &value2));                  \
            if (temp == NULL) {                                                          \
                PyErr_Clear();                                                           \
                PyObjC_GIL_RETURN(nil);                                                  \
            }                                                                            \
            if (PyObjC_PythonToObjC(@encode(id), temp, &result) == -1) {                 \
                Py_DECREF(temp);                                                         \
                PyErr_Clear();                                                           \
                result = nil;                                                            \
            }                                                                            \
            Py_DECREF(temp);                                                             \
        PyObjC_END_WITH_GIL                                                              \
        return result;                                                                   \
    }

#define GET_VALUE(name, type, value)                                                     \
    -(type)name { return value; }

SET_VALUE(setVectorFloat2, simd_float2, "<2f>")
SET_VALUE(setVectorFloat3, simd_float3, "<3f>")
SET_VALUE(setVectorFloat4, simd_float4, "<4f>")

GET_VALUE(getVectorUChar16, simd_uchar16,
          ((simd_uchar16){1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 16}))
GET_VALUE(getVectorDouble2, simd_double2, ((simd_double2){-42.9, 42.8}))
GET_VALUE(getVectorFloat2, simd_float2, ((simd_float2){-9.5, 10.5}))
GET_VALUE(getVectorFloat3, simd_float3, ((simd_float3){-8.5, 9.5, 12.5}))
GET_VALUE(getVectorFloat4, simd_float4, ((simd_float4){-7.5, 13.5, 14.5, 16.5}))
GET_VALUE(getVectorInt2, simd_int2, ((simd_int2){42, 43}))
#if PyObjC_BUILD_RELEASE >= 1012
GET_VALUE(getGKBox, GKBox, ((GKBox){{1.5, 2.5, 3.5}, {4.5, 5.5, 6.5}}))
GET_VALUE(getGKQuad, GKQuad, ((GKQuad){{7.5, 8.5}, {9.5, 10.5}}))
#endif /*  PyObjC_BUILD_RELEASE >= 1012 */
#if PyObjC_BUILD_RELEASE >= 1011
GET_VALUE(getMDLAxisAlignedBoundingBox, MDLAxisAlignedBoundingBox,
          ((MDLAxisAlignedBoundingBox){{11.5, 12.5, 13.5}, {14.5, 15.5, 16.5}}))
#endif /*  PyObjC_BUILD_RELEASE >= 1011 */
#if PyObjC_BUILD_RELEASE >= 1011
GET_VALUE(getMDLVoxelIndexExtent, MDLVoxelIndexExtent,
          ((MDLVoxelIndexExtent){{-1, -2, -3, -4}, {-5, -6, -7, -8}}))
#endif /*  PyObjC_BUILD_RELEASE >= 1011 */
#if PyObjC_BUILD_RELEASE >= 1014
GET_VALUE(getMPSAxisAlignedBoundingBox, MPSAxisAlignedBoundingBox,
          ((MPSAxisAlignedBoundingBox){{-1.5, -2.5, -3.5}, {-5.5, -6.5, -7.5}}))
#endif /* PyObjC_BUILD_RELEASE >= 1014 */
#if PyObjC_BUILD_RELEASE >= 1013
GET_VALUE(getMPSImageHistogramInfo, MPSImageHistogramInfo,
          ((MPSImageHistogramInfo){
              1ULL << 40, YES, {-8.5, -9.5, -10.5, -11.5}, {-12.5, -13.5, -14.5, -15.5}}))
#endif /* PyObjC_BUILD_RELEASE >= 1013 */
GET_VALUE(getMatrixDouble4x4, matrix_double4x4,
          ((matrix_double4x4){{{-20.5, -21.5, -22.5, -23.5},
                               {-30.5, -31.5, -32.5, -33.5},
                               {-40.5, -41.5, -42.5, -43.5},
                               {-50.5, -51.5, -52.5, -53.5}}}))
GET_VALUE(getMatrixFloat2x2, matrix_float2x2,
          ((matrix_float2x2){{{-20.5, -21.5}, {-30.5, -31.5}}}))
GET_VALUE(getMatrixFloat3x3, matrix_float3x3,
          ((matrix_float3x3){{{-120.5, -121.5, -122.5},
                              {-130.5, -131.5, -132.5},
                              {-140.5, -141.5, -142.5}}}))
GET_VALUE(getMatrixFloat4x4, matrix_float4x4,
          ((matrix_float4x4){{{-220.5, -221.5, -222.5, 10.5},
                              {-230.5, -231.5, -232.5, 11.5},
                              {-240.5, -241.5, -242.5, 12.5},
                              {-250.5, -251.5, -252.5, 13.5}}}))
#if PyObjC_BUILD_RELEASE >= 1013
GET_VALUE(getSimdFloat4x4, simd_float4x4,
          ((simd_float4x4){{{-320.5, -321.5, -322.5, 1.5},
                            {-330.5, -331.5, -332.5, 2.5},
                            {-340.5, -341.5, -342.5, 3.5},
                            {-350.5, -351.5, -352.5, 4.5}}}))
GET_VALUE(getSimdQuatf, simd_quatf, ((simd_quatf){{-420.5, -421.5, -422.5}}))
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

SET_VALUE_VALUE(setVectorFloat3, andFloat3, simd_float3, "<3f>", simd_float3, "<3f>")
SET_VALUE_VALUE(setVectorFloat3, andInt4, simd_float3, "<3f>", simd_int4, "<4i>")
SET_VALUE_VALUE(setVectorInt4, andFloat3, simd_int4, "<4i>", simd_float3, "<3f>")
SET_VALUE_VALUE(setId, andFloat2, id, "@", simd_float2, "<2f>")
SET_VALUE_VALUE(setId, andFloat3, id, "@", simd_float3, "<3f>")
SET_VALUE_VALUE(setId, andFloat4, id, "@", simd_float4, "<4f>")

CALC_VALUE_VALUE(calcId, andFloat2, id, "@", simd_float2, "<2f>")
CALC_VALUE_VALUE(calcId, andFloat3, id, "@", simd_float3, "<3f>")
CALC_VALUE_VALUE(calcId, andFloat4, id, "@", simd_float4, "<4f>")

@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "vector", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_vector(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_vector(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    if (PyModule_AddObject(m, "OC_Vector", PyObjC_IdToPython([OC_Vector class])) < 0) {
        return NULL;
    }

    return m;
}
