#!/usr/bin/env python3
"""
Helper script for generating Modules/objc/helpers-vector.m

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

"""

import objc
import typing
import pathlib
import Quartz  # noqa: F401
from objc._callable_docstr import describe_type

FILE = pathlib.Path(__file__).resolve().parent.parent / "Modules/objc/helpers-vector.m"

CALL_PREFIX = "call"
MKIMP_PREFIX = "mkimp"

# grep full_signature ../*/Lib/*/_metadata.py | sed 's@.*full_signature.: \([^ ]*\).*@\1@' | sort -u
ALL_SIGNATURES = [
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
    b"@@:@Q{_matrix_float4x4=[4<4f>]}",
    b"@@:@Z@<2i>qQqZ",
    b"@@:@q<2i>ffff",
    b"@@:@q<2i>fffff",
    b"@@:@{GKBox=<3f><3f>}",
    b"@@:@{GKQuad=<2f><2f>}",
    b"@@:@{_MDLAxisAlignedBoundingBox=<3f><3f>}f",
    b"@@:@{_matrix_float2x2=[2<2f>]}",
    b"@@:@{_matrix_float3x3=[3<3f>]}",
    b"@@:@{_matrix_float4x4=[4<4f>]}",
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
    b"@@:{_MDLVoxelIndexExtent=<4i><4i>}",
    b"@@:{_matrix_float4x4=[4<4f>]}",
    b"@@:{_matrix_float4x4=[4<4f>]}Z",
    b"Z@:<2i>@@@@",
    b"Z@:<2i>qf@@@",
    b"Z@:<4i>ZZZZ",
    b"^{CGColor=}@:<3f>",
    b"^{CGColor=}@:<3f>^{CGColorSpace=}",
    b"f@:<2f>",
    b"f@:<2i>",
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
    b"v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}",
    b"v@:{_MDLAxisAlignedBoundingBox=<3f><3f>}Z",
    b"v@:{_matrix_double4x4=[4<4d>]}",
    b"v@:{_matrix_double4x4=[4<4d>]}d",
    b"v@:{_matrix_float2x2=[2<2f>]}",
    b"v@:{_matrix_float3x3=[3<3f>]}",
    b"v@:{_matrix_float4x4=[4<4f>]}",
    b"v@:{_matrix_float4x4=[4<4f>]}d",
    b"v@:{_simd_float4x4=[4<4f>]}",
    b"v@:{_simd_quatd=<4d>}d",
    b"v@:{_simd_quatf=<4f>}",
    b"v@:{_simd_quatf=<4f>}<3f>",
    b"v@:{_simd_quatf=<4f>}d",
    b"{GKBox=<3f><3f>}@:",
    b"{GKQuad=<2f><2f>}@:",
    b"{GKTriangle=[3<3f>]}@:Q",
    b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:",
    b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:<4i>",
    b"{_MDLAxisAlignedBoundingBox=<3f><3f>}@:d",
    b"{_MDLVoxelIndexExtent=<4i><4i>}@:",
    b"{_MPSAxisAlignedBoundingBox=<3f><3f>}@:",
    b"{_MPSImageHistogramInfo=QZ<4f><4f>}@:",
    b"{_matrix_double4x4=[4<4d>]}@:",
    b"{_matrix_double4x4=[4<4d>]}@:d",
    b"{_matrix_float2x2=[2<2f>]}@:",
    b"{_matrix_float3x3=[3<3f>]}@:",
    b"{_matrix_float4x4=[4<4f>]}@:",
    b"{_matrix_float4x4=[4<4f>]}@:@d",
    b"{_matrix_float4x4=[4<4f>]}@:d",
    b"{_simd_float4x4=[4<4f>]}@:",
    b"{_simd_float4x4=[4<4f>]}@:{_simd_float4x4=[4<4f>]}@",
    b"{_simd_quatd=<4d>}@:d",
    b"{_simd_quatf=<4f>}@:",
    b"{_simd_quatf=<4f>}@:d",
]

PREFIX = """\
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
    print("static PyObject*", file=stream)
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
    print("    int isIMP = PyObjCIMP_Check(method);", file=stream)
    print("", file=stream)

    if arg_types:
        arg_type_names = ", " + ", ".join([describe_type(arg) for arg in arg_types])
        arg_names = ", " + ", ".join(f"arg{idx}" for idx in range(len(arg_types)))
    else:
        arg_type_names = ""
        arg_names = ""

    print("    Py_BEGIN_ALLOW_THREADS", file=stream)
    print("    @try {", file=stream)
    print("        if (isIMP) {", file=stream)
    print(
        f"            {'rv = ' if rv_type != objc._C_VOID else ''}(({describe_type(rv_type)}(*)(id, SEL{arg_type_names}))(PyObjCIMP_GetIMP(method)))(",  # noqa: B950
        file=stream,
    )
    print(
        f"                PyObjCObject_GetObject(self), PyObjCIMP_GetSelector(method){arg_names});",
        file=stream,
    )
    print("", file=stream)
    print("        } else {", file=stream)
    print("            super.receiver    = PyObjCObject_GetObject(self);", file=stream)
    print(
        "            super.super_class = PyObjCSelector_GetClass(method);", file=stream
    )
    print("", file=stream)
    print(
        f"            {'rv = ' if rv_type != objc._C_VOID else ''}(({describe_type(rv_type)}(*)(struct objc_super*, SEL{arg_type_names}))objc_msgSendSuper)(",  # noqa: B950
        file=stream,
    )
    print(
        f"                      &super, PyObjCSelector_GetSelector(method){arg_names});",
        file=stream,
    )
    print("        }", file=stream)
    print("", file=stream)
    print(
        "        } @catch (NSObject * localException) {  // LCOV_EXCL_LINE", file=stream
    )
    print(
        "            PyObjCErr_FromObjC(localException); // LCOV_EXCL_LINE", file=stream
    )
    print("        } // LCOV_EXCL_LINE", file=stream)
    print("        Py_END_ALLOW_THREADS", file=stream)
    print("", file=stream)
    print("        if (PyErr_Occurred()) { // LCOV_BR_EXCL_LINE", file=stream)
    print("            return NULL;        // LCOV_EXCL_LINE", file=stream)
    print("        }", file=stream)
    print("", file=stream)

    if rv_type != objc._C_VOID:
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
    #      (Preferable: drop the older PyObjCUnsupportedMethod_IMP
    #       variant, mkimp is a better interface because this
    #       matches the semantics of the FFI caller.
    #
    #       This requires wider changes..
    print("int", file=stream)
    print("PyObjC_setup_simd(void)", file=stream)
    print("{", file=stream)

    for signature in ALL_SIGNATURES:
        call_name = function_name(CALL_PREFIX, signature)
        mkimp_name = function_name(MKIMP_PREFIX, signature)
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

    print("", file=stream)
    print("    return 0;", file=stream)
    print("}", file=stream)


def main():
    with open(FILE, "w") as stream:
        print(PREFIX, file=stream)
        for signature in ALL_SIGNATURES:
            generate_call(stream, signature)
            generate_mkimp(stream, signature)
        generate_setup_function(stream)


if __name__ == "__main__":
    main()
