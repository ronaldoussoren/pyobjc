/*
 * Specific support for methods using SIMD types
 *
 * These helpers implement the method signatures
 * used in Cocoa bindings because there is no generic support
 * for SIMD types in libffi
 * (see <https://github.com/libffi/libffi/issues/408>
 *
 * There should be helpers in here for all methods that
 * use SIMD types in there arguments or return values, specifically
 * when SIMD types or structs containing SIMD types
 * are returned or passed by value. Pass by reference
 * arguments are handled correctly by the implementation
 * using libffi.
 *
 * Every implementation in this file should be tested
 * in PyObjCTest/test_vector_proxy.py, with a helper
 * method in Modules/objc/vector.m.
 *
 * The implementation of new number of arguments should
 * follow the structure with macros in this file, even
 * if there is only one user at first.
 *
 * When registering a method with "Z" (NSBOOL) as one of the
 * encodings * used, also register "B" (bool).
 *
 * XXX: There should be "imp" variants for signatures
 * used in protocols that are intended to be implemented
 * by API users, those should ``imp_implementationWithBlock``
 * as used in block-as-imp.m (and fold the mechanism used
 * in that file into registry.[hm])
 *
 * XXX: Use the Parse helpers to simplify the generated
 *      implementation. Basically only the actual invocation
 *      needs to be custom, the rest can be the same as in
 *      the FFI caller.
 *
 *      But: check generated code size and only do this when
 *      this reduces code size!
 *
 * XXX: Also use this for simple basic methods '-(id)method',
 *      '-(void)method:arg', and '(void)method', but this also
 *      needs the 'imp' variants.
 *
 */
#import "pyobjc.h"
#include <simd/simd.h>

#import <GameplayKit/GameplayKit.h>
#import <MetalPerformanceShaders/MetalPerformanceShaders.h>
#import <ModelIO/ModelIO.h>

#define CALL_RV(name, rv_type, rv_encoding)                                              \
    static PyObject* name(PyObject* method, PyObject* self,                              \
                          PyObject* const* arguments __attribute__((__unused__)),        \
                          size_t           nargs)                                        \
    {                                                                                    \
        struct objc_super super;                                                         \
                                                                                         \
        rv_type rv;                                                                      \
                                                                                         \
        if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)                             \
            return NULL;                                                                 \
                                                                                         \
        int isIMP = PyObjCIMP_Check(method);                                             \
        Py_BEGIN_ALLOW_THREADS                                                           \
            @try {                                                                       \
                if (isIMP) {                                                             \
                    rv = ((rv_type(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(              \
                        PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));    \
                                                                                         \
                } else {                                                                 \
                    super.receiver    = PyObjCObject_GetObject(self);                    \
                    super.super_class = PyObjCSelector_GetClass(method);                 \
                                                                                         \
                    rv = ((rv_type(*)(struct objc_super*, SEL))objc_msgSendSuper)(       \
                        &super, PyObjCSelector_GetSelector(method));                     \
                }                                                                        \
                                                                                         \
            } @catch (NSObject * localException) {  /* LCOV_EXCL_LINE */                 \
                PyObjCErr_FromObjC(localException); /* LCOV_EXCL_LINE */                 \
            }                                                                            \
        Py_END_ALLOW_THREADS                                                             \
                                                                                         \
        if (PyErr_Occurred()) { /* LCOV_BR_EXCL_LINE */                                  \
            return NULL;        /* LCOV_EXCL_LINE */                                     \
        }                                                                                \
                                                                                         \
        return pythonify_c_value(rv_encoding, &rv);                                      \
    }

#define CALL_RV_ARG1(name, rv_type, arg_type, rv_encoding, arg_encoding)                 \
    static PyObject* name(PyObject* method, PyObject* self, PyObject* const* arguments,  \
                          size_t nargs)                                                  \
    {                                                                                    \
        struct objc_super super;                                                         \
                                                                                         \
        rv_type  rv;                                                                     \
        arg_type arg;                                                                    \
                                                                                         \
        if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)                             \
            return NULL;                                                                 \
                                                                                         \
        if (depythonify_c_value(arg_encoding, arguments[0], &arg) == -1) {               \
            return NULL;                                                                 \
        }                                                                                \
                                                                                         \
        int isIMP = PyObjCIMP_Check(method);                                             \
        Py_BEGIN_ALLOW_THREADS                                                           \
            @try {                                                                       \
                if (isIMP) {                                                             \
                    rv = ((rv_type(*)(id, SEL, arg_type))(PyObjCIMP_GetIMP(method)))(    \
                        PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),     \
                        arg);                                                            \
                                                                                         \
                } else {                                                                 \
                    super.receiver    = PyObjCObject_GetObject(self);                    \
                    super.super_class = PyObjCSelector_GetClass(method);                 \
                                                                                         \
                    rv = ((rv_type(*)(struct objc_super*, SEL,                           \
                                      arg_type))objc_msgSendSuper)(                      \
                        &super, PyObjCSelector_GetSelector(method), arg);                \
                }                                                                        \
                                                                                         \
            } @catch (NSObject * localException) {  /* LCOV_EXCL_LINE */                 \
                PyObjCErr_FromObjC(localException); /* LCOV_EXCL_LINE */                 \
            }                                                                            \
        Py_END_ALLOW_THREADS                                                             \
                                                                                         \
        if (PyErr_Occurred()) { /* LCOV_BR_EXCL_LINE */                                  \
            return NULL;        /* LCOV_EXCL_LINE */                                     \
        }                                                                                \
                                                                                         \
        return pythonify_c_value(rv_encoding, &rv);                                      \
    }

#define CALL_RV_ARG2(name, rv_type, arg1_type, arg2_type, rv_encoding, arg1_encoding,    \
                     arg2_encoding)                                                      \
    static PyObject* name(PyObject* method, PyObject* self, PyObject* const* arguments,  \
                          size_t nargs)                                                  \
    {                                                                                    \
        struct objc_super super;                                                         \
                                                                                         \
        rv_type   rv;                                                                    \
        arg1_type arg1;                                                                  \
        arg2_type arg2;                                                                  \
                                                                                         \
        if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)                             \
            return NULL;                                                                 \
                                                                                         \
        if (depythonify_c_value(arg1_encoding, arguments[0], &arg1) == -1) {             \
            return NULL;                                                                 \
        }                                                                                \
                                                                                         \
        if (depythonify_c_value(arg2_encoding, arguments[1], &arg2) == -1) {             \
            return NULL;                                                                 \
        }                                                                                \
                                                                                         \
        int isIMP = PyObjCIMP_Check(method);                                             \
        Py_BEGIN_ALLOW_THREADS                                                           \
            @try {                                                                       \
                if (isIMP) {                                                             \
                    rv = ((rv_type(*)(id, SEL, arg1_type, arg2_type))(PyObjCIMP_GetIMP(  \
                        method)))(PyObjCObject_GetObject(self),                          \
                                  PyObjCIMP_GetSelector(method), arg1, arg2);            \
                                                                                         \
                } else {                                                                 \
                    super.receiver    = PyObjCObject_GetObject(self);                    \
                    super.super_class = PyObjCSelector_GetClass(method);                 \
                                                                                         \
                    rv = ((rv_type(*)(struct objc_super*, SEL, arg1_type,                \
                                      arg2_type))objc_msgSendSuper)(                     \
                        &super, PyObjCSelector_GetSelector(method), arg1, arg2);         \
                }                                                                        \
                                                                                         \
            } @catch (NSObject * localException) {  /* LCOV_EXCL_LINE */                 \
                PyObjCErr_FromObjC(localException); /* LCOV_EXCL_LINE */                 \
            }                                                                            \
        Py_END_ALLOW_THREADS                                                             \
                                                                                         \
        if (PyErr_Occurred()) { /* LCOV_BR_EXCL_LINE */                                  \
            return NULL;        /* LCOV_EXCL_LINE */                                     \
        }                                                                                \
                                                                                         \
        return pythonify_c_value(rv_encoding, &rv);                                      \
    }

#define CALL_RV_ARG3(name, rv_type, arg1_type, arg2_type, arg3_type, rv_encoding,        \
                     arg1_encoding, arg2_encoding, arg3_encoding)                        \
    static PyObject* name(PyObject* method, PyObject* self, PyObject* const* arguments,  \
                          size_t nargs)                                                  \
    {                                                                                    \
        struct objc_super super;                                                         \
                                                                                         \
        rv_type   rv;                                                                    \
        arg1_type arg1;                                                                  \
        arg2_type arg2;                                                                  \
        arg3_type arg3;                                                                  \
                                                                                         \
        if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)                             \
            return NULL;                                                                 \
                                                                                         \
        if (depythonify_c_value(arg1_encoding, arguments[0], &arg1) == -1) {             \
            return NULL;                                                                 \
        }                                                                                \
                                                                                         \
        if (depythonify_c_value(arg2_encoding, arguments[1], &arg2) == -1) {             \
            return NULL;                                                                 \
        }                                                                                \
        if (depythonify_c_value(arg3_encoding, arguments[2], &arg3) == -1) {             \
            return NULL;                                                                 \
        }                                                                                \
                                                                                         \
        int isIMP = PyObjCIMP_Check(method);                                             \
        Py_BEGIN_ALLOW_THREADS                                                           \
            @try {                                                                       \
                if (isIMP) {                                                             \
                    rv = ((rv_type(*)(id, SEL, arg1_type, arg2_type, arg3_type))(        \
                        PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),         \
                                                   PyObjCIMP_GetSelector(method), arg1,  \
                                                   arg2, arg3);                          \
                                                                                         \
                } else {                                                                 \
                    super.receiver    = PyObjCObject_GetObject(self);                    \
                    super.super_class = PyObjCSelector_GetClass(method);                 \
                                                                                         \
                    rv = ((rv_type(*)(struct objc_super*, SEL, arg1_type, arg2_type,     \
                                      arg3_type))objc_msgSendSuper)(                     \
                        &super, PyObjCSelector_GetSelector(method), arg1, arg2, arg3);   \
                }                                                                        \
                                                                                         \
            } @catch (NSObject * localException) {  /* LCOV_EXCL_LINE */                 \
                PyObjCErr_FromObjC(localException); /* LCOV_EXCL_LINE */                 \
            }                                                                            \
        Py_END_ALLOW_THREADS                                                             \
                                                                                         \
        if (PyErr_Occurred()) { /* LCOV_BR_EXCL_LINE */                                  \
            return NULL;        /* LCOV_EXCL_LINE */                                     \
        }                                                                                \
                                                                                         \
        return pythonify_c_value(rv_encoding, &rv);                                      \
    }

#define CALL_V(name)                                                                     \
    static PyObject* name(PyObject* method, PyObject* self,                              \
                          PyObject* const* arguments __attribute__((__unused__)),        \
                          size_t           nargs)                                        \
    {                                                                                    \
        struct objc_super super;                                                         \
                                                                                         \
        if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)                             \
            return NULL;                                                                 \
                                                                                         \
        int isIMP = PyObjCIMP_Check(method);                                             \
        Py_BEGIN_ALLOW_THREADS                                                           \
            @try {                                                                       \
                if (isIMP) {                                                             \
                    ((void (*)(id, SEL))(PyObjCIMP_GetIMP(method)))(                     \
                        PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));    \
                                                                                         \
                } else {                                                                 \
                    super.receiver    = PyObjCObject_GetObject(self);                    \
                    super.super_class = PyObjCSelector_GetClass(method);                 \
                                                                                         \
                    ((void (*)(struct objc_super*, SEL))objc_msgSendSuper)(              \
                        &super, PyObjCSelector_GetSelector(method));                     \
                }                                                                        \
                                                                                         \
            } @catch (NSObject * localException) {  /* LCOV_EXCL_LINE */                 \
                PyObjCErr_FromObjC(localException); /* LCOV_EXCL_LINE */                 \
            }                                                                            \
        Py_END_ALLOW_THREADS                                                             \
                                                                                         \
        if (PyErr_Occurred()) { /* LCOV_BR_EXCL_LINE */                                  \
            return NULL;        /* LCOV_EXCL_LINE */                                     \
        }                                                                                \
                                                                                         \
        Py_INCREF(Py_None);                                                              \
        return Py_None;                                                                  \
    }

#define CALL_V_ARG1(name, arg_type, arg_encoding)                                        \
    static PyObject* name(PyObject* method, PyObject* self, PyObject* const* arguments,  \
                          size_t nargs)                                                  \
    {                                                                                    \
        arg_type          arg;                                                           \
        struct objc_super super;                                                         \
                                                                                         \
        if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)                             \
            return NULL;                                                                 \
                                                                                         \
        if (depythonify_c_value(arg_encoding, arguments[0], &arg) == -1) {               \
            return NULL;                                                                 \
        }                                                                                \
                                                                                         \
        int isIMP = PyObjCIMP_Check(method);                                             \
        Py_BEGIN_ALLOW_THREADS                                                           \
            @try {                                                                       \
                if (isIMP) {                                                             \
                    ((void (*)(id, SEL, arg_type))(PyObjCIMP_GetIMP(method)))(           \
                        PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),     \
                        arg);                                                            \
                                                                                         \
                } else {                                                                 \
                    super.receiver    = PyObjCObject_GetObject(self);                    \
                    super.super_class = PyObjCSelector_GetClass(method);                 \
                                                                                         \
                    ((void (*)(struct objc_super*, SEL, arg_type))objc_msgSendSuper)(    \
                        &super, PyObjCSelector_GetSelector(method), arg);                \
                }                                                                        \
                                                                                         \
            } @catch (NSObject * localException) {  /* LCOV_EXCL_LINE */                 \
                PyObjCErr_FromObjC(localException); /* LCOV_EXCL_LINE */                 \
            }                                                                            \
        Py_END_ALLOW_THREADS                                                             \
                                                                                         \
        if (PyErr_Occurred()) { /* LCOV_BR_EXCL_LINE */                                  \
            return NULL;        /* LCOV_EXCL_LINE */                                     \
        }                                                                                \
                                                                                         \
        Py_INCREF(Py_None);                                                              \
        return Py_None;                                                                  \
    }

#define CALL_V_ARG2(name, arg1_type, arg2_type, arg1_encoding, arg2_encoding)            \
    static PyObject* name(PyObject* method, PyObject* self, PyObject* const* arguments,  \
                          size_t nargs)                                                  \
    {                                                                                    \
        arg1_type         arg1;                                                          \
        arg2_type         arg2;                                                          \
        struct objc_super super;                                                         \
                                                                                         \
        if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)                             \
            return NULL;                                                                 \
                                                                                         \
        if (depythonify_c_value(arg1_encoding, arguments[0], &arg1) == -1) {             \
            return NULL;                                                                 \
        }                                                                                \
        if (depythonify_c_value(arg2_encoding, arguments[1], &arg2) == -1) {             \
            return NULL;                                                                 \
        }                                                                                \
                                                                                         \
        int isIMP = PyObjCIMP_Check(method);                                             \
        Py_BEGIN_ALLOW_THREADS                                                           \
            @try {                                                                       \
                if (isIMP) {                                                             \
                    ((void (*)(id, SEL, arg1_type, arg2_type))(PyObjCIMP_GetIMP(         \
                        method)))(PyObjCObject_GetObject(self),                          \
                                  PyObjCIMP_GetSelector(method), arg1, arg2);            \
                                                                                         \
                } else {                                                                 \
                    super.receiver    = PyObjCObject_GetObject(self);                    \
                    super.super_class = PyObjCSelector_GetClass(method);                 \
                                                                                         \
                    ((void (*)(struct objc_super*, SEL, arg1_type,                       \
                               arg2_type))objc_msgSendSuper)(                            \
                        &super, PyObjCSelector_GetSelector(method), arg1, arg2);         \
                }                                                                        \
                                                                                         \
            } @catch (NSObject * localException) {  /* LCOV_EXCL_LINE */                 \
                PyObjCErr_FromObjC(localException); /* LCOV_EXCL_LINE */                 \
            }                                                                            \
        Py_END_ALLOW_THREADS                                                             \
                                                                                         \
        if (PyErr_Occurred()) { /* LCOV_BR_EXCL_LINE */                                  \
            return NULL;        /* LCOV_EXCL_LINE */                                     \
        }                                                                                \
                                                                                         \
        Py_INCREF(Py_None);                                                              \
        return Py_None;                                                                  \
    }

#define CALL_V_ARG3(name, arg1_type, arg2_type, arg3_type, arg1_encoding, arg2_encoding, \
                    arg3_encoding)                                                       \
    static PyObject* name(PyObject* method, PyObject* self, PyObject* const* arguments,  \
                          size_t nargs)                                                  \
    {                                                                                    \
        arg1_type         arg1;                                                          \
        arg2_type         arg2;                                                          \
        arg3_type         arg3;                                                          \
        struct objc_super super;                                                         \
                                                                                         \
        if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)                             \
            return NULL;                                                                 \
                                                                                         \
        if (depythonify_c_value(arg1_encoding, arguments[0], &arg1) == -1) {             \
            return NULL;                                                                 \
        }                                                                                \
        if (depythonify_c_value(arg2_encoding, arguments[1], &arg2) == -1) {             \
            return NULL;                                                                 \
        }                                                                                \
        if (depythonify_c_value(arg3_encoding, arguments[2], &arg3) == -1) {             \
            return NULL;                                                                 \
        }                                                                                \
                                                                                         \
        int isIMP = PyObjCIMP_Check(method);                                             \
        Py_BEGIN_ALLOW_THREADS                                                           \
            @try {                                                                       \
                if (isIMP) {                                                             \
                    ((void (*)(id, SEL, arg1_type, arg2_type, arg3_type))(               \
                        PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),         \
                                                   PyObjCIMP_GetSelector(method), arg1,  \
                                                   arg2, arg3);                          \
                                                                                         \
                } else {                                                                 \
                    super.receiver    = PyObjCObject_GetObject(self);                    \
                    super.super_class = PyObjCSelector_GetClass(method);                 \
                                                                                         \
                    ((void (*)(struct objc_super*, SEL, arg1_type, arg2_type,            \
                               arg3_type))objc_msgSendSuper)(                            \
                        &super, PyObjCSelector_GetSelector(method), arg1, arg2, arg3);   \
                }                                                                        \
                                                                                         \
            } @catch (NSObject * localException) {  /* LCOV_EXCL_LINE */                 \
                PyObjCErr_FromObjC(localException); /* LCOV_EXCL_LINE */                 \
            }                                                                            \
        Py_END_ALLOW_THREADS                                                             \
                                                                                         \
        if (PyErr_Occurred()) { /* LCOV_BR_EXCL_LINE */                                  \
            return NULL;        /* LCOV_EXCL_LINE */                                     \
        }                                                                                \
                                                                                         \
        Py_INCREF(Py_None);                                                              \
        return Py_None;                                                                  \
    }

// CALL_V(call_v)

// CALL_V_ARG1(call_v_id, id, "@")
CALL_V_ARG1(call_v_v2f, simd_float2, "<2f>")
CALL_V_ARG1(call_v_v3f, simd_float3, "<3f>")
CALL_V_ARG1(call_v_v4f, simd_float4, "<4f>")

// CALL_RV(call_id, id, "@")
CALL_RV(call_GKBox, GKBox, "{GKBox=<3f><3f>}")
CALL_RV(call_GKQuad, GKQuad, "{GKQuad=<2f><2f>}")
CALL_RV(call_MDLAxisAlignedBoundingBox, MDLAxisAlignedBoundingBox,
        "{_MDLAxisAlignedBoundingBox=<3f><3f>}")
CALL_RV(call_MDLVoxelIndexExtent, MDLVoxelIndexExtent, "{_MDLVoxelIndexExtent=<4i><4i>}")
CALL_RV(call_MPSAxisAlignedBoundingBox, MPSAxisAlignedBoundingBox,
        "{_MPSAxisAlignedBoundingBox=<3f><3f>}")
CALL_RV(call_MPSImageHistogramInfo, MPSImageHistogramInfo,
        "{_MPSImageHistogramInfo=QZ<4f><4f>}")
CALL_RV(call_matrix_double4x4, matrix_double4x4, "{_matrix_double4x4=[4<4d>]}")
CALL_RV(call_matrix_float2x2, matrix_float2x2, "{_matrix_float2x2=[2<2f>]}")
CALL_RV(call_matrix_float3x3, matrix_float3x3, "{_matrix_float3x3=[3<3f>]}")
CALL_RV(call_matrix_float4x4, matrix_float4x4, "{_matrix_float4x4=[4<4f>]}")
CALL_RV(call_simd_float4x4, simd_float4x4, "{_simd_float4x4=[4<4f>]}")
CALL_RV(call_simd_quatf, simd_quatf, "{_simd_quatf=<4f>}")
CALL_RV(call_v16C, simd_uchar16, "<16C>")
CALL_RV(call_v2d, simd_double2, "<2d>")
CALL_RV(call_v2f, simd_float2, "<2f>")
CALL_RV(call_v2i, simd_int2, "<2i>")
CALL_RV(call_v3f, simd_float3, "<3f>")
CALL_RV(call_v4f, simd_float4, "<4f>")

CALL_RV_ARG1(call_GKTriangle_Q, GKTriangle, NSUInteger, "{GKTriangle=[3<3f>]}", "Q")
CALL_RV_ARG1(call_MDLAxisAlignedBoundingBox_d, MDLAxisAlignedBoundingBox, double,
             "{_MDLAxisAlignedBoundingBox=<3f><3f>}", "d")
CALL_RV_ARG1(call_MDLAxisAlignedBoundingBox_v4i, MDLAxisAlignedBoundingBox, vector_int4,
             "{_MDLAxisAlignedBoundingBox=<3f><3f>}", "<4i>")
CALL_RV_ARG1(call_f_v2f, float, vector_float2, "f", "<2f>")
CALL_RV_ARG1(call_f_v2i, float, vector_int2, "f", "<2i>")
CALL_RV_ARG1(call_id_2f, id, vector_float2, "@", "<2f>")
CALL_RV_ARG1(call_id_2i, id, vector_int2, "@", "<2i>")
CALL_RV_ARG1(call_id_3f, id, vector_float3, "@", "<3f>")
CALL_RV_ARG1(call_id_4f, id, vector_float4, "@", "<4f>")
CALL_RV_ARG1(call_id_v2f, id, simd_float2, "@", "<2f>")
CALL_RV_ARG1(call_id_v3f, id, simd_float3, "@", "<3f>")
CALL_RV_ARG1(call_id_v4f, id, simd_float4, "@", "<4f>")
CALL_RV_ARG1(call_m4x4d_d, matrix_double4x4, double, "{_matrix_double4x4=[4<4d>]}", "d")
CALL_RV_ARG1(call_m4x4f_d, matrix_float4x4, double, "{_matrix_float4x4=[4<4f>]}", "d")
CALL_RV_ARG1(call_qautd_d, simd_quatd, double, "{_simd_quatd=<4d>}", "d")
CALL_RV_ARG1(call_quatf_d, simd_quatf, double, "{_simd_quatf=<4f>}", "d")
CALL_RV_ARG1(call_v2d_d, simd_double2, double, "<2d>", "d")
CALL_RV_ARG1(call_v2f_Q, vector_float2, NSUInteger, "<2f>", "Q")
CALL_RV_ARG1(call_v2f_d, simd_float2, double, "<2f>", "d")
CALL_RV_ARG1(call_v2f_q, vector_float2, double, "<2f>", "q")
CALL_RV_ARG1(call_v3d_d, vector_double3, double, "<3d>", "d")
CALL_RV_ARG1(call_v3f_Q, vector_float3, NSUInteger, "<3f>", "Q")
CALL_RV_ARG1(call_v3f_d, simd_float3, double, "<3f>", "d")
CALL_RV_ARG1(call_v3f_v3f, simd_float3, simd_float3, "<3f>", "<3f>")
CALL_RV_ARG1(call_v3f_v4i, simd_float3, simd_int4, "<3f>", "<41>")
CALL_RV_ARG1(call_v4d_d, simd_double4, double, "<4d>", "d")
CALL_RV_ARG1(call_v4f_d, simd_float4, double, "<4f>", "d")
CALL_RV_ARG1(call_v4i_v3f, simd_int4, simd_float3, "<4i>", "<3f>")

CALL_RV_ARG2(call_id_id_v2f, id, id, simd_float2, "@", "@", "<2f>")
CALL_RV_ARG2(call_id_id_v3f, id, id, simd_float3, "@", "@", "<3f>")
CALL_RV_ARG2(call_id_id_v4f, id, id, simd_float4, "@", "@", "<4f>")
CALL_RV_ARG2(call_id_v2i_v2i, id, simd_float2, simd_float2, "@", "<2f>", "<2f>")
CALL_RV_ARG2(call_m4x4f_id_d, matrix_float4x4, id, double, "{_matrix_float4x4=[4<4f>]}",
             "@", "d")
CALL_RV_ARG2(call_m4x4f_m4x4f_id, simd_float4x4, simd_float4x4, id,
             "{_simd_float4x4=[4<4f>]}", "{_simd_float4x4=[4<4f>]}", "@")
CALL_RV_ARG2(call_v3f_v2i_v2i, simd_float3, simd_int2, simd_int2, "<3f>", "<2i>", "<2i>")
CALL_RV_ARG2(call_v3f_v3f_id, simd_float3, simd_float3, id, "<3f>", "<3f>", "@")

int
PyObjC_setup_simd(void)
{

#define REGISTER_RV(name, rv_encoding)                                                   \
    if (PyObjC_RegisterSignatureMapping(rv_encoding "@:", name,                          \
                                        PyObjCUnsupportedMethod_IMP)                     \
        == -1) {   /* LCOV_BR_EXCL_LINE */                                               \
        return -1; /* LCOV_EXCL_LINE */                                                  \
    }

#define REGISTER_RV_ARG1(name, rv_encoding, arg_encoding)                                \
    if (PyObjC_RegisterSignatureMapping(rv_encoding "@:" arg_encoding, name,             \
                                        PyObjCUnsupportedMethod_IMP)                     \
        == -1) {   /* LCOV_BR_EXCL_LINE */                                               \
        return -1; /* LCOV_EXCL_LINE */                                                  \
    }

#define REGISTER_RV_ARG2(name, rv_encoding, arg1_encoding, arg2_encoding)                \
    REGISTER_RV_ARG1(name, rv_encoding, arg1_encoding arg2_encoding)

#define REGISTER_RV_ARG3(name, rv_encoding, arg1_encoding, arg2_encoding, arg3_encoding) \
    REGISTER_RV_ARG1(name, rv_encoding, arg1_encoding arg2_encoding, arg3_encoding)

#define REGISTER_V(name)                                                                 \
    if (PyObjC_RegisterSignatureMapping("v@:", name, PyObjCUnsupportedMethod_IMP)        \
        == -1) {   /* LCOV_BR_EXCL_LINE */                                               \
        return -1; /* LCOV_EXCL_LINE */                                                  \
    }

#define REGISTER_V_ARG1(name, arg_encoding)                                              \
    if (PyObjC_RegisterSignatureMapping("v@:" arg_encoding, name,                        \
                                        PyObjCUnsupportedMethod_IMP)                     \
        == -1) {   /* LCOV_BR_EXCL_LINE */                                               \
        return -1; /* LCOV_EXCL_LINE */                                                  \
    }

#define REGISTER_V_ARG2(name, arg1_encoding, arg2_encoding)                              \
    REGISTER_V_ARG1(name, arg1_encoding arg2_encoding)

#define REGISTER_V_ARG3(name, arg1_encoding, arg2_encoding, arg3_encoding)               \
    REGISTER_V_ARG1(name, arg1_encoding arg2_encoding arg3_encoding)

    // REGISTER_RV(call_id, "@")
    REGISTER_RV(call_GKBox, "{GKBox=<3f><3f>}")
    REGISTER_RV(call_GKQuad, "{GKQuad=<2f><2f>}")
    REGISTER_RV(call_MDLAxisAlignedBoundingBox, "{_MDLAxisAlignedBoundingBox=<3f><3f>}")
    REGISTER_RV(call_MDLVoxelIndexExtent, "{_MDLVoxelIndexExtent=<4i><4i>}")
    REGISTER_RV(call_MPSAxisAlignedBoundingBox, "{_MPSAxisAlignedBoundingBox=<3f><3f>}")
    REGISTER_RV(call_MPSImageHistogramInfo, "{_MPSImageHistogramInfo=QZ<4f><4f>}")
    REGISTER_RV(call_matrix_double4x4, "{_matrix_double4x4=[4<4d>]}")
    REGISTER_RV(call_matrix_float2x2, "{_matrix_float2x2=[2<2f>]}")
    REGISTER_RV(call_matrix_float3x3, "{_matrix_float3x3=[3<3f>]}")
    REGISTER_RV(call_matrix_float4x4, "{_matrix_float4x4=[4<4f>]}")
    REGISTER_RV(call_simd_float4x4, "{_simd_float4x4=[4<4f>]}")
    REGISTER_RV(call_simd_quatf, "{_simd_quatf=<4f>}")
    REGISTER_RV(call_v16C, "<16C>")
    REGISTER_RV(call_v2d, "<2d>")
    REGISTER_RV(call_v2f, "<2f>")
    REGISTER_RV(call_v2i, "<2i>")
    REGISTER_RV(call_v3f, "<3f>")
    REGISTER_RV(call_v4f, "<4f>")

    REGISTER_RV_ARG1(call_GKTriangle_Q, "{GKTriangle=[3<3f>]}", "Q")
    REGISTER_RV_ARG1(call_MDLAxisAlignedBoundingBox_d,
                     "{_MDLAxisAlignedBoundingBox=<3f><3f>}", "d")
    REGISTER_RV_ARG1(call_MDLAxisAlignedBoundingBox_v4i,
                     "{_MDLAxisAlignedBoundingBox=<3f><3f>}", "<4i>")
    REGISTER_RV_ARG1(call_f_v2f, "f", "<2f>")
    REGISTER_RV_ARG1(call_f_v2i, "f", "<2i>")
    REGISTER_RV_ARG1(call_id_2f, "@", "<2f>")
    REGISTER_RV_ARG1(call_id_2i, "@", "<2i>")
    REGISTER_RV_ARG1(call_id_3f, "@", "<3f>")
    REGISTER_RV_ARG1(call_id_4f, "@", "<4f>")
    REGISTER_RV_ARG1(call_id_v2f, "@", "<2f>")
    REGISTER_RV_ARG1(call_id_v3f, "@", "<3f>")
    REGISTER_RV_ARG1(call_id_v4f, "@", "<4f>")
    REGISTER_RV_ARG1(call_m4x4d_d, "{_matrix_double4x4=[4<4d>]}", "d")
    REGISTER_RV_ARG1(call_m4x4f_d, "{_matrix_float4x4=[4<4f>]}", "d")
    REGISTER_RV_ARG1(call_qautd_d, "{_simd_quatd=<4d>}", "d")
    REGISTER_RV_ARG1(call_quatf_d, "{_simd_quatf=<4f>}", "d")
    REGISTER_RV_ARG1(call_v2d_d, "<2d>", "d")
    REGISTER_RV_ARG1(call_v2f_Q, "<2f>", "Q")
    REGISTER_RV_ARG1(call_v2f_d, "<2f>", "d")
    REGISTER_RV_ARG1(call_v2f_q, "<2f>", "q")
    REGISTER_RV_ARG1(call_v3d_d, "<3d>", "d")
    REGISTER_RV_ARG1(call_v3f_Q, "<3f>", "Q")
    REGISTER_RV_ARG1(call_v3f_d, "<3f>", "d")
    REGISTER_RV_ARG1(call_v3f_v3f, "<3f>", "<3f>")
    REGISTER_RV_ARG1(call_v3f_v4i, "<3f>", "<4i>")
    REGISTER_RV_ARG1(call_v4d_d, "<4d>", "d")
    REGISTER_RV_ARG1(call_v4f_d, "<4f>", "d")
    REGISTER_RV_ARG1(call_v4i_v3f, "<4i>", "<3f>")

    REGISTER_RV_ARG2(call_id_id_v2f, "@", "@", "<2f>")
    REGISTER_RV_ARG2(call_id_id_v3f, "@", "@", "<3f>")
    REGISTER_RV_ARG2(call_id_id_v4f, "@", "@", "<4f>")
    REGISTER_RV_ARG2(call_id_v2i_v2i, "@", "<2f>", "<2f>")
    REGISTER_RV_ARG2(call_m4x4f_id_d, "{_matrix_float4x4=[4<4f>]}", "@", "d")
    REGISTER_RV_ARG2(call_m4x4f_m4x4f_id, "{_simd_float4x4=[4<4f>]}",
                     "{_simd_float4x4=[4<4f>]}", "@")
    REGISTER_RV_ARG2(call_v3f_v2i_v2i, "<3f>", "<2i>", "<2i>")
    REGISTER_RV_ARG2(call_v3f_v3f_id, "<3f>", "<3f>", "@")

    // REGISTER_V(call_v)

    // REGISTER_V_ARG1(call_v_id, "@")
    REGISTER_V_ARG1(call_v_v2f, "<2f>")
    REGISTER_V_ARG1(call_v_v3f, "<3f>")
    REGISTER_V_ARG1(call_v_v4f, "<4f>")

    return 0;
}
