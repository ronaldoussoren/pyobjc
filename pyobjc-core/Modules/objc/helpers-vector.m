/*
 * This file is generated using Tools/generate-helpers-vector.py
 *
 *     ** DO NOT EDIT **
 */
#import "pyobjc.h"
#include <simd/simd.h>

#import <GameplayKit/GameplayKit.h>
#import <MetalPerformanceShaders/MetalPerformanceShaders.h>
#import <ModelIO/ModelIO.h>

static PyObject*
call_v16C(PyObject* method, PyObject* self,
          PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    simd_uchar16      rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_uchar16(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_uchar16(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<16C>", &rv);
}

static PyObject*
call_v2d(PyObject* method, PyObject* self,
         PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    simd_double2      rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_double2(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_double2(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<2d>", &rv);
}

static PyObject*
call_v2d_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double2      rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_double2(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv =
                    ((simd_double2(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                        &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<2d>", &rv);
}

static PyObject*
call_v2f(PyObject* method, PyObject* self,
         PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    simd_float2       rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float2(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float2(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<2f>", &rv);
}

static PyObject*
call_v2f_Q(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super  super;
    simd_float2        rv;
    unsigned long long arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("Q", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float2(*)(id, SEL, unsigned long long))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float2(*)(struct objc_super*, SEL,
                                      unsigned long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<2f>", &rv);
}

static PyObject*
call_v2f_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float2       rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float2(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float2(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<2f>", &rv);
}

static PyObject*
call_v2f_q(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float2       rv;
    long long         arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("q", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float2(*)(id, SEL, long long))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((
                    simd_float2(*)(struct objc_super*, SEL, long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<2f>", &rv);
}

static PyObject*
call_v2i(PyObject* method, PyObject* self,
         PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    simd_int2         rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_int2(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_int2(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<2i>", &rv);
}

static PyObject*
call_v3d_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double3      rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_double3(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv =
                    ((simd_double3(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                        &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<3d>", &rv);
}

static PyObject*
call_v3f(PyObject* method, PyObject* self,
         PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    simd_float3       rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float3(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<3f>", &rv);
}

static PyObject*
call_v3f_v2i_v2i(PyObject* method, PyObject* self, PyObject* const* arguments,
                 size_t nargs)
{
    struct objc_super super;
    simd_float3       rv;
    simd_int2         arg0;
    simd_int2         arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2i>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, simd_int2, simd_int2))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float3(*)(struct objc_super*, SEL, simd_int2,
                                      simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<3f>", &rv);
}

static PyObject*
call_v3f_v3f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3       rv;
    simd_float3       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float3(*)(struct objc_super*, SEL,
                                      simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<3f>", &rv);
}

static PyObject*
call_v3f_v3f_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                size_t nargs)
{
    struct objc_super super;
    simd_float3       rv;
    simd_float3       arg0;
    id                arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, simd_float3, id))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float3(*)(struct objc_super*, SEL, simd_float3,
                                      id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<3f>", &rv);
}

static PyObject*
call_v3f_v4i(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3       rv;
    simd_int4         arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4i>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, simd_int4))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((
                    simd_float3(*)(struct objc_super*, SEL, simd_int4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<3f>", &rv);
}

static PyObject*
call_v3f_Q(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super  super;
    simd_float3        rv;
    unsigned long long arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("Q", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, unsigned long long))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float3(*)(struct objc_super*, SEL,
                                      unsigned long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<3f>", &rv);
}

static PyObject*
call_v3f_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3       rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float3(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<3f>", &rv);
}

static PyObject*
call_v4d_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double4      rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_double4(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv =
                    ((simd_double4(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                        &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<4d>", &rv);
}

static PyObject*
call_v4f(PyObject* method, PyObject* self,
         PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    simd_float4       rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float4(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float4(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<4f>", &rv);
}

static PyObject*
call_v4f_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float4       rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float4(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float4(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<4f>", &rv);
}

static PyObject*
call_v4i_v3f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_int4         rv;
    simd_float3       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_int4(*)(id, SEL, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((
                    simd_int4(*)(struct objc_super*, SEL, simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("<4i>", &rv);
}

static PyObject*
call_id_v2f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float2       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float2))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v2f_v2I_q_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                     size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float2       arg0;
    simd_uint2        arg1;
    long long         arg2;
    id                arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2I>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[3], &arg3) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float2, simd_uint2, long long, id))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float2, simd_uint2, long long,
                             id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v2f_v2f(PyObject* method, PyObject* self, PyObject* const* arguments,
                size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float2       arg0;
    simd_float2       arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float2, simd_float2))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float2,
                             simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v2i(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_int2         arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2i>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_int2))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v2i_i_i_Z(PyObject* method, PyObject* self, PyObject* const* arguments,
                  size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_int2         arg0;
    int               arg1;
    int               arg2;
    BOOL              arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2i>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("i", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("i", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[3], &arg3) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_int2, int, int, BOOL))(PyObjCIMP_GetIMP(
                    method)))(PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),
                              arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_int2, int, int,
                             BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v2i_i_i_Z_Class(PyObject* method, PyObject* self, PyObject* const* arguments,
                        size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_int2         arg0;
    int               arg1;
    int               arg2;
    BOOL              arg3;
    Class             arg4;

    if (PyObjC_CheckArgCount(method, 5, 5, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2i>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("i", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("i", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("#", arguments[4], &arg4) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_int2, int, int, BOOL, Class))(PyObjCIMP_GetIMP(
                    method)))(PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),
                              arg0, arg1, arg2, arg3, arg4);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_int2, int, int, BOOL,
                             Class))objc_msgSendSuper)(&super,
                                                       PyObjCSelector_GetSelector(method),
                                                       arg0, arg1, arg2, arg3, arg4);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v3f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float3       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v3f_v2I_Z_Z_Z_q_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                           size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float3       arg0;
    simd_uint2        arg1;
    BOOL              arg2;
    BOOL              arg3;
    BOOL              arg4;
    long long         arg5;
    id                arg6;

    if (PyObjC_CheckArgCount(method, 7, 7, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2I>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[5], &arg5) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[6], &arg6) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint2, BOOL, BOOL, BOOL,
                             long long, id))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1, arg2, arg3, arg4, arg5, arg6);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint2, BOOL, BOOL,
                             BOOL, long long, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v3f_v2I_Z_Z_q_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                         size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float3       arg0;
    simd_uint2        arg1;
    BOOL              arg2;
    BOOL              arg3;
    long long         arg4;
    id                arg5;

    if (PyObjC_CheckArgCount(method, 6, 6, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2I>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[5], &arg5) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint2, BOOL, BOOL, long long,
                             id))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1, arg2, arg3, arg4, arg5);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint2, BOOL, BOOL,
                             long long, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v3f_v2I_Z_q_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                       size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float3       arg0;
    simd_uint2        arg1;
    BOOL              arg2;
    long long         arg3;
    id                arg4;

    if (PyObjC_CheckArgCount(method, 5, 5, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2I>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[4], &arg4) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint2, BOOL, long long, id))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3, arg4);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint2, BOOL,
                             long long, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v3f_v2I_i_Z_q_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                         size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float3       arg0;
    simd_uint2        arg1;
    int               arg2;
    BOOL              arg3;
    long long         arg4;
    id                arg5;

    if (PyObjC_CheckArgCount(method, 6, 6, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2I>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("i", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[5], &arg5) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint2, int, BOOL, long long, id))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3, arg4, arg5);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint2, int, BOOL,
                             long long, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v3f_v2I_q_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                     size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float3       arg0;
    simd_uint2        arg1;
    long long         arg2;
    id                arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2I>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[3], &arg3) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint2, long long, id))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint2, long long,
                             id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v3f_v3I_Z_q_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                       size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float3       arg0;
    simd_uint3        arg1;
    BOOL              arg2;
    long long         arg3;
    id                arg4;

    if (PyObjC_CheckArgCount(method, 5, 5, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<3I>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[4], &arg4) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint3, BOOL, long long, id))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3, arg4);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint3, BOOL,
                             long long, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v3f_v3I_q_Z_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                       size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float3       arg0;
    simd_uint3        arg1;
    long long         arg2;
    BOOL              arg3;
    id                arg4;

    if (PyObjC_CheckArgCount(method, 5, 5, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<3I>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[4], &arg4) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint3, long long, BOOL, id))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3, arg4);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint3, long long,
                             BOOL, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v3f_Q_Q_q_Z_Z_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                         size_t nargs)
{
    struct objc_super  super;
    id                 rv;
    simd_float3        arg0;
    unsigned long long arg1;
    unsigned long long arg2;
    long long          arg3;
    BOOL               arg4;
    BOOL               arg5;
    id                 arg6;

    if (PyObjC_CheckArgCount(method, 7, 7, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[5], &arg5) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[6], &arg6) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, unsigned long long, unsigned long long,
                             long long, BOOL, BOOL, id))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1, arg2, arg3, arg4, arg5, arg6);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, unsigned long long,
                             unsigned long long, long long, BOOL, BOOL,
                             id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v3f_Z_q_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                   size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float3       arg0;
    BOOL              arg1;
    long long         arg2;
    id                arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[3], &arg3) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, BOOL, long long, id))(PyObjCIMP_GetIMP(
                    method)))(PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),
                              arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, BOOL, long long,
                             id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_v4f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float4       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float4))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, simd_float4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_v2d_v2d_v2i_Z(PyObject* method, PyObject* self, PyObject* const* arguments,
                         size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    simd_double2      arg1;
    simd_double2      arg2;
    simd_int2         arg3;
    BOOL              arg4;

    if (PyObjC_CheckArgCount(method, 5, 5, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2d>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2d>", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[4], &arg4) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_double2, simd_double2, simd_int2, BOOL))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3, arg4);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, simd_double2, simd_double2,
                             simd_int2, BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_v2f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    simd_float2       arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_float2))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_v3f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    simd_float3       arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<3f>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_v4f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    simd_float4       arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<4f>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_float4))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, simd_float4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_id_v2i(PyObject* method, PyObject* self, PyObject* const* arguments,
                  size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    id                arg1;
    simd_int2         arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[2], &arg2) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, id, simd_int2))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1, arg2);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((
                    id(*)(struct objc_super*, SEL, id, id, simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_id_v2i_f(PyObject* method, PyObject* self, PyObject* const* arguments,
                    size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    id                arg1;
    simd_int2         arg2;
    float             arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[3], &arg3) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, id, simd_int2, float))(PyObjCIMP_GetIMP(
                    method)))(PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),
                              arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, id, simd_int2,
                             float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_Q_v2f(PyObject* method, PyObject* self, PyObject* const* arguments,
                 size_t nargs)
{
    struct objc_super  super;
    id                 rv;
    id                 arg0;
    unsigned long long arg1;
    simd_float2        arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[2], &arg2) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, unsigned long long, simd_float2))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, unsigned long long,
                             simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_Q_v3f(PyObject* method, PyObject* self, PyObject* const* arguments,
                 size_t nargs)
{
    struct objc_super  super;
    id                 rv;
    id                 arg0;
    unsigned long long arg1;
    simd_float3        arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<3f>", arguments[2], &arg2) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, unsigned long long, simd_float3))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, unsigned long long,
                             simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_Q_v4f(PyObject* method, PyObject* self, PyObject* const* arguments,
                 size_t nargs)
{
    struct objc_super  super;
    id                 rv;
    id                 arg0;
    unsigned long long arg1;
    simd_float4        arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<4f>", arguments[2], &arg2) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, unsigned long long, simd_float4))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, unsigned long long,
                             simd_float4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_Q_matrix_float4x4(PyObject* method, PyObject* self, PyObject* const* arguments,
                             size_t nargs)
{
    struct objc_super  super;
    id                 rv;
    id                 arg0;
    unsigned long long arg1;
    matrix_float4x4    arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{_matrix_float4x4=[4<4f>]}", arguments[2], &arg2) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, unsigned long long, matrix_float4x4))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, unsigned long long,
                             matrix_float4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_Z_id_v2i_q_Q_q_Z(PyObject* method, PyObject* self, PyObject* const* arguments,
                            size_t nargs)
{
    struct objc_super  super;
    id                 rv;
    id                 arg0;
    BOOL               arg1;
    id                 arg2;
    simd_int2          arg3;
    long long          arg4;
    unsigned long long arg5;
    long long          arg6;
    BOOL               arg7;

    if (PyObjC_CheckArgCount(method, 8, 8, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[5], &arg5) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[6], &arg6) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[7], &arg7) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, BOOL, id, simd_int2, long long,
                             unsigned long long, long long, BOOL))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3, arg4, arg5, arg6, arg7);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, BOOL, id, simd_int2, long long,
                             unsigned long long, long long, BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6, arg7);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_q_v2i_f_f_f_f(PyObject* method, PyObject* self, PyObject* const* arguments,
                         size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    long long         arg1;
    simd_int2         arg2;
    float             arg3;
    float             arg4;
    float             arg5;
    float             arg6;

    if (PyObjC_CheckArgCount(method, 7, 7, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[5], &arg5) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[6], &arg6) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, long long, simd_int2, float, float, float,
                             float))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1, arg2, arg3, arg4, arg5, arg6);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, long long, simd_int2, float,
                             float, float, float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_q_v2i_f_f_f_f_f(PyObject* method, PyObject* self, PyObject* const* arguments,
                           size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    long long         arg1;
    simd_int2         arg2;
    float             arg3;
    float             arg4;
    float             arg5;
    float             arg6;
    float             arg7;

    if (PyObjC_CheckArgCount(method, 8, 8, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[5], &arg5) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[6], &arg6) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[7], &arg7) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, long long, simd_int2, float, float, float,
                             float, float))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1, arg2, arg3, arg4, arg5, arg6, arg7);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, long long, simd_int2, float,
                             float, float, float, float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6, arg7);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_GKBox(PyObject* method, PyObject* self, PyObject* const* arguments,
                 size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    GKBox             arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{GKBox=<3f><3f>}", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, GKBox))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, GKBox))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_GKQuad(PyObject* method, PyObject* self, PyObject* const* arguments,
                  size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    GKQuad            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{GKQuad=<2f><2f>}", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, GKQuad))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, GKQuad))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_MDLAxisAlignedBoundingBox_f(PyObject* method, PyObject* self,
                                       PyObject* const* arguments, size_t nargs)
{
    struct objc_super         super;
    id                        rv;
    id                        arg0;
    MDLAxisAlignedBoundingBox arg1;
    float                     arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{_MDLAxisAlignedBoundingBox=<3f><3f>}", arguments[1], &arg1)
        == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[2], &arg2) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, MDLAxisAlignedBoundingBox, float))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id, MDLAxisAlignedBoundingBox,
                             float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_matrix_float2x2(PyObject* method, PyObject* self, PyObject* const* arguments,
                           size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    matrix_float2x2   arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{_matrix_float2x2=[2<2f>]}", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, matrix_float2x2))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id,
                             matrix_float2x2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_matrix_float3x3(PyObject* method, PyObject* self, PyObject* const* arguments,
                           size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    matrix_float3x3   arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{_matrix_float3x3=[3<3f>]}", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, matrix_float3x3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id,
                             matrix_float3x3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_id_matrix_float4x4(PyObject* method, PyObject* self, PyObject* const* arguments,
                           size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    matrix_float4x4   arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{_matrix_float4x4=[4<4f>]}", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, matrix_float4x4))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, id,
                             matrix_float4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_CGColor_CGColor_id_v2i(PyObject* method, PyObject* self,
                               PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    CGColorRef        arg0;
    CGColorRef        arg1;
    id                arg2;
    simd_int2         arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("^{CGColor=}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("^{CGColor=}", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[3], &arg3) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, CGColorRef, CGColorRef, id, simd_int2))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, CGColorRef, CGColorRef, id,
                             simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_f_v2f_v2f(PyObject* method, PyObject* self, PyObject* const* arguments,
                  size_t nargs)
{
    struct objc_super super;
    id                rv;
    float             arg0;
    simd_float2       arg1;
    simd_float2       arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("f", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[2], &arg2) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, simd_float2, simd_float2))(PyObjCIMP_GetIMP(
                    method)))(PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),
                              arg0, arg1, arg2);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, float, simd_float2,
                             simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_f_v2f_v2f_Class(PyObject* method, PyObject* self, PyObject* const* arguments,
                        size_t nargs)
{
    struct objc_super super;
    id                rv;
    float             arg0;
    simd_float2       arg1;
    simd_float2       arg2;
    Class             arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("f", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("#", arguments[3], &arg3) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, simd_float2, simd_float2, Class))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, float, simd_float2, simd_float2,
                             Class))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_f_v2f_Q_Q_Q_q_Z_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                           size_t nargs)
{
    struct objc_super  super;
    id                 rv;
    float              arg0;
    simd_float2        arg1;
    unsigned long long arg2;
    unsigned long long arg3;
    unsigned long long arg4;
    long long          arg5;
    BOOL               arg6;
    id                 arg7;

    if (PyObjC_CheckArgCount(method, 8, 8, nargs) == -1)
        return NULL;

    if (depythonify_c_value("f", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[5], &arg5) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[6], &arg6) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[7], &arg7) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, simd_float2, unsigned long long,
                             unsigned long long, unsigned long long, long long, BOOL,
                             id))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1, arg2, arg3, arg4, arg5, arg6, arg7);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, float, simd_float2,
                             unsigned long long, unsigned long long, unsigned long long,
                             long long, BOOL, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6, arg7);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_f_v2f_Q_Q_q_Z_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                         size_t nargs)
{
    struct objc_super  super;
    id                 rv;
    float              arg0;
    simd_float2        arg1;
    unsigned long long arg2;
    unsigned long long arg3;
    long long          arg4;
    BOOL               arg5;
    id                 arg6;

    if (PyObjC_CheckArgCount(method, 7, 7, nargs) == -1)
        return NULL;

    if (depythonify_c_value("f", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[5], &arg5) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[6], &arg6) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, simd_float2, unsigned long long,
                             unsigned long long, long long, BOOL, id))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3, arg4, arg5, arg6);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, float, simd_float2,
                             unsigned long long, unsigned long long, long long, BOOL,
                             id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_f_id_v2i_i_q_Z(PyObject* method, PyObject* self, PyObject* const* arguments,
                       size_t nargs)
{
    struct objc_super super;
    id                rv;
    float             arg0;
    id                arg1;
    simd_int2         arg2;
    int               arg3;
    long long         arg4;
    BOOL              arg5;

    if (PyObjC_CheckArgCount(method, 6, 6, nargs) == -1)
        return NULL;

    if (depythonify_c_value("f", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("i", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[5], &arg5) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, id, simd_int2, int, long long, BOOL))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3, arg4, arg5);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, float, id, simd_int2, int,
                             long long, BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_f_id_v2i_i_q_CGColor_CGColor(PyObject* method, PyObject* self,
                                     PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    float             arg0;
    id                arg1;
    simd_int2         arg2;
    int               arg3;
    long long         arg4;
    CGColorRef        arg5;
    CGColorRef        arg6;

    if (PyObjC_CheckArgCount(method, 7, 7, nargs) == -1)
        return NULL;

    if (depythonify_c_value("f", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("i", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("^{CGColor=}", arguments[5], &arg5) == -1) {
        return NULL;
    }
    if (depythonify_c_value("^{CGColor=}", arguments[6], &arg6) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, id, simd_int2, int, long long, CGColorRef,
                             CGColorRef))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1, arg2, arg3, arg4, arg5, arg6);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, float, id, simd_int2, int,
                             long long, CGColorRef, CGColorRef))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_f_id_v2i_q(PyObject* method, PyObject* self, PyObject* const* arguments,
                   size_t nargs)
{
    struct objc_super super;
    id                rv;
    float             arg0;
    id                arg1;
    simd_int2         arg2;
    long long         arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("f", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[3], &arg3) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, id, simd_int2, long long))(PyObjCIMP_GetIMP(
                    method)))(PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),
                              arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, float, id, simd_int2,
                             long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_f_f_id_v2i(PyObject* method, PyObject* self, PyObject* const* arguments,
                   size_t nargs)
{
    struct objc_super super;
    id                rv;
    float             arg0;
    float             arg1;
    id                arg2;
    simd_int2         arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("f", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[3], &arg3) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, float, id, simd_int2))(PyObjCIMP_GetIMP(
                    method)))(PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),
                              arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, float, float, id,
                             simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_GKBox(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    GKBox             arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{GKBox=<3f><3f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, GKBox))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, GKBox))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_GKBox_f(PyObject* method, PyObject* self, PyObject* const* arguments,
                size_t nargs)
{
    struct objc_super super;
    id                rv;
    GKBox             arg0;
    float             arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{GKBox=<3f><3f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, GKBox, float))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, GKBox, float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_GKQuad(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    GKQuad            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{GKQuad=<2f><2f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, GKQuad))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, GKQuad))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_GKQuad_f(PyObject* method, PyObject* self, PyObject* const* arguments,
                 size_t nargs)
{
    struct objc_super super;
    id                rv;
    GKQuad            arg0;
    float             arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{GKQuad=<2f><2f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, GKQuad, float))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, GKQuad, float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_MDLVoxelIndexExtent(PyObject* method, PyObject* self, PyObject* const* arguments,
                            size_t nargs)
{
    struct objc_super   super;
    id                  rv;
    MDLVoxelIndexExtent arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_MDLVoxelIndexExtent=<4i><4i>}", arguments[0], &arg0)
        == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, MDLVoxelIndexExtent))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL,
                             MDLVoxelIndexExtent))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_matrix_float4x4(PyObject* method, PyObject* self, PyObject* const* arguments,
                        size_t nargs)
{
    struct objc_super super;
    id                rv;
    matrix_float4x4   arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_matrix_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, matrix_float4x4))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, matrix_float4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_id_matrix_float4x4_Z(PyObject* method, PyObject* self, PyObject* const* arguments,
                          size_t nargs)
{
    struct objc_super super;
    id                rv;
    matrix_float4x4   arg0;
    BOOL              arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_matrix_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, matrix_float4x4, BOOL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((id(*)(struct objc_super*, SEL, matrix_float4x4,
                             BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("@", &rv);
}

static PyObject*
call_Z_v2i_id_id_id_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                       size_t nargs)
{
    struct objc_super super;
    BOOL              rv;
    simd_int2         arg0;
    id                arg1;
    id                arg2;
    id                arg3;
    id                arg4;

    if (PyObjC_CheckArgCount(method, 5, 5, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2i>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[4], &arg4) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((BOOL(*)(id, SEL, simd_int2, id, id, id, id))(PyObjCIMP_GetIMP(
                    method)))(PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),
                              arg0, arg1, arg2, arg3, arg4);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((BOOL(*)(struct objc_super*, SEL, simd_int2, id, id, id,
                               id))objc_msgSendSuper)(&super,
                                                      PyObjCSelector_GetSelector(method),
                                                      arg0, arg1, arg2, arg3, arg4);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("Z", &rv);
}

static PyObject*
call_Z_v2i_q_f_id_id_id(PyObject* method, PyObject* self, PyObject* const* arguments,
                        size_t nargs)
{
    struct objc_super super;
    BOOL              rv;
    simd_int2         arg0;
    long long         arg1;
    float             arg2;
    id                arg3;
    id                arg4;
    id                arg5;

    if (PyObjC_CheckArgCount(method, 6, 6, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2i>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[4], &arg4) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[5], &arg5) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((BOOL(*)(id, SEL, simd_int2, long long, float, id, id, id))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3, arg4, arg5);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((BOOL(*)(struct objc_super*, SEL, simd_int2, long long, float, id,
                               id, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("Z", &rv);
}

static PyObject*
call_Z_v4i_Z_Z_Z_Z(PyObject* method, PyObject* self, PyObject* const* arguments,
                   size_t nargs)
{
    struct objc_super super;
    BOOL              rv;
    simd_int4         arg0;
    BOOL              arg1;
    BOOL              arg2;
    BOOL              arg3;
    BOOL              arg4;

    if (PyObjC_CheckArgCount(method, 5, 5, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4i>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[3], &arg3) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[4], &arg4) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((BOOL(*)(id, SEL, simd_int4, BOOL, BOOL, BOOL, BOOL))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3, arg4);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((BOOL(*)(struct objc_super*, SEL, simd_int4, BOOL, BOOL, BOOL,
                               BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("Z", &rv);
}

static PyObject*
call_CGColor_v3f(PyObject* method, PyObject* self, PyObject* const* arguments,
                 size_t nargs)
{
    struct objc_super super;
    CGColorRef        rv;
    simd_float3       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((CGColorRef(*)(id, SEL, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((CGColorRef(*)(struct objc_super*, SEL,
                                     simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("^{CGColor=}", &rv);
}

static PyObject*
call_CGColor_v3f_CGColorSpace(PyObject* method, PyObject* self,
                              PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    CGColorRef        rv;
    simd_float3       arg0;
    CGColorSpaceRef   arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("^{CGColorSpace=}", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((CGColorRef(*)(id, SEL, simd_float3, CGColorSpaceRef))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((CGColorRef(*)(struct objc_super*, SEL, simd_float3,
                                     CGColorSpaceRef))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("^{CGColor=}", &rv);
}

static PyObject*
call_f_v2f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    float             rv;
    simd_float2       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((float (*)(id, SEL, simd_float2))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((float (*)(struct objc_super*, SEL, simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("f", &rv);
}

static PyObject*
call_f_v2i(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    float             rv;
    simd_int2         arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2i>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((float (*)(id, SEL, simd_int2))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((float (*)(struct objc_super*, SEL, simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("f", &rv);
}

static PyObject*
call_v_v2d_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double2      arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2d>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double2, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_double2,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v2f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float2       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float2))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v2f_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float2       arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float2, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_float2,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v3d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double3      arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3d>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_double3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v3d_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double3      arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3d>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double3, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_double3,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v3f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v3f_v3f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3       arg0;
    simd_float3       arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<3f>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float3, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_float3,
                           simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v3f_v3f_v3f(PyObject* method, PyObject* self, PyObject* const* arguments,
                   size_t nargs)
{
    struct objc_super super;
    simd_float3       arg0;
    simd_float3       arg1;
    simd_float3       arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<3f>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<3f>", arguments[2], &arg2) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float3, simd_float3, simd_float3))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_float3, simd_float3,
                           simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v3f_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3       arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float3, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_float3,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v4d_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double4      arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4d>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double4, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_double4,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v4f(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float4       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float4))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_float4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v4f_d(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float4       arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4f>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float4, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_float4,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_v4i(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_int4         arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4i>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_int4))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_int4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_id_v2f_v2f(PyObject* method, PyObject* self, PyObject* const* arguments,
                  size_t nargs)
{
    struct objc_super super;
    id                arg0;
    simd_float2       arg1;
    simd_float2       arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[2], &arg2) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, id, simd_float2, simd_float2))(PyObjCIMP_GetIMP(
                    method)))(PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method),
                              arg0, arg1, arg2);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, id, simd_float2,
                           simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_id_v2f_v2f_q(PyObject* method, PyObject* self, PyObject* const* arguments,
                    size_t nargs)
{
    struct objc_super super;
    id                arg0;
    simd_float2       arg1;
    simd_float2       arg2;
    long long         arg3;

    if (PyObjC_CheckArgCount(method, 4, 4, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2f>", arguments[2], &arg2) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[3], &arg3) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, id, simd_float2, simd_float2, long long))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1,
                                               arg2, arg3);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, id, simd_float2, simd_float2,
                           long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_f_v2i(PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    float             arg0;
    simd_int2         arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("f", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<2i>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, float, simd_int2))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, float, simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_MDLAxisAlignedBoundingBox(PyObject* method, PyObject* self,
                                 PyObject* const* arguments, size_t nargs)
{
    struct objc_super         super;
    MDLAxisAlignedBoundingBox arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_MDLAxisAlignedBoundingBox=<3f><3f>}", arguments[0], &arg0)
        == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, MDLAxisAlignedBoundingBox))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, MDLAxisAlignedBoundingBox))
                     objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_MDLAxisAlignedBoundingBox_Z(PyObject* method, PyObject* self,
                                   PyObject* const* arguments, size_t nargs)
{
    struct objc_super         super;
    MDLAxisAlignedBoundingBox arg0;
    BOOL                      arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_MDLAxisAlignedBoundingBox=<3f><3f>}", arguments[0], &arg0)
        == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, MDLAxisAlignedBoundingBox, BOOL))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, MDLAxisAlignedBoundingBox,
                           BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_matrix_double4x4(PyObject* method, PyObject* self, PyObject* const* arguments,
                        size_t nargs)
{
    struct objc_super super;
    matrix_double4x4  arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_matrix_double4x4=[4<4d>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, matrix_double4x4))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, matrix_double4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_matrix_double4x4_d(PyObject* method, PyObject* self, PyObject* const* arguments,
                          size_t nargs)
{
    struct objc_super super;
    matrix_double4x4  arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_matrix_double4x4=[4<4d>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, matrix_double4x4, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, matrix_double4x4,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_matrix_float2x2(PyObject* method, PyObject* self, PyObject* const* arguments,
                       size_t nargs)
{
    struct objc_super super;
    matrix_float2x2   arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_matrix_float2x2=[2<2f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, matrix_float2x2))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, matrix_float2x2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_matrix_float3x3(PyObject* method, PyObject* self, PyObject* const* arguments,
                       size_t nargs)
{
    struct objc_super super;
    matrix_float3x3   arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_matrix_float3x3=[3<3f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, matrix_float3x3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, matrix_float3x3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_matrix_float4x4(PyObject* method, PyObject* self, PyObject* const* arguments,
                       size_t nargs)
{
    struct objc_super super;
    matrix_float4x4   arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_matrix_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, matrix_float4x4))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, matrix_float4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_matrix_float4x4_d(PyObject* method, PyObject* self, PyObject* const* arguments,
                         size_t nargs)
{
    struct objc_super super;
    matrix_float4x4   arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_matrix_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, matrix_float4x4, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, matrix_float4x4,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_simd_float4x4(PyObject* method, PyObject* self, PyObject* const* arguments,
                     size_t nargs)
{
    struct objc_super super;
    simd_float4x4     arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_simd_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float4x4))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_float4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_simd_quatd_d(PyObject* method, PyObject* self, PyObject* const* arguments,
                    size_t nargs)
{
    struct objc_super super;
    simd_quatd        arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_simd_quatd=<4d>}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_quatd, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_quatd,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_simd_quatf(PyObject* method, PyObject* self, PyObject* const* arguments,
                  size_t nargs)
{
    struct objc_super super;
    simd_quatf        arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_simd_quatf=<4f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_quatf))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_quatf))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_simd_quatf_v3f(PyObject* method, PyObject* self, PyObject* const* arguments,
                      size_t nargs)
{
    struct objc_super super;
    simd_quatf        arg0;
    simd_float3       arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_simd_quatf=<4f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<3f>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_quatf, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_quatf,
                           simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_v_simd_quatf_d(PyObject* method, PyObject* self, PyObject* const* arguments,
                    size_t nargs)
{
    struct objc_super super;
    simd_quatf        arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_simd_quatf=<4f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_quatf, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0,
                    arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                ((void (*)(struct objc_super*, SEL, simd_quatf,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    Py_RETURN_NONE;
}

static PyObject*
call_GKBox(PyObject* method, PyObject* self,
           PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    GKBox             rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((GKBox(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((GKBox(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{GKBox=<3f><3f>}", &rv);
}

static PyObject*
call_GKQuad(PyObject* method, PyObject* self,
            PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    GKQuad            rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((GKQuad(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((GKQuad(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{GKQuad=<2f><2f>}", &rv);
}

static PyObject*
call_GKTriangle_Q(PyObject* method, PyObject* self, PyObject* const* arguments,
                  size_t nargs)
{
    struct objc_super  super;
    GKTriangle         rv;
    unsigned long long arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("Q", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((GKTriangle(*)(id, SEL, unsigned long long))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((GKTriangle(*)(struct objc_super*, SEL,
                                     unsigned long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{GKTriangle=[3<3f>]}", &rv);
}

static PyObject*
call_MDLAxisAlignedBoundingBox(PyObject* method, PyObject* self,
                               PyObject* const* arguments __attribute__((__unused__)),
                               size_t           nargs)
{
    struct objc_super         super;
    MDLAxisAlignedBoundingBox rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MDLAxisAlignedBoundingBox(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((MDLAxisAlignedBoundingBox(*)(struct objc_super*, SEL))
                          objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_MDLAxisAlignedBoundingBox=<3f><3f>}", &rv);
}

static PyObject*
call_MDLAxisAlignedBoundingBox_v4i(PyObject* method, PyObject* self,
                                   PyObject* const* arguments, size_t nargs)
{
    struct objc_super         super;
    MDLAxisAlignedBoundingBox rv;
    simd_int4                 arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4i>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MDLAxisAlignedBoundingBox(*)(id, SEL, simd_int4))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((MDLAxisAlignedBoundingBox(*)(struct objc_super*, SEL,
                                                    simd_int4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_MDLAxisAlignedBoundingBox=<3f><3f>}", &rv);
}

static PyObject*
call_MDLAxisAlignedBoundingBox_d(PyObject* method, PyObject* self,
                                 PyObject* const* arguments, size_t nargs)
{
    struct objc_super         super;
    MDLAxisAlignedBoundingBox rv;
    double                    arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MDLAxisAlignedBoundingBox(*)(id, SEL, double))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((MDLAxisAlignedBoundingBox(*)(struct objc_super*, SEL,
                                                    double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_MDLAxisAlignedBoundingBox=<3f><3f>}", &rv);
}

static PyObject*
call_MDLVoxelIndexExtent(PyObject* method, PyObject* self,
                         PyObject* const* arguments __attribute__((__unused__)),
                         size_t           nargs)
{
    struct objc_super   super;
    MDLVoxelIndexExtent rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MDLVoxelIndexExtent(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((MDLVoxelIndexExtent(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_MDLVoxelIndexExtent=<4i><4i>}", &rv);
}

static PyObject*
call_MPSAxisAlignedBoundingBox(PyObject* method, PyObject* self,
                               PyObject* const* arguments __attribute__((__unused__)),
                               size_t           nargs)
{
    struct objc_super         super;
    MPSAxisAlignedBoundingBox rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MPSAxisAlignedBoundingBox(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((MPSAxisAlignedBoundingBox(*)(struct objc_super*, SEL))
                          objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_MPSAxisAlignedBoundingBox=<3f><3f>}", &rv);
}

static PyObject*
call_MPSImageHistogramInfo(PyObject* method, PyObject* self,
                           PyObject* const* arguments __attribute__((__unused__)),
                           size_t           nargs)
{
    struct objc_super     super;
    MPSImageHistogramInfo rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MPSImageHistogramInfo(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((MPSImageHistogramInfo(*)(struct objc_super*, SEL))
                          objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_MPSImageHistogramInfo=QZ<4f><4f>}", &rv);
}

static PyObject*
call_matrix_double4x4(PyObject* method, PyObject* self,
                      PyObject* const* arguments __attribute__((__unused__)),
                      size_t           nargs)
{
    struct objc_super super;
    matrix_double4x4  rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((matrix_double4x4(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((matrix_double4x4(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_matrix_double4x4=[4<4d>]}", &rv);
}

static PyObject*
call_matrix_double4x4_d(PyObject* method, PyObject* self, PyObject* const* arguments,
                        size_t nargs)
{
    struct objc_super super;
    matrix_double4x4  rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((matrix_double4x4(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((matrix_double4x4(*)(struct objc_super*, SEL,
                                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_matrix_double4x4=[4<4d>]}", &rv);
}

static PyObject*
call_matrix_float2x2(PyObject* method, PyObject* self,
                     PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    matrix_float2x2   rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((matrix_float2x2(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((matrix_float2x2(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_matrix_float2x2=[2<2f>]}", &rv);
}

static PyObject*
call_matrix_float3x3(PyObject* method, PyObject* self,
                     PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    matrix_float3x3   rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((matrix_float3x3(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((matrix_float3x3(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_matrix_float3x3=[3<3f>]}", &rv);
}

static PyObject*
call_matrix_float4x4(PyObject* method, PyObject* self,
                     PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    matrix_float4x4   rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((matrix_float4x4(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((matrix_float4x4(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_matrix_float4x4=[4<4f>]}", &rv);
}

static PyObject*
call_matrix_float4x4_id_d(PyObject* method, PyObject* self, PyObject* const* arguments,
                          size_t nargs)
{
    struct objc_super super;
    matrix_float4x4   rv;
    id                arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((matrix_float4x4(*)(id, SEL, id, double))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((matrix_float4x4(*)(struct objc_super*, SEL, id,
                                          double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_matrix_float4x4=[4<4f>]}", &rv);
}

static PyObject*
call_matrix_float4x4_d(PyObject* method, PyObject* self, PyObject* const* arguments,
                       size_t nargs)
{
    struct objc_super super;
    matrix_float4x4   rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((matrix_float4x4(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((matrix_float4x4(*)(struct objc_super*, SEL,
                                          double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_matrix_float4x4=[4<4f>]}", &rv);
}

static PyObject*
call_simd_float4x4(PyObject* method, PyObject* self,
                   PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    simd_float4x4     rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float4x4(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float4x4(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_simd_float4x4=[4<4f>]}", &rv);
}

static PyObject*
call_simd_float4x4_simd_float4x4_id(PyObject* method, PyObject* self,
                                    PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float4x4     rv;
    simd_float4x4     arg0;
    id                arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{_simd_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[1], &arg1) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float4x4(*)(id, SEL, simd_float4x4, id))(
                    PyObjCIMP_GetIMP(method)))(PyObjCObject_GetObject(self),
                                               PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_float4x4(*)(struct objc_super*, SEL, simd_float4x4,
                                        id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_simd_float4x4=[4<4f>]}", &rv);
}

static PyObject*
call_simd_quatd_d(PyObject* method, PyObject* self, PyObject* const* arguments,
                  size_t nargs)
{
    struct objc_super super;
    simd_quatd        rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_quatd(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_quatd(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_simd_quatd=<4d>}", &rv);
}

static PyObject*
call_simd_quatf(PyObject* method, PyObject* self,
                PyObject* const* arguments __attribute__((__unused__)), size_t nargs)
{
    struct objc_super super;
    simd_quatf        rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_quatf(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_quatf(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_simd_quatf=<4f>}", &rv);
}

static PyObject*
call_simd_quatf_d(PyObject* method, PyObject* self, PyObject* const* arguments,
                  size_t nargs)
{
    struct objc_super super;
    simd_quatf        rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    int isIMP = PyObjCIMP_Check(method);

    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_quatf(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = PyObjCObject_GetObject(self);
                super.super_class = PyObjCSelector_GetClass(method);

                rv = ((simd_quatf(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) {   // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE
        }                                       // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
        return NULL;        // LCOV_EXCL_LINE
    }

    return pythonify_c_value("{_simd_quatf=<4f>}", &rv);
}
int
PyObjC_setup_simd(void)
{

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<16C>@:", call_v16C, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2d>@:", call_v2d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2d>@:d", call_v2d_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2f>@:", call_v2f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2f>@:Q", call_v2f_Q, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2f>@:d", call_v2f_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2f>@:q", call_v2f_q, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2i>@:", call_v2i, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3d>@:d", call_v3d_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:", call_v3f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:<2i><2i>", call_v3f_v2i_v2i, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:<3f>", call_v3f_v3f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:<3f>@", call_v3f_v3f_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:<4i>", call_v3f_v4i, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:Q", call_v3f_Q, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:d", call_v3f_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<4d>@:d", call_v4d_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<4f>@:", call_v4f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<4f>@:d", call_v4f_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<4i>@:<3f>", call_v4i_v3f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2f>", call_id_v2f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2f><2I>q@", call_id_v2f_v2I_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2f><2f>", call_id_v2f_v2f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2i>", call_id_v2i, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2i>iiZ", call_id_v2i_i_i_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2i>iiB", call_id_v2i_i_i_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2i>iiZ#", call_id_v2i_i_i_Z_Class, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2i>iiB#", call_id_v2i_i_i_Z_Class, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f>", call_id_v3f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>ZZZq@", call_id_v3f_v2I_Z_Z_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>BBBq@", call_id_v3f_v2I_Z_Z_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>ZZq@", call_id_v3f_v2I_Z_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>BBq@", call_id_v3f_v2I_Z_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>Zq@", call_id_v3f_v2I_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>Bq@", call_id_v3f_v2I_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>iZq@", call_id_v3f_v2I_i_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>iBq@", call_id_v3f_v2I_i_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>q@", call_id_v3f_v2I_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><3I>Zq@", call_id_v3f_v3I_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><3I>Bq@", call_id_v3f_v3I_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><3I>qZ@", call_id_v3f_v3I_q_Z_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><3I>qB@", call_id_v3f_v3I_q_Z_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f>QQqZZ@", call_id_v3f_Q_Q_q_Z_Z_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f>QQqBB@", call_id_v3f_Q_Q_q_Z_Z_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f>Zq@", call_id_v3f_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f>Bq@", call_id_v3f_Z_q_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<4f>", call_id_v4f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@<2d><2d><2i>Z", call_id_id_v2d_v2d_v2i_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@<2d><2d><2i>B", call_id_id_v2d_v2d_v2i_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@<2f>", call_id_id_v2f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@<3f>", call_id_id_v3f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@<4f>", call_id_id_v4f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@@<2i>", call_id_id_id_v2i, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@@<2i>f", call_id_id_id_v2i_f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@Q<2f>", call_id_id_Q_v2f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@Q<3f>", call_id_id_Q_v3f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@Q<4f>", call_id_id_Q_v4f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@Q{_matrix_float4x4=[4<4f>]}", call_id_id_Q_matrix_float4x4,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@Z@<2i>qQqZ", call_id_id_Z_id_v2i_q_Q_q_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@B@<2i>qQqB", call_id_id_Z_id_v2i_q_Q_q_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@q<2i>ffff", call_id_id_q_v2i_f_f_f_f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@q<2i>fffff", call_id_id_q_v2i_f_f_f_f_f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{GKBox=<3f><3f>}", call_id_id_GKBox, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{GKQuad=<2f><2f>}", call_id_id_GKQuad, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{_MDLAxisAlignedBoundingBox=<3f><3f>}f",
            call_id_id_MDLAxisAlignedBoundingBox_f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{_matrix_float2x2=[2<2f>]}", call_id_id_matrix_float2x2,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{_matrix_float3x3=[3<3f>]}", call_id_id_matrix_float3x3,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{_matrix_float4x4=[4<4f>]}", call_id_id_matrix_float4x4,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:^{CGColor=}^{CGColor=}@<2i>", call_id_CGColor_CGColor_id_v2i,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f><2f>", call_id_f_v2f_v2f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f><2f>#", call_id_f_v2f_v2f_Class, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f>QQQqZ@", call_id_f_v2f_Q_Q_Q_q_Z_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f>QQQqB@", call_id_f_v2f_Q_Q_Q_q_Z_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f>QQqZ@", call_id_f_v2f_Q_Q_q_Z_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f>QQqB@", call_id_f_v2f_Q_Q_q_Z_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f@<2i>iqZ", call_id_f_id_v2i_i_q_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f@<2i>iqB", call_id_f_id_v2i_i_q_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f@<2i>iq^{CGColor=}^{CGColor=}", call_id_f_id_v2i_i_q_CGColor_CGColor,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f@<2i>q", call_id_f_id_v2i_q, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:ff@<2i>", call_id_f_f_id_v2i, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{GKBox=<3f><3f>}", call_id_GKBox, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{GKBox=<3f><3f>}f", call_id_GKBox_f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{GKQuad=<2f><2f>}", call_id_GKQuad, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{GKQuad=<2f><2f>}f", call_id_GKQuad_f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{_MDLVoxelIndexExtent=<4i><4i>}", call_id_MDLVoxelIndexExtent,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{_matrix_float4x4=[4<4f>]}", call_id_matrix_float4x4,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{_matrix_float4x4=[4<4f>]}Z", call_id_matrix_float4x4_Z,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{_matrix_float4x4=[4<4f>]}B", call_id_matrix_float4x4_Z,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "Z@:<2i>@@@@", call_Z_v2i_id_id_id_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "B@:<2i>@@@@", call_Z_v2i_id_id_id_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "Z@:<2i>qf@@@", call_Z_v2i_q_f_id_id_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "B@:<2i>qf@@@", call_Z_v2i_q_f_id_id_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "Z@:<4i>ZZZZ", call_Z_v4i_Z_Z_Z_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "B@:<4i>BBBB", call_Z_v4i_Z_Z_Z_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "^{CGColor=}@:<3f>", call_CGColor_v3f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "^{CGColor=}@:<3f>^{CGColorSpace=}", call_CGColor_v3f_CGColorSpace,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "f@:<2f>", call_f_v2f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "f@:<2i>", call_f_v2i, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<2d>d", call_v_v2d_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<2f>", call_v_v2f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<2f>d", call_v_v2f_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3d>", call_v_v3d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3d>d", call_v_v3d_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3f>", call_v_v3f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3f><3f>", call_v_v3f_v3f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3f><3f><3f>", call_v_v3f_v3f_v3f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3f>d", call_v_v3f_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<4d>d", call_v_v4d_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<4f>", call_v_v4f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<4f>d", call_v_v4f_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<4i>", call_v_v4i, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:@<2f><2f>", call_v_id_v2f_v2f, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:@<2f><2f>q", call_v_id_v2f_v2f_q, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:f<2i>", call_v_f_v2i, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}", call_v_MDLAxisAlignedBoundingBox,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}Z",
            call_v_MDLAxisAlignedBoundingBox_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}B",
            call_v_MDLAxisAlignedBoundingBox_Z, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_matrix_double4x4=[4<4d>]}", call_v_matrix_double4x4,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_matrix_double4x4=[4<4d>]}d", call_v_matrix_double4x4_d,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_matrix_float2x2=[2<2f>]}", call_v_matrix_float2x2,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_matrix_float3x3=[3<3f>]}", call_v_matrix_float3x3,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_matrix_float4x4=[4<4f>]}", call_v_matrix_float4x4,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_matrix_float4x4=[4<4f>]}d", call_v_matrix_float4x4_d,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_simd_float4x4=[4<4f>]}", call_v_simd_float4x4,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_simd_quatd=<4d>}d", call_v_simd_quatd_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_simd_quatf=<4f>}", call_v_simd_quatf, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_simd_quatf=<4f>}<3f>", call_v_simd_quatf_v3f,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{_simd_quatf=<4f>}d", call_v_simd_quatf_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{GKBox=<3f><3f>}@:", call_GKBox, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{GKQuad=<2f><2f>}@:", call_GKQuad, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{GKTriangle=[3<3f>]}@:Q", call_GKTriangle_Q, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_MDLAxisAlignedBoundingBox=<3f><3f>}@:", call_MDLAxisAlignedBoundingBox,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_MDLAxisAlignedBoundingBox=<3f><3f>}@:<4i>",
            call_MDLAxisAlignedBoundingBox_v4i, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_MDLAxisAlignedBoundingBox=<3f><3f>}@:d", call_MDLAxisAlignedBoundingBox_d,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_MDLVoxelIndexExtent=<4i><4i>}@:", call_MDLVoxelIndexExtent,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_MPSAxisAlignedBoundingBox=<3f><3f>}@:", call_MPSAxisAlignedBoundingBox,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_MPSImageHistogramInfo=QZ<4f><4f>}@:", call_MPSImageHistogramInfo,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_MPSImageHistogramInfo=QB<4f><4f>}@:", call_MPSImageHistogramInfo,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_matrix_double4x4=[4<4d>]}@:", call_matrix_double4x4,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_matrix_double4x4=[4<4d>]}@:d", call_matrix_double4x4_d,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_matrix_float2x2=[2<2f>]}@:", call_matrix_float2x2,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_matrix_float3x3=[3<3f>]}@:", call_matrix_float3x3,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_matrix_float4x4=[4<4f>]}@:", call_matrix_float4x4,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_matrix_float4x4=[4<4f>]}@:@d", call_matrix_float4x4_id_d,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_matrix_float4x4=[4<4f>]}@:d", call_matrix_float4x4_d,
            PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_simd_float4x4=[4<4f>]}@:", call_simd_float4x4, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_simd_float4x4=[4<4f>]}@:{_simd_float4x4=[4<4f>]}@",
            call_simd_float4x4_simd_float4x4_id, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_simd_quatd=<4d>}@:d", call_simd_quatd_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_simd_quatf=<4f>}@:", call_simd_quatf, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_simd_quatf=<4f>}@:d", call_simd_quatf_d, PyObjCUnsupportedMethod_IMP)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    return 0;
}
