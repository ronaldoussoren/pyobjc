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

NS_ASSUME_NONNULL_BEGIN

static inline int
extract_method_info(PyObject* method, PyObject* self, bool* isIMP, id* self_obj,
                    Class* super_class, int* flags, PyObjCMethodSignature** methinfo)
{
    *isIMP = !!PyObjCIMP_Check(method);

    if (*isIMP) {
        *flags    = PyObjCIMP_GetFlags(method);
        *methinfo = PyObjCIMP_GetSignature(method);
    } else {
        *flags    = PyObjCSelector_GetFlags(method);
        *methinfo = PyObjCSelector_GetMetadata(method);
    }

    if ((*flags) & PyObjCSelector_kCLASS_METHOD) {
        if (PyObjCObject_Check(self)) {
            *self_obj = PyObjCObject_GetObject(self);
            if (*self_obj == nil && PyErr_Occurred()) {
                return -1;
            }
            if (*self_obj != NULL) {
                *self_obj = object_getClass(*self_obj);
                if (*self_obj == nil && PyErr_Occurred()) {
                    return -1;
                }
            }

        } else if (PyObjCClass_Check(self)) {
            *self_obj = PyObjCClass_GetClass(self);
            if (*self_obj == nil && PyErr_Occurred()) {
                return -1;
            }

        } else if (PyType_Check(self)
                   && PyType_IsSubtype((PyTypeObject*)self, &PyType_Type)) {
            PyObject* c = PyObjCClass_ClassForMetaClass(self);
            if (c == NULL) {
                *self_obj = nil;

            } else {
                *self_obj = PyObjCClass_GetClass(c);
                if (*self_obj == nil && PyErr_Occurred()) {
                    return -1;
                }
            }

        } else {
            PyErr_Format(
                PyExc_TypeError,
                "Need Objective-C object or class as self, not an instance of '%s'",
                Py_TYPE(self)->tp_name);
            return -1;
        }

    } else {
        int err;
        if (PyObjCObject_Check(self)) {
            *self_obj = PyObjCObject_GetObject(self);
            if (*self_obj == nil && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                return -1;                              // LCOV_EXCL_LINE
            }

        } else {
            err = depythonify_c_value(@encode(id), self, self_obj);
            if (err == -1)
                return -1;
        }
    }

    if (*isIMP) {
        *super_class = nil;
    } else {
        if ((*flags) & PyObjCSelector_kCLASS_METHOD) {
            *super_class = object_getClass(PyObjCSelector_GetClass(method));
        } else {
            *super_class = PyObjCSelector_GetClass(method);
        }
    }

    return 0;
}

static PyObject*
adjust_retval(PyObjCMethodSignature* methinfo, PyObject* self, int flags,
              PyObject* result)
{
    if (methinfo->rettype->alreadyRetained) {
        if (PyObjCObject_Check(result)) {
            /* pythonify_c_return_value has retained the object, but we already
             * own a reference, therefore give the ref away again
             */
            [PyObjCObject_GetObject(result) release];
        }
    }

    if (methinfo->rettype->alreadyCFRetained) {
        if (PyObjCObject_Check(result)) {
            /* pythonify_c_return_value has retained the object, but we already
             * own a reference, therefore give the ref away again
             */
            CFRelease(PyObjCObject_GetObject(result));
        }
    }

    if (self != NULL && result != self && PyObjCObject_Check(self)
        && PyObjCObject_Check(result) && !(flags & PyObjCSelector_kRETURNS_UNINITIALIZED)
        && (((PyObjCObject*)self)->flags & PyObjCObject_kUNINITIALIZED)) {

        [PyObjCObject_GetObject(result) release]; /* XXX??? */
        PyObjCObject_ClearObject(self);
    }
    return result;
}

static PyObject* _Nullable call_v2d(PyObject* method, PyObject* self,
                                    PyObject* const* arguments
                                    __attribute__((__unused__)),
                                    size_t nargs)
{
    struct objc_super super;
    simd_double2      rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_double2(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_double2(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<2d>", &rv);
}

static IMP
mkimp_v2d(PyObject* callable, PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_double2 (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_double2 oc_result;
      if (depythonify_c_value("<2d>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v2d_d(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double2      rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_double2(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv =
                    ((simd_double2(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                        &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<2d>", &rv);
}

static IMP
mkimp_v2d_d(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_double2 (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_double2 oc_result;
      if (depythonify_c_value("<2d>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v2f(PyObject* method, PyObject* self,
                                    PyObject* const* arguments
                                    __attribute__((__unused__)),
                                    size_t nargs)
{
    struct objc_super super;
    simd_float2       rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float2(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float2(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<2f>", &rv);
}

static IMP
mkimp_v2f(PyObject* callable, PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float2 (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float2 oc_result;
      if (depythonify_c_value("<2f>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v2f_Q(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super  super;
    simd_float2        rv;
    unsigned long long arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("Q", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float2(*)(id, SEL, unsigned long long))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float2(*)(struct objc_super*, SEL,
                                      unsigned long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<2f>", &rv);
}

static IMP
mkimp_v2f_Q(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float2 (^block)(id, unsigned long long) =
        ^(id _Nullable self, unsigned long long arg0) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[3] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("Q", &arg0);
          if (args[2] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          simd_float2 oc_result;
          if (depythonify_c_value("<2f>", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 3; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 3; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v2f_d(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float2       rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float2(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float2(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<2f>", &rv);
}

static IMP
mkimp_v2f_d(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float2 (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float2 oc_result;
      if (depythonify_c_value("<2f>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v2f_q(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float2       rv;
    long long         arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("q", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float2(*)(id, SEL, long long))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((
                    simd_float2(*)(struct objc_super*, SEL, long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<2f>", &rv);
}

static IMP
mkimp_v2f_q(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float2 (^block)(id, long long) = ^(id _Nullable self, long long arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("q", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float2 oc_result;
      if (depythonify_c_value("<2f>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v2i(PyObject* method, PyObject* self,
                                    PyObject* const* arguments
                                    __attribute__((__unused__)),
                                    size_t nargs)
{
    struct objc_super super;
    simd_int2         rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_int2(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_int2(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<2i>", &rv);
}

static IMP
mkimp_v2i(PyObject* callable, PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_int2 (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_int2 oc_result;
      if (depythonify_c_value("<2i>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v3d_d(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double3      rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_double3(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv =
                    ((simd_double3(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                        &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<3d>", &rv);
}

static IMP
mkimp_v3d_d(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_double3 (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_double3 oc_result;
      if (depythonify_c_value("<3d>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v3f(PyObject* method, PyObject* self,
                                    PyObject* const* arguments
                                    __attribute__((__unused__)),
                                    size_t nargs)
{
    struct objc_super super;
    simd_float3       rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float3(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<3f>", &rv);
}

static IMP
mkimp_v3f(PyObject* callable, PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float3 (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float3 oc_result;
      if (depythonify_c_value("<3f>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v3f_v2i_v2i(PyObject* method, PyObject* self,
                                            PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, simd_int2, simd_int2))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float3(*)(struct objc_super*, SEL, simd_int2,
                                      simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<3f>", &rv);
}

static IMP
mkimp_v3f_v2i_v2i(PyObject*              callable,
                  PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float3 (^block)(id, simd_int2, simd_int2) =
        ^(id _Nullable self, simd_int2 arg0, simd_int2 arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<2i>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2i>", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          simd_float3 oc_result;
          if (depythonify_c_value("<3f>", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v3f_v3f(PyObject* method, PyObject* self,
                                        PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3       rv;
    simd_float3       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float3(*)(struct objc_super*, SEL,
                                      simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<3f>", &rv);
}

static IMP
mkimp_v3f_v3f(PyObject*              callable,
              PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float3 (^block)(id, simd_float3) = ^(id _Nullable self, simd_float3 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<3f>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float3 oc_result;
      if (depythonify_c_value("<3f>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v3f_v3f_id(PyObject* method, PyObject* self,
                                           PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, simd_float3, id))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float3(*)(struct objc_super*, SEL, simd_float3,
                                      id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<3f>", &rv);
}

static IMP
mkimp_v3f_v3f_id(PyObject*              callable,
                 PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float3 (^block)(id, simd_float3, id) =
        ^(id _Nullable self, simd_float3 arg0, id arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("@", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          simd_float3 oc_result;
          if (depythonify_c_value("<3f>", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v3f_v4i(PyObject* method, PyObject* self,
                                        PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3       rv;
    simd_int4         arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4i>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, simd_int4))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((
                    simd_float3(*)(struct objc_super*, SEL, simd_int4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<3f>", &rv);
}

static IMP
mkimp_v3f_v4i(PyObject*              callable,
              PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float3 (^block)(id, simd_int4) = ^(id _Nullable self, simd_int4 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<4i>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float3 oc_result;
      if (depythonify_c_value("<3f>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v3f_Q(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super  super;
    simd_float3        rv;
    unsigned long long arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("Q", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, unsigned long long))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float3(*)(struct objc_super*, SEL,
                                      unsigned long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<3f>", &rv);
}

static IMP
mkimp_v3f_Q(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float3 (^block)(id, unsigned long long) =
        ^(id _Nullable self, unsigned long long arg0) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[3] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("Q", &arg0);
          if (args[2] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          simd_float3 oc_result;
          if (depythonify_c_value("<3f>", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 3; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 3; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v3f_d(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3       rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float3(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<3f>", &rv);
}

static IMP
mkimp_v3f_d(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float3 (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float3 oc_result;
      if (depythonify_c_value("<3f>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v4d_d(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double4      rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_double4(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv =
                    ((simd_double4(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                        &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<4d>", &rv);
}

static IMP
mkimp_v4d_d(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_double4 (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_double4 oc_result;
      if (depythonify_c_value("<4d>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v4f(PyObject* method, PyObject* self,
                                    PyObject* const* arguments
                                    __attribute__((__unused__)),
                                    size_t nargs)
{
    struct objc_super super;
    simd_float4       rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float4(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float4(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<4f>", &rv);
}

static IMP
mkimp_v4f(PyObject* callable, PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float4 (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float4 oc_result;
      if (depythonify_c_value("<4f>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v4f_d(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float4       rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float4(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float4(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<4f>", &rv);
}

static IMP
mkimp_v4f_d(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float4 (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float4 oc_result;
      if (depythonify_c_value("<4f>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v4i_v3f(PyObject* method, PyObject* self,
                                        PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_int4         rv;
    simd_float3       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_int4(*)(id, SEL, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((
                    simd_int4(*)(struct objc_super*, SEL, simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<4i>", &rv);
}

static IMP
mkimp_v4i_v3f(PyObject*              callable,
              PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_int4 (^block)(id, simd_float3) = ^(id _Nullable self, simd_float3 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<3f>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_int4 oc_result;
      if (depythonify_c_value("<4i>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v2d_id(PyObject* method, PyObject* self,
                                          PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_double2      arg0;
    id                arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2d>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_double2, id))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv =
                    ((id(*)(struct objc_super*, SEL, simd_double2, id))objc_msgSendSuper)(
                        &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v2d_id(PyObject*              callable,
                PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_double2, id) = ^(id _Nullable self, simd_double2 arg0, id arg1) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[4] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<2d>", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("@", &arg1);
      if (args[3] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v2d_q(PyObject* method, PyObject* self,
                                         PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_double2      arg0;
    long long         arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2d>", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("q", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv =
                    ((id(*)(id, SEL, simd_double2, long long))(PyObjCIMP_GetIMP(method)))(
                        self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_double2,
                             long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v2d_q(PyObject*              callable,
               PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_double2, long long) =
        ^(id _Nullable self, simd_double2 arg0, long long arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<2d>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("q", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v2f(PyObject* method, PyObject* self,
                                       PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float2       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v2f(PyObject*              callable,
             PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float2) = ^(id _Nullable self, simd_float2 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<2f>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v2f_v2I_q_id(PyObject* method, PyObject* self,
                                                PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float2, simd_uint2, long long, id))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float2, simd_uint2, long long,
                             id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v2f_v2I_q_id(PyObject*              callable,
                      PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float2, simd_uint2, long long, id) =
        ^(id _Nullable self, simd_float2 arg0, simd_uint2 arg1, long long arg2, id arg3) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[6] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<2f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2I>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("q", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("@", &arg3);
          if (args[5] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 5 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v2f_v2f(PyObject* method, PyObject* self,
                                           PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float2, simd_float2))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float2,
                             simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v2f_v2f(PyObject*              callable,
                 PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float2, simd_float2) =
        ^(id _Nullable self, simd_float2 arg0, simd_float2 arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<2f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2f>", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v2i(PyObject* method, PyObject* self,
                                       PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_int2         arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2i>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_int2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v2i(PyObject*              callable,
             PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_int2) = ^(id _Nullable self, simd_int2 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<2i>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v2i_i_i_Z(PyObject* method, PyObject* self,
                                             PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_int2, int, int, BOOL))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_int2, int, int,
                             BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v2i_i_i_Z(PyObject*              callable,
                   PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_int2, int, int, BOOL) =
        ^(id _Nullable self, simd_int2 arg0, int arg1, int arg2, BOOL arg3) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[6] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<2i>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("i", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("i", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("Z", &arg3);
          if (args[5] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 5 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v2i_i_i_Z_Class(PyObject* method, PyObject* self,
                                                   PyObject* const* arguments,
                                                   size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_int2, int, int, BOOL, Class))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_int2, int, int, BOOL,
                             Class))objc_msgSendSuper)(&super,
                                                       PyObjCSelector_GetSelector(method),
                                                       arg0, arg1, arg2, arg3, arg4);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v2i_i_i_Z_Class(PyObject*              callable,
                         PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_int2, int, int, BOOL, Class) =
        ^(id _Nullable self, simd_int2 arg0, int arg1, int arg2, BOOL arg3, Class arg4) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[7] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<2i>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("i", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("i", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("Z", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("#", &arg4);
          if (args[6] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 6 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v3f(PyObject* method, PyObject* self,
                                       PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float3       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v3f(PyObject*              callable,
             PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float3) = ^(id _Nullable self, simd_float3 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<3f>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v3f_v2I_Z_Z_Z_q_id(PyObject* method, PyObject* self,
                                                      PyObject* const* arguments,
                                                      size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint2, BOOL, BOOL, BOOL,
                             long long, id))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2, arg3, arg4,
                    arg5, arg6);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint2, BOOL, BOOL,
                             BOOL, long long, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v3f_v2I_Z_Z_Z_q_id(PyObject*              callable,
                            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float3, simd_uint2, BOOL, BOOL, BOOL, long long, id) =
        ^(id _Nullable self, simd_float3 arg0, simd_uint2 arg1, BOOL arg2, BOOL arg3,
          BOOL arg4, long long arg5, id arg6) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[9] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2I>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("Z", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("Z", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("Z", &arg4);
          if (args[6] == NULL)
              goto error;
          args[7] = pythonify_c_value("q", &arg5);
          if (args[7] == NULL)
              goto error;
          args[8] = pythonify_c_value("@", &arg6);
          if (args[8] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 8 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 9; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 9; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v3f_v2I_Z_Z_q_id(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint2, BOOL, BOOL, long long,
                             id))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2, arg3, arg4,
                    arg5);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint2, BOOL, BOOL,
                             long long, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v3f_v2I_Z_Z_q_id(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float3, simd_uint2, BOOL, BOOL, long long, id) =
        ^(id _Nullable self, simd_float3 arg0, simd_uint2 arg1, BOOL arg2, BOOL arg3,
          long long arg4, id arg5) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[8] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2I>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("Z", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("Z", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("q", &arg4);
          if (args[6] == NULL)
              goto error;
          args[7] = pythonify_c_value("@", &arg5);
          if (args[7] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 7 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 8; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 8; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v3f_v2I_Z_q_id(PyObject* method, PyObject* self,
                                                  PyObject* const* arguments,
                                                  size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint2, BOOL, long long, id))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint2, BOOL,
                             long long, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v3f_v2I_Z_q_id(PyObject*              callable,
                        PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float3, simd_uint2, BOOL, long long, id) =
        ^(id _Nullable self, simd_float3 arg0, simd_uint2 arg1, BOOL arg2, long long arg3,
          id arg4) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[7] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2I>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("Z", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("q", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("@", &arg4);
          if (args[6] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 6 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v3f_v2I_i_Z_q_id(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint2, int, BOOL, long long, id))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4, arg5);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint2, int, BOOL,
                             long long, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v3f_v2I_i_Z_q_id(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float3, simd_uint2, int, BOOL, long long, id) =
        ^(id _Nullable self, simd_float3 arg0, simd_uint2 arg1, int arg2, BOOL arg3,
          long long arg4, id arg5) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[8] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2I>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("i", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("Z", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("q", &arg4);
          if (args[6] == NULL)
              goto error;
          args[7] = pythonify_c_value("@", &arg5);
          if (args[7] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 7 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 8; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 8; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v3f_v2I_q_id(PyObject* method, PyObject* self,
                                                PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint2, long long, id))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint2, long long,
                             id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v3f_v2I_q_id(PyObject*              callable,
                      PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float3, simd_uint2, long long, id) =
        ^(id _Nullable self, simd_float3 arg0, simd_uint2 arg1, long long arg2, id arg3) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[6] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2I>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("q", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("@", &arg3);
          if (args[5] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 5 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v3f_v3I_Z_q_id(PyObject* method, PyObject* self,
                                                  PyObject* const* arguments,
                                                  size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint3, BOOL, long long, id))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint3, BOOL,
                             long long, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v3f_v3I_Z_q_id(PyObject*              callable,
                        PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float3, simd_uint3, BOOL, long long, id) =
        ^(id _Nullable self, simd_float3 arg0, simd_uint3 arg1, BOOL arg2, long long arg3,
          id arg4) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[7] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<3I>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("Z", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("q", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("@", &arg4);
          if (args[6] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 6 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v3f_v3I_q_Z_id(PyObject* method, PyObject* self,
                                                  PyObject* const* arguments,
                                                  size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, simd_uint3, long long, BOOL, id))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, simd_uint3, long long,
                             BOOL, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v3f_v3I_q_Z_id(PyObject*              callable,
                        PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float3, simd_uint3, long long, BOOL, id) =
        ^(id _Nullable self, simd_float3 arg0, simd_uint3 arg1, long long arg2, BOOL arg3,
          id arg4) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[7] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<3I>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("q", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("Z", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("@", &arg4);
          if (args[6] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 6 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v3f_Q_Q_q_Z_Z_id(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, unsigned long long, unsigned long long,
                             long long, BOOL, BOOL, id))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2, arg3, arg4,
                    arg5, arg6);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, unsigned long long,
                             unsigned long long, long long, BOOL, BOOL,
                             id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v3f_Q_Q_q_Z_Z_id(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float3, unsigned long long, unsigned long long, long long, BOOL,
                BOOL, id) = ^(id _Nullable self, simd_float3 arg0,
                              unsigned long long arg1, unsigned long long arg2,
                              long long arg3, BOOL arg4, BOOL arg5, id arg6) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[9] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<3f>", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("Q", &arg1);
      if (args[3] == NULL)
          goto error;
      args[4] = pythonify_c_value("Q", &arg2);
      if (args[4] == NULL)
          goto error;
      args[5] = pythonify_c_value("q", &arg3);
      if (args[5] == NULL)
          goto error;
      args[6] = pythonify_c_value("Z", &arg4);
      if (args[6] == NULL)
          goto error;
      args[7] = pythonify_c_value("Z", &arg5);
      if (args[7] == NULL)
          goto error;
      args[8] = pythonify_c_value("@", &arg6);
      if (args[8] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             8 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 9; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 9; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v3f_Z_q_id(PyObject* method, PyObject* self,
                                              PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float3, BOOL, long long, id))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float3, BOOL, long long,
                             id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v3f_Z_q_id(PyObject*              callable,
                    PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float3, BOOL, long long, id) =
        ^(id _Nullable self, simd_float3 arg0, BOOL arg1, long long arg2, id arg3) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[6] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("Z", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("q", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("@", &arg3);
          if (args[5] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 5 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_v4f(PyObject* method, PyObject* self,
                                       PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float4       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float4))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_v4f(PyObject*              callable,
             PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float4) = ^(id _Nullable self, simd_float4 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<4f>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_v2d_v2d_v2i_Z(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_double2, simd_double2, simd_int2, BOOL))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, simd_double2, simd_double2,
                             simd_int2, BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_v2d_v2d_v2i_Z(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, simd_double2, simd_double2, simd_int2, BOOL) =
        ^(id _Nullable self, id arg0, simd_double2 arg1, simd_double2 arg2,
          simd_int2 arg3, BOOL arg4) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[7] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2d>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2d>", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("<2i>", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("Z", &arg4);
          if (args[6] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 6 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_v2f(PyObject* method, PyObject* self,
                                          PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_float2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_v2f(PyObject*              callable,
                PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, simd_float2) = ^(id _Nullable self, id arg0, simd_float2 arg1) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[4] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("@", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("<2f>", &arg1);
      if (args[3] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_v3f(PyObject* method, PyObject* self,
                                          PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_v3f(PyObject*              callable,
                PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, simd_float3) = ^(id _Nullable self, id arg0, simd_float3 arg1) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[4] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("@", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("<3f>", &arg1);
      if (args[3] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_v4f(PyObject* method, PyObject* self,
                                          PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_float4))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, simd_float4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_v4f(PyObject*              callable,
                PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, simd_float4) = ^(id _Nullable self, id arg0, simd_float4 arg1) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[4] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("@", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("<4f>", &arg1);
      if (args[3] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_id_v2i(PyObject* method, PyObject* self,
                                             PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, id, simd_int2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((
                    id(*)(struct objc_super*, SEL, id, id, simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_id_v2i(PyObject*              callable,
                   PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, id, simd_int2) =
        ^(id _Nullable self, id arg0, id arg1, simd_int2 arg2) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[5] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("@", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2i>", &arg2);
          if (args[4] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_id_v2i_f(PyObject* method, PyObject* self,
                                               PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, id, simd_int2, float))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, id, simd_int2,
                             float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_id_v2i_f(PyObject*              callable,
                     PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, id, simd_int2, float) =
        ^(id _Nullable self, id arg0, id arg1, simd_int2 arg2, float arg3) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[6] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("@", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2i>", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("f", &arg3);
          if (args[5] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 5 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_Q_v2f(PyObject* method, PyObject* self,
                                            PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, unsigned long long, simd_float2))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, unsigned long long,
                             simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_Q_v2f(PyObject*              callable,
                  PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, unsigned long long, simd_float2) =
        ^(id _Nullable self, id arg0, unsigned long long arg1, simd_float2 arg2) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[5] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("Q", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2f>", &arg2);
          if (args[4] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_Q_v3f(PyObject* method, PyObject* self,
                                            PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, unsigned long long, simd_float3))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, unsigned long long,
                             simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_Q_v3f(PyObject*              callable,
                  PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, unsigned long long, simd_float3) =
        ^(id _Nullable self, id arg0, unsigned long long arg1, simd_float3 arg2) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[5] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("Q", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<3f>", &arg2);
          if (args[4] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_Q_v4f(PyObject* method, PyObject* self,
                                            PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, unsigned long long, simd_float4))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, unsigned long long,
                             simd_float4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_Q_v4f(PyObject*              callable,
                  PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, unsigned long long, simd_float4) =
        ^(id _Nullable self, id arg0, unsigned long long arg1, simd_float4 arg2) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[5] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("Q", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<4f>", &arg2);
          if (args[4] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_Q_simd_float4x4(PyObject* method, PyObject* self,
                                                      PyObject* const* arguments,
                                                      size_t           nargs)
{
    struct objc_super  super;
    id                 rv;
    id                 arg0;
    unsigned long long arg1;
    simd_float4x4      arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Q", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{simd_float4x4=[4<4f>]}", arguments[2], &arg2) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, unsigned long long, simd_float4x4))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, unsigned long long,
                             simd_float4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_Q_simd_float4x4(PyObject*              callable,
                            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, unsigned long long, simd_float4x4) =
        ^(id _Nullable self, id arg0, unsigned long long arg1, simd_float4x4 arg2) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[5] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("Q", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("{simd_float4x4=[4<4f>]}", &arg2);
          if (args[4] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_Z_id_v2i_q_Q_q_Z(PyObject* method, PyObject* self,
                                                       PyObject* const* arguments,
                                                       size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, BOOL, id, simd_int2, long long,
                             unsigned long long, long long, BOOL))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4, arg5, arg6,
                                               arg7);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, BOOL, id, simd_int2, long long,
                             unsigned long long, long long, BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6, arg7);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_Z_id_v2i_q_Q_q_Z(PyObject*              callable,
                             PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, BOOL, id, simd_int2, long long, unsigned long long, long long,
                BOOL) = ^(id _Nullable self, id arg0, BOOL arg1, id arg2, simd_int2 arg3,
                          long long arg4, unsigned long long arg5, long long arg6,
                          BOOL arg7) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[10] = {NULL};
      PyObject* pyself   = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("@", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("Z", &arg1);
      if (args[3] == NULL)
          goto error;
      args[4] = pythonify_c_value("@", &arg2);
      if (args[4] == NULL)
          goto error;
      args[5] = pythonify_c_value("<2i>", &arg3);
      if (args[5] == NULL)
          goto error;
      args[6] = pythonify_c_value("q", &arg4);
      if (args[6] == NULL)
          goto error;
      args[7] = pythonify_c_value("Q", &arg5);
      if (args[7] == NULL)
          goto error;
      args[8] = pythonify_c_value("q", &arg6);
      if (args[8] == NULL)
          goto error;
      args[9] = pythonify_c_value("Z", &arg7);
      if (args[9] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             9 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 10; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 10; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_q_v2i_f_f_f_f(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, long long, simd_int2, float, float, float,
                             float))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2, arg3, arg4,
                    arg5, arg6);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, long long, simd_int2, float,
                             float, float, float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_q_v2i_f_f_f_f(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, long long, simd_int2, float, float, float, float) =
        ^(id _Nullable self, id arg0, long long arg1, simd_int2 arg2, float arg3,
          float arg4, float arg5, float arg6) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[9] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("q", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2i>", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("f", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("f", &arg4);
          if (args[6] == NULL)
              goto error;
          args[7] = pythonify_c_value("f", &arg5);
          if (args[7] == NULL)
              goto error;
          args[8] = pythonify_c_value("f", &arg6);
          if (args[8] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 8 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 9; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 9; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_q_v2i_f_f_f_f_f(PyObject* method, PyObject* self,
                                                      PyObject* const* arguments,
                                                      size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, long long, simd_int2, float, float, float,
                             float, float))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2, arg3, arg4,
                    arg5, arg6, arg7);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, long long, simd_int2, float,
                             float, float, float, float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6, arg7);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_q_v2i_f_f_f_f_f(PyObject*              callable,
                            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, long long, simd_int2, float, float, float, float, float) =
        ^(id _Nullable self, id arg0, long long arg1, simd_int2 arg2, float arg3,
          float arg4, float arg5, float arg6, float arg7) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[10] = {NULL};
          PyObject* pyself   = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("q", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2i>", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("f", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("f", &arg4);
          if (args[6] == NULL)
              goto error;
          args[7] = pythonify_c_value("f", &arg5);
          if (args[7] == NULL)
              goto error;
          args[8] = pythonify_c_value("f", &arg6);
          if (args[8] == NULL)
              goto error;
          args[9] = pythonify_c_value("f", &arg7);
          if (args[9] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 9 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 10; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 10; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#if PyObjC_BUILD_RELEASE >= 1012

static PyObject* _Nullable call_id_id_GKBox(PyObject* method, PyObject* self,
                                            PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, GKBox))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, GKBox))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_GKBox(PyObject*              callable,
                  PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, GKBox) = ^(id _Nullable self, id arg0, GKBox arg1) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[4] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("@", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("{GKBox=<3f><3f>}", &arg1);
      if (args[3] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
static PyObject* _Nullable call_id_id_GKQuad(PyObject* method, PyObject* self,
                                             PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, GKQuad))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, GKQuad))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
static IMP
mkimp_id_id_GKQuad(PyObject*              callable,
                   PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, GKQuad) = ^(id _Nullable self, id arg0, GKQuad arg1) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[4] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("@", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("{GKQuad=<2f><2f>}", &arg1);
      if (args[3] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
static PyObject* _Nullable call_id_id_MDLAxisAlignedBoundingBox_f(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
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
    if (depythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", arguments[1], &arg1)
        == -1) {
        return NULL;
    }
    if (depythonify_c_value("f", arguments[2], &arg2) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, MDLAxisAlignedBoundingBox, float))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, MDLAxisAlignedBoundingBox,
                             float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static IMP
mkimp_id_id_MDLAxisAlignedBoundingBox_f(PyObject*              callable,
                                        PyObjCMethodSignature* methinfo
                                        __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, MDLAxisAlignedBoundingBox, float) =
        ^(id _Nullable self, id arg0, MDLAxisAlignedBoundingBox arg1, float arg2) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[5] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("f", &arg2);
          if (args[4] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

static PyObject* _Nullable call_id_id_simd_float2x2(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    simd_float2x2     arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{simd_float2x2=[2<2f>]}", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_float2x2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((
                    id(*)(struct objc_super*, SEL, id, simd_float2x2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_simd_float2x2(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, simd_float2x2) =
        ^(id _Nullable self, id arg0, simd_float2x2 arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("{simd_float2x2=[2<2f>]}", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_simd_float3x3(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    simd_float3x3     arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{simd_float3x3=[3<3f>]}", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_float3x3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((
                    id(*)(struct objc_super*, SEL, id, simd_float3x3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_simd_float3x3(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, simd_float3x3) =
        ^(id _Nullable self, id arg0, simd_float3x3 arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("{simd_float3x3=[3<3f>]}", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_id_simd_float4x4(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    simd_float4x4     arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{simd_float4x4=[4<4f>]}", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_float4x4))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((
                    id(*)(struct objc_super*, SEL, id, simd_float4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_id_simd_float4x4(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, simd_float4x4) =
        ^(id _Nullable self, id arg0, simd_float4x4 arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("{simd_float4x4=[4<4f>]}", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

#if PyObjC_BUILD_RELEASE >= 1013
static PyObject* _Nullable call_id_id_simd_quatf(PyObject* method, PyObject* self,
                                                 PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    simd_quatf        arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{simd_quatf=<4f>}", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_quatf))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, id, simd_quatf))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static IMP
mkimp_id_id_simd_quatf(PyObject*              callable,
                       PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, simd_quatf) = ^(id _Nullable self, id arg0, simd_quatf arg1) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[4] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("@", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("{simd_quatf=<4f>}", &arg1);
      if (args[3] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static PyObject* _Nullable call_id_id_simd_quatf_id(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
{
    struct objc_super super;
    id                rv;
    id                arg0;
    simd_quatf        arg1;
    id                arg2;

    if (PyObjC_CheckArgCount(method, 3, 3, nargs) == -1)
        return NULL;

    if (depythonify_c_value("@", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("{simd_quatf=<4f>}", arguments[1], &arg1) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[2], &arg2) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, id, simd_quatf, id))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((
                    id(*)(struct objc_super*, SEL, id, simd_quatf, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static IMP
mkimp_id_id_simd_quatf_id(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, id, simd_quatf, id) =
        ^(id _Nullable self, id arg0, simd_quatf arg1, id arg2) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[5] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("{simd_quatf=<4f>}", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("@", &arg2);
          if (args[4] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

static PyObject* _Nullable call_id_CGColor_CGColor_id_v2i(PyObject*        method,
                                                          PyObject*        self,
                                                          PyObject* const* arguments,
                                                          size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, CGColorRef, CGColorRef, id, simd_int2))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, CGColorRef, CGColorRef, id,
                             simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_CGColor_CGColor_id_v2i(PyObject* callable, PyObjCMethodSignature* methinfo
                                __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, CGColorRef, CGColorRef, id, simd_int2) =
        ^(id _Nullable self, CGColorRef arg0, CGColorRef arg1, id arg2, simd_int2 arg3) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[6] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("^{CGColor=}", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("^{CGColor=}", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("@", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("<2i>", &arg3);
          if (args[5] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 5 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_f_v2f_v2f(PyObject* method, PyObject* self,
                                             PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, simd_float2, simd_float2))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, float, simd_float2,
                             simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_f_v2f_v2f(PyObject*              callable,
                   PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, float, simd_float2, simd_float2) =
        ^(id _Nullable self, float arg0, simd_float2 arg1, simd_float2 arg2) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[5] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("f", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2f>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2f>", &arg2);
          if (args[4] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_f_v2f_v2f_Class(PyObject* method, PyObject* self,
                                                   PyObject* const* arguments,
                                                   size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, simd_float2, simd_float2, Class))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, float, simd_float2, simd_float2,
                             Class))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_f_v2f_v2f_Class(PyObject*              callable,
                         PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, float, simd_float2, simd_float2, Class) =
        ^(id _Nullable self, float arg0, simd_float2 arg1, simd_float2 arg2, Class arg3) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[6] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("f", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2f>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2f>", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("#", &arg3);
          if (args[5] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 5 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_f_v2f_Q_Q_Q_q_Z_id(PyObject* method, PyObject* self,
                                                      PyObject* const* arguments,
                                                      size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, simd_float2, unsigned long long,
                             unsigned long long, unsigned long long, long long, BOOL,
                             id))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2, arg3, arg4,
                    arg5, arg6, arg7);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, float, simd_float2,
                             unsigned long long, unsigned long long, unsigned long long,
                             long long, BOOL, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6, arg7);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_f_v2f_Q_Q_Q_q_Z_id(PyObject*              callable,
                            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, float, simd_float2, unsigned long long, unsigned long long,
                unsigned long long, long long, BOOL,
                id) = ^(id _Nullable self, float arg0, simd_float2 arg1,
                        unsigned long long arg2, unsigned long long arg3,
                        unsigned long long arg4, long long arg5, BOOL arg6, id arg7) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[10] = {NULL};
      PyObject* pyself   = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("f", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("<2f>", &arg1);
      if (args[3] == NULL)
          goto error;
      args[4] = pythonify_c_value("Q", &arg2);
      if (args[4] == NULL)
          goto error;
      args[5] = pythonify_c_value("Q", &arg3);
      if (args[5] == NULL)
          goto error;
      args[6] = pythonify_c_value("Q", &arg4);
      if (args[6] == NULL)
          goto error;
      args[7] = pythonify_c_value("q", &arg5);
      if (args[7] == NULL)
          goto error;
      args[8] = pythonify_c_value("Z", &arg6);
      if (args[8] == NULL)
          goto error;
      args[9] = pythonify_c_value("@", &arg7);
      if (args[9] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             9 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 10; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 10; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_f_v2f_Q_Q_q_Z_id(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments,
                                                    size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, simd_float2, unsigned long long,
                             unsigned long long, long long, BOOL, id))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4, arg5, arg6);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, float, simd_float2,
                             unsigned long long, unsigned long long, long long, BOOL,
                             id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_f_v2f_Q_Q_q_Z_id(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, float, simd_float2, unsigned long long, unsigned long long, long long,
                BOOL, id) = ^(id _Nullable self, float arg0, simd_float2 arg1,
                              unsigned long long arg2, unsigned long long arg3,
                              long long arg4, BOOL arg5, id arg6) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[9] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("f", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("<2f>", &arg1);
      if (args[3] == NULL)
          goto error;
      args[4] = pythonify_c_value("Q", &arg2);
      if (args[4] == NULL)
          goto error;
      args[5] = pythonify_c_value("Q", &arg3);
      if (args[5] == NULL)
          goto error;
      args[6] = pythonify_c_value("q", &arg4);
      if (args[6] == NULL)
          goto error;
      args[7] = pythonify_c_value("Z", &arg5);
      if (args[7] == NULL)
          goto error;
      args[8] = pythonify_c_value("@", &arg6);
      if (args[8] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             8 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 9; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 9; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_f_id_v2i_i_q_Z(PyObject* method, PyObject* self,
                                                  PyObject* const* arguments,
                                                  size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, id, simd_int2, int, long long, BOOL))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4, arg5);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, float, id, simd_int2, int,
                             long long, BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_f_id_v2i_i_q_Z(PyObject*              callable,
                        PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, float, id, simd_int2, int, long long, BOOL) =
        ^(id _Nullable self, float arg0, id arg1, simd_int2 arg2, int arg3,
          long long arg4, BOOL arg5) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[8] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("f", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("@", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2i>", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("i", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("q", &arg4);
          if (args[6] == NULL)
              goto error;
          args[7] = pythonify_c_value("Z", &arg5);
          if (args[7] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 7 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 8; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 8; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_f_id_v2i_i_q_CGColor_CGColor(
    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, id, simd_int2, int, long long, CGColorRef,
                             CGColorRef))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2, arg3, arg4,
                    arg5, arg6);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, float, id, simd_int2, int,
                             long long, CGColorRef, CGColorRef))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5, arg6);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_f_id_v2i_i_q_CGColor_CGColor(PyObject* callable, PyObjCMethodSignature* methinfo
                                      __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, float, id, simd_int2, int, long long, CGColorRef, CGColorRef) =
        ^(id _Nullable self, float arg0, id arg1, simd_int2 arg2, int arg3,
          long long arg4, CGColorRef arg5, CGColorRef arg6) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[9] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("f", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("@", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2i>", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("i", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("q", &arg4);
          if (args[6] == NULL)
              goto error;
          args[7] = pythonify_c_value("^{CGColor=}", &arg5);
          if (args[7] == NULL)
              goto error;
          args[8] = pythonify_c_value("^{CGColor=}", &arg6);
          if (args[8] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 8 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 9; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 9; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_f_id_v2i_q(PyObject* method, PyObject* self,
                                              PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, id, simd_int2, long long))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, float, id, simd_int2,
                             long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_f_id_v2i_q(PyObject*              callable,
                    PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, float, id, simd_int2, long long) =
        ^(id _Nullable self, float arg0, id arg1, simd_int2 arg2, long long arg3) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[6] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("f", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("@", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2i>", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("q", &arg3);
          if (args[5] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 5 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_f_f_id_v2i(PyObject* method, PyObject* self,
                                              PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, float, float, id, simd_int2))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, float, float, id,
                             simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_f_f_id_v2i(PyObject*              callable,
                    PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, float, float, id, simd_int2) =
        ^(id _Nullable self, float arg0, float arg1, id arg2, simd_int2 arg3) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[6] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("f", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("f", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("@", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("<2i>", &arg3);
          if (args[5] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 5 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 6; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#if PyObjC_BUILD_RELEASE >= 1012

static PyObject* _Nullable call_id_GKBox(PyObject* method, PyObject* self,
                                         PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    GKBox             arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{GKBox=<3f><3f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, GKBox))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, GKBox))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_GKBox(PyObject*              callable,
               PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, GKBox) = ^(id _Nullable self, GKBox arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("{GKBox=<3f><3f>}", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */
#if PyObjC_BUILD_RELEASE >= 1012

static PyObject* _Nullable call_id_GKBox_f(PyObject* method, PyObject* self,
                                           PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, GKBox, float))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, GKBox, float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_GKBox_f(PyObject*              callable,
                 PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, GKBox, float) = ^(id _Nullable self, GKBox arg0, float arg1) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[4] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("{GKBox=<3f><3f>}", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("f", &arg1);
      if (args[3] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
static PyObject* _Nullable call_id_GKQuad(PyObject* method, PyObject* self,
                                          PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    GKQuad            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{GKQuad=<2f><2f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, GKQuad))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, GKQuad))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
static IMP
mkimp_id_GKQuad(PyObject*              callable,
                PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, GKQuad) = ^(id _Nullable self, GKQuad arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("{GKQuad=<2f><2f>}", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
static PyObject* _Nullable call_id_GKQuad_f(PyObject* method, PyObject* self,
                                            PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, GKQuad, float))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, GKQuad, float))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
static IMP
mkimp_id_GKQuad_f(PyObject*              callable,
                  PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, GKQuad, float) = ^(id _Nullable self, GKQuad arg0, float arg1) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[4] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("{GKQuad=<2f><2f>}", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("f", &arg1);
      if (args[3] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
static PyObject* _Nullable call_id_MDLVoxelIndexExtent(PyObject* method, PyObject* self,
                                                       PyObject* const* arguments,
                                                       size_t           nargs)
{
    struct objc_super   super;
    id                  rv;
    MDLVoxelIndexExtent arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{MDLVoxelIndexExtent=<4i><4i>}", arguments[0], &arg0)
        == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, MDLVoxelIndexExtent))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL,
                             MDLVoxelIndexExtent))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static IMP
mkimp_id_MDLVoxelIndexExtent(PyObject*              callable,
                             PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, MDLVoxelIndexExtent) =
        ^(id _Nullable self, MDLVoxelIndexExtent arg0) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[3] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("{MDLVoxelIndexExtent=<4i><4i>}", &arg0);
          if (args[2] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 3; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 3; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

static PyObject* _Nullable call_id_simd_float4x4(PyObject* method, PyObject* self,
                                                 PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    id                rv;
    simd_float4x4     arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float4x4))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_simd_float4x4(PyObject*              callable,
                       PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float4x4) = ^(id _Nullable self, simd_float4x4 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("{simd_float4x4=[4<4f>]}", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      id oc_result;
      if (depythonify_c_value("@", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_id_simd_float4x4_Z(PyObject* method, PyObject* self,
                                                   PyObject* const* arguments,
                                                   size_t           nargs)
{
    struct objc_super super;
    id                rv;
    simd_float4x4     arg0;
    BOOL              arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((id(*)(id, SEL, simd_float4x4, BOOL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((id(*)(struct objc_super*, SEL, simd_float4x4,
                             BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return adjust_retval(methinfo, self, flags, pythonify_c_value("@", &rv));
}

static IMP
mkimp_id_simd_float4x4_Z(PyObject*              callable,
                         PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    id (^block)(id, simd_float4x4, BOOL) =
        ^(id _Nullable self, simd_float4x4 arg0, BOOL arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("{simd_float4x4=[4<4f>]}", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("Z", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          id oc_result;
          if (depythonify_c_value("@", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_Z_v2i_id_id_id_id(PyObject* method, PyObject* self,
                                                  PyObject* const* arguments,
                                                  size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((BOOL(*)(id, SEL, simd_int2, id, id, id, id))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((BOOL(*)(struct objc_super*, SEL, simd_int2, id, id, id,
                               id))objc_msgSendSuper)(&super,
                                                      PyObjCSelector_GetSelector(method),
                                                      arg0, arg1, arg2, arg3, arg4);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("Z", &rv);
}

static IMP
mkimp_Z_v2i_id_id_id_id(PyObject*              callable,
                        PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    BOOL (^block)(id, simd_int2, id, id, id, id) =
        ^(id _Nullable self, simd_int2 arg0, id arg1, id arg2, id arg3, id arg4) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[7] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<2i>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("@", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("@", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("@", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("@", &arg4);
          if (args[6] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 6 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          BOOL oc_result;
          if (depythonify_c_value("Z", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_Z_v2i_q_f_id_id_id(PyObject* method, PyObject* self,
                                                   PyObject* const* arguments,
                                                   size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((BOOL(*)(id, SEL, simd_int2, long long, float, id, id, id))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4, arg5);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((BOOL(*)(struct objc_super*, SEL, simd_int2, long long, float, id,
                               id, id))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4, arg5);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("Z", &rv);
}

static IMP
mkimp_Z_v2i_q_f_id_id_id(PyObject*              callable,
                         PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    BOOL (^block)(id, simd_int2, long long, float, id, id, id) =
        ^(id _Nullable self, simd_int2 arg0, long long arg1, float arg2, id arg3, id arg4,
          id arg5) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[8] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<2i>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("q", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("f", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("@", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("@", &arg4);
          if (args[6] == NULL)
              goto error;
          args[7] = pythonify_c_value("@", &arg5);
          if (args[7] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 7 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          BOOL oc_result;
          if (depythonify_c_value("Z", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 8; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 8; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_Z_v4i_Z_Z_Z_Z(PyObject* method, PyObject* self,
                                              PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((BOOL(*)(id, SEL, simd_int4, BOOL, BOOL, BOOL, BOOL))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3, arg4);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((BOOL(*)(struct objc_super*, SEL, simd_int4, BOOL, BOOL, BOOL,
                               BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3,
                    arg4);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("Z", &rv);
}

static IMP
mkimp_Z_v4i_Z_Z_Z_Z(PyObject*              callable,
                    PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    BOOL (^block)(id, simd_int4, BOOL, BOOL, BOOL, BOOL) =
        ^(id _Nullable self, simd_int4 arg0, BOOL arg1, BOOL arg2, BOOL arg3, BOOL arg4) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[7] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<4i>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("Z", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("Z", &arg2);
          if (args[4] == NULL)
              goto error;
          args[5] = pythonify_c_value("Z", &arg3);
          if (args[5] == NULL)
              goto error;
          args[6] = pythonify_c_value("Z", &arg4);
          if (args[6] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 6 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          BOOL oc_result;
          if (depythonify_c_value("Z", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 7; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_CGColor_v3f(PyObject* method, PyObject* self,
                                            PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    CGColorRef        rv;
    simd_float3       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((CGColorRef(*)(id, SEL, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((CGColorRef(*)(struct objc_super*, SEL,
                                     simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("^{CGColor=}", &rv);
}

static IMP
mkimp_CGColor_v3f(PyObject*              callable,
                  PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    CGColorRef (^block)(id, simd_float3) = ^(id _Nullable self, simd_float3 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<3f>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      CGColorRef oc_result;
      if (depythonify_c_value("^{CGColor=}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_CGColor_v3f_CGColorSpace(PyObject* method, PyObject* self,
                                                         PyObject* const* arguments,
                                                         size_t           nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((CGColorRef(*)(id, SEL, simd_float3, CGColorSpaceRef))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((CGColorRef(*)(struct objc_super*, SEL, simd_float3,
                                     CGColorSpaceRef))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("^{CGColor=}", &rv);
}

static IMP
mkimp_CGColor_v3f_CGColorSpace(PyObject* callable, PyObjCMethodSignature* methinfo
                               __attribute__((__unused__)))
{
    Py_INCREF(callable);

    CGColorRef (^block)(id, simd_float3, CGColorSpaceRef) =
        ^(id _Nullable self, simd_float3 arg0, CGColorSpaceRef arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("^{CGColorSpace=}", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          CGColorRef oc_result;
          if (depythonify_c_value("^{CGColor=}", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_f_v2f(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    float             rv;
    simd_float2       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((float (*)(id, SEL, simd_float2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((float (*)(struct objc_super*, SEL, simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("f", &rv);
}

static IMP
mkimp_f_v2f(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    float (^block)(id, simd_float2) = ^(id _Nullable self, simd_float2 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<2f>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      float oc_result;
      if (depythonify_c_value("f", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_f_v2i(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    float             rv;
    simd_int2         arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2i>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((float (*)(id, SEL, simd_int2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((float (*)(struct objc_super*, SEL, simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("f", &rv);
}

static IMP
mkimp_f_v2i(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    float (^block)(id, simd_int2) = ^(id _Nullable self, simd_int2 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<2i>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      float oc_result;
      if (depythonify_c_value("f", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v2d(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double2      arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2d>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_double2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v2d(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_double2) = ^(id _Nullable self, simd_double2 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<2d>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v2d_d(PyObject* method, PyObject* self,
                                        PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double2, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_double2,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v2d_d(PyObject*              callable,
              PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_double2, double) =
        ^(id _Nullable self, simd_double2 arg0, double arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<2d>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("d", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v2f(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float2       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<2f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v2f(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float2) = ^(id _Nullable self, simd_float2 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<2f>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v2f_d(PyObject* method, PyObject* self,
                                        PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float2, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float2,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v2f_d(PyObject*              callable,
              PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float2, double) =
        ^(id _Nullable self, simd_float2 arg0, double arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<2f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("d", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v3d(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double3      arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3d>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_double3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v3d(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_double3) = ^(id _Nullable self, simd_double3 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<3d>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v3d_d(PyObject* method, PyObject* self,
                                        PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double3, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_double3,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v3d_d(PyObject*              callable,
              PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_double3, double) =
        ^(id _Nullable self, simd_double3 arg0, double arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3d>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("d", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v3f(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<3f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v3f(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float3) = ^(id _Nullable self, simd_float3 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<3f>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v3f_v3f(PyObject* method, PyObject* self,
                                          PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float3, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float3,
                           simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v3f_v3f(PyObject*              callable,
                PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float3, simd_float3) =
        ^(id _Nullable self, simd_float3 arg0, simd_float3 arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<3f>", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v3f_v3f_v3f(PyObject* method, PyObject* self,
                                              PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float3, simd_float3, simd_float3))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float3, simd_float3,
                           simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v3f_v3f_v3f(PyObject*              callable,
                    PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float3, simd_float3, simd_float3) =
        ^(id _Nullable self, simd_float3 arg0, simd_float3 arg1, simd_float3 arg2) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[5] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<3f>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<3f>", &arg2);
          if (args[4] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v3f_d(PyObject* method, PyObject* self,
                                        PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float3, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float3,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v3f_d(PyObject*              callable,
              PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float3, double) =
        ^(id _Nullable self, simd_float3 arg0, double arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<3f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("d", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v4d_d(PyObject* method, PyObject* self,
                                        PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double4, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_double4,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v4d_d(PyObject*              callable,
              PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_double4, double) =
        ^(id _Nullable self, simd_double4 arg0, double arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<4d>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("d", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v4f(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float4       arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4f>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float4))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v4f(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float4) = ^(id _Nullable self, simd_float4 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<4f>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v4f_d(PyObject* method, PyObject* self,
                                        PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float4, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float4,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v4f_d(PyObject*              callable,
              PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float4, double) =
        ^(id _Nullable self, simd_float4 arg0, double arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("<4f>", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("d", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_v4i(PyObject* method, PyObject* self,
                                      PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_int4         arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4i>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_int4))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_int4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_v4i(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_int4) = ^(id _Nullable self, simd_int4 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<4i>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_id_v2f_v2f(PyObject* method, PyObject* self,
                                             PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, id, simd_float2, simd_float2))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0, arg1, arg2);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, id, simd_float2,
                           simd_float2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_id_v2f_v2f(PyObject*              callable,
                   PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, id, simd_float2, simd_float2) =
        ^(id _Nullable self, id arg0, simd_float2 arg1, simd_float2 arg2) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[5] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("@", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2f>", &arg1);
          if (args[3] == NULL)
              goto error;
          args[4] = pythonify_c_value("<2f>", &arg2);
          if (args[4] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 4 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 5; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_id_v2f_v2f_q(PyObject* method, PyObject* self,
                                               PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, id, simd_float2, simd_float2, long long))(
                    PyObjCIMP_GetIMP(method)))(self_obj, PyObjCIMP_GetSelector(method),
                                               arg0, arg1, arg2, arg3);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, id, simd_float2, simd_float2,
                           long long))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1, arg2, arg3);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_id_v2f_v2f_q(PyObject*              callable,
                     PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, id, simd_float2, simd_float2, long long) = ^(
        id _Nullable self, id arg0, simd_float2 arg1, simd_float2 arg2, long long arg3) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[6] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("@", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("<2f>", &arg1);
      if (args[3] == NULL)
          goto error;
      args[4] = pythonify_c_value("<2f>", &arg2);
      if (args[4] == NULL)
          goto error;
      args[5] = pythonify_c_value("q", &arg3);
      if (args[5] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             5 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 6; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 6; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_f_v2i(PyObject* method, PyObject* self,
                                        PyObject* const* arguments, size_t nargs)
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, float, simd_int2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, float, simd_int2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_f_v2i(PyObject*              callable,
              PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, float, simd_int2) =
        ^(id _Nullable self, float arg0, simd_int2 arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("f", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<2i>", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

#if PyObjC_BUILD_RELEASE >= 1011
static PyObject* _Nullable call_v_MDLAxisAlignedBoundingBox(PyObject*        method,
                                                            PyObject*        self,
                                                            PyObject* const* arguments,
                                                            size_t           nargs)
{
    struct objc_super         super;
    MDLAxisAlignedBoundingBox arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", arguments[0], &arg0)
        == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, MDLAxisAlignedBoundingBox))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, MDLAxisAlignedBoundingBox))
                     objc_msgSendSuper)(&super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static IMP
mkimp_v_MDLAxisAlignedBoundingBox(PyObject* callable, PyObjCMethodSignature* methinfo
                                  __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, MDLAxisAlignedBoundingBox) =
        ^(id _Nullable self, MDLAxisAlignedBoundingBox arg0) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[3] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", &arg0);
          if (args[2] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 3; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 3; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static PyObject* _Nullable call_v_MDLAxisAlignedBoundingBox_Z(PyObject*        method,
                                                              PyObject*        self,
                                                              PyObject* const* arguments,
                                                              size_t           nargs)
{
    struct objc_super         super;
    MDLAxisAlignedBoundingBox arg0;
    BOOL                      arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", arguments[0], &arg0)
        == -1) {
        return NULL;
    }
    if (depythonify_c_value("Z", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, MDLAxisAlignedBoundingBox, BOOL))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, MDLAxisAlignedBoundingBox,
                           BOOL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static IMP
mkimp_v_MDLAxisAlignedBoundingBox_Z(PyObject* callable, PyObjCMethodSignature* methinfo
                                    __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, MDLAxisAlignedBoundingBox, BOOL) =
        ^(id _Nullable self, MDLAxisAlignedBoundingBox arg0, BOOL arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("Z", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

static PyObject* _Nullable call_v_simd_double4x4(PyObject* method, PyObject* self,
                                                 PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double4x4    arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_double4x4=[4<4d>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double4x4))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_double4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_simd_double4x4(PyObject*              callable,
                       PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_double4x4) = ^(id _Nullable self, simd_double4x4 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("{simd_double4x4=[4<4d>]}", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_simd_double4x4_d(PyObject* method, PyObject* self,
                                                   PyObject* const* arguments,
                                                   size_t           nargs)
{
    struct objc_super super;
    simd_double4x4    arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_double4x4=[4<4d>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_double4x4, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_double4x4,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_simd_double4x4_d(PyObject*              callable,
                         PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_double4x4, double) =
        ^(id _Nullable self, simd_double4x4 arg0, double arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("{simd_double4x4=[4<4d>]}", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("d", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_simd_float2x2(PyObject* method, PyObject* self,
                                                PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float2x2     arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_float2x2=[2<2f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float2x2))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float2x2))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_simd_float2x2(PyObject*              callable,
                      PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float2x2) = ^(id _Nullable self, simd_float2x2 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("{simd_float2x2=[2<2f>]}", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_simd_float3x3(PyObject* method, PyObject* self,
                                                PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float3x3     arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_float3x3=[3<3f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float3x3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float3x3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_simd_float3x3(PyObject*              callable,
                      PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float3x3) = ^(id _Nullable self, simd_float3x3 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("{simd_float3x3=[3<3f>]}", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_simd_float4x4(PyObject* method, PyObject* self,
                                                PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float4x4     arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float4x4))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float4x4))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_simd_float4x4(PyObject*              callable,
                      PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float4x4) = ^(id _Nullable self, simd_float4x4 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("{simd_float4x4=[4<4f>]}", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_v_simd_float4x4_d(PyObject* method, PyObject* self,
                                                  PyObject* const* arguments,
                                                  size_t           nargs)
{
    struct objc_super super;
    simd_float4x4     arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_float4x4, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_float4x4,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}

static IMP
mkimp_v_simd_float4x4_d(PyObject*              callable,
                        PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_float4x4, double) =
        ^(id _Nullable self, simd_float4x4 arg0, double arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("{simd_float4x4=[4<4f>]}", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("d", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

#if PyObjC_BUILD_RELEASE >= 1013
static PyObject* _Nullable call_v_simd_quatd_d(PyObject* method, PyObject* self,
                                               PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_quatd        arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_quatd=<4d>}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_quatd, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_quatd,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static IMP
mkimp_v_simd_quatd_d(PyObject*              callable,
                     PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_quatd, double) =
        ^(id _Nullable self, simd_quatd arg0, double arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("{simd_quatd=<4d>}", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("d", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static PyObject* _Nullable call_v_simd_quatf(PyObject* method, PyObject* self,
                                             PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_quatf        arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_quatf=<4f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_quatf))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_quatf))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static IMP
mkimp_v_simd_quatf(PyObject*              callable,
                   PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_quatf) = ^(id _Nullable self, simd_quatf arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("{simd_quatf=<4f>}", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      if (result != Py_None) {
          Py_DECREF(result);
          PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                       callable);
          goto error;
      }
      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static PyObject* _Nullable call_v_simd_quatf_v3f(PyObject* method, PyObject* self,
                                                 PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_quatf        arg0;
    simd_float3       arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_quatf=<4f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("<3f>", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_quatf, simd_float3))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_quatf,
                           simd_float3))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static IMP
mkimp_v_simd_quatf_v3f(PyObject*              callable,
                       PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_quatf, simd_float3) =
        ^(id _Nullable self, simd_quatf arg0, simd_float3 arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("{simd_quatf=<4f>}", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("<3f>", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static PyObject* _Nullable call_v_simd_quatf_d(PyObject* method, PyObject* self,
                                               PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_quatf        arg0;
    double            arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_quatf=<4f>}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("d", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                ((void (*)(id, SEL, simd_quatf, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                ((void (*)(struct objc_super*, SEL, simd_quatf,
                           double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    Py_RETURN_NONE;
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static IMP
mkimp_v_simd_quatf_d(PyObject*              callable,
                     PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    void (^block)(id, simd_quatf, double) =
        ^(id _Nullable self, simd_quatf arg0, double arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("{simd_quatf=<4f>}", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("d", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          if (result != Py_None) {
              Py_DECREF(result);
              PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",
                           callable);
              goto error;
          }
          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */
#if PyObjC_BUILD_RELEASE >= 1012

static PyObject* _Nullable call_GKBox(PyObject* method, PyObject* self,
                                      PyObject* const* arguments
                                      __attribute__((__unused__)),
                                      size_t nargs)
{
    struct objc_super super;
    GKBox             rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((GKBox(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((GKBox(*)(struct objc_super*, SEL))objc_msgSendSuper_stret)(
#else
                rv = ((GKBox(*)(struct objc_super*, SEL))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{GKBox=<3f><3f>}", &rv);
}

static IMP
mkimp_GKBox(PyObject*              callable,
            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    GKBox (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      GKBox oc_result;
      if (depythonify_c_value("{GKBox=<3f><3f>}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
static PyObject* _Nullable call_GKQuad(PyObject* method, PyObject* self,
                                       PyObject* const* arguments
                                       __attribute__((__unused__)),
                                       size_t nargs)
{
    struct objc_super super;
    GKQuad            rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((GKQuad(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((GKQuad(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{GKQuad=<2f><2f>}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
static IMP
mkimp_GKQuad(PyObject*              callable,
             PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    GKQuad (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      GKQuad oc_result;
      if (depythonify_c_value("{GKQuad=<2f><2f>}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
static PyObject* _Nullable call_GKTriangle_Q(PyObject* method, PyObject* self,
                                             PyObject* const* arguments, size_t nargs)
{
    struct objc_super  super;
    GKTriangle         rv;
    unsigned long long arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("Q", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((GKTriangle(*)(id, SEL, unsigned long long))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((GKTriangle(*)(struct objc_super*, SEL,
                                     unsigned long long))objc_msgSendSuper_stret)(
#else
                rv = ((GKTriangle(*)(struct objc_super*, SEL,
                                     unsigned long long))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{GKTriangle=[3<3f>]}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
static IMP
mkimp_GKTriangle_Q(PyObject*              callable,
                   PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    GKTriangle (^block)(id, unsigned long long) =
        ^(id _Nullable self, unsigned long long arg0) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[3] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("Q", &arg0);
          if (args[2] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          GKTriangle oc_result;
          if (depythonify_c_value("{GKTriangle=[3<3f>]}", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 3; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 3; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
static PyObject* _Nullable call_MDLAxisAlignedBoundingBox(PyObject*        method,
                                                          PyObject*        self,
                                                          PyObject* const* arguments
                                                          __attribute__((__unused__)),
                                                          size_t nargs)
{
    struct objc_super         super;
    MDLAxisAlignedBoundingBox rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MDLAxisAlignedBoundingBox(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((MDLAxisAlignedBoundingBox(*)(struct objc_super*,
                                                    SEL))objc_msgSendSuper_stret)(
#else
                rv = ((MDLAxisAlignedBoundingBox(*)(struct objc_super*,
                                                    SEL))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static IMP
mkimp_MDLAxisAlignedBoundingBox(PyObject* callable, PyObjCMethodSignature* methinfo
                                __attribute__((__unused__)))
{
    Py_INCREF(callable);

    MDLAxisAlignedBoundingBox (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      MDLAxisAlignedBoundingBox oc_result;
      if (depythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", result, &oc_result)
          == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static PyObject* _Nullable call_MDLAxisAlignedBoundingBox_v4i(PyObject*        method,
                                                              PyObject*        self,
                                                              PyObject* const* arguments,
                                                              size_t           nargs)
{
    struct objc_super         super;
    MDLAxisAlignedBoundingBox rv;
    simd_int4                 arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("<4i>", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MDLAxisAlignedBoundingBox(*)(id, SEL, simd_int4))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((MDLAxisAlignedBoundingBox(*)(struct objc_super*, SEL,
                                                    simd_int4))objc_msgSendSuper_stret)(
#else
                rv = ((MDLAxisAlignedBoundingBox(*)(struct objc_super*, SEL,
                                                    simd_int4))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static IMP
mkimp_MDLAxisAlignedBoundingBox_v4i(PyObject* callable, PyObjCMethodSignature* methinfo
                                    __attribute__((__unused__)))
{
    Py_INCREF(callable);

    MDLAxisAlignedBoundingBox (^block)(id, simd_int4) = ^(id _Nullable self,
                                                          simd_int4 arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("<4i>", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      MDLAxisAlignedBoundingBox oc_result;
      if (depythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", result, &oc_result)
          == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static PyObject* _Nullable call_MDLAxisAlignedBoundingBox_d(PyObject*        method,
                                                            PyObject*        self,
                                                            PyObject* const* arguments,
                                                            size_t           nargs)
{
    struct objc_super         super;
    MDLAxisAlignedBoundingBox rv;
    double                    arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MDLAxisAlignedBoundingBox(*)(id, SEL, double))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((MDLAxisAlignedBoundingBox(*)(struct objc_super*, SEL,
                                                    double))objc_msgSendSuper_stret)(
#else
                rv = ((MDLAxisAlignedBoundingBox(*)(struct objc_super*, SEL,
                                                    double))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static IMP
mkimp_MDLAxisAlignedBoundingBox_d(PyObject* callable, PyObjCMethodSignature* methinfo
                                  __attribute__((__unused__)))
{
    Py_INCREF(callable);

    MDLAxisAlignedBoundingBox (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      MDLAxisAlignedBoundingBox oc_result;
      if (depythonify_c_value("{MDLAxisAlignedBoundingBox=<3f><3f>}", result, &oc_result)
          == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static PyObject* _Nullable call_MDLVoxelIndexExtent(PyObject* method, PyObject* self,
                                                    PyObject* const* arguments
                                                    __attribute__((__unused__)),
                                                    size_t nargs)
{
    struct objc_super   super;
    MDLVoxelIndexExtent rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MDLVoxelIndexExtent(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((MDLVoxelIndexExtent(*)(struct objc_super*,
                                              SEL))objc_msgSendSuper_stret)(
#else
                rv = ((MDLVoxelIndexExtent(*)(struct objc_super*, SEL))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{MDLVoxelIndexExtent=<4i><4i>}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
static IMP
mkimp_MDLVoxelIndexExtent(PyObject*              callable,
                          PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    MDLVoxelIndexExtent (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      MDLVoxelIndexExtent oc_result;
      if (depythonify_c_value("{MDLVoxelIndexExtent=<4i><4i>}", result, &oc_result)
          == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

static PyObject* _Nullable call_simd_double4x4(PyObject* method, PyObject* self,
                                               PyObject* const* arguments
                                               __attribute__((__unused__)),
                                               size_t nargs)
{
    struct objc_super super;
    simd_double4x4    rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_double4x4(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv =
                    ((simd_double4x4(*)(struct objc_super*, SEL))objc_msgSendSuper_stret)(
#else
                rv = ((simd_double4x4(*)(struct objc_super*, SEL))objc_msgSendSuper)(
#endif
                        &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_double4x4=[4<4d>]}", &rv);
}

static IMP
mkimp_simd_double4x4(PyObject*              callable,
                     PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_double4x4 (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_double4x4 oc_result;
      if (depythonify_c_value("{simd_double4x4=[4<4d>]}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_simd_double4x4_d(PyObject* method, PyObject* self,
                                                 PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_double4x4    rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_double4x4(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((simd_double4x4(*)(struct objc_super*, SEL,
                                         double))objc_msgSendSuper_stret)(
#else
                rv = ((
                    simd_double4x4(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_double4x4=[4<4d>]}", &rv);
}

static IMP
mkimp_simd_double4x4_d(PyObject*              callable,
                       PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_double4x4 (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_double4x4 oc_result;
      if (depythonify_c_value("{simd_double4x4=[4<4d>]}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_simd_float2x2(PyObject* method, PyObject* self,
                                              PyObject* const* arguments
                                              __attribute__((__unused__)),
                                              size_t nargs)
{
    struct objc_super super;
    simd_float2x2     rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float2x2(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_float2x2(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_float2x2=[2<2f>]}", &rv);
}

static IMP
mkimp_simd_float2x2(PyObject*              callable,
                    PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float2x2 (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float2x2 oc_result;
      if (depythonify_c_value("{simd_float2x2=[2<2f>]}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_simd_float3x3(PyObject* method, PyObject* self,
                                              PyObject* const* arguments
                                              __attribute__((__unused__)),
                                              size_t nargs)
{
    struct objc_super super;
    simd_float3x3     rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float3x3(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((simd_float3x3(*)(struct objc_super*, SEL))objc_msgSendSuper_stret)(
#else
                rv = ((simd_float3x3(*)(struct objc_super*, SEL))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_float3x3=[3<3f>]}", &rv);
}

static IMP
mkimp_simd_float3x3(PyObject*              callable,
                    PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float3x3 (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float3x3 oc_result;
      if (depythonify_c_value("{simd_float3x3=[3<3f>]}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_simd_float4x4(PyObject* method, PyObject* self,
                                              PyObject* const* arguments
                                              __attribute__((__unused__)),
                                              size_t nargs)
{
    struct objc_super super;
    simd_float4x4     rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float4x4(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((simd_float4x4(*)(struct objc_super*, SEL))objc_msgSendSuper_stret)(
#else
                rv = ((simd_float4x4(*)(struct objc_super*, SEL))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_float4x4=[4<4f>]}", &rv);
}

static IMP
mkimp_simd_float4x4(PyObject*              callable,
                    PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float4x4 (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float4x4 oc_result;
      if (depythonify_c_value("{simd_float4x4=[4<4f>]}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_simd_float4x4_id_d(PyObject* method, PyObject* self,
                                                   PyObject* const* arguments,
                                                   size_t           nargs)
{
    struct objc_super super;
    simd_float4x4     rv;
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

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float4x4(*)(id, SEL, id, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((simd_float4x4(*)(struct objc_super*, SEL, id,
                                        double))objc_msgSendSuper_stret)(
#else
                rv = ((simd_float4x4(*)(struct objc_super*, SEL, id,
                                        double))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_float4x4=[4<4f>]}", &rv);
}

static IMP
mkimp_simd_float4x4_id_d(PyObject*              callable,
                         PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float4x4 (^block)(id, id, double) = ^(id _Nullable self, id arg0, double arg1) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[4] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("@", &arg0);
      if (args[2] == NULL)
          goto error;
      args[3] = pythonify_c_value("d", &arg1);
      if (args[3] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float4x4 oc_result;
      if (depythonify_c_value("{simd_float4x4=[4<4f>]}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 4; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_simd_float4x4_d(PyObject* method, PyObject* self,
                                                PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_float4x4     rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float4x4(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((simd_float4x4(*)(struct objc_super*, SEL,
                                        double))objc_msgSendSuper_stret)(
#else
                rv = ((
                    simd_float4x4(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_float4x4=[4<4f>]}", &rv);
}

static IMP
mkimp_simd_float4x4_d(PyObject*              callable,
                      PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float4x4 (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_float4x4 oc_result;
      if (depythonify_c_value("{simd_float4x4=[4<4f>]}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

static PyObject* _Nullable call_simd_float4x4_simd_float4x4_id(PyObject*        method,
                                                               PyObject*        self,
                                                               PyObject* const* arguments,
                                                               size_t           nargs)
{
    struct objc_super super;
    simd_float4x4     rv;
    simd_float4x4     arg0;
    id                arg1;

    if (PyObjC_CheckArgCount(method, 2, 2, nargs) == -1)
        return NULL;

    if (depythonify_c_value("{simd_float4x4=[4<4f>]}", arguments[0], &arg0) == -1) {
        return NULL;
    }
    if (depythonify_c_value("@", arguments[1], &arg1) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_float4x4(*)(id, SEL, simd_float4x4, id))(PyObjCIMP_GetIMP(
                    method)))(self_obj, PyObjCIMP_GetSelector(method), arg0, arg1);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((simd_float4x4(*)(struct objc_super*, SEL, simd_float4x4,
                                        id))objc_msgSendSuper_stret)(
#else
                rv = ((simd_float4x4(*)(struct objc_super*, SEL, simd_float4x4,
                                        id))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method), arg0, arg1);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_float4x4=[4<4f>]}", &rv);
}

static IMP
mkimp_simd_float4x4_simd_float4x4_id(PyObject* callable, PyObjCMethodSignature* methinfo
                                     __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_float4x4 (^block)(id, simd_float4x4, id) =
        ^(id _Nullable self, simd_float4x4 arg0, id arg1) {
          PyGILState_STATE state = PyGILState_Ensure();

          int       cookie;
          PyObject* args[4] = {NULL};
          PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
          if (pyself == NULL) {
              goto error;
          }

          args[1] = pyself;
          args[2] = pythonify_c_value("{simd_float4x4=[4<4f>]}", &arg0);
          if (args[2] == NULL)
              goto error;
          args[3] = pythonify_c_value("@", &arg1);
          if (args[3] == NULL)
              goto error;

          PyObject* result = PyObject_Vectorcall(
              callable, args + 1, 3 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
          if (result == NULL)
              goto error;
          simd_float4x4 oc_result;
          if (depythonify_c_value("{simd_float4x4=[4<4f>]}", result, &oc_result) == -1) {
              Py_DECREF(result);
              goto error;
          }

          Py_DECREF(result);
          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }

          PyObjCObject_ReleaseTransient(pyself, cookie);
          PyGILState_Release(state);
          return oc_result;

      error:
          if (pyself) {
              PyObjCObject_ReleaseTransient(pyself, cookie);
          }

          for (size_t i = 2; i < 4; i++) {
              Py_CLEAR(args[i]);
          }
          PyObjCErr_ToObjCWithGILState(&state);
        };

    return imp_implementationWithBlock(block);
}

#if PyObjC_BUILD_RELEASE >= 1013
static PyObject* _Nullable call_simd_quatd_d(PyObject* method, PyObject* self,
                                             PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_quatd        rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_quatd(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((simd_quatd(*)(struct objc_super*, SEL,
                                     double))objc_msgSendSuper_stret)(
#else
                rv = ((simd_quatd(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_quatd=<4d>}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static IMP
mkimp_simd_quatd_d(PyObject*              callable,
                   PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_quatd (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_quatd oc_result;
      if (depythonify_c_value("{simd_quatd=<4d>}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static PyObject* _Nullable call_simd_quatf(PyObject* method, PyObject* self,
                                           PyObject* const* arguments
                                           __attribute__((__unused__)),
                                           size_t nargs)
{
    struct objc_super super;
    simd_quatf        rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_quatf(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_quatf(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_quatf=<4f>}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static IMP
mkimp_simd_quatf(PyObject*              callable,
                 PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_quatf (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_quatf oc_result;
      if (depythonify_c_value("{simd_quatf=<4f>}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static PyObject* _Nullable call_simd_quatf_d(PyObject* method, PyObject* self,
                                             PyObject* const* arguments, size_t nargs)
{
    struct objc_super super;
    simd_quatf        rv;
    double            arg0;

    if (PyObjC_CheckArgCount(method, 1, 1, nargs) == -1)
        return NULL;

    if (depythonify_c_value("d", arguments[0], &arg0) == -1) {
        return NULL;
    }

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_quatf(*)(id, SEL, double))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method), arg0);

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_quatf(*)(struct objc_super*, SEL, double))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method), arg0);
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{simd_quatf=<4f>}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static IMP
mkimp_simd_quatf_d(PyObject*              callable,
                   PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_quatf (^block)(id, double) = ^(id _Nullable self, double arg0) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[3] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;
      args[2] = pythonify_c_value("d", &arg0);
      if (args[2] == NULL)
          goto error;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             2 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_quatf oc_result;
      if (depythonify_c_value("{simd_quatf=<4f>}", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 3; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

static PyObject* _Nullable call_v16C(PyObject* method, PyObject* self,
                                     PyObject* const* arguments
                                     __attribute__((__unused__)),
                                     size_t nargs)
{
    struct objc_super super;
    simd_uchar16      rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((simd_uchar16(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

                rv = ((simd_uchar16(*)(struct objc_super*, SEL))objc_msgSendSuper)(
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("<16C>", &rv);
}

static IMP
mkimp_v16C(PyObject*              callable,
           PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    simd_uchar16 (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      simd_uchar16 oc_result;
      if (depythonify_c_value("<16C>", result, &oc_result) == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}

#if PyObjC_BUILD_RELEASE >= 1013
static PyObject* _Nullable call_MPSImageHistogramInfo(PyObject* method, PyObject* self,
                                                      PyObject* const* arguments
                                                      __attribute__((__unused__)),
                                                      size_t nargs)
{
    struct objc_super     super;
    MPSImageHistogramInfo rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MPSImageHistogramInfo(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((MPSImageHistogramInfo(*)(struct objc_super*,
                                                SEL))objc_msgSendSuper_stret)(
#else
                rv = ((
                    MPSImageHistogramInfo(*)(struct objc_super*, SEL))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{MPSImageHistogramInfo=QZ<4f><4f>}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
static IMP
mkimp_MPSImageHistogramInfo(PyObject*              callable,
                            PyObjCMethodSignature* methinfo __attribute__((__unused__)))
{
    Py_INCREF(callable);

    MPSImageHistogramInfo (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      MPSImageHistogramInfo oc_result;
      if (depythonify_c_value("{MPSImageHistogramInfo=QZ<4f><4f>}", result, &oc_result)
          == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1014
static PyObject* _Nullable call_MPSAxisAlignedBoundingBox(PyObject*        method,
                                                          PyObject*        self,
                                                          PyObject* const* arguments
                                                          __attribute__((__unused__)),
                                                          size_t nargs)
{
    struct objc_super         super;
    MPSAxisAlignedBoundingBox rv;

    if (PyObjC_CheckArgCount(method, 0, 0, nargs) == -1)
        return NULL;

    bool                   isIMP;
    id                     self_obj;
    Class                  super_class;
    int                    flags;
    PyObjCMethodSignature* methinfo;

    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,
                            &methinfo)
        == -1) {
        return NULL;
    }
    Py_BEGIN_ALLOW_THREADS
        @try {
            if (isIMP) {
                rv = ((MPSAxisAlignedBoundingBox(*)(id, SEL))(PyObjCIMP_GetIMP(method)))(
                    self_obj, PyObjCIMP_GetSelector(method));

            } else {
                super.receiver    = self_obj;
                super.super_class = super_class;

#ifdef __x86_64__
                rv = ((MPSAxisAlignedBoundingBox(*)(struct objc_super*,
                                                    SEL))objc_msgSendSuper_stret)(
#else
                rv = ((MPSAxisAlignedBoundingBox(*)(struct objc_super*,
                                                    SEL))objc_msgSendSuper)(
#endif
                    &super, PyObjCSelector_GetSelector(method));
            }

        } @catch (NSObject* localException) { // LCOV_EXCL_LINE
            PyObjCErr_FromObjC(localException);
        } // LCOV_EXCL_LINE
    Py_END_ALLOW_THREADS

    if (PyErr_Occurred()) {
        return NULL;
    }

    return pythonify_c_value("{_MPSAxisAlignedBoundingBox=<3f><3f>}", &rv);
}
#endif /* PyObjC_BUILD_RELEASE >= 1014 */

#if PyObjC_BUILD_RELEASE >= 1014
static IMP
mkimp_MPSAxisAlignedBoundingBox(PyObject* callable, PyObjCMethodSignature* methinfo
                                __attribute__((__unused__)))
{
    Py_INCREF(callable);

    MPSAxisAlignedBoundingBox (^block)(id) = ^(id _Nullable self) {
      PyGILState_STATE state = PyGILState_Ensure();

      int       cookie;
      PyObject* args[2] = {NULL};
      PyObject* pyself  = PyObjCObject_NewTransient(self, &cookie);
      if (pyself == NULL) {
          goto error;
      }

      args[1] = pyself;

      PyObject* result = PyObject_Vectorcall(callable, args + 1,
                                             1 | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);
      if (result == NULL)
          goto error;
      MPSAxisAlignedBoundingBox oc_result;
      if (depythonify_c_value("{_MPSAxisAlignedBoundingBox=<3f><3f>}", result, &oc_result)
          == -1) {
          Py_DECREF(result);
          goto error;
      }

      Py_DECREF(result);
      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }

      PyObjCObject_ReleaseTransient(pyself, cookie);
      PyGILState_Release(state);
      return oc_result;

  error:
      if (pyself) {
          PyObjCObject_ReleaseTransient(pyself, cookie);
      }

      for (size_t i = 2; i < 2; i++) {
          Py_CLEAR(args[i]);
      }
      PyObjCErr_ToObjCWithGILState(&state);
    };

    return imp_implementationWithBlock(block);
}
#endif /* PyObjC_BUILD_RELEASE >= 1014 */

int
PyObjC_setup_simd(PyObject* module __attribute__((__unused__)))
{

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2d>@:", call_v2d, mkimp_v2d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2d>@:d", call_v2d_d, mkimp_v2d_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2f>@:", call_v2f, mkimp_v2f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2f>@:Q", call_v2f_Q, mkimp_v2f_Q)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2f>@:d", call_v2f_d, mkimp_v2f_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2f>@:q", call_v2f_q, mkimp_v2f_q)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<2i>@:", call_v2i, mkimp_v2i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3d>@:d", call_v3d_d, mkimp_v3d_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:", call_v3f, mkimp_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:<2i><2i>", call_v3f_v2i_v2i, mkimp_v3f_v2i_v2i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:<3f>", call_v3f_v3f, mkimp_v3f_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:<3f>@", call_v3f_v3f_id, mkimp_v3f_v3f_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:<4i>", call_v3f_v4i, mkimp_v3f_v4i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:Q", call_v3f_Q, mkimp_v3f_Q)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<3f>@:d", call_v3f_d, mkimp_v3f_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<4d>@:d", call_v4d_d, mkimp_v4d_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<4f>@:", call_v4f, mkimp_v4f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<4f>@:d", call_v4f_d, mkimp_v4f_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<4i>@:<3f>", call_v4i_v3f, mkimp_v4i_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2d>@", call_id_v2d_id, mkimp_id_v2d_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2d>q", call_id_v2d_q, mkimp_id_v2d_q)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2f>", call_id_v2f, mkimp_id_v2f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2f><2I>q@", call_id_v2f_v2I_q_id, mkimp_id_v2f_v2I_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2f><2f>", call_id_v2f_v2f, mkimp_id_v2f_v2f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2i>", call_id_v2i, mkimp_id_v2i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2i>iiZ", call_id_v2i_i_i_Z, mkimp_id_v2i_i_i_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2i>iiB", call_id_v2i_i_i_Z, mkimp_id_v2i_i_i_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2i>iiZ#", call_id_v2i_i_i_Z_Class, mkimp_id_v2i_i_i_Z_Class)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<2i>iiB#", call_id_v2i_i_i_Z_Class, mkimp_id_v2i_i_i_Z_Class)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f>", call_id_v3f, mkimp_id_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>ZZZq@", call_id_v3f_v2I_Z_Z_Z_q_id, mkimp_id_v3f_v2I_Z_Z_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>BBBq@", call_id_v3f_v2I_Z_Z_Z_q_id, mkimp_id_v3f_v2I_Z_Z_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>ZZq@", call_id_v3f_v2I_Z_Z_q_id, mkimp_id_v3f_v2I_Z_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>BBq@", call_id_v3f_v2I_Z_Z_q_id, mkimp_id_v3f_v2I_Z_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>Zq@", call_id_v3f_v2I_Z_q_id, mkimp_id_v3f_v2I_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>Bq@", call_id_v3f_v2I_Z_q_id, mkimp_id_v3f_v2I_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>iZq@", call_id_v3f_v2I_i_Z_q_id, mkimp_id_v3f_v2I_i_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>iBq@", call_id_v3f_v2I_i_Z_q_id, mkimp_id_v3f_v2I_i_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><2I>q@", call_id_v3f_v2I_q_id, mkimp_id_v3f_v2I_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><3I>Zq@", call_id_v3f_v3I_Z_q_id, mkimp_id_v3f_v3I_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><3I>Bq@", call_id_v3f_v3I_Z_q_id, mkimp_id_v3f_v3I_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><3I>qZ@", call_id_v3f_v3I_q_Z_id, mkimp_id_v3f_v3I_q_Z_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f><3I>qB@", call_id_v3f_v3I_q_Z_id, mkimp_id_v3f_v3I_q_Z_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f>QQqZZ@", call_id_v3f_Q_Q_q_Z_Z_id, mkimp_id_v3f_Q_Q_q_Z_Z_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f>QQqBB@", call_id_v3f_Q_Q_q_Z_Z_id, mkimp_id_v3f_Q_Q_q_Z_Z_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f>Zq@", call_id_v3f_Z_q_id, mkimp_id_v3f_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<3f>Bq@", call_id_v3f_Z_q_id, mkimp_id_v3f_Z_q_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:<4f>", call_id_v4f, mkimp_id_v4f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@<2d><2d><2i>Z", call_id_id_v2d_v2d_v2i_Z, mkimp_id_id_v2d_v2d_v2i_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@<2d><2d><2i>B", call_id_id_v2d_v2d_v2i_Z, mkimp_id_id_v2d_v2d_v2i_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@<2f>", call_id_id_v2f, mkimp_id_id_v2f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@<3f>", call_id_id_v3f, mkimp_id_id_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@<4f>", call_id_id_v4f, mkimp_id_id_v4f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@@<2i>", call_id_id_id_v2i, mkimp_id_id_id_v2i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@@<2i>f", call_id_id_id_v2i_f, mkimp_id_id_id_v2i_f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@Q<2f>", call_id_id_Q_v2f, mkimp_id_id_Q_v2f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@Q<3f>", call_id_id_Q_v3f, mkimp_id_id_Q_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@Q<4f>", call_id_id_Q_v4f, mkimp_id_id_Q_v4f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@Q{simd_float4x4=[4<4f>]}", call_id_id_Q_simd_float4x4,
            mkimp_id_id_Q_simd_float4x4)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@Z@<2i>qQqZ", call_id_id_Z_id_v2i_q_Q_q_Z, mkimp_id_id_Z_id_v2i_q_Q_q_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@B@<2i>qQqB", call_id_id_Z_id_v2i_q_Q_q_Z, mkimp_id_id_Z_id_v2i_q_Q_q_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@q<2i>ffff", call_id_id_q_v2i_f_f_f_f, mkimp_id_id_q_v2i_f_f_f_f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@q<2i>fffff", call_id_id_q_v2i_f_f_f_f_f, mkimp_id_id_q_v2i_f_f_f_f_f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#if PyObjC_BUILD_RELEASE >= 1012

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{GKBox=<3f><3f>}", call_id_id_GKBox, mkimp_id_id_GKBox)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{GKQuad=<2f><2f>}", call_id_id_GKQuad, mkimp_id_id_GKQuad)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{MDLAxisAlignedBoundingBox=<3f><3f>}f",
            call_id_id_MDLAxisAlignedBoundingBox_f,
            mkimp_id_id_MDLAxisAlignedBoundingBox_f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{simd_float2x2=[2<2f>]}", call_id_id_simd_float2x2,
            mkimp_id_id_simd_float2x2)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{simd_float3x3=[3<3f>]}", call_id_id_simd_float3x3,
            mkimp_id_id_simd_float3x3)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{simd_float4x4=[4<4f>]}", call_id_id_simd_float4x4,
            mkimp_id_id_simd_float4x4)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{simd_quatf=<4f>}", call_id_id_simd_quatf, mkimp_id_id_simd_quatf)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:@{simd_quatf=<4f>}@", call_id_id_simd_quatf_id, mkimp_id_id_simd_quatf_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:^{CGColor=}^{CGColor=}@<2i>", call_id_CGColor_CGColor_id_v2i,
            mkimp_id_CGColor_CGColor_id_v2i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f><2f>", call_id_f_v2f_v2f, mkimp_id_f_v2f_v2f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f><2f>#", call_id_f_v2f_v2f_Class, mkimp_id_f_v2f_v2f_Class)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f>QQQqZ@", call_id_f_v2f_Q_Q_Q_q_Z_id, mkimp_id_f_v2f_Q_Q_Q_q_Z_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f>QQQqB@", call_id_f_v2f_Q_Q_Q_q_Z_id, mkimp_id_f_v2f_Q_Q_Q_q_Z_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f>QQqZ@", call_id_f_v2f_Q_Q_q_Z_id, mkimp_id_f_v2f_Q_Q_q_Z_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f<2f>QQqB@", call_id_f_v2f_Q_Q_q_Z_id, mkimp_id_f_v2f_Q_Q_q_Z_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f@<2i>iqZ", call_id_f_id_v2i_i_q_Z, mkimp_id_f_id_v2i_i_q_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f@<2i>iqB", call_id_f_id_v2i_i_q_Z, mkimp_id_f_id_v2i_i_q_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f@<2i>iq^{CGColor=}^{CGColor=}", call_id_f_id_v2i_i_q_CGColor_CGColor,
            mkimp_id_f_id_v2i_i_q_CGColor_CGColor)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:f@<2i>q", call_id_f_id_v2i_q, mkimp_id_f_id_v2i_q)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:ff@<2i>", call_id_f_f_id_v2i, mkimp_id_f_f_id_v2i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#if PyObjC_BUILD_RELEASE >= 1012

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{GKBox=<3f><3f>}", call_id_GKBox, mkimp_id_GKBox)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1012 */
#if PyObjC_BUILD_RELEASE >= 1012

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{GKBox=<3f><3f>}f", call_id_GKBox_f, mkimp_id_GKBox_f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{GKQuad=<2f><2f>}", call_id_GKQuad, mkimp_id_GKQuad)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{GKQuad=<2f><2f>}f", call_id_GKQuad_f, mkimp_id_GKQuad_f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{MDLVoxelIndexExtent=<4i><4i>}", call_id_MDLVoxelIndexExtent,
            mkimp_id_MDLVoxelIndexExtent)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{simd_float4x4=[4<4f>]}", call_id_simd_float4x4, mkimp_id_simd_float4x4)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{simd_float4x4=[4<4f>]}Z", call_id_simd_float4x4_Z,
            mkimp_id_simd_float4x4_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "@@:{simd_float4x4=[4<4f>]}B", call_id_simd_float4x4_Z,
            mkimp_id_simd_float4x4_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "Z@:<2i>@@@@", call_Z_v2i_id_id_id_id, mkimp_Z_v2i_id_id_id_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "B@:<2i>@@@@", call_Z_v2i_id_id_id_id, mkimp_Z_v2i_id_id_id_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "Z@:<2i>qf@@@", call_Z_v2i_q_f_id_id_id, mkimp_Z_v2i_q_f_id_id_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "B@:<2i>qf@@@", call_Z_v2i_q_f_id_id_id, mkimp_Z_v2i_q_f_id_id_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "Z@:<4i>ZZZZ", call_Z_v4i_Z_Z_Z_Z, mkimp_Z_v4i_Z_Z_Z_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "B@:<4i>BBBB", call_Z_v4i_Z_Z_Z_Z, mkimp_Z_v4i_Z_Z_Z_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "^{CGColor=}@:<3f>", call_CGColor_v3f, mkimp_CGColor_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "^{CGColor=}@:<3f>^{CGColorSpace=}", call_CGColor_v3f_CGColorSpace,
            mkimp_CGColor_v3f_CGColorSpace)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "f@:<2f>", call_f_v2f, mkimp_f_v2f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "f@:<2i>", call_f_v2i, mkimp_f_v2i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<2d>", call_v_v2d, mkimp_v_v2d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<2d>d", call_v_v2d_d, mkimp_v_v2d_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<2f>", call_v_v2f, mkimp_v_v2f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<2f>d", call_v_v2f_d, mkimp_v_v2f_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3d>", call_v_v3d, mkimp_v_v3d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3d>d", call_v_v3d_d, mkimp_v_v3d_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3f>", call_v_v3f, mkimp_v_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3f><3f>", call_v_v3f_v3f, mkimp_v_v3f_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3f><3f><3f>", call_v_v3f_v3f_v3f, mkimp_v_v3f_v3f_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<3f>d", call_v_v3f_d, mkimp_v_v3f_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<4d>d", call_v_v4d_d, mkimp_v_v4d_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<4f>", call_v_v4f, mkimp_v_v4f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<4f>d", call_v_v4f_d, mkimp_v_v4f_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:<4i>", call_v_v4i, mkimp_v_v4i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:@<2f><2f>", call_v_id_v2f_v2f, mkimp_v_id_v2f_v2f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:@<2f><2f>q", call_v_id_v2f_v2f_q, mkimp_v_id_v2f_v2f_q)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:f<2i>", call_v_f_v2i, mkimp_v_f_v2i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

#if PyObjC_BUILD_RELEASE >= 1011
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{MDLAxisAlignedBoundingBox=<3f><3f>}", call_v_MDLAxisAlignedBoundingBox,
            mkimp_v_MDLAxisAlignedBoundingBox)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{MDLAxisAlignedBoundingBox=<3f><3f>}Z",
            call_v_MDLAxisAlignedBoundingBox_Z, mkimp_v_MDLAxisAlignedBoundingBox_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{MDLAxisAlignedBoundingBox=<3f><3f>}B",
            call_v_MDLAxisAlignedBoundingBox_Z, mkimp_v_MDLAxisAlignedBoundingBox_Z)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{simd_double4x4=[4<4d>]}", call_v_simd_double4x4, mkimp_v_simd_double4x4)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{simd_double4x4=[4<4d>]}d", call_v_simd_double4x4_d,
            mkimp_v_simd_double4x4_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{simd_float2x2=[2<2f>]}", call_v_simd_float2x2, mkimp_v_simd_float2x2)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{simd_float3x3=[3<3f>]}", call_v_simd_float3x3, mkimp_v_simd_float3x3)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{simd_float4x4=[4<4f>]}", call_v_simd_float4x4, mkimp_v_simd_float4x4)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{simd_float4x4=[4<4f>]}d", call_v_simd_float4x4_d,
            mkimp_v_simd_float4x4_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{simd_quatd=<4d>}d", call_v_simd_quatd_d, mkimp_v_simd_quatd_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{simd_quatf=<4f>}", call_v_simd_quatf, mkimp_v_simd_quatf)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{simd_quatf=<4f>}<3f>", call_v_simd_quatf_v3f, mkimp_v_simd_quatf_v3f)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "v@:{simd_quatf=<4f>}d", call_v_simd_quatf_d, mkimp_v_simd_quatf_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */
#if PyObjC_BUILD_RELEASE >= 1012

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{GKBox=<3f><3f>}@:", call_GKBox, mkimp_GKBox)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{GKQuad=<2f><2f>}@:", call_GKQuad, mkimp_GKQuad)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1012
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{GKTriangle=[3<3f>]}@:Q", call_GKTriangle_Q, mkimp_GKTriangle_Q)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1012 */

#if PyObjC_BUILD_RELEASE >= 1011
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{MDLAxisAlignedBoundingBox=<3f><3f>}@:", call_MDLAxisAlignedBoundingBox,
            mkimp_MDLAxisAlignedBoundingBox)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{MDLAxisAlignedBoundingBox=<3f><3f>}@:<4i>",
            call_MDLAxisAlignedBoundingBox_v4i, mkimp_MDLAxisAlignedBoundingBox_v4i)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{MDLAxisAlignedBoundingBox=<3f><3f>}@:d", call_MDLAxisAlignedBoundingBox_d,
            mkimp_MDLAxisAlignedBoundingBox_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

#if PyObjC_BUILD_RELEASE >= 1011
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{MDLVoxelIndexExtent=<4i><4i>}@:", call_MDLVoxelIndexExtent,
            mkimp_MDLVoxelIndexExtent)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1011 */

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_double4x4=[4<4d>]}@:", call_simd_double4x4, mkimp_simd_double4x4)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_double4x4=[4<4d>]}@:d", call_simd_double4x4_d, mkimp_simd_double4x4_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_float2x2=[2<2f>]}@:", call_simd_float2x2, mkimp_simd_float2x2)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_float3x3=[3<3f>]}@:", call_simd_float3x3, mkimp_simd_float3x3)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_float4x4=[4<4f>]}@:", call_simd_float4x4, mkimp_simd_float4x4)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_float4x4=[4<4f>]}@:@d", call_simd_float4x4_id_d,
            mkimp_simd_float4x4_id_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_float4x4=[4<4f>]}@:d", call_simd_float4x4_d, mkimp_simd_float4x4_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_float4x4=[4<4f>]}@:{simd_float4x4=[4<4f>]}@",
            call_simd_float4x4_simd_float4x4_id, mkimp_simd_float4x4_simd_float4x4_id)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_quatd=<4d>}@:d", call_simd_quatd_d, mkimp_simd_quatd_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_quatf=<4f>}@:", call_simd_quatf, mkimp_simd_quatf)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{simd_quatf=<4f>}@:d", call_simd_quatf_d, mkimp_simd_quatf_d)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "<16C>@:", call_v16C, mkimp_v16C)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{MPSImageHistogramInfo=QZ<4f><4f>}@:", call_MPSImageHistogramInfo,
            mkimp_MPSImageHistogramInfo)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1013
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{MPSImageHistogramInfo=QB<4f><4f>}@:", call_MPSImageHistogramInfo,
            mkimp_MPSImageHistogramInfo)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1013 */

#if PyObjC_BUILD_RELEASE >= 1014
    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE
            "{_MPSAxisAlignedBoundingBox=<3f><3f>}@:", call_MPSAxisAlignedBoundingBox,
            mkimp_MPSAxisAlignedBoundingBox)
        == -1) {
        return -1; // LCOV_EXCL_LINE
    }
#endif /* PyObjC_BUILD_RELEASE >= 1014 */

    return 0;
}
NS_ASSUME_NONNULL_END
