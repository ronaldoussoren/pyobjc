#!/usr/bin/env python3
"""
Helper script for generating support code for vector types,
including testcases and the supporting extension for that.

The code currently is fairly gross, but works.

XXX: There should be "imp" variants for signatures
     used in protocols that are intended to be implemented
     by API users, those should ``imp_implementationWithBlock``
     as used in block-as-imp.m (and fold the mechanism used
     in that file into registry.[hm])

XXX: Use the Parse helpers to simplify the generated
     implementation. Basically only the actual invocation
     needs to be custom, the rest can be the same as in
     the FFI caller.

     But: check generated code size and only do this when
     this reduces code size!

XXX: Also use this for simple basic methods '-(id)method',
     '-(void)method:arg', and '(void)method', but this also
     needs the 'imp' variants.

XXX: Use subtests

XXX: Use jinja2 in code generation

XXX: 'simd_' to 'vector_'

XXX: 'GK..' types are only available on recentisch macOS
     versions, add guards.
"""

import objc
from objc import simd
import typing
import pathlib
import Quartz  # noqa: F401
from objc._callable_docstr import describe_type

HELPER_FILE = (
    pathlib.Path(__file__).resolve().parent.parent / "Modules/objc/helpers-vector.m"
)
TESTEXT_FILE = (
    pathlib.Path(__file__).resolve().parent.parent / "Modules/objc/test/vectorcall.m"
)
TEST_FILE = (
    pathlib.Path(__file__).resolve().parent.parent / "PyObjCTest/test_vectorcall.py"
)

CALL_PREFIX = "call"
MKIMP_PREFIX = "mkimp"


# grep full_signature ../*/Lib/*/_metadata.py | sed 's@.*full_signature.: \([^ ]*\).*@\1@' | sort -u
ALL_SIGNATURES = [
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
    b"@@:^{CGColor=}^{CGColor=}@<2i>",
    b"@@:f<2f><2f>",
    b"@@:f<2f><2f>#",
    b"@@:f<2f>QQQqZ@",
    b"@@:f<2f>QQqZ@",
    b"@@:f@<2i>iqZ",
    b"@@:f@<2i>iq^{CGColor=}^{CGColor=}",
    b"@@:f@<2i>q",
    b"@@:ff@<2i>",
    b"@@:{GKBox=<3f><3f>}",
    b"@@:{GKBox=<3f><3f>}f",
    b"@@:{GKQuad=<2f><2f>}",
    b"@@:{GKQuad=<2f><2f>}f",
    b"@@:{MDLVoxelIndexExtent=<4i><4i>}",
    b"@@:{simd_float4x4=[4<4f>]}",
    b"@@:{simd_float4x4=[4<4f>]}Z",
    b"Z@:<2i>@@@@",
    b"Z@:<2i>qf@@@",
    b"Z@:<4i>ZZZZ",
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
    b"{simd_double4x4=[4<4d>]}@:",
    b"{simd_double4x4=[4<4d>]}@:d",
    b"{simd_float2x2=[2<2f>]}@:",
    b"{simd_float3x3=[3<3f>]}@:",
    b"{simd_float4x4=[4<4f>]}@:",
    b"{simd_float4x4=[4<4f>]}@:@d",
    b"{simd_float4x4=[4<4f>]}@:d",
    b"{simd_float4x4=[4<4f>]}@:{simd_float4x4=[4<4f>]}@",
    b"{simd_quatd=<4d>}@:d",
    b"{simd_quatf=<4f>}@:",
    b"{simd_quatf=<4f>}@:d",
    b"<16C>@:",
    b"{MPSImageHistogramInfo=QZ<4f><4f>}@:",
    b"{_MPSAxisAlignedBoundingBox=<3f><3f>}@:",
]

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
#endif /*  PyObjC_BULD_RELEASE < 1013 */


NS_ASSUME_NONNULL_BEGIN

static inline int
extract_method_info(PyObject* method, PyObject* self, bool* isIMP, id* self_obj,
      Class* super_class, int* flags, PyObjCMethodSignature** methinfo)
{
    *isIMP = !!PyObjCIMP_Check(method);

    if (*isIMP) {
        *flags = PyObjCIMP_GetFlags(method);
        *methinfo = PyObjCIMP_GetSignature(method);
    } else {
        *flags = PyObjCSelector_GetFlags(method);
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
            if (*self_obj == nil && PyErr_Occurred()) {  // LCOV_BR_EXCL_LINE
                return -1; // LCOV_EXCL_LINE
            }

        } else {
            err = depythonify_c_value(@encode(id), self, self_obj);
            if (err == -1) return -1;
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

static PyObject* adjust_retval(PyObjCMethodSignature* methinfo, PyObject* self, int flags, PyObject* result)
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
        && PyObjCObject_Check(result)
        && !(flags & PyObjCSelector_kRETURNS_UNINITIALIZED)
        && (((PyObjCObject*)self)->flags & PyObjCObject_kUNINITIALIZED)) {

        [PyObjCObject_GetObject(result) release]; /* XXX??? */
        PyObjCObject_ClearObject(self);
    }
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

#import <GameplayKit/GameplayKit.h>
#import <MetalPerformanceShaders/MetalPerformanceShaders.h>
#import <ModelIO/ModelIO.h>

@interface OC_VectorCall : NSObject {
    PyObject* values;
}
@end


static PyObject* clsvalues = NULL;
static BOOL shouldRaise = NO;

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

-(BOOL)shouldRaise
{
   return shouldRaise;
}
+(BOOL)shouldRaise
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

-(id _Nullable)storedvalue
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

+(id _Nullable)storedvalue
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

@interface OC_VectorCallInvoke: NSObject {
}
@end

@implementation OC_VectorCallInvoke

"""

TESTEXT_SUFFIX = """\
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

    if (PyModule_AddObject(m, "OC_VectorCall", PyObjC_IdToPython([OC_VectorCall class])) < 0) {
        return NULL;
    }
    if (PyModule_AddObject(m, "OC_VectorCallInvoke", PyObjC_IdToPython([OC_VectorCallInvoke class])) < 0) {
        return NULL;
    }

    return m;
}
"""

TEST_PREFIX = """\
#
# This file is generated using Tools/generate-helpers-vector.py
#
#    ** DO NOT EDIT **
#
from PyObjCTools.TestSupport import TestCase
import objc
from functools import partial
from objc import simd


# Needs to be replaced by minimal definitions for
# CGColor and CGColorSpace
import Quartz # noqa: F401

from .vectorcall import OC_VectorCall, OC_VectorCallInvoke

class NoObjCClass:
    @property
    def __pyobjc_object__(self):
        raise TypeError("Cannot proxy")

class NoBool:
    def __bool__(self):
        raise TypeError("no valid in boolean context")

NoObjCValueObject = NoObjCClass()

# Register full signatures for the helper methods
"""

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


def function_name(prefix: str, signature: bytes) -> str:
    """
    Return the function name for a specific role and signature
    """
    name = [prefix]
    for idx, part in enumerate(objc.splitSignature(signature)):
        if idx in (1, 2):
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

            # Likely a CFType
            name.append(label.lstrip("_"))

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


def generate_call(stream: typing.IO[str], signature: bytes) -> None:
    """
    Generate the function to call a selector with the specified signature
    """
    # XXX: For methods returning an object check if self is uninitialized
    #      (see FFI caller)
    signature_parts = objc.splitSignature(signature)
    rv_type = signature_parts[0]
    arg_types = signature_parts[3:]

    print("", file=stream)
    print("static PyObject* _Nullable", file=stream)
    print(f"{function_name(CALL_PREFIX, signature)}(", file=stream)
    if arg_types:
        print(
            "    PyObject* method, PyObject* self, PyObject* const* arguments, size_t nargs)",
            file=stream,
        )
    else:
        print(
            "    PyObject* method, PyObject* self, PyObject* const* arguments __attribute__((__unused__)), size_t nargs)",
            file=stream,
        )
    print("{", file=stream)
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
        arg_type_names = ", " + ", ".join([describe_type(arg) for arg in arg_types])
        arg_names = ", " + ", ".join(f"arg{idx}" for idx in range(len(arg_types)))
    else:
        arg_type_names = ""
        arg_names = ""

    print("    bool isIMP;", file=stream)
    print("    id self_obj;", file=stream)
    print("    Class super_class;", file=stream)
    print("    int flags;", file=stream)
    print("    PyObjCMethodSignature* methinfo;", file=stream)
    print("", file=stream)
    print(
        "    if (extract_method_info(method, self, &isIMP, &self_obj, &super_class, &flags, &methinfo) == -1) {",
        file=stream,
    )
    print("         return NULL;", file=stream)
    print("    }", file=stream)
    print("    Py_BEGIN_ALLOW_THREADS", file=stream)
    print("    @try {", file=stream)
    print("        if (isIMP) {", file=stream)
    print(
        f"            {'rv = ' if rv_type != objc._C_VOID else ''}(({describe_type(rv_type)}(*)(id, SEL{arg_type_names}))(PyObjCIMP_GetIMP(method)))(",  # noqa: B950
        file=stream,
    )
    print(
        f"                self_obj, PyObjCIMP_GetSelector(method){arg_names});",
        file=stream,
    )
    print("", file=stream)
    print("        } else {", file=stream)
    print("            super.receiver    = self_obj;", file=stream)
    print("            super.super_class = super_class;", file=stream)
    print("", file=stream)
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
    print("        }", file=stream)
    print("", file=stream)
    print(
        "        } @catch (NSObject * localException) {  // LCOV_EXCL_LINE", file=stream
    )
    print("            PyObjCErr_FromObjC(localException);", file=stream)
    print("        } // LCOV_EXCL_LINE", file=stream)
    print("        Py_END_ALLOW_THREADS", file=stream)
    print("", file=stream)
    print("        if (PyErr_Occurred()) {", file=stream)
    print("            return NULL;", file=stream)
    print("        }", file=stream)
    print("", file=stream)

    if rv_type == objc._C_ID:
        print(
            f'    return adjust_retval(methinfo, self, flags, pythonify_c_value("{rv_type.decode()}", &rv));',
            file=stream,
        )

    elif rv_type != objc._C_VOID:
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
    # - For methods returning an object: check if the 'methinfo'
    #   says that the result is "already_retained" or "already_cfretained"
    #   and adjust the retaincount
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
    print(f"        PyObject* args[{len(arg_types)+2}] = {{NULL}};", file=stream)
    print(
        "        PyObject* pyself = PyObjCObject_NewTransient(self, &cookie);",
        file=stream,
    )
    print("        if (pyself == NULL) {", file=stream)
    print("            goto error;", file=stream)
    print("        }", file=stream)
    print("", file=stream)
    print("        args[1] = pyself;", file=stream)
    for idx, tp in enumerate(arg_types):
        print(
            f'        args[{idx+2}] = pythonify_c_value("{tp.decode()}", &arg{idx});',
            file=stream,
        )
        print(f"        if (args[{idx+2}] == NULL) goto error;", file=stream)
    print("", file=stream)
    print(
        "        PyObject* result = PyObject_Vectorcall(callable, args + 1,",
        file=stream,
    )
    print(
        f"                                          {len(arg_types)+1} | PY_VECTORCALL_ARGUMENTS_OFFSET, NULL);",
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
        print(
            f'        if (depythonify_c_value("{rv_type.decode()}", result, &oc_result) == -1) {{',
            file=stream,
        )
        print("            Py_DECREF(result);", file=stream)
        print("            goto error;", file=stream)
        print("         }", file=stream)
        print("", file=stream)
    print("        Py_DECREF(result);", file=stream)
    print(f"        for (size_t i = 2; i < {len(arg_types)+2}; i++) {{", file=stream)
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
    print("        if (pyself) {", file=stream)
    print("            PyObjCObject_ReleaseTransient(pyself, cookie);", file=stream)
    print("        }", file=stream)
    print("", file=stream)
    print(f"        for (size_t i = 2; i < {len(arg_types)+2}; i++) {{", file=stream)
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


def generate_setup_function(stream: typing.IO[str]):
    """
    Generate the function that's used to register
    the generated functions with the core bridge.
    """
    # XXX: Register the mkimp implementation "somewhere"
    #      Preferable: drop the older PyObjCUnsupportedMethod_IMP
    #       variant, mkimp is a better interface because this
    #       matches the semantics of the FFI caller.
    #
    #       This requires wider changes..
    print("int", file=stream)
    print(
        "PyObjC_setup_simd(PyObject* module __attribute__((__unused__)))", file=stream
    )
    print("{", file=stream)

    seen_call = {}
    seen_mkimp = {}
    for idx, signature in enumerate(ALL_SIGNATURES):
        if b"GKBox" in signature:
            print("#if PyObjC_BUILD_RELEASE >= 1012", file=stream)
        if b"MDL" in signature:
            print("#if PyObjC_BUILD_RELEASE >= 1011", file=stream)
        if b"MPS" in signature:
            print("#if PyObjC_BUILD_RELEASE >= 1013", file=stream)
        call_name = function_name(CALL_PREFIX, signature)
        mkimp_name = function_name(MKIMP_PREFIX, signature)

        if call_name in seen_call:
            raise RuntimeError(f"{call_name}: {idx!r} {seen_call[call_name]!r}")
        if mkimp_name in seen_call:
            raise RuntimeError(f"{mkimp_name}: {idx!r} {seen_mkimp[mkimp_name]!r}")

        seen_call[call_name] = idx
        seen_mkimp[mkimp_name] = idx

        print("", file=stream)
        print(
            "    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE", file=stream
        )
        print(f'        "{signature.decode()}",', file=stream)
        print(f"        {call_name},", file=stream)
        print(f"        {mkimp_name}) == -1) {{", file=stream)
        print("            return -1; // LCOV_EXCL_LINE", file=stream)
        print("    }", file=stream)

        alt_signature = BOOL_to_bool(signature)
        if alt_signature != signature:
            # Types "BOOL" and "bool" have different encoding, but
            # are treated the same. Make sure that both are handled.
            print("", file=stream)
            print(
                "    if (PyObjC_RegisterSignatureMapping( // LCOV_BR_EXCL_LINE",
                file=stream,
            )
            print(f'        "{alt_signature.decode()}",', file=stream)
            print(f"        {call_name},", file=stream)
            print(f"        {mkimp_name}) == -1) {{", file=stream)
            print("            return -1; // LCOV_EXCL_LINE", file=stream)
            print("    }", file=stream)

        if b"GKBox" in signature:
            print("#endif /* PyObjC_BUILD_RELEASE >= 1012 */", file=stream)
        if b"MDL" in signature:
            print("#endif /* PyObjC_BUILD_RELEASE >= 1011 */", file=stream)
        if b"MPS" in signature:
            print("#endif /* PyObjC_BUILD_RELEASE >= 1013 */", file=stream)

    print("", file=stream)
    print("    return 0;", file=stream)
    print("}", file=stream)


def sel_for_signature(signature):
    name = []
    for idx, part in enumerate(objc.splitSignature(signature)):
        if idx in (1, 2):
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

            # Likely a CFType
            name.append(label.lstrip("_"))

        else:
            raise RuntimeError(f"Don't know how to handle {part!r} in {signature!r}")

    # [ returnvalue, arg, arg ]
    if len(name) == 1:
        return name[0]
    else:
        return name[0] + ":".join(name[1:]) + ":"
    # return ":".join(name) + (":" if len(name) > 1 else "")


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


def generate_testext_callimp(stream, signature, instance=True):
    # XXX: Add some kind of hook to raise an exception when the method is called.
    parts = objc.splitSignature(signature)
    sel = sel_for_signature(signature)
    if not instance:
        sel = "cls" + sel

    if ":" not in sel:
        print(
            f"{'-' if instance else '+'} ({describe_type(parts[0])}){sel}", file=stream
        )
        print("{", file=stream)
        print("    if ([self shouldRaise]) {", file=stream)
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

    print(
        f"{'-' if instance else '+'} ({describe_type(parts[0])})", end="", file=stream
    )
    for idx, selpart in enumerate(sel.split(":")[:-1]):
        print(
            f"{selpart}:({describe_type(parts[idx+3])})arg{idx}", end=" ", file=stream
        )
    print("\n{", file=stream)
    print("    PyObject* items;", file=stream)
    print("    PyObject* tmp;", file=stream)
    print("", file=stream)
    print("    if ([self shouldRaise]) {", file=stream)
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
        print(
            f'        tmp = PyObjC_ObjCToPython("{parts[idx+3].decode()}", &arg{idx});',
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
            f"{selpart}:{as_objc_literal(parts[idx+3], valid_value(parts[idx+3]))} ",
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
    # This registers the custom metadata on NSObject because
    # this allows reusing the registration for both the C extension
    # as the Python implementation.
    #
    # The selector names are specializedenough to not cause problems here.

    print(
        f'objc.registerMetaDataForSelector(b"NSObject", '
        f'b"{sel_for_signature(signature)}", '
        f'{{"full_signature": b"{signature.decode()}"}})',
        file=stream,
    )
    print(
        f'objc.registerMetaDataForSelector(b"NSObject", '
        f'b"cls{sel_for_signature(signature)}", '
        f'{{"full_signature": b"{signature.decode()}"}})',
        file=stream,
    )


class LiteralRepr:
    def __init__(self, value: str, objc_value: typing.Optional[str] = None) -> None:
        self._value = value

        if objc_value is not None:
            self._objc_literal = lambda: objc_value

    def __repr__(self) -> str:
        return self._value


# VAlues to use during testing, valid entries must match what's used in
# the ObjC generator for return values.
VALUES = {
    # typestr: (valid, invalid)
    objc._C_ID: ("hello", LiteralRepr("NoObjCValueObject")),
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


def generate_call_testcase(stream, signature, *, instance=True, imp=False):
    oc_sel = sel_for_signature(signature)
    if not instance:
        oc_sel = "cls" + oc_sel
    sel = oc_sel.replace(":", "_")

    print(f"    def test_{sel}{'_imp' if imp else ''}(self):", file=stream)
    sigparts = objc.splitSignature(signature)
    print("        OC_VectorCall.clearRaise()", file=stream)
    print("        # Verify method type", file=stream)
    print(
        f"        self.assert{not instance}(OC_VectorCall.{sel}.isClassMethod)",
        file=stream,
    )

    print("        # Check that the signature is as expected", file=stream)
    print(
        f"        self.assertResultHasType(OC_VectorCall.{sel}, {sigparts[0]})",
        file=stream,
    )
    for idx, p in enumerate(sigparts[3:]):
        print(
            f"        self.assertArgHasType(OC_VectorCall.{sel}, {idx}, {p})",
            file=stream,
        )
    print("", file=stream)
    print("        # Create test object", file=stream)
    if instance:
        print("        oc = OC_VectorCall.alloc().init()", file=stream)
    else:
        print("        oc = OC_VectorCall", file=stream)
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
    print("", file=stream)
    print("        # Valid call", file=stream)
    print(
        f"        rv = caller({', '.join(repr(valid_value(s))  for s in sigparts[3:])})",
        file=stream,
    )
    if sigparts[0] == objc._C_VOID:
        print("        self.assertIs(rv, None)", file=stream)
    else:
        print(
            f"        self.assertEqual(rv, {valid_value(sigparts[0])!r})", file=stream
        )

    print("", file=stream)

    print("        stored = oc.storedvalue()", file=stream)
    print("        self.assertIsInstance(stored, (list, tuple))", file=stream)
    print(f"        self.assertEqual(len(stored), {len(sigparts)-3})", file=stream)
    for i, s in enumerate(sigparts[3:]):
        print(f"        self.assertEqual(stored[{i}], {valid_value(s)!r})", file=stream)
    print("", file=stream)

    if len(sigparts) > 3:
        print("        # Too few arguments call", file=stream)
        print(
            "        with self.assertRaisesRegex(TypeError, 'expected.*arguments.*got'):",
            file=stream,
        )
        print(
            f"            caller({', '.join(repr(valid_value(s))  for s in sigparts[3:-1])})",
            file=stream,
        )
    print("", file=stream)
    print("        # Too many arguments call", file=stream)
    print(
        "        with self.assertRaisesRegex(TypeError, 'expected.*arguments.*got'):",
        file=stream,
    )
    print(
        f"            caller({', '.join(repr(valid_value(s))  for s in sigparts[3:] + (sigparts[1],))})",
        file=stream,
    )
    print("", file=stream)
    if len(sigparts) > 3:
        print("        # Bad value for arguments", file=stream)
    for idx in range(len(sigparts) - 3):
        print("        with self.assertRaises((TypeError, ValueError)):", file=stream)
        print(
            f"            caller("
            f"{', '.join(repr(invalid_value(s) if i == idx else valid_value(s)) for i, s in enumerate(sigparts[3:]))})",
            file=stream,
        )
        print("", file=stream)

    print("        # Exception handling", file=stream)
    print("        OC_VectorCall.setRaise()", file=stream)
    print(
        "        with self.assertRaisesRegex(objc.error, 'SimpleException'):",
        file=stream,
    )
    print(
        f"            caller({', '.join(repr(valid_value(s))  for s in sigparts[3:])})",
        file=stream,
    )

    if imp:
        print("", file=stream)
        print("        # Call with invalid type for self", file=stream)
        if instance:
            print(
                "        with self.assertRaisesRegex(ValueError, 'unrecognized selector'):",
                file=stream,
            )
        else:
            print(
                "        with self.assertRaisesRegex(TypeError, 'Need Objective-C object or class as self'):",
                file=stream,
            )
        print(
            f"            imp(42, {', '.join(repr(valid_value(s))  for s in sigparts[3:])})",
            file=stream,
        )
        if instance:
            print("", file=stream)
            print(
                "        with self.assertRaisesRegex(TypeError, 'Cannot proxy'):",
                file=stream,
            )
            print(
                f"            imp(NoObjCValueObject, {', '.join(repr(valid_value(s))  for s in sigparts[3:])})",
                file=stream,
            )

    print("", file=stream)

    # XXX: Actually test
    #
    # - Second test (requires more updates: class method instead of instance)
    # - Third/fourth test: Call through IMP for instance/class method


def generate_imp_testhelper(stream, signature, instance=True):
    signature_parts = objc.splitSignature(signature)
    oc_sel = sel_for_signature(signature)
    sel = oc_sel.replace(":", "_")

    arg_names = tuple(f"arg{idx}" for idx in range(len(signature_parts) - 3))

    if not instance:
        print("    @classmethod", file=stream)

    if arg_names:
        print(f"    def {sel}(self, {', '.join(arg_names)}):", file=stream)
        print(f"        self.argvalues = ({', '.join(arg_names)},)", file=stream)
    else:
        print(f"    def {sel}(self):", file=stream)
        print("        self.argvalues = None", file=stream)

    print("        if getattr(self, 'shouldRaise', False):", file=stream)
    print("            raise RuntimeError('failure!')", file=stream)

    if signature_parts[0] != objc._C_VOID:
        print(f"        return {repr(valid_value(signature_parts[0]))}", file=stream)

    print("", file=stream)


def generate_imp_testcase(stream, signature, instance=True):
    signature_parts = objc.splitSignature(signature)
    oc_sel = sel_for_signature(signature)
    sel = oc_sel.replace(":", "_")

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
        "            with self.assertRaisesRegex(RuntimeError, 'failure'):", file=stream
    )
    print(
        f"                OC_VectorCallInvoke.{oc_sel.replace(':', '')}On_(value)",
        file=stream,
    )
    print("        finally:", file=stream)
    print("            del value.shouldRaise", file=stream)

    print("", file=stream)


def main():
    # Helper in objc._objc
    with open(HELPER_FILE, "w") as stream:
        print(HELPER_PREFIX, file=stream)
        for signature in ALL_SIGNATURES:
            if b"GKBox" in signature:
                print("#if PyObjC_BUILD_RELEASE >= 1012", file=stream)

            generate_call(stream, signature)
            generate_mkimp(stream, signature)
            if b"GKBox" in signature:
                print("#endif /* PyObjC_BUILD_RELEASE >= 1012 */", file=stream)
        generate_setup_function(stream)
        print("NS_ASSUME_NONNULL_END", file=stream)

    # Test extension for testing calling
    with open(TESTEXT_FILE, "w") as stream:
        print(TESTEXT_PREFIX, file=stream)

        for signature in ALL_SIGNATURES:
            generate_testext_callimp(stream, signature)
            generate_testext_callimp(stream, signature, instance=False)

        print(TESTEXT_MID, file=stream)

        for signature in ALL_SIGNATURES:
            generate_testext_callfromobjc(stream, signature)

        print(TESTEXT_SUFFIX, file=stream)

    # Test extension for testing implementing
    #  (or in same file?)

    # Unittest file
    with open(TEST_FILE, "w") as stream:
        print(TEST_PREFIX, file=stream)

        for signature in ALL_SIGNATURES:
            generate_register(stream, signature)

        print("", file=stream)
        print("class OC_VectorCallInstance(objc.lookUpClass('NSObject')):", file=stream)
        for signature in ALL_SIGNATURES:
            generate_imp_testhelper(stream, signature)

        print("", file=stream)
        print("class OC_VectorCallClass(objc.lookUpClass('NSObject')):", file=stream)
        for signature in ALL_SIGNATURES:
            generate_imp_testhelper(stream, signature, instance=False)

        print("", file=stream)
        print(TESTCASE, file=stream)
        for signature in ALL_SIGNATURES:
            generate_call_testcase(stream, signature)
            generate_call_testcase(stream, signature, instance=False)

            generate_call_testcase(stream, signature, imp=True)
            generate_call_testcase(stream, signature, instance=False, imp=True)

            generate_imp_testcase(stream, signature)
            generate_imp_testcase(stream, signature, instance=False)


if __name__ == "__main__":
    main()
