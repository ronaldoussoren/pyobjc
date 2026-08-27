#!/ usr / bin / env python3
"""
Helper script for generating support code for vector types,
including testcases and the supporting extension for that.

The code currently is fairly gross, but works.

XXX:
- Add support for byref arguments
- Generate TEST2_FILE
"""

import objc
import Quartz  # noqa: F401
from objc import simd
import typing
import pathlib
from objc._callable_docstr import describe_type as _describe_type

HELPER_FILE = (
    pathlib.Path(__file__).resolve().parent.parent / "Modules/objc/helpers-vector.m"
)
TESTEXT_FILE = (
    pathlib.Path(__file__).resolve().parent.parent / "Modules/objc/test/vectorcall.m"
)
TEST_FILE = (
    pathlib.Path(__file__).resolve().parent.parent / "PyObjCTest/test_vectorcall.py"
)

HELPER2_FILE = (
    pathlib.Path(__file__).resolve().parent.parent / "Modules/objc/helpers-function.m"
)
TESTEXT2_FILE = (
    pathlib.Path(__file__).resolve().parent.parent
    / "Modules/objc/test/vectorfunccall.m"
)
TEST2_FILE = (
    pathlib.Path(__file__).resolve().parent.parent / "PyObjCTest/test_vectorfunccall.py"
)

CALL_PREFIX = "call"
MKIMP_PREFIX = "mkimp"

# XXX : The 'grep' command should be integrated into this script(but written in Python)
# grep full_signature ../*/Lib/**/_metadata.py                                             \
#    | sed 's@.*full_signature.: \([^ ]*\).*@\1@' | sort -u
#
# XXX : The list below is censored, actually running the grep command will find a number of
# "pointer to" arguments which I've stripped for now.


def describe_type(value):
    return _describe_type(value).split(".")[-1]


def needs_wrapper(signature):
    for tp in objc.splitSignature(signature):
        if tp.startswith(objc._C_VECTOR_B):
            return True
        elif tp.startswith(objc._C_STRUCT_B):
            _, fields = objc.splitStructSignature(tp)
            for _, f in fields:
                if needs_wrapper(f):
                    return True
                elif f.startswith(objc._C_ARY_B):
                    f = f[1:-1]
                    while f[:1].isdigit():
                        f = f[1:]
                    if needs_wrapper(f):
                        return True
    return False


METH_SIGNATURES = [
    b"<16C>@:",
    b"<2d>@:",
    b"<2d>@:d",
    b"<2f>@:",
    b"<2f>@:Q",
    b"<2f>@:d",
    b"<2f>@:q",
    b"<2i>@:",
    b"<3d>@:d",
    b"<3f>@:",
    b"<3f>@:<2i><2i>",
    b"<3f>@:<3f>",
    b"<3f>@:<3f>@",
    b"<3f>@:<4i>",
    b"<3f>@:Q",
    b"<3f>@:d",
    b"<4d>@:d",
    b"<4f>@:",
    b"<4f>@:d",
    b"<4i>@:<3f>",
    b"@@:<2d>@",
    b"@@:<2d>q",
    b"@@:<2f>",
    b"@@:<2f><2I>q@",
    b"@@:<2f><2f>",
    b"@@:<2i>",
    b"@@:<2i>iiZ",
    b"@@:<2i>iiZ#",
    b"@@:<3f>",
    b"@@:<3f><2I>ZZZq@",
    b"@@:<3f><2I>ZZq@",
    b"@@:<3f><2I>Zq@",
    b"@@:<3f><2I>iZq@",
    b"@@:<3f><2I>q@",
    b"@@:<3f><3I>Zq@",
    b"@@:<3f><3I>qZ@",
    b"@@:<3f>QQqZZ@",
    b"@@:<3f>Zq@",
    b"@@:<4f>",
    b"@@:@<2d><2d><2i>Z",
    b"@@:@<2f>",
    b"@@:@<3f>",
    b"@@:@<4f>",
    b"@@:@@<2i>",
    b"@@:@@<2i>f",
    b"@@:@Q<2f>",
    b"@@:@Q<3f>",
    b"@@:@Q<4f>",
    b"@@:@Q{simd_float4x4=[4<4f>]}",
    b"@@:@Z@<2i>qQqZ",
    b"@@:@^{CGColorConversionInfo=}@^{MPSFunctions_AABB=<4f><4f>}Q^@",
    b"@@:@^{CGColorSpace=}^{CGColorSpace=}@^{MPSFunctions_AABB=<4f><4f>}Q^@",
    b"@@:@^{MPSImageHistogramInfo=QZ<4f><4f>}",
    b"@@:@q<2i>ffff",
    b"@@:@q<2i>fffff",
    b"@@:@{GKBox=<3f><3f>}",
    b"@@:@{GKQuad=<2f><2f>}",
    b"@@:@{MDLAxisAlignedBoundingBox=<3f><3f>}f",
    b"@@:@{simd_float2x2=[2<2f>]}",
    b"@@:@{simd_float3x3=[3<3f>]}",
    b"@@:@{simd_float4x4=[4<4f>]}",
    b"@@:@{simd_quatf=<4f>}",
    b"@@:@{simd_quatf=<4f>}@",
    b"@@:^<2f>",
    b"@@:^<2f>Q",
    b"@@:^<2f>QfZ",
    b"@@:^<2f>q^@",
    b"@@:^<3f>QfZ",
    b"@@:^{CGColor=}^{CGColor=}@<2i>",
    b"@@:f<2f><2f>",
    b"@@:f<2f><2f>#",
    b"@@:f<2f>QQQqZ@",
    b"@@:f<2f>QQqZ@",
    b"@@:f@<2i>iqZ",
    b"@@:f@<2i>iq^{CGColor=}^{CGColor=}",
    b"@@:f@<2i>q",
    b"@@:ff@<2i>",
    b"@@:qq^<2f>^<2f>",
    b"@@:{GKBox=<3f><3f>}",
    b"@@:{GKBox=<3f><3f>}f",
    b"@@:{GKQuad=<2f><2f>}",
    b"@@:{GKQuad=<2f><2f>}f",
    b"@@:{MDLVoxelIndexExtent=<4i><4i>}",
    b"@@:{simd_float4x4=[4<4f>]}",
    b"@@:{simd_float4x4=[4<4f>]}Z",
    b"Q@:^<2d>Q",
    b"Q@:^<2f>Q",
    b"Q@:^<3d>Q",
    b"Q@:^<3d>Qd",
    b"Q@:^<3f>Q",
    b"Q@:^<3f>Qd",
    b"Q@:^<4d>Q",
    b"Q@:^<4f>Q",
    b"Q@:^{simd_double4x4=[4<4d>]}Q",
    b"Q@:^{simd_float4x4=[4<4f>]}Q",
    b"Q@:^{simd_quatd=<4d>}Q",
    b"Q@:^{simd_quatd=<4d>}Qd",
    b"Q@:^{simd_quatf=<4f>}Q",
    b"Q@:^{simd_quatf=<4f>}Qd",
    b"Z@:<2i>@@@@",
    b"Z@:<2i>qf@@@",
    b"Z@:<4i>ZZZZ",
    b"Z@:^{simd_float4x4=[4<4f>]}@^@",
    b"^<2f>@:",
    b"^{CGColor=}@:<3f>",
    b"^{CGColor=}@:<3f>^{CGColorSpace=}",
    b"f@:<2f>",
    b"f@:<2i>",
    b"v@:<2d>",
    b"v@:<2d>d",
    b"v@:<2f>",
    b"v@:<2f>d",
    b"v@:<3d>",
    b"v@:<3d>d",
    b"v@:<3f>",
    b"v@:<3f><3f>",
    b"v@:<3f><3f><3f>",
    b"v@:<3f>d",
    b"v@:<4d>d",
    b"v@:<4f>",
    b"v@:<4f>d",
    b"v@:<4i>",
    b"v@:@<2f><2f>",
    b"v@:@<2f><2f>q",
    b"v@:^<2d>^dQ",
    b"v@:^<2f>^dQ",
    b"v@:^<3d>Q^dQ",
    b"v@:^<3d>Qd",
    b"v@:^<3d>^dQ",
    b"v@:^<3f>Q^dQ",
    b"v@:^<3f>Qd",
    b"v@:^<3f>^dQ",
    b"v@:^<4d>^dQ",
    b"v@:^<4f>^dQ",
    b"v@:^{simd_double4x4=[4<4d>]}Q",
    b"v@:^{simd_double4x4=[4<4d>]}^dQ",
    b"v@:^{simd_float4x4=[4<4f>]}Q",
    b"v@:^{simd_float4x4=[4<4f>]}^dQ",
    b"v@:^{simd_quatd=<4d>}Q^dQ",
    b"v@:^{simd_quatd=<4d>}Qd",
    b"v@:^{simd_quatd=<4d>}^dQ",
    b"v@:^{simd_quatf=<4f>}Q^dQ",
    b"v@:^{simd_quatf=<4f>}Qd",
    b"v@:^{simd_quatf=<4f>}^dQ",
    b"v@:f<2i>",
    b"v@:{MDLAxisAlignedBoundingBox=<3f><3f>}",
    b"v@:{MDLAxisAlignedBoundingBox=<3f><3f>}Z",
    b"v@:{simd_double4x4=[4<4d>]}",
    b"v@:{simd_double4x4=[4<4d>]}d",
    b"v@:{simd_float2x2=[2<2f>]}",
    b"v@:{simd_float3x3=[3<3f>]}",
    b"v@:{simd_float4x4=[4<4f>]}",
    b"v@:{simd_float4x4=[4<4f>]}d",
    b"v@:{simd_quatd=<4d>}d",
    b"v@:{simd_quatf=<4f>}",
    b"v@:{simd_quatf=<4f>}<3f>",
    b"v@:{simd_quatf=<4f>}d",
    b"{GKBox=<3f><3f>}@:",
    b"{GKQuad=<2f><2f>}@:",
    b"{GKTriangle=[3<3f>]}@:Q",
    b"{MDLAxisAlignedBoundingBox=<3f><3f>}@:",
    b"{MDLAxisAlignedBoundingBox=<3f><3f>}@:<4i>",
    b"{MDLAxisAlignedBoundingBox=<3f><3f>}@:d",
    b"{MDLVoxelIndexExtent=<4i><4i>}@:",
    b"{MPSFunctions_AABB=<4f><4f>}@:{MPSFunctions_AABB=<4f><4f>}",
    b"{MPSImageHistogramInfo=QZ<4f><4f>}@:",
    b"{_MPSAxisAlignedBoundingBox=<3f><3f>}@:",
    b"{simd_double4x4=[4<4d>]}@:",
    b"{simd_double4x4=[4<4d>]}@:d",
    b"{simd_float2x2=[2<2f>]}@:",
    b"{simd_float3x3=[3<3f>]}@:",
    b"{simd_float4x3=[4<3f>]}@:",
    b"{simd_float4x4=[4<4f>]}@:",
    b"{simd_float4x4=[4<4f>]}@:@d",
    b"{simd_float4x4=[4<4f>]}@:d",
    b"{simd_float4x4=[4<4f>]}@:{simd_float4x4=[4<4f>]}@",
    b"{simd_quatd=<4d>}@:d",
    b"{simd_quatf=<4f>}@:",
    b"{simd_quatf=<4f>}@:d",
]
METH_SIGNATURES = [item for item in METH_SIGNATURES if needs_wrapper(item)]


# XXX: Extract this from compiled metadata files
FUNC_SIGNATURES = [
    b"<3f>@",
    b"@{simd_float4x4=[4<4f>]}",
    b"@{simd_float4x4=[4<4f>]}ffq",
    b"B@<3f>",
    b"{simd_float3x3=[3<3f>]}@",
    b"{simd_float4x4=[4<4f>]}@",
    # XXX: byref
    # b"{simd_float4x4=[4<4f>]}@^tq",
    b"{simd_float4x4=[4<4f>]}@q",
    b"{CGPoint=dd}<2f>{CGRect={CGPoint=dd}{CGSize=dd}}QQ",
    b"<3f>{SCNVector3=ddd}",
    b"{SCNVector3=ddd}<3f>",
    b"<4f>{SCNVector4=dddd}",
    b"{SCNVector4=dddd}<4f>",
    b"{simd_float4x4=[4<4f>]}{CATransform3D=dddddddddddddddd}",
    b"{CATransform3D=dddddddddddddddd}{simd_float4x4=[4<4f>]}",
    b"{simd_float4x4=[4<4f>]}^{cp_frame=}C<4f><2f>",
    b"{simd_float4x4=[4<4f>]}^{cp_drawable=}CQ",
    b"<4f>^{cp_view=}",
    b"{simd_float4x4=[4<4f>]}^{cp_frame=}IC<4f><2f>",
    b"v^{cp_drawable=}<2f>",
    b"<2f>^{cp_drawable=}",
]
FUNC_SIGNATURES = [item for item in FUNC_SIGNATURES if needs_wrapper(item)]

HELPER_PREFIX = """\
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

static inline int
extract_method_info(PyObject* method, PyObject* self, bool* isIMP, id _Nonnull* self_obj,
                    Class _Nonnull* super_class, int* flags, PyObjCMethodSignature** methinfo)
{
    assert(PyObjCNativeSelector_Check(method) || PyObjCIMP_Check(method));

    *isIMP = !!PyObjCIMP_Check(method);

    if (*isIMP) {
        *flags    = PyObjCIMP_GetFlags(method);
        *methinfo = (PyObjCMethodSignature* _Nonnull)PyObjCIMP_GetSignature(method);
    } else {
        *flags    = PyObjCSelector_GetFlags(method);
        *methinfo = PyObjCSelector_GetMetadata(method);
    }

    if ((*flags) & PyObjCSelector_kCLASS_METHOD) {
        if (PyObjCObject_Check(self)) {
            *self_obj = PyObjCObject_GetObject(self);
            if (*self_obj == nil && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                return -1;                              // LCOV_EXCL_LINE
            }
            if (*self_obj != (id _Nonnull)NULL) { // LCOV_BR_EXCL_LINE
                /* object_getClass never returns Nil for non-nil objects */
                *self_obj = (id _Nonnull)object_getClass(*self_obj); // LCOV_EXCL_LINE
            }

        } else if (PyObjCClass_Check(self)) {
            /* PyObjCClass_GetClass only returns Nil on internal errors */
            *self_obj = (Class _Nonnull)PyObjCClass_GetClass(self);
            if (*self_obj == nil && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                return -1;                              // LCOV_EXCL_LINE
            } // LCOV_EXCL_LINE

        } else if (PyType_Check(self) // LCOV_BR_EXCL_LINE
                   && PyType_IsSubtype((PyTypeObject*)self, &PyType_Type)) {
            PyObject* c = PyObjCClass_ClassForMetaClass(self);
            if (c == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                *self_obj = (Class _Nonnull)nil;
                PyErr_Format(
                    PyExc_TypeError,
                    "Need Objective-C object or class as self, not an instance of '%s'",
                    Py_TYPE(self)->tp_name);
                return -1;
                // LCOV_EXCL_STOP

            } else { // LCOV_BR_EXCL_LINE
                *self_obj = PyObjCClass_GetClass(c);
                if (*self_obj == nil && PyErr_Occurred()) { // LCOV_BR_EXCL_LINE
                    return -1;                              // LCOV_EXCL_LINE
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
            /* PyObjCObject_GetObject only returns NULL if 'self' is not an objc_object,
             * which cannot happen here.
             */
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
        /* _Nonnull is safe because of the IMP path doesn't use the super class */
        *super_class = (Class _Nonnull)Nil;
    } else {
        if ((*flags) & PyObjCSelector_kCLASS_METHOD) {
            /* _Nonnull is safe because object_getClass will only return Nil when the
             * class itself is Nil */
            *super_class =
                (Class _Nonnull)object_getClass(PyObjCSelector_GetClass(method));
        } else {
            *super_class = (Class _Nonnull)PyObjCSelector_GetClass(method);
        }
    }

    if (*self_obj != nil && (*methinfo != NULL) && (*methinfo)->initializer) {
        /* the called method will steal a reference to self */
        [*self_obj retain];
    }

    assert(*self_obj != nil);
    assert(*methinfo != NULL);
    assert(*isIMP || (*super_class != Nil));

    return 0;
}

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

    if (methinfo->initializer) {
        /* method returns +1 without being annotated as such */
        [retval release];
    }
    return result;
}

"""

HELPER2_PREFIX = """\
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

    assert (!methinfo->initializer);

    return result;
}

"""

TESTEXT_PREFIX = """\
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

/* Compositor services pointer types */
typedef void cp_drawable;
typedef void cp_frame;
typedef void cp_view;

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
    if (self == nil) { // LCOV_BR_EXCL_LINE
        return nil; // LCOV_EXCL_LINE
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

        Py_CLEAR(values);
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
"""

TESTEXT_MID = """\
@end

    @interface OC_VectorCallInvoke : NSObject {
}
@end

@implementation OC_VectorCallInvoke

"""

TESTEXT_SUFFIX = """\
@end

    static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    if (PyModule_AddObject(m, "OC_VectorCall", PyObjC_IdToPython([OC_VectorCall class]))
        < 0) {
        return -1;
    }
    if (PyModule_AddObject(m, "OC_VectorCallInvoke",
                           PyObjC_IdToPython([OC_VectorCallInvoke class]))
        < 0) {
        return -1;
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
    .m_name     = "vectorcall",
    .m_doc      = NULL,
    .m_size     = 0,
    .m_methods  = mod_methods,
    .m_slots    = mod_slots,
    .m_traverse = NULL,
    .m_clear    = NULL,
    .m_free     = NULL,
};

PyObject* PyInit_vectorcall(void);

PyObject* __attribute__((__visibility__("default"))) _Nullable PyInit_vectorcall(void)
{
    return PyModuleDef_Init(&mod_module);
}
"""

TESTEXT2_PREFIX = """\
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

/* Compositor services pointer types */
typedef void cp_drawable;
typedef void cp_frame;
typedef void cp_view;

static PyObject* values   = NULL;
static BOOL      shouldRaise = NO;

static BOOL f_shouldRaise(void)
{
    return shouldRaise;
}

static void f_clearRaise(void)
{
    shouldRaise = NO;
}

static void f_setRaise(void)
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

"""

TESTEXT2_MID = """\
typedef void (*F)(void);
static struct function {
    char* name;
    F     function;
} gFunctionMap[] = {
    {"shouldRaise", (F)f_shouldRaise},
    {"clearRaise", (F)f_clearRaise},
    {"setRaise", (F)f_setRaise},
    {"storedvalue", (F)f_storedvalue},
"""

TESTEXT2_SUFFIX = """\
    {NULL, NULL}
};

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static int
mod_exec_module(PyObject* m)
{
    if (PyObjC_ImportAPI(m) < 0) {
        return -1;
    }

    PyObject* v = PyCapsule_New(gFunctionMap, "objc.__inline__", NULL);
    if (v == NULL) { // LCOV_BR_EXCL_LINE
        return -1; // LCOV_EXCL_LINE
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
"""

TEST_PREFIX_START = """\
#
# This file is generated using Tools/generate-helpers-vector.py
#
#     ** DO NOT EDIT **
#
from functools import partial  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_os_level, NoObjCClass  # noqa: F401
import objc
from objc import simd

#Tests use CGColorRef and CGColorSpaceRef. Try to import Quartz
#to get proper definitions for these types, otherwise fall back
#to minimal definitions (those aren't 100% correct, but good enough
#for these  tests)
try:
    import Quartz # noqa: F401
except ImportError:
    CGColorRef = objc.registerCFSignature("CGColorRef", b"^{CGColor=}", 0)
    CGColorSpaceRef = objc.registerCFSignature(
        "CGColorSpaceRef", b"^{CGColorSpace=}", 0
)
"""

TEST_PREFIX_STOP = """
class NoBool:
    def __bool__(self):
        raise TypeError("no valid in boolean context")

NoObjCValueObject = NoObjCClass()

#Register full signatures for the helper methods
"""

TEST_PREFIX = TEST_PREFIX_START + """
from .vectorcall import OC_VectorCall, OC_VectorCallInvoke
clearRaise = OC_VectorCall.clearRaise
""" + TEST_PREFIX_STOP

TEST2_PREFIX = TEST_PREFIX_START + """
from .vectorfunccall import function_list
""" + TEST_PREFIX_STOP

TESTCASE = """\

class TestVectorCall(TestCase):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.addTypeEqualityFunc(simd.matrix_float2x2, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.matrix_float3x3, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.matrix_float4x3, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.matrix_float4x4, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.matrix_double4x4, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_quatf, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_quatd, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_float4x4, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_float2x2, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_float3x3, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_float4x3, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_float4x4, "assertMatrixEqual")
        self.addTypeEqualityFunc(simd.simd_double4x4, "assertMatrixEqual")

    def assertMatrixEqual(self, first, second, msg=None):
        self.assertEqual(type(first), type(second))
        if hasattr(first, "vector"):
            self.assertSequenceEqual(first.vector, second.vector, msg)
        else:
            self.assertSequenceEqual(first.columns, second.columns, msg)
"""


def function_name(prefix: str, signature: bytes, *, function: bool = False) -> str:
    """
    Return the function name for a specific role and signature
    """
    name = [prefix]
    for idx, part in enumerate(objc.splitSignature(signature)):
        if idx in (1, 2) and not function:
            continue
        if part == objc._C_ID:
            name.append("id")
        elif part == objc._C_SEL:
            name.append("SEL")
        elif part == objc._C_CLASS:
            name.append("Class")
        elif len(part) == 1:
            name.append(part.decode())
        elif part.startswith(objc._C_VECTOR_B):
            name.append("v" + part.decode()[1:-1])
        elif part.startswith(objc._C_STRUCT_B):
            name.append(objc.splitStructSignature(part)[0].lstrip("_"))
        elif part.startswith(objc._C_PTR + objc._C_STRUCT_B):
            label, fields = objc.splitStructSignature(part[1:])
            if fields:
                raise RuntimeError(
                    f"Don't know how to handle {part!r} in {signature!r}"
                )

            name.append(label.lstrip("_"))

        elif part == objc._C_PTR + objc._C_CHAR_AS_TEXT:
            name.append("charp")
        elif part == objc._C_PTR + objc._C_VOID:
            name.append("voidp")
        else:
            raise RuntimeError(f"Don't know how to handle {part!r} in {signature!r}")

    assert "_".join(name).isidentifier()
    return "_".join(name)


def use_stret(typestr):
    if not typestr.startswith(objc._C_STRUCT_B):
        return False

    size = objc._sizeOfType(typestr)
    if size > 16 or size not in (1, 2, 4, 8, 16):
        return True

    return False


def generate_call(
    stream: typing.IO[str], signature: bytes, *, function: bool = False
) -> None:
    """
    Generate the function to call a selector with the specified signature
    """
    signature_parts = objc.splitSignature(signature)
    rv_type = signature_parts[0]
    arg_types = signature_parts[(1 if function else 3) :]

    print("", file=stream)
    print("static PyObject* _Nullable", file=stream)
    print(f"{function_name(CALL_PREFIX, signature, function=function)}(", file=stream)
    if arg_types:
        print(
            f"    PyObject* method, {'' if function else 'PyObject* self, '}PyObject* const* arguments, size_t nargs)",
            file=stream,
        )
    else:
        print(
            f"    PyObject* method, {'' if function else 'PyObject* self, '}"
            "PyObject* const* arguments __attribute__((__unused__)), size_t nargs)",
            file=stream,
        )
    print("{", file=stream)
    if not function:
        print("    struct objc_super super;", file=stream)
    if rv_type != objc._C_VOID:
        print(f"    {describe_type(rv_type)} rv;", file=stream)
    for idx, arg in enumerate(arg_types):
        print(f"    {describe_type(arg)} arg{idx};", file=stream)

    print("", file=stream)
    print(
        f"    if (PyObjC_CheckArgCount(method, {len(arg_types)}, {len(arg_types)}, nargs) == -1)",
        file=stream,
    )
    print("        return NULL;", file=stream)
    print("", file=stream)

    for idx, arg in enumerate(arg_types):
        print(
            f'    if (depythonify_c_value("{arg.decode()}", arguments[{idx}], &arg{idx}) == -1) {{',
            file=stream,
        )
        print("        return NULL;", file=stream)
        print("    }", file=stream)

    print("", file=stream)

    if arg_types:
        arg_type_names = ("" if function else ", ") + ", ".join(
            [describe_type(arg) for arg in arg_types]
        )
        arg_names = ("" if function else ", ") + ", ".join(
            f"arg{idx}" for idx in range(len(arg_types))
        )
    else:
        arg_type_names = ""
        arg_names = ""

    if not function:
        print("    bool                   isIMP;", file=stream)
        print("    id                     self_obj;", file=stream)
        print("    Class                  super_class;", file=stream)
        print("    int                    flags;", file=stream)
        print("    PyObjCMethodSignature* methinfo = NULL;", file=stream)
        print("", file=stream)
        print(
            "    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags,",
            file=stream,
        )
        print(
            "                            &methinfo)",
            file=stream,
        )
        print(
            "           == -1) {",
            file=stream,
        )
        print("         Py_CLEAR(methinfo);", file=stream)
        print("         return NULL;", file=stream)
        print("    }", file=stream)
        print("    Py_BEGIN_ALLOW_THREADS", file=stream)
        print("    @try {", file=stream)
        print("        if (isIMP) {", file=stream)
        print("            // LCOV_BR_EXCL_START", file=stream)
        print(
            f"            {'rv = ' if rv_type != objc._C_VOID else ''}(({describe_type(rv_type)}(*)(id, SEL{arg_type_names}))(PyObjCIMP_GetIMP(method)))(",  # noqa: B950
            file=stream,
        )
        print(
            f"                self_obj, PyObjCIMP_GetSelector(method){arg_names});",
            file=stream,
        )
        print("            // LCOV_BR_EXCL_STOP", file=stream)
        print("", file=stream)
        print("        } else {", file=stream)
        print("            super.receiver    = self_obj;", file=stream)
        print("            super.super_class = super_class;", file=stream)
        print("", file=stream)
        print("            // LCOV_BR_EXCL_START", file=stream)
        if use_stret(rv_type):
            print("#ifdef __x86_64__", file=stream)
            print(
                f"            {'rv = ' if rv_type != objc._C_VOID else ''}(({describe_type(rv_type)}(*)(struct objc_super*, SEL{arg_type_names}))objc_msgSendSuper_stret)(",  # noqa: B950
                file=stream,
            )
            print("#else", file=stream)

        print(
            f"            {'rv = ' if rv_type != objc._C_VOID else ''}(({describe_type(rv_type)}(*)(struct objc_super*, SEL{arg_type_names}))objc_msgSendSuper)(",  # noqa: B950
            file=stream,
        )
        if use_stret(rv_type):
            print("#endif", file=stream)
        print(
            f"                      &super, PyObjCSelector_GetSelector(method){arg_names});",
            file=stream,
        )
        print("            // LCOV_BR_EXCL_STOP", file=stream)
        print("        }", file=stream)
        print("", file=stream)

    else:
        print("    void* function = PyObjCFunc_GetCallable(method);", file=stream)
        print(
            "    PyObjCMethodSignature* methinfo = PyObjCFunc_GetMethodSignature(method);",
            file=stream,
        )
        print("", file=stream)
        print("    Py_BEGIN_ALLOW_THREADS", file=stream)
        print("        @try {", file=stream)
        print(
            f"            {'rv = ' if rv_type != objc._C_VOID else ''}(({describe_type(rv_type)}(*)({arg_type_names}))function)(",  # noqa: B950
            file=stream,
        )
        print(
            f"                      {arg_names});",
            file=stream,
        )

    print(
        "        } @catch (NSObject * localException) { // LCOV_BR_EXCL_LINE",
        file=stream,
    )
    print(
        "            PyObjCErr_FromObjC(localException); // LCOV_BR_EXCL_LINE",
        file=stream,
    )
    print("        }", file=stream)
    print("    Py_END_ALLOW_THREADS", file=stream)

    print("", file=stream)
    print("    if (PyErr_Occurred()) {", file=stream)
    print("        Py_CLEAR(methinfo);", file=stream)
    print("        return NULL;", file=stream)
    print("    }", file=stream)
    print("", file=stream)

    if rv_type == objc._C_ID:
        print("    PyObject* result = adjust_retval(methinfo, rv);", file=stream)
        print("    Py_CLEAR(methinfo);", file=stream)
        print("    return result;", file=stream)

    elif rv_type != objc._C_VOID:
        print("    Py_CLEAR(methinfo);", file=stream)
        print(f'    return pythonify_c_value("{rv_type.decode()}", &rv);', file=stream)
    else:
        print("    Py_RETURN_NONE;", file=stream)
    print("}", file=stream)


def generate_mkimp(stream: typing.IO[str], signature: bytes) -> None:
    """
    Generate a function that creates an IMP that will call
    a Python function from Objective-C
    """
    # XXX:
    # - For methods returning an object : check if the 'methinfo'
    # says that the result is "already_retained" or "already_cfretained"
    # and adjust    the retaincount
    signature_parts = objc.splitSignature(signature)
    rv_type = signature_parts[0]
    arg_types = signature_parts[3:]

    if arg_types:
        arg_type_names = ", " + ", ".join([describe_type(arg) for arg in arg_types])
        arg_decl = ", " + ", ".join(
            f"{describe_type(arg)} arg{idx}" for idx, arg in enumerate(arg_types)
        )
        if "quatf" in [describe_type(arg) for arg in arg_types]:
            raise RuntimeError(signature)
    else:
        arg_type_names = ""
        arg_decl = ""

    print("", file=stream)
    print("static IMP", file=stream)
    print(f"{function_name(MKIMP_PREFIX, signature)}(", file=stream)
    print("    PyObject* callable,", file=stream)
    print(
        "    PyObjCMethodSignature* methinfo __attribute__((__unused__)))", file=stream
    )
    print("{", file=stream)
    print("    Py_INCREF(callable);", file=stream)
    print("", file=stream)
    print(
        f"    {describe_type(rv_type)} (^block)(id{arg_type_names}) = ^(id _Nullable self{arg_decl}) {{",
        file=stream,
    )
    print("        PyGILState_STATE state = PyGILState_Ensure();", file=stream)
    print("", file=stream)
    print("        int       cookie;", file=stream)
    print(f"        PyObject* args[{len(arg_types) + 2}] = {{NULL}};", file=stream)
    print(
        "        PyObject* pyself = PyObjCObject_NewTransient(self, &cookie);",
        file=stream,
    )
    print("        if (pyself == NULL) { // LCOV_BR_EXCL_LINE", file=stream)
    print("            goto error; // LCOV_EXCL_LINE", file=stream)
    print("        } // LCOV_EXCL_LINE", file=stream)
    print("", file=stream)
    print("        args[1] = pyself;", file=stream)
    for idx, tp in enumerate(arg_types):
        print(
            f'        args[{idx + 2}] = pythonify_c_value("{tp.decode()}", &arg{idx});',
            file=stream,
        )
        print(f"        if (args[{idx + 2}] == NULL) // LCOV_BR_EXCL_LINE", file=stream)
        print("            goto error; // LCOV_EXCL_LINE", file=stream)
    print("", file=stream)
    print(
        "        PyObject* result = PyObject_Vectorcall(callable, args + 1,",
        file=stream,
    )
    print(
        f"                                          {len(arg_types) + 1} | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);",
        file=stream,
    )
    print("        if (result == NULL) goto error;", file=stream)
    if rv_type == objc._C_VOID:
        print("        if (result != Py_None) {", file=stream)
        print("            Py_DECREF(result);", file=stream)
        print(
            '            PyErr_Format(PyExc_ValueError, "%R: void return, but did return a value",',
            file=stream,
        )
        print("                         callable);", file=stream)
        print("            goto error;", file=stream)
        print("        }", file=stream)
    else:
        print(f"        {describe_type(rv_type)} oc_result;", file=stream)

        if rv_type in (objc._C_BOOL, objc._C_NSBOOL) or rv_type.startswith(objc._C_PTR):
            lcov_br = " // LCOV_BR_EXCL_LINE"
            lcov_ln = " // LCOV_EXCL_LINE"
        else:
            lcov_br = lcov_ln = ""

        print(
            f'        if (depythonify_c_value("{rv_type.decode()}", result, &oc_result) == -1) {{{lcov_br}',
            file=stream,
        )
        print(f"            Py_DECREF(result);{lcov_ln}", file=stream)
        print(f"            goto error;{lcov_ln}", file=stream)
        print("         }", file=stream)
        print("", file=stream)
    print("        Py_DECREF(result);", file=stream)
    if len(arg_types):
        print(
            f"        for (size_t i = 2; i < {len(arg_types) + 2}; i++) {{", file=stream
        )
        print("            Py_CLEAR(args[i]);", file=stream)
        print("        }", file=stream)
    print("", file=stream)
    print("        PyObjCObject_ReleaseTransient(pyself, cookie);", file=stream)
    print("        PyGILState_Release(state);", file=stream)
    if rv_type == objc._C_VOID:
        print("        return;", file=stream)
    else:
        print("        return oc_result;", file=stream)
    print("", file=stream)
    print("    error:", file=stream)
    print("        if (pyself) { // LCOV_BR_EXCL_LINE", file=stream)
    print("            PyObjCObject_ReleaseTransient(pyself, cookie);", file=stream)
    print("        }", file=stream)
    print("", file=stream)
    if len(arg_types):
        print(
            f"        for (size_t i = 2; i < {len(arg_types) + 2}; i++) {{", file=stream
        )
        print("            Py_CLEAR(args[i]);", file=stream)
        print("        }", file=stream)
    print("        PyObjCErr_ToObjCWithGILState(&state);", file=stream)
    print("    };", file=stream)
    print("", file=stream)
    print("    return imp_implementationWithBlock(block);", file=stream)
    print("}", file=stream)


def BOOL_to_bool(signature: bytes) -> bytes:
    """
    Return 'signature' replacing _C_NSBOOL by _C_BOOL.
    """
    result = []
    for p in objc.splitSignature(signature):
        if p == objc._C_NSBOOL:
            result.append(objc._C_BOOL)
        elif p.startswith(objc._C_STRUCT_B):
            struct_name, struct_fields = objc.splitStructSignature(p)
            result.append(objc._C_STRUCT_B)
            result.append(struct_name.encode())
            result.append(b"=")
            for _, t in struct_fields:
                result.append(BOOL_to_bool(t))
            result.append(objc._C_STRUCT_E)
        else:
            result.append(p)

    return b"".join(result)


def print_macos_available(stream, signature, pfx="    "):
    if b"GKBox" in signature or b"GKTriangle" in signature or b"GKQuad" in signature:
        print(f"{pfx}if objc.macos_available(10, 12):", file=stream)
        return "    "
    elif b"MDL" in signature:
        print(f"{pfx}if objc.macos_available(10, 11):", file=stream)
        return "    "
    elif b"MPSAxisAlignedBoundingBox" in signature:
        print(f"{pfx}if objc.macos_available(10, 14):", file=stream)
        return "    "
    elif b"MPSFunctions_AABB" in signature:
        print(f"{pfx}if objc.macos_available(27, 0):", file=stream)
        return "    "
    elif b"MPS" in signature or b"simd_quat" in signature:
        print(f"{pfx}if objc.macos_available(10, 13):", file=stream)
        return "    "
    return ""


def print_min_os_level(stream, signature):
    if b"GKBox" in signature or b"GKTriangle" in signature or b"GKQuad" in signature:
        print('    @min_os_level("10.12")', file=stream)
    elif b"MDL" in signature:
        print('    @min_os_level("10.11")', file=stream)
    elif b"MPSAxisAlignedBoundingBox" in signature:
        print('    @min_os_level("10.14")', file=stream)
    elif b"MPSFunctions_AABB" in signature:
        print('    @min_os_level("27.0")', file=stream)
    elif b"MPS" in signature or b"simd_quat" in signature:
        print('    @min_os_level("10.13")', file=stream)


def pre_lines(stream, signature):
    if b"GKBox" in signature or b"GKTriangle" in signature or b"GKQuad" in signature:
        print("#if PyObjC_BUILD_RELEASE >= 1012", file=stream)
    elif b"MDL" in signature:
        print("#if PyObjC_BUILD_RELEASE >= 1011", file=stream)
    elif b"MPSAxisAlignedBoundingBox" in signature:
        print("#if PyObjC_BUILD_RELEASE >= 1014", file=stream)
    elif b"MPSFunctions_AABB" in signature:
        print("#if PyObjC_BUILD_RELEASE >= 2700", file=stream)
    elif b"MPS" in signature or b"simd_quat" in signature:
        print("#if PyObjC_BUILD_RELEASE >= 1013", file=stream)


def post_lines(stream, signature):
    if b"GKBox" in signature or b"GKTriangle" in signature or b"GKQuad" in signature:
        print("#endif /* PyObjC_BUILD_RELEASE >= 1012 */", file=stream)
    elif b"MDL" in signature:
        print("#endif /* PyObjC_BUILD_RELEASE >= 1011 */", file=stream)
    elif b"MPSAxisAlignedBoundingBox" in signature:
        print("#endif /* PyObjC_BUILD_RELEASE >= 1014 */", file=stream)
    elif b"MPSFunctions_AABB" in signature:
        print("#endif /* PyObjC_BUILD_RELEASE >= 2700 */", file=stream)
    elif b"MPS" in signature or b"simd_quat" in signature:
        print("#endif /* PyObjC_BUILD_RELEASE >= 1013 */", file=stream)


def generate_setup_function_method(stream: typing.IO[str]):
    """
    Generate the function that's used to register
    the generated functions with the core bridge.
    """
    print("int", file=stream)
    print(
        "PyObjC_setup_simd(PyObject* module __attribute__((__unused__)))", file=stream
    )
    print("{", file=stream)

    seen_call = {}
    seen_mkimp = {}
    for idx, signature in enumerate(METH_SIGNATURES):
        print("", file=stream)
        pre_lines(stream, signature)

        call_name = function_name(CALL_PREFIX, signature)
        mkimp_name = function_name(MKIMP_PREFIX, signature)

        if call_name in seen_call:
            raise RuntimeError(f"{call_name}: {idx!r} {seen_call[call_name]!r}")
        if mkimp_name in seen_call:
            raise RuntimeError(f"{mkimp_name}: {idx!r} {seen_mkimp[mkimp_name]!r}")

        seen_call[call_name] = idx
        seen_mkimp[mkimp_name] = idx

        print(
            "    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE", file=stream
        )
        print(
            f'        "{signature.decode()}", {call_name}, {mkimp_name})', file=stream
        )
        print("       == -1) {", file=stream)
        print("            return -1; // LCOV_EXCL_LINE", file=stream)
        print("    }", file=stream)

        alt_signature = BOOL_to_bool(signature)
        if alt_signature != signature:
            print("", file=stream)
            print(
                "    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE",
                file=stream,
            )
            print(
                f'        "{alt_signature.decode()}", {call_name}, {mkimp_name})',
                file=stream,
            )
            print("       == -1) {", file=stream)
            print("            return -1; // LCOV_EXCL_LINE", file=stream)
            print("    }", file=stream)

        post_lines(stream, signature)

    print("", file=stream)
    print("    return 0;", file=stream)
    print("}", file=stream)


def generate_setup_function_func(stream: typing.IO[str]):
    """
    Generate the function that's used to register
    the generated functions with the core bridge.
    """
    print("int", file=stream)
    print(
        "PyObjC_setup_simd_functions(PyObject* module __attribute__((__unused__)))",
        file=stream,
    )
    print("{", file=stream)
    print("    // LCOV_BR_EXCL_START", file=stream)

    seen_call = {}
    for idx, signature in enumerate(FUNC_SIGNATURES):
        print("", file=stream)
        pre_lines(stream, signature)

        call_name = function_name(CALL_PREFIX, signature, function=True)

        if call_name in seen_call:
            raise RuntimeError(f"{call_name}: {idx!r} {seen_call[call_name]!r}")

        seen_call[call_name] = idx

        print("    if (PyObjC_RegisterFunctionSignatureMapping(", file=stream)
        print(f'        "{signature.decode()}", {call_name})', file=stream)
        print("       == -1) { // LCOV_BR_EXCL_LINE", file=stream)
        print("            return -1; // LCOV_EXCL_LINE", file=stream)
        print("    }", file=stream)

        alt_signature = BOOL_to_bool(signature)
        if alt_signature != signature:
            print("", file=stream)
            print("    if (PyObjC_RegisterFunctionSignatureMapping(", file=stream)
            print(f'        "{alt_signature.decode()}", {call_name})', file=stream)
            print("       == -1) { // LCOV_BR_EXCL_LINE", file=stream)
            print("            return -1; // LCOV_EXCL_LINE", file=stream)
            print("    }", file=stream)

        post_lines(stream, signature)

    print("", file=stream)
    print("    return 0;", file=stream)
    print("    // LCOV_BR_EXCL_STOP", file=stream)
    print("}", file=stream)


def sel_for_signature(signature, *, function=False):
    name = []
    for idx, part in enumerate(objc.splitSignature(signature)):
        if idx in (1, 2) and not function:
            continue
        if part == objc._C_ID:
            name.append("id")
        elif part == objc._C_SEL:
            name.append("SEL")
        elif part == objc._C_CLASS:
            name.append("Class")
        elif len(part) == 1:
            name.append(part.decode())
        elif part.startswith(objc._C_VECTOR_B):
            name.append("v" + part.decode()[1:-1])
        elif part.startswith(objc._C_STRUCT_B):
            name.append(objc.splitStructSignature(part)[0].lstrip("_").replace("_", ""))
        elif part.startswith(objc._C_PTR + objc._C_STRUCT_B):
            label, fields = objc.splitStructSignature(part[1:])
            if fields:
                raise RuntimeError(
                    f"Don't know how to handle {part!r} in {signature!r}"
                )
            name.append(label.lstrip("_"))

        elif part.startswith(objc._C_PTR + objc._C_CHAR_AS_TEXT):
            name.append("charp")

        elif part.startswith(objc._C_PTR + objc._C_VOID):
            name.append("voidp")

        else:
            raise RuntimeError(f"Don't know how to handle {part!r} in {signature!r}")

    if len(name) == 1:
        return name[0]
    else:
        return name[0] + ":".join(name[1:]) + ":"


def as_objc_literal(typestr, value):
    if hasattr(value, "_objc_literal"):
        return value._objc_literal()
    elif isinstance(value, bool):
        return "YES" if value else "NO"
    elif isinstance(value, str):
        return f'@"{value}"'
    elif isinstance(value, LiteralRepr):
        return value
    elif typestr.startswith(objc._C_STRUCT_B):
        name, fields = objc.splitStructSignature(typestr)
        if name.startswith("_"):
            name = name[1:]

        elems = []
        for v, (_, t) in zip(value, fields):
            if isinstance(v, (list, tuple)):
                elems.append(f"{{{', '.join(as_objc_literal(t, x) for x in v)}}}")

            else:
                elems.append(f"{as_objc_literal(t, v)}")

        return f"({name}){{{', '.join(elems)}}}"

    return repr(value)


def generate_testext_callimp(stream, signature, instance=True, function_list=None):
    """
    function_list is not None: function
    instance = True: instance method
    instance = False: class method
    """
    parts = objc.splitSignature(signature)
    sel = sel_for_signature(signature, function=(function_list is not None))
    if not instance:
        sel = "cls" + sel

    if ":" not in sel:
        if function_list is not None:
            print(
                f"static {describe_type(parts[0])} {sel.replace(':', '_')}(void)",
                file=stream,
            )
            function_list.append(sel.replace(":", "_"))

        else:
            print(
                f"{'-' if instance else '+'} ({describe_type(parts[0])}){sel}",
                file=stream,
            )
        print("{", file=stream)
        print("    if (shouldRaise) {", file=stream)
        print("        shouldRaise = NO;", file=stream)
        print(
            '        [NSException raise:@"SimpleException" format:@"hello world"];',
            file=stream,
        )
        print("    }", file=stream)
        print("", file=stream)
        print("    PyObjC_BEGIN_WITH_GIL", file=stream)
        if instance:
            print("         values = PyList_New(0);", file=stream)
            print("         if (values == NULL) PyObjC_GIL_FORWARD_EXC();", file=stream)
        else:
            print("         clsvalues = PyList_New(0);", file=stream)
            print(
                "         if (clsvalues == NULL) PyObjC_GIL_FORWARD_EXC();", file=stream
            )
        print("    PyObjC_END_WITH_GIL", file=stream)

        print(
            f"    return {as_objc_literal(parts[0], valid_value(parts[0]))};",
            file=stream,
        )
        print("}", file=stream)
        print("", file=stream)
        return

    if function_list is not None:
        function_list.append(sel.replace(":", "_"))
        print(
            f"static {describe_type(parts[0])} {sel.replace(':', '_')}(",
            end="",
            file=stream,
        )
        for idx, _selpart in enumerate(sel.split(":")[:-1]):
            print(
                f"{'' if idx == 0 else ', '}{describe_type(parts[idx + 1])} arg{idx}",
                end=" ",
                file=stream,
            )
        print(")", end="", file=stream)
    else:
        print(
            f"{'-' if instance else '+'} ({describe_type(parts[0])})",
            end="",
            file=stream,
        )
        for idx, selpart in enumerate(sel.split(":")[:-1]):
            print(
                f"{selpart}:({describe_type(parts[idx + 3])})arg{idx}",
                end=" ",
                file=stream,
            )
    print("\n{", file=stream)
    print("    PyObject* items;", file=stream)
    print("    PyObject* tmp;", file=stream)
    print("", file=stream)
    print("    if (shouldRaise) {", file=stream)
    print("        shouldRaise = NO;", file=stream)
    print(
        '        [NSException raise:@"SimpleException" format:@"hello world"];',
        file=stream,
    )
    print("    }", file=stream)
    print("", file=stream)
    print("    PyObjC_BEGIN_WITH_GIL", file=stream)
    if instance:
        print("        items = values = PyList_New(0);", file=stream)
    else:
        print("        items = clsvalues = PyList_New(0);", file=stream)

    print("        if (items == NULL) PyObjC_GIL_FORWARD_EXC();", file=stream)

    for idx, _selpart in enumerate(sel.split(":")[:-1]):
        offset = 3 if function_list is None else 1
        print(
            f'        tmp = PyObjC_ObjCToPython("{parts[idx + offset].decode()}", &arg{idx});',
            file=stream,
        )
        print("        if (tmp == NULL) PyObjC_GIL_FORWARD_EXC();", file=stream)

        # This leaks 'tmp' on error, but that's not a problem for tests
        print(
            "        if (PyList_Append(items, tmp) == -1) PyObjC_GIL_FORWARD_EXC();",
            file=stream,
        )

    print("    PyObjC_END_WITH_GIL", file=stream)
    if parts[0] != objc._C_VOID:
        print(
            f"    return {as_objc_literal(parts[0], valid_value(parts[0]))};",
            file=stream,
        )
    print("}", file=stream)
    print("", file=stream)


def generate_testext_callfromobjc(stream, signature):
    parts = objc.splitSignature(signature)
    sel = sel_for_signature(signature)

    if ":" not in sel:
        if parts[0] == objc._C_VOID:
            print(f"+(void){sel}On:(OC_VectorCall*)value", file=stream)
            print("{", file=stream)
            print("    [value {sel}];", file=stream)
            print("}", file=stream)
        else:
            print(f"+(id){sel}On:(OC_VectorCall*)value", file=stream)
            print("{", file=stream)
            print("     id cinter;", file=stream)
            print(f"    {describe_type(parts[0])} result = [value {sel}];", file=stream)
            print("     PyObjC_BEGIN_WITH_GIL", file=stream)
            print(
                f'    PyObject* inter =  PyObjC_ObjCToPython("{parts[0].decode()}", &result);',
                file=stream,
            )
            print(
                '     if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {',
                file=stream,
            )
            print("         PyObjC_GIL_FORWARD_EXC();", file=stream)
            print("     }", file=stream)
            print("     PyObjC_END_WITH_GIL", file=stream)
            print("     return cinter;", file=stream)
            print("}", file=stream)
        print("", file=stream)
        return

    rtype = "void" if parts[0] == objc._C_VOID else "id"
    print(f"+({rtype}){sel.replace(':', '')}On:(OC_VectorCall*)value", file=stream)
    print("{", file=stream)
    print("    ", end="", file=stream)
    if parts[0] != objc._C_VOID:
        print(f"{describe_type(parts[0])} result = ", end="", file=stream)
    print("[value ", end="", file=stream)
    for idx, selpart in enumerate(sel.split(":")[:-1]):
        print(
            f"{selpart}:{as_objc_literal(parts[idx + 3], valid_value(parts[idx + 3]))} ",
            end=" ",
            file=stream,
        )

    print("];", file=stream)
    if parts[0] != objc._C_VOID:
        print("     id cinter;", file=stream)
        print("     PyObjC_BEGIN_WITH_GIL", file=stream)
        print(
            f'    PyObject* inter =  PyObjC_ObjCToPython("{parts[0].decode()}", &result);',
            file=stream,
        )
        print('     if (PyObjC_PythonToObjC("@", inter, &cinter) == -1) {', file=stream)
        print("         PyObjC_GIL_FORWARD_EXC();", file=stream)
        print("     }", file=stream)
        print("     PyObjC_END_WITH_GIL", file=stream)
        print("     return cinter;", file=stream)
    print("}", file=stream)
    print("", file=stream)


def generate_register(stream, signature):
    # This registers the custom metadata on             NSObject because
    # this allows reusing the registration for both the C extension
    # as the Python                                     implementation.
    #
    # The selector names are specializedenough to not cause problems here.

    pfx = print_macos_available(stream, signature, pfx="")
    print(
        f'{pfx}objc.registerMetaDataForSelector(b"NSObject", '
        f'b"{sel_for_signature(signature)}", '
        f'{{"full_signature": b"{signature.decode()}"}})',
        file=stream,
    )
    print(
        f'{pfx}objc.registerMetaDataForSelector(b"NSObject", '
        f'b"cls{sel_for_signature(signature)}", '
        f'{{"full_signature": b"{signature.decode()}"}})',
        file=stream,
    )


class LiteralRepr:
    def __init__(self, value: str, objc_value: str | None = None) -> None:
        self._value = value

        if objc_value is not None:
            self._objc_literal = lambda: objc_value

    def __repr__(self) -> str:
        return self._value


# Values to use during testing, valid entries must match what's used in
# the ObjC generator for return values.
VALUES = {
    # typestr : (valid, invalid)
    objc._C_ID: ("hello", LiteralRepr("NoObjCValueObject")),
    objc._C_UCHR: (21, None),
    objc._C_INT: (-42, None),
    objc._C_UINT: (42, None),
    objc._C_SHT: (-5, None),
    objc._C_USHT: (55, None),
    objc._C_LNG: (-(2**44), None),
    objc._C_ULNG: (2**45, None),
    objc._C_LNGLNG: (-(2**44), None),
    objc._C_ULNGLNG: (2**45, None),
    objc._C_FLT: (2.5e9, None),
    objc._C_DBL: (-55.7e10, None),
    objc._C_BOOL: (True, LiteralRepr("NoBool()")),
    objc._C_NSBOOL: (False, LiteralRepr("NoBool()")),
    objc._C_CLASS: (
        LiteralRepr('objc.lookUpClass("NSObject")', "[NSObject class]"),
        42,
    ),
    b"{GKBox=<3f><3f>}": (
        (simd.vector_float3(1, 2, 3), simd.vector_float3(4, 5, 6)),
        None,
    ),
    b"{_MPSAxisAlignedBoundingBox=<3f><3f>}": (
        (simd.vector_float3(1.5, 2.5, 3.5), simd.vector_float3(4.5, 5.5, 6.5)),
        None,
    ),
    b"{GKQuad=<2f><2f>}": (
        (simd.vector_float2(9, 10), simd.vector_float2(11, 12)),
        None,
    ),
    b"{MDLAxisAlignedBoundingBox=<3f><3f>}": (
        (simd.vector_float3(-8, -9, -10), simd.vector_float3(-11, -12, -13)),
        None,
    ),
    b"^{CGColor=}": (
        LiteralRepr("'color!'", '(CGColorRef)@"color!"'),
        LiteralRepr("NoObjCValueObject"),
    ),
    b"^{CGColorSpace=}": (
        LiteralRepr("'colorspace!'", '(CGColorSpaceRef)@"colorspace!"'),
        LiteralRepr("NoObjCValueObject"),
    ),
    b"{MDLVoxelIndexExtent=<4i><4i>}": (
        (simd.vector_int4(100, 101, 102, 103), simd.vector_int4(-20, -21, -22, -23)),
        None,
    ),
    b"{GKTriangle=[3<3f>]}": (
        (
            (
                simd.vector_float3(-18.5, -19.5, -110.5),
                simd.vector_float3(-111.5, -112.5, -113.5),
                simd.vector_float3(-17.5, 11.5, 122.5),
            ),
        ),
        None,
    ),
    b"{MPSImageHistogramInfo=QZ<4f><4f>}": (
        (
            2**42,
            True,
            simd.vector_float4(1, 2, 3, 4),
            simd.vector_float4(-1, -2, -3, -4),
        ),
        None,
    ),
    b"{MPSFunctions_AABB=<4f><4f>}": (
        (
            simd.vector_float4(1, 2, 3, 4),
            simd.vector_float4(-1, -2, -3, -4),
        ),
        None,
    ),
    objc._C_PTR + objc._C_CHAR_AS_TEXT: (LiteralRepr('b"names"', "names"), None),
    objc._C_PTR + objc._C_VOID: (LiteralRepr('b"bytes"', "bytes"), None),
    b"{CGPoint=dd}": (LiteralRepr("(1.0, 2.0)", "(CGPoint){1.0, 2.0}"), None),
    b"{CGRect={CGPoint=dd}{CGSize=dd}}": (
        LiteralRepr("((1.0, 2.0), (3.0, 4.0))", "(CGRect){{1.0, 2.0}, {3.0, 4.0}}"),
        None,
    ),
    b"{SCNVector3=ddd}": (
        LiteralRepr("(1.0, 2.0, 3.0)", "(SCNVector3){1.0, 2.0, 3.0}"),
        None,
    ),
    b"{SCNVector4=dddd}": (
        LiteralRepr("(1.0, 2.0, 3.0, 4.0)", "(SCNVector4){1.0, 2.0, 3.0, 4.0}"),
        None,
    ),
    b"{CATransform3D=dddddddddddddddd}": (
        LiteralRepr(
            "(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0)",
            "(CATransform3D){1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0}",
        ),
        None,
    ),
    b"^{cp_frame=}": (LiteralRepr("None", "NULL"), 3.5),
    b"^{cp_drawable=}": (LiteralRepr("None", "NULL"), 3.5),
    b"^{cp_view=}": (LiteralRepr("None", "NULL"), 3.5),
}

SIMD_TYPES = {
    objc._C_UCHR: "uchar",
    objc._C_INT: "int",
    objc._C_UINT: "uint",
    objc._C_SHT: "int",
    objc._C_USHT: "uint",
    objc._C_FLT: "float",
    objc._C_DBL: "double",
}


def valid_value(typestr):
    if typestr.startswith(objc._C_VECTOR_B):
        t = typestr[-2:-1]
        c = int(typestr[1:-2])
        if t in (objc._C_FLT, objc._C_DBL):
            return getattr(simd, f"vector_{SIMD_TYPES[t]}{c}")(
                *(x * 1.5 for x in range(c))
            )
        else:
            return getattr(simd, f"vector_{SIMD_TYPES[t]}{c}")(*range(c))

    if typestr.startswith(objc._C_STRUCT_B):
        name, elem = objc.splitStructSignature(typestr)
        matrix = getattr(simd, name, None)
        if matrix is not None:
            assert len(elem) == 1
            elemtp = elem[0][-1]
            if elemtp.startswith(objc._C_ARY_B):
                elemtp = elemtp[1:-1]
                cnt = b""
                while elemtp[:1].isdigit():
                    cnt = cnt + elemtp[:1]
                    elemtp = elemtp[1:]

                value = (valid_value(elemtp),) * int(cnt)
                return LiteralRepr(
                    f"simd.{name}({value!r})",
                    f"({name}){{{{{', '.join(as_objc_literal(elemtp, v) for v in value)}}}}}",
                )
            else:
                value = valid_value(elemtp)
                return LiteralRepr(
                    f"simd.{name}({value!r})",
                    f"({name}){{{as_objc_literal(elemtp, value)}}}",
                )

    return VALUES[typestr][0]


def invalid_value(typestr):
    if typestr.startswith(objc._C_VECTOR_B):
        return None
    if typestr.startswith(objc._C_STRUCT_B):
        return None
    return VALUES[typestr][1]


def generate_call_testcase(
    stream, signature, *, instance=True, imp=False, function=False
):
    oc_sel = sel_for_signature(signature, function=function)
    if not instance:
        oc_sel = "cls" + oc_sel
    sel = oc_sel.replace(":", "_")

    print_min_os_level(stream, signature)
    print(f"    def test_{sel}{'_imp' if imp else ''}(self):", file=stream)
    sigparts = objc.splitSignature(signature)
    print("        clearRaise()   # noqa: F821", file=stream)

    callable_name = sel if function else f"OC_VectorCall.{sel}"
    stored_value = "storedvalue" if function else "oc.storedvalue"
    set_raise = "setRaise" if function else "OC_VectorCall.setRaise"
    no_qa = "  # noqa: F821" if function else ""
    arg_off = 1 if function else 3

    if not function:
        print("        # Verify method type", file=stream)
        print(
            f"        self.assert{not instance}(OC_VectorCall.{sel}.isClassMethod)",
            file=stream,
        )
        print("        # Verify that method is not an initializer", file=stream)
        print(
            f"        self.assertIsNotInitializer(OC_VectorCall.{sel})",
            file=stream,
        )

    print("        # Check that the signature is as expected", file=stream)
    print(
        f"        self.assertResultHasType({callable_name},{no_qa}\n{sigparts[0]}){no_qa}",
        file=stream,
    )
    for idx, p in enumerate(sigparts[arg_off:]):
        print(
            f"        self.assertArgHasType({callable_name},{no_qa}\n{idx}, {p})",
            file=stream,
        )
    print("", file=stream)

    if not function:
        print("        # Create test object", file=stream)
        if instance:
            print("        oc = OC_VectorCall.alloc().init()", file=stream)
        else:
            print("        oc = OC_VectorCall", file=stream)
            if imp:
                print("        oc_inst = OC_VectorCall.alloc().init()", file=stream)
        print("        self.assertIsNot(oc, None)", file=stream)
        print("", file=stream)

        print(
            "        # Set caller to the selector/IMP to call (With bound self)",
            file=stream,
        )
        if imp:
            print(f"        imp = oc.methodForSelector_(b'{oc_sel}')", file=stream)
            print("        self.assertIsInstance(imp, objc.IMP)", file=stream)
            print("        caller = partial(imp, oc)", file=stream)

        else:
            print(f"        caller = oc.{sel}", file=stream)
    else:
        print(f"        caller = {callable_name}{no_qa}", file=stream)

    print("", file=stream)
    print("        # Valid call", file=stream)
    print(
        f"        rv = caller({', '.join(repr(valid_value(s)) for s in sigparts[arg_off:])})",
        file=stream,
    )
    if sigparts[0] == objc._C_VOID:
        print("        self.assertIs(rv, None)", file=stream)
    else:
        print(
            f"        self.assertEqual(rv, {valid_value(sigparts[0])!r})", file=stream
        )

    if imp and not instance:
        print("", file=stream)
        print("        # Valid call through instance", file=stream)
        print(
            f"        rv = imp(oc_inst, {', '.join(repr(valid_value(s)) for s in sigparts[3:])})",
            file=stream,
        )
        if sigparts[0] == objc._C_VOID:
            print("        self.assertIs(rv, None)", file=stream)
        else:
            print(
                f"        self.assertEqual(rv, {valid_value(sigparts[0])!r})",
                file=stream,
            )

        print("", file=stream)
        print("        # Valid call through meta", file=stream)
        print(
            f"        rv = imp(type(oc), {', '.join(repr(valid_value(s)) for s in sigparts[3:])})",
            file=stream,
        )
        if sigparts[0] == objc._C_VOID:
            print("        self.assertIs(rv, None)", file=stream)
        else:
            print(
                f"        self.assertEqual(rv, {valid_value(sigparts[0])!r})",
                file=stream,
            )

    print("", file=stream)

    print(f"        stored = {stored_value}(){no_qa}", file=stream)
    print("        self.assertIsInstance(stored, (list, tuple))", file=stream)
    print(
        f"        self.assertEqual(len(stored), {len(sigparts) - arg_off})",
        file=stream,
    )
    for i, s in enumerate(sigparts[arg_off:]):
        print(f"        self.assertEqual(stored[{i}], {valid_value(s)!r})", file=stream)
    print("", file=stream)

    if len(sigparts) > arg_off:
        print("        # Too few arguments call", file=stream)
        print(
            "        with self.assertRaisesRegex(TypeError, 'expected.*arguments.*got'):",
            file=stream,
        )
        print(
            f"            caller({', '.join(repr(valid_value(s)) for s in sigparts[arg_off:-1])})",
            file=stream,
        )
    print("", file=stream)
    print("        # Too many arguments call", file=stream)
    print(
        "        with self.assertRaisesRegex(TypeError, 'expected.*arguments.*got'):",
        file=stream,
    )
    print(
        f"            caller({', '.join(repr(valid_value(s)) for s in sigparts[arg_off:] + (sigparts[1],))})",
        file=stream,
    )
    print("", file=stream)
    if len(sigparts) > arg_off:
        print("        # Bad value for arguments", file=stream)
    for idx in range(len(sigparts) - arg_off):
        print("        with self.assertRaises((TypeError, ValueError)):", file=stream)
        print(
            f"            caller("
            f"{', '.join(repr(invalid_value(s) if i == idx else valid_value(s)) for i, s in enumerate(sigparts[arg_off:]))})",
            file=stream,
        )
        print("", file=stream)

    print("        # Exception handling", file=stream)
    print(f"        {set_raise}(){no_qa}", file=stream)
    print(
        "        with self.assertRaisesRegex(objc.error, 'SimpleException'):",
        file=stream,
    )
    print(
        f"            caller({', '.join(repr(valid_value(s)) for s in sigparts[arg_off:])})",
        file=stream,
    )

    if imp:
        print("", file=stream)
        if instance:
            print("", file=stream)
            print(
                "        with self.assertRaisesRegex(TypeError, 'Cannot proxy'):",
                file=stream,
            )
            print(
                f"            imp(NoObjCValueObject, {', '.join(repr(valid_value(s)) for s in sigparts[3:])})",
                file=stream,
            )

        else:
            print(
                "        with self.assertRaisesRegex(TypeError, 'Need Objective-C object'):",
                file=stream,
            )
            print(
                f"            imp(42, {', '.join(repr(valid_value(s)) for s in sigparts[3:])})",
                file=stream,
            )

    if function and len(sigparts) > arg_off:
        print("", file=stream)
        print(
            "        with self.assertRaisesRegex(TypeError, 'does not accept keyword arguments'):",
            file=stream,
        )
        print(
            f"                caller({', '.join(f'arg{i}={valid_value(s)!r}' for i, s in enumerate(sigparts[arg_off:]))})",
            file=stream,
        )

    print("", file=stream)


# XXX : Actually test
#
# - Second test(requires more updates : class method instead of instance)
# - Third / fourth test : Call through IMP for instance / class method


def generate_imp_testhelper(stream, signature, instance=True):
    signature_parts = objc.splitSignature(signature)
    oc_sel = sel_for_signature(signature)
    sel = oc_sel.replace(":", "_")

    arg_names = tuple(f"arg{idx}" for idx in range(len(signature_parts) - 3))

    pfx = print_macos_available(stream, signature)
    if not instance:
        print(f"{pfx}    @classmethod", file=stream)

    if arg_names:
        print(f"{pfx}    def {sel}(self, {', '.join(arg_names)}):", file=stream)
        print(f"{pfx}        self.argvalues = ({', '.join(arg_names)},)", file=stream)
    else:
        print(f"{pfx}    def {sel}(self):", file=stream)
        print(f"{pfx}        self.argvalues = None", file=stream)

    print(f"{pfx}        if getattr(self, 'shouldRaise', False):", file=stream)
    print(f"{pfx}            raise RuntimeError('failure!')", file=stream)

    print(
        f"{pfx}        if getattr(self, 'returnInvalid', False): return NoObjCClass()",
        file=stream,
    )

    if signature_parts[0] != objc._C_VOID:
        print(
            f"{pfx}        return {repr(valid_value(signature_parts[0]))}", file=stream
        )

    print("", file=stream)


def generate_imp_testcase(stream, signature, instance=True):
    signature_parts = objc.splitSignature(signature)
    oc_sel = sel_for_signature(signature)
    sel = oc_sel.replace(":", "_")

    print_min_os_level(stream, signature)
    print(
        f"    def test_imp_{sel}{'' if instance else '_cls'}(self):",
        file=stream,
    )
    if instance:
        print("        value = OC_VectorCallInstance.alloc().init()", file=stream)
    else:
        print("        value = OC_VectorCallClass", file=stream)

    print("        value.argvalues = 1", file=stream)
    print(
        f"        result = OC_VectorCallInvoke.{oc_sel.replace(':', '')}On_(value)",
        file=stream,
    )
    if signature_parts[0] == objc._C_VOID:
        print("        self.assertIs(result, None)", file=stream)
    else:
        print(
            f"        self.assertEqual(result, {repr(valid_value(signature_parts[0]))})",
            file=stream,
        )

    if len(signature_parts) == 3:
        print("        self.assertIs(value.argvalues, None)", file=stream)
    else:
        print(
            f"        self.assertEqual(value.argvalues, ({', '.join(repr(valid_value(tp)) for tp in signature_parts[3:])},))",
            file=stream,
        )
    print("", file=stream)
    print("        # Test raising an exception", file=stream)
    print("        value.shouldRaise = True", file=stream)
    print("        try:", file=stream)
    print(
        "            with self.assertRaisesRegex(RuntimeError, 'failure'):",
        file=stream,
    )
    print(
        f"                OC_VectorCallInvoke.{oc_sel.replace(':', '')}On_(value)",
        file=stream,
    )
    print("        finally:", file=stream)
    print("            del value.shouldRaise", file=stream)

    if signature_parts[0] not in (
        objc._C_BOOL,
        objc._C_NSBOOL,
    ) and not signature_parts[0].startswith(objc._C_PTR):
        print("", file=stream)
        print("        value.returnInvalid = True", file=stream)
        print("        try:", file=stream)
        print(
            "            with self.assertRaises((ValueError, TypeError)):",
            file=stream,
        )
        print(
            f"                OC_VectorCallInvoke.{oc_sel.replace(':', '')}On_(value)",
            file=stream,
        )
        print("        finally:", file=stream)
        print("            del value.returnInvalid", file=stream)

    print("", file=stream)


def main():
    with open(HELPER_FILE, "w") as stream:
        print(HELPER_PREFIX, file=stream)
        for signature in METH_SIGNATURES:
            pre_lines(stream, signature)

            generate_call(stream, signature)
            generate_mkimp(stream, signature)

            post_lines(stream, signature)
        generate_setup_function_method(stream)
        print("NS_ASSUME_NONNULL_END", file=stream)

    with open(HELPER2_FILE, "w") as stream:
        print(HELPER2_PREFIX, file=stream)
        for signature in FUNC_SIGNATURES:
            pre_lines(stream, signature)

            generate_call(stream, signature, function=True)

            post_lines(stream, signature)
        generate_setup_function_func(stream)
        print("NS_ASSUME_NONNULL_END", file=stream)

    with open(TESTEXT_FILE, "w") as stream:
        print(TESTEXT_PREFIX, file=stream)

        for signature in METH_SIGNATURES:
            pre_lines(stream, signature)
            generate_testext_callimp(stream, signature)
            generate_testext_callimp(stream, signature, instance=False)
            post_lines(stream, signature)

        print(TESTEXT_MID, file=stream)

        for signature in METH_SIGNATURES:
            pre_lines(stream, signature)
            generate_testext_callfromobjc(stream, signature)
            post_lines(stream, signature)

        print(TESTEXT_SUFFIX, file=stream)

    with open(TESTEXT2_FILE, "w") as stream:
        print(TESTEXT2_PREFIX, file=stream)
        all_functions = []

        for signature in FUNC_SIGNATURES:
            pre_lines(stream, signature)
            generate_testext_callimp(stream, signature, function_list=all_functions)
            post_lines(stream, signature)

        print(TESTEXT2_MID, file=stream)
        for name in all_functions:
            print(f'    {{ "{name}", (F){name} }},', file=stream)

        print(TESTEXT2_SUFFIX, file=stream)

    with open(TEST_FILE, "w") as stream:
        print(TEST_PREFIX, file=stream)

        for signature in METH_SIGNATURES:
            generate_register(stream, signature)

        print("", file=stream)
        print("class OC_VectorCallInstance(objc.lookUpClass('NSObject')):", file=stream)
        for signature in METH_SIGNATURES:
            generate_imp_testhelper(stream, signature)

        print("", file=stream)
        print("class OC_VectorCallClass(objc.lookUpClass('NSObject')):", file=stream)
        for signature in METH_SIGNATURES:
            generate_imp_testhelper(stream, signature, instance=False)

        print("", file=stream)
        print(TESTCASE, file=stream)
        for signature in METH_SIGNATURES:
            generate_call_testcase(stream, signature)
            generate_call_testcase(stream, signature, instance=False)

            generate_call_testcase(stream, signature, imp=True)
            generate_call_testcase(stream, signature, instance=False, imp=True)

            generate_imp_testcase(stream, signature)
            generate_imp_testcase(stream, signature, instance=False)

    with open(TEST2_FILE, "w") as stream:
        print(TEST2_PREFIX, file=stream)

        print("objc.loadFunctionList(function_list, globals(), [", file=stream)
        print('    ("shouldRaise", b"Z"),', file=stream)
        print('    ("clearRaise", b"v"),', file=stream)
        print('    ("setRaise", b"v"),', file=stream)
        print('    ("storedvalue", b"@"),', file=stream)
        for signature in FUNC_SIGNATURES:
            print(
                f'    ("{sel_for_signature(signature, function=True).replace(":", "_")}", {signature}),',
                file=stream,
            )
        print("])", file=stream)

        print("", file=stream)
        print(TESTCASE, file=stream)
        for signature in FUNC_SIGNATURES:
            generate_call_testcase(stream, signature, function=True)


if __name__ == "__main__":
    main()
