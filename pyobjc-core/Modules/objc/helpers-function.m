/*
 * This file is generated using Tools/generate-helpers-vector.py
 *
 *     ** DO NOT EDIT **
 */
#import "pyobjc.h"
#include <simd/simd.h>

#if PyObjC_BUILD_RELEASE >= 1011
#import <GameplayKit/GameplayKit.h>
#import <ModelIO/ModelIO.h>
#endif

#if PyObjC_BUILD_RELEASE >= 1013
#import <MetalPerformanceShaders/MetalPerformanceShaders.h>
#endif

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

/* Compositor services pointer types */
typedef void cp_drawable;
typedef void cp_frame;
typedef void cp_view;

NS_ASSUME_NONNULL_BEGIN

static PyObject* _Nullable adjust_retval(PyObjCMethodSignature* methinfo,
                                         id _Nullable retval)
{
    PyObject* result = id_to_python(retval);
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        // LCOV_EXCL_START
        assert(PyErr_Occurred());
        return NULL;
        // LCOV_EXCL_STOP
    }
    if (methinfo->rettype->alreadyRetained) {
        /* pythonify_c_return_value has retained the object, but we already
         * own a reference, therefore give the ref away again
         */
        [retval release];
    }

    if (methinfo->rettype->alreadyCFRetained) {
        /* pythonify_c_return_value has retained the object, but we already
         * own a reference, therefore give the ref away again
         */
        CFRelease(retval);
    }

    assert(!methinfo->initializer);

    return result;
}

static PyObject* _Nullable call_v3f_id(PyObject* method, PyObject* const* arguments,
                                       size_t nargs)
{
    simd_float3 rv;
    id          arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float3 (*)(id))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("<3f>", &rv);
}

static PyObject* _Nullable call_id_simd_float4x4(PyObject*        method,
                                                 PyObject* const* arguments, size_t nargs)
{
    id            rv;
    simd_float4x4 arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((id (*)(simd_float4x4))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    PyObject* result = adjust_retval(methinfo, rv);
    Py_CLEAR(methinfo);
    return result;
}

static PyObject* _Nullable call_id_simd_float4x4_f_f_q(PyObject*        method,
                                                       PyObject* const* arguments,
                                                       size_t           nargs)
{
    id            rv;
    simd_float4x4 arg0;
    float         arg1;
    float         arg2;
    long long     arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[3], &arg3) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((id (*)(simd_float4x4, float, float, long long))function)(arg0, arg1,
                                                                            arg2, arg3);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    PyObject* result = adjust_retval(methinfo, rv);
    Py_CLEAR(methinfo);
    return result;
}

static PyObject* _Nullable call_B_id_v3f(PyObject* method, PyObject* const* arguments,
                                         size_t nargs)
{
    bool        rv;
    id          arg0;
    simd_float3 arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<3f>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((bool (*)(id, simd_float3))function)(arg0, arg1);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("B", &rv);
}

static PyObject* _Nullable call_simd_float3x3_id(PyObject*        method,
                                                 PyObject* const* arguments, size_t nargs)
{
    simd_float3x3 rv;
    id            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float3x3 (*)(id))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{simd_float3x3=[3<3f>]}", &rv);
}

static PyObject* _Nullable call_simd_float4x4_id(PyObject*        method,
                                                 PyObject* const* arguments, size_t nargs)
{
    simd_float4x4 rv;
    id            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float4x4 (*)(id))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{simd_float4x4=[4<4f>]}", &rv);
}

static PyObject* _Nullable call_simd_float4x4_id_q(PyObject*        method,
                                                   PyObject* const* arguments,
                                                   size_t           nargs)
{
    simd_float4x4 rv;
    id            arg0;
    long long     arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[1], &arg1) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float4x4 (*)(id, long long))function)(arg0, arg1);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{simd_float4x4=[4<4f>]}", &rv);
}

static PyObject* _Nullable call_CGPoint_v2f_CGRect_Q_Q(PyObject*        method,
                                                       PyObject* const* arguments,
                                                       size_t           nargs)
{
    CGPoint            rv;
    simd_float2        arg0;
    CGRect             arg1;
    unsigned long long arg2;
    unsigned long long arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{CGRect={CGPoint=dd}{CGSize=dd}}", arguments[1], &arg1)
        == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[3], &arg3) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((CGPoint (*)(simd_float2, CGRect, unsigned long long,
                               unsigned long long))function)(arg0, arg1, arg2, arg3);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{CGPoint=dd}", &rv);
}

static PyObject* _Nullable call_v3f_SCNVector3(PyObject*        method,
                                               PyObject* const* arguments, size_t nargs)
{
    simd_float3 rv;
    SCNVector3  arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{SCNVector3=ddd}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float3 (*)(SCNVector3))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("<3f>", &rv);
}

static PyObject* _Nullable call_SCNVector3_v3f(PyObject*        method,
                                               PyObject* const* arguments, size_t nargs)
{
    SCNVector3  rv;
    simd_float3 arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((SCNVector3 (*)(simd_float3))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{SCNVector3=ddd}", &rv);
}

static PyObject* _Nullable call_v4f_SCNVector4(PyObject*        method,
                                               PyObject* const* arguments, size_t nargs)
{
    simd_float4 rv;
    SCNVector4  arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{SCNVector4=dddd}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float4 (*)(SCNVector4))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("<4f>", &rv);
}

static PyObject* _Nullable call_SCNVector4_v4f(PyObject*        method,
                                               PyObject* const* arguments, size_t nargs)
{
    SCNVector4  rv;
    simd_float4 arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((SCNVector4 (*)(simd_float4))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{SCNVector4=dddd}", &rv);
}

static PyObject* _Nullable call_simd_float4x4_CATransform3D(PyObject*        method,
                                                            PyObject* const* arguments,
                                                            size_t           nargs)
{
    simd_float4x4 rv;
    CATransform3D arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{CATransform3D=dddddddddddddddd}", arguments[0], &arg0)
        == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float4x4 (*)(CATransform3D))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{simd_float4x4=[4<4f>]}", &rv);
}

static PyObject* _Nullable call_CATransform3D_simd_float4x4(PyObject*        method,
                                                            PyObject* const* arguments,
                                                            size_t           nargs)
{
    CATransform3D rv;
    simd_float4x4 arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((CATransform3D (*)(simd_float4x4))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{CATransform3D=dddddddddddddddd}", &rv);
}

static PyObject* _Nullable call_simd_float4x4_cp_frame_C_v4f_v2f(
    PyObject* method, PyObject* const* arguments, size_t nargs)
{
    simd_float4x4 rv;
    cp_frame*     arg0;
    unsigned char arg1;
    simd_float4   arg2;
    simd_float2   arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("^{cp_frame=}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("C", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<4f>", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[3], &arg3) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float4x4 (*)(cp_frame*, unsigned char, simd_float4,
                                     simd_float2))function)(arg0, arg1, arg2, arg3);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{simd_float4x4=[4<4f>]}", &rv);
}

static PyObject* _Nullable call_simd_float4x4_cp_drawable_C_Q(PyObject*        method,
                                                              PyObject* const* arguments,
                                                              size_t           nargs)
{
    simd_float4x4      rv;
    cp_drawable*       arg0;
    unsigned char      arg1;
    unsigned long long arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("^{cp_drawable=}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("C", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[2], &arg2) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float4x4 (*)(cp_drawable*, unsigned char,
                                     unsigned long long))function)(arg0, arg1, arg2);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{simd_float4x4=[4<4f>]}", &rv);
}

static PyObject* _Nullable call_v4f_cp_view(PyObject* method, PyObject* const* arguments,
                                            size_t nargs)
{
    simd_float4 rv;
    cp_view*    arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("^{cp_view=}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float4 (*)(cp_view*))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("<4f>", &rv);
}

static PyObject* _Nullable call_simd_float4x4_cp_frame_I_C_v4f_v2f(
    PyObject* method, PyObject* const* arguments, size_t nargs)
{
    simd_float4x4 rv;
    cp_frame*     arg0;
    unsigned int  arg1;
    unsigned char arg2;
    simd_float4   arg3;
    simd_float2   arg4;

    if (PyObjC_CheckArgCount(method, 5, 5, nargs) == -1)
        return NULL;

    if (depythonify_c_value("^{cp_frame=}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("I", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("C", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<4f>", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[4], &arg4) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float4x4 (*)(cp_frame*, unsigned int, unsigned char, simd_float4,
                                     simd_float2))function)(arg0, arg1, arg2, arg3, arg4);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("{simd_float4x4=[4<4f>]}", &rv);
}

static PyObject* _Nullable call_v_cp_drawable_v2f(PyObject*        method,
                                                  PyObject* const* arguments,
                                                  size_t           nargs)
{
    cp_drawable* arg0;
    simd_float2  arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("^{cp_drawable=}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            ((void (*)(cp_drawable*, simd_float2))function)(arg0, arg1);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_RETURN_NONE;
}

static PyObject* _Nullable call_v2f_cp_drawable(PyObject*        method,
                                                PyObject* const* arguments, size_t nargs)
{
    simd_float2  rv;
    cp_drawable* arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("^{cp_drawable=}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    void*                  function = PyObjCFunc_GetCallable(method);
    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);
    if (methinfo == NULL) // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE

    Py_BEGIN_ALLOW_THREADS
        @try {
            rv = ((simd_float2 (*)(cp_drawable*))function)(arg0);
        } @catch (NSObject* localException) {   // LCOV_BR_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE
        }
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        Py_CLEAR(methinfo);
        return NULL;
    }

    Py_CLEAR(methinfo);
    return pythonify_c_value("<2f>", &rv);
}
int
PyObjC_setup_simd_functions(PyObject* module __attribute__((__unused__)))
{
    // LCOV_BR_EXCL_START

    if (PyObjC_RegisterFunctionSignatureMapping("<3f>@", call_v3f_id)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("@{simd_float4x4=[4<4f>]}",
                                                call_id_simd_float4x4)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("@{simd_float4x4=[4<4f>]}ffq",
                                                call_id_simd_float4x4_f_f_q)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("B@<3f>", call_B_id_v3f)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("{simd_float3x3=[3<3f>]}@",
                                                call_simd_float3x3_id)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("{simd_float4x4=[4<4f>]}@",
                                                call_simd_float4x4_id)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("{simd_float4x4=[4<4f>]}@q",
                                                call_simd_float4x4_id_q)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping(
            "{CGPoint=dd}<2f>{CGRect={CGPoint=dd}{CGSize=dd}}QQ",
            call_CGPoint_v2f_CGRect_Q_Q)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("<3f>{SCNVector3=ddd}",
                                                call_v3f_SCNVector3)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("{SCNVector3=ddd}<3f>",
                                                call_SCNVector3_v3f)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("<4f>{SCNVector4=dddd}",
                                                call_v4f_SCNVector4)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("{SCNVector4=dddd}<4f>",
                                                call_SCNVector4_v4f)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping(
            "{simd_float4x4=[4<4f>]}{CATransform3D=dddddddddddddddd}",
            call_simd_float4x4_CATransform3D)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping(
            "{CATransform3D=dddddddddddddddd}{simd_float4x4=[4<4f>]}",
            call_CATransform3D_simd_float4x4)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping(
            "{simd_float4x4=[4<4f>]}^{cp_frame=}C<4f><2f>",
            call_simd_float4x4_cp_frame_C_v4f_v2f)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping(
            "{simd_float4x4=[4<4f>]}^{cp_drawable=}CQ",
            call_simd_float4x4_cp_drawable_C_Q)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("<4f>^{cp_view=}", call_v4f_cp_view)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping(
            "{simd_float4x4=[4<4f>]}^{cp_frame=}IC<4f><2f>",
            call_simd_float4x4_cp_frame_I_C_v4f_v2f)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("v^{cp_drawable=}<2f>",
                                                call_v_cp_drawable_v2f)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterFunctionSignatureMapping("<2f>^{cp_drawable=}",
                                                call_v2f_cp_drawable)
        == -1) {   // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
    }

    return 0;
    // LCOV_BR_EXCL_STOP
}
NS_ASSUME_NONNULL_END
