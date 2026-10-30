#
# This file is generated using Tools/generate-helpers-vector.py
#
#     ** DO NOT EDIT **
#
from functools import partial  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_os_level, NoObjCClass  # noqa: F401
import objc
from objc import simd

# Tests use CGColorRef and CGColorSpaceRef. Try to import Quartz
# to get proper definitions for these types, otherwise fall back
# to minimal definitions (those aren't 100% correct, but good enough
# for these  tests)
try:
    import Quartz  # noqa: F401
except ImportError:
    CGColorRef = objc.registerCFSignature("CGColorRef", b"^{CGColor=}", 0)
    CGColorSpaceRef = objc.registerCFSignature(
        "CGColorSpaceRef", b"^{CGColorSpace=}", 0
    )

from .vectorfunccall import function_list


class NoBool:
    def __bool__(self):
        raise TypeError("no valid in boolean context")


NoObjCValueObject = NoObjCClass()

# Register full signatures for the helper methods

objc.loadFunctionList(
    function_list,
    globals(),
    [
        ("shouldRaise", b"Z"),
        ("clearRaise", b"v"),
        ("setRaise", b"v"),
        ("storedvalue", b"@"),
        ("v3fid_", b"<3f>@"),
        ("idsimdfloat4x4_", b"@{simd_float4x4=[4<4f>]}"),
        ("idsimdfloat4x4_f_f_q_", b"@{simd_float4x4=[4<4f>]}ffq"),
        ("Bid_v3f_", b"B@<3f>"),
        ("simdfloat3x3id_", b"{simd_float3x3=[3<3f>]}@"),
        ("simdfloat4x4id_", b"{simd_float4x4=[4<4f>]}@"),
        ("simdfloat4x4id_q_", b"{simd_float4x4=[4<4f>]}@q"),
        (
            "CGPointv2f_CGRect_Q_Q_",
            b"{CGPoint=dd}<2f>{CGRect={CGPoint=dd}{CGSize=dd}}QQ",
        ),
        ("v3fSCNVector3_", b"<3f>{SCNVector3=ddd}"),
        ("SCNVector3v3f_", b"{SCNVector3=ddd}<3f>"),
        ("v4fSCNVector4_", b"<4f>{SCNVector4=dddd}"),
        ("SCNVector4v4f_", b"{SCNVector4=dddd}<4f>"),
        (
            "simdfloat4x4CATransform3D_",
            b"{simd_float4x4=[4<4f>]}{CATransform3D=dddddddddddddddd}",
        ),
        (
            "CATransform3Dsimdfloat4x4_",
            b"{CATransform3D=dddddddddddddddd}{simd_float4x4=[4<4f>]}",
        ),
        (
            "simdfloat4x4cp_frame_C_v4f_v2f_",
            b"{simd_float4x4=[4<4f>]}^{cp_frame=}C<4f><2f>",
        ),
        ("simdfloat4x4cp_drawable_C_Q_", b"{simd_float4x4=[4<4f>]}^{cp_drawable=}CQ"),
        ("v4fcp_view_", b"<4f>^{cp_view=}"),
        (
            "simdfloat4x4cp_frame_I_C_v4f_v2f_",
            b"{simd_float4x4=[4<4f>]}^{cp_frame=}IC<4f><2f>",
        ),
        ("vcp_drawable_v2f_", b"v^{cp_drawable=}<2f>"),
        ("v2fcp_drawable_", b"<2f>^{cp_drawable=}"),
    ],
)


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

    def test_v3fid_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(v3fid_, b"<3f>")  # noqa: F821  # noqa: F821
        self.assertArgHasType(v3fid_, 0, b"@")  # noqa: F821

        caller = v3fid_  # noqa: F821

        # Valid call
        rv = caller("hello")
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller("hello", "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(NoObjCValueObject)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller("hello")

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0="hello")

    def test_idsimdfloat4x4_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(idsimdfloat4x4_, b"@")  # noqa: F821  # noqa: F821
        self.assertArgHasType(
            idsimdfloat4x4_, 0, b"{simd_float4x4=[4<4f>]}"  # noqa: F821
        )

        caller = idsimdfloat4x4_  # noqa: F821

        # Valid call
        rv = caller(
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            )
        )
        self.assertEqual(rv, "hello")

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                )
            )

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(
                arg0=simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                )
            )

    def test_idsimdfloat4x4_f_f_q_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            idsimdfloat4x4_f_f_q_, b"@"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(
            idsimdfloat4x4_f_f_q_, 0, b"{simd_float4x4=[4<4f>]}"  # noqa: F821
        )
        self.assertArgHasType(idsimdfloat4x4_f_f_q_, 1, b"f")  # noqa: F821
        self.assertArgHasType(idsimdfloat4x4_f_f_q_, 2, b"f")  # noqa: F821
        self.assertArgHasType(idsimdfloat4x4_f_f_q_, 3, b"q")  # noqa: F821

        caller = idsimdfloat4x4_f_f_q_  # noqa: F821

        # Valid call
        rv = caller(
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
            2500000000.0,
            2500000000.0,
            -17592186044416,
        )
        self.assertEqual(rv, "hello")

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(
            stored[0],
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )
        self.assertEqual(stored[1], 2500000000.0)
        self.assertEqual(stored[2], 2500000000.0)
        self.assertEqual(stored[3], -17592186044416)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                2500000000.0,
                2500000000.0,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                2500000000.0,
                2500000000.0,
                -17592186044416,
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(None, 2500000000.0, 2500000000.0, -17592186044416)

        with self.assertRaises((TypeError, ValueError)):
            caller(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                None,
                2500000000.0,
                -17592186044416,
            )

        with self.assertRaises((TypeError, ValueError)):
            caller(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                2500000000.0,
                None,
                -17592186044416,
            )

        with self.assertRaises((TypeError, ValueError)):
            caller(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                2500000000.0,
                2500000000.0,
                None,
            )

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                2500000000.0,
                2500000000.0,
                -17592186044416,
            )

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(
                arg0=simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                arg1=2500000000.0,
                arg2=2500000000.0,
                arg3=-17592186044416,
            )

    def test_Bid_v3f_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(Bid_v3f_, b"B")  # noqa: F821  # noqa: F821
        self.assertArgHasType(Bid_v3f_, 0, b"@")  # noqa: F821
        self.assertArgHasType(Bid_v3f_, 1, b"<3f>")  # noqa: F821

        caller = Bid_v3f_  # noqa: F821

        # Valid call
        rv = caller("hello", objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, True)

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller("hello", objc.simd.vector_float3(0.0, 1.5, 3.0), "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(NoObjCValueObject, objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaises((TypeError, ValueError)):
            caller("hello", None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller("hello", objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0="hello", arg1=objc.simd.vector_float3(0.0, 1.5, 3.0))

    def test_simdfloat3x3id_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            simdfloat3x3id_, b"{simd_float3x3=[3<3f>]}"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(simdfloat3x3id_, 0, b"@")  # noqa: F821

        caller = simdfloat3x3id_  # noqa: F821

        # Valid call
        rv = caller("hello")
        self.assertEqual(
            rv,
            simd.simd_float3x3(
                (
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                    objc.simd.vector_float3(0.0, 1.5, 3.0),
                )
            ),
        )

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller("hello", "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(NoObjCValueObject)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller("hello")

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0="hello")

    def test_simdfloat4x4id_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            simdfloat4x4id_, b"{simd_float4x4=[4<4f>]}"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(simdfloat4x4id_, 0, b"@")  # noqa: F821

        caller = simdfloat4x4id_  # noqa: F821

        # Valid call
        rv = caller("hello")
        self.assertEqual(
            rv,
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], "hello")

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller("hello", "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(NoObjCValueObject)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller("hello")

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0="hello")

    def test_simdfloat4x4id_q_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            simdfloat4x4id_q_, b"{simd_float4x4=[4<4f>]}"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(simdfloat4x4id_q_, 0, b"@")  # noqa: F821
        self.assertArgHasType(simdfloat4x4id_q_, 1, b"q")  # noqa: F821

        caller = simdfloat4x4id_q_  # noqa: F821

        # Valid call
        rv = caller("hello", -17592186044416)
        self.assertEqual(
            rv,
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], "hello")
        self.assertEqual(stored[1], -17592186044416)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller("hello")

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller("hello", -17592186044416, "hello")

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(NoObjCValueObject, -17592186044416)

        with self.assertRaises((TypeError, ValueError)):
            caller("hello", None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller("hello", -17592186044416)

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0="hello", arg1=-17592186044416)

    def test_CGPointv2f_CGRect_Q_Q_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            CGPointv2f_CGRect_Q_Q_, b"{CGPoint=dd}"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(CGPointv2f_CGRect_Q_Q_, 0, b"<2f>")  # noqa: F821
        self.assertArgHasType(
            CGPointv2f_CGRect_Q_Q_, 1, b"{CGRect={CGPoint=dd}{CGSize=dd}}"  # noqa: F821
        )
        self.assertArgHasType(CGPointv2f_CGRect_Q_Q_, 2, b"Q")  # noqa: F821
        self.assertArgHasType(CGPointv2f_CGRect_Q_Q_, 3, b"Q")  # noqa: F821

        caller = CGPointv2f_CGRect_Q_Q_  # noqa: F821

        # Valid call
        rv = caller(
            objc.simd.vector_float2(0.0, 1.5),
            ((1.0, 2.0), (3.0, 4.0)),
            35184372088832,
            35184372088832,
        )
        self.assertEqual(rv, (1.0, 2.0))

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], objc.simd.vector_float2(0.0, 1.5))
        self.assertEqual(stored[1], ((1.0, 2.0), (3.0, 4.0)))
        self.assertEqual(stored[2], 35184372088832)
        self.assertEqual(stored[3], 35184372088832)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                objc.simd.vector_float2(0.0, 1.5),
                ((1.0, 2.0), (3.0, 4.0)),
                35184372088832,
            )

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                objc.simd.vector_float2(0.0, 1.5),
                ((1.0, 2.0), (3.0, 4.0)),
                35184372088832,
                35184372088832,
                objc.simd.vector_float2(0.0, 1.5),
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(None, ((1.0, 2.0), (3.0, 4.0)), 35184372088832, 35184372088832)

        with self.assertRaises((TypeError, ValueError)):
            caller(
                objc.simd.vector_float2(0.0, 1.5), None, 35184372088832, 35184372088832
            )

        with self.assertRaises((TypeError, ValueError)):
            caller(
                objc.simd.vector_float2(0.0, 1.5),
                ((1.0, 2.0), (3.0, 4.0)),
                None,
                35184372088832,
            )

        with self.assertRaises((TypeError, ValueError)):
            caller(
                objc.simd.vector_float2(0.0, 1.5),
                ((1.0, 2.0), (3.0, 4.0)),
                35184372088832,
                None,
            )

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(
                objc.simd.vector_float2(0.0, 1.5),
                ((1.0, 2.0), (3.0, 4.0)),
                35184372088832,
                35184372088832,
            )

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(
                arg0=objc.simd.vector_float2(0.0, 1.5),
                arg1=((1.0, 2.0), (3.0, 4.0)),
                arg2=35184372088832,
                arg3=35184372088832,
            )

    def test_v3fSCNVector3_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(v3fSCNVector3_, b"<3f>")  # noqa: F821  # noqa: F821
        self.assertArgHasType(v3fSCNVector3_, 0, b"{SCNVector3=ddd}")  # noqa: F821

        caller = v3fSCNVector3_  # noqa: F821

        # Valid call
        rv = caller((1.0, 2.0, 3.0))
        self.assertEqual(rv, objc.simd.vector_float3(0.0, 1.5, 3.0))

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], (1.0, 2.0, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller((1.0, 2.0, 3.0), (1.0, 2.0, 3.0))

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller((1.0, 2.0, 3.0))

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0=(1.0, 2.0, 3.0))

    def test_SCNVector3v3f_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            SCNVector3v3f_, b"{SCNVector3=ddd}"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(SCNVector3v3f_, 0, b"<3f>")  # noqa: F821

        caller = SCNVector3v3f_  # noqa: F821

        # Valid call
        rv = caller(objc.simd.vector_float3(0.0, 1.5, 3.0))
        self.assertEqual(rv, (1.0, 2.0, 3.0))

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float3(0.0, 1.5, 3.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                objc.simd.vector_float3(0.0, 1.5, 3.0),
                objc.simd.vector_float3(0.0, 1.5, 3.0),
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(objc.simd.vector_float3(0.0, 1.5, 3.0))

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0=objc.simd.vector_float3(0.0, 1.5, 3.0))

    def test_v4fSCNVector4_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(v4fSCNVector4_, b"<4f>")  # noqa: F821  # noqa: F821
        self.assertArgHasType(v4fSCNVector4_, 0, b"{SCNVector4=dddd}")  # noqa: F821

        caller = v4fSCNVector4_  # noqa: F821

        # Valid call
        rv = caller((1.0, 2.0, 3.0, 4.0))
        self.assertEqual(rv, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], (1.0, 2.0, 3.0, 4.0))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller((1.0, 2.0, 3.0, 4.0), (1.0, 2.0, 3.0, 4.0))

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller((1.0, 2.0, 3.0, 4.0))

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0=(1.0, 2.0, 3.0, 4.0))

    def test_SCNVector4v4f_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            SCNVector4v4f_, b"{SCNVector4=dddd}"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(SCNVector4v4f_, 0, b"<4f>")  # noqa: F821

        caller = SCNVector4v4f_  # noqa: F821

        # Valid call
        rv = caller(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(rv, (1.0, 2.0, 3.0, 4.0))

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0=objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

    def test_simdfloat4x4CATransform3D_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            simdfloat4x4CATransform3D_, b"{simd_float4x4=[4<4f>]}"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(
            simdfloat4x4CATransform3D_,  # noqa: F821
            0,
            b"{CATransform3D=dddddddddddddddd}",
        )

        caller = simdfloat4x4CATransform3D_  # noqa: F821

        # Valid call
        rv = caller(
            (
                1.0,
                2.0,
                3.0,
                4.0,
                5.0,
                6.0,
                7.0,
                8.0,
                9.0,
                10.0,
                11.0,
                12.0,
                13.0,
                14.0,
                15.0,
                16.0,
            )
        )
        self.assertEqual(
            rv,
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            (
                1.0,
                2.0,
                3.0,
                4.0,
                5.0,
                6.0,
                7.0,
                8.0,
                9.0,
                10.0,
                11.0,
                12.0,
                13.0,
                14.0,
                15.0,
                16.0,
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                (
                    1.0,
                    2.0,
                    3.0,
                    4.0,
                    5.0,
                    6.0,
                    7.0,
                    8.0,
                    9.0,
                    10.0,
                    11.0,
                    12.0,
                    13.0,
                    14.0,
                    15.0,
                    16.0,
                ),
                (
                    1.0,
                    2.0,
                    3.0,
                    4.0,
                    5.0,
                    6.0,
                    7.0,
                    8.0,
                    9.0,
                    10.0,
                    11.0,
                    12.0,
                    13.0,
                    14.0,
                    15.0,
                    16.0,
                ),
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(
                (
                    1.0,
                    2.0,
                    3.0,
                    4.0,
                    5.0,
                    6.0,
                    7.0,
                    8.0,
                    9.0,
                    10.0,
                    11.0,
                    12.0,
                    13.0,
                    14.0,
                    15.0,
                    16.0,
                )
            )

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(
                arg0=(
                    1.0,
                    2.0,
                    3.0,
                    4.0,
                    5.0,
                    6.0,
                    7.0,
                    8.0,
                    9.0,
                    10.0,
                    11.0,
                    12.0,
                    13.0,
                    14.0,
                    15.0,
                    16.0,
                )
            )

    def test_CATransform3Dsimdfloat4x4_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            CATransform3Dsimdfloat4x4_,  # noqa: F821
            b"{CATransform3D=dddddddddddddddd}",
        )  # noqa: F821
        self.assertArgHasType(
            CATransform3Dsimdfloat4x4_, 0, b"{simd_float4x4=[4<4f>]}"  # noqa: F821
        )

        caller = CATransform3Dsimdfloat4x4_  # noqa: F821

        # Valid call
        rv = caller(
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            )
        )
        self.assertEqual(
            rv,
            (
                1.0,
                2.0,
                3.0,
                4.0,
                5.0,
                6.0,
                7.0,
                8.0,
                9.0,
                10.0,
                11.0,
                12.0,
                13.0,
                14.0,
                15.0,
                16.0,
            ),
        )

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(
            stored[0],
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                ),
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(
                simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                )
            )

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(
                arg0=simd.simd_float4x4(
                    (
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                        objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    )
                )
            )

    def test_simdfloat4x4cp_frame_C_v4f_v2f_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            simdfloat4x4cp_frame_C_v4f_v2f_, b"{simd_float4x4=[4<4f>]}"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(
            simdfloat4x4cp_frame_C_v4f_v2f_, 0, b"^{cp_frame=}"  # noqa: F821
        )
        self.assertArgHasType(simdfloat4x4cp_frame_C_v4f_v2f_, 1, b"C")  # noqa: F821
        self.assertArgHasType(simdfloat4x4cp_frame_C_v4f_v2f_, 2, b"<4f>")  # noqa: F821
        self.assertArgHasType(simdfloat4x4cp_frame_C_v4f_v2f_, 3, b"<2f>")  # noqa: F821

        caller = simdfloat4x4cp_frame_C_v4f_v2f_  # noqa: F821

        # Valid call
        rv = caller(
            None,
            21,
            objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
            objc.simd.vector_float2(0.0, 1.5),
        )
        self.assertEqual(
            rv,
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 4)
        self.assertEqual(stored[0], None)
        self.assertEqual(stored[1], 21)
        self.assertEqual(stored[2], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(stored[3], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(None, 21, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                None,
                21,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                objc.simd.vector_float2(0.0, 1.5),
                None,
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(
                3.5,
                21,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaises((TypeError, ValueError)):
            caller(
                None,
                None,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaises((TypeError, ValueError)):
            caller(None, 21, None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises((TypeError, ValueError)):
            caller(None, 21, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(
                None,
                21,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(
                arg0=None,
                arg1=21,
                arg2=objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                arg3=objc.simd.vector_float2(0.0, 1.5),
            )

    def test_simdfloat4x4cp_drawable_C_Q_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            simdfloat4x4cp_drawable_C_Q_, b"{simd_float4x4=[4<4f>]}"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(
            simdfloat4x4cp_drawable_C_Q_, 0, b"^{cp_drawable=}"  # noqa: F821
        )
        self.assertArgHasType(simdfloat4x4cp_drawable_C_Q_, 1, b"C")  # noqa: F821
        self.assertArgHasType(simdfloat4x4cp_drawable_C_Q_, 2, b"Q")  # noqa: F821

        caller = simdfloat4x4cp_drawable_C_Q_  # noqa: F821

        # Valid call
        rv = caller(None, 21, 35184372088832)
        self.assertEqual(
            rv,
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 3)
        self.assertEqual(stored[0], None)
        self.assertEqual(stored[1], 21)
        self.assertEqual(stored[2], 35184372088832)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(None, 21)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(None, 21, 35184372088832, None)

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(3.5, 21, 35184372088832)

        with self.assertRaises((TypeError, ValueError)):
            caller(None, None, 35184372088832)

        with self.assertRaises((TypeError, ValueError)):
            caller(None, 21, None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(None, 21, 35184372088832)

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0=None, arg1=21, arg2=35184372088832)

    def test_v4fcp_view_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(v4fcp_view_, b"<4f>")  # noqa: F821  # noqa: F821
        self.assertArgHasType(v4fcp_view_, 0, b"^{cp_view=}")  # noqa: F821

        caller = v4fcp_view_  # noqa: F821

        # Valid call
        rv = caller(None)
        self.assertEqual(rv, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], None)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(None, None)

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(3.5)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(None)

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0=None)

    def test_simdfloat4x4cp_frame_I_C_v4f_v2f_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(
            simdfloat4x4cp_frame_I_C_v4f_v2f_, b"{simd_float4x4=[4<4f>]}"  # noqa: F821
        )  # noqa: F821
        self.assertArgHasType(
            simdfloat4x4cp_frame_I_C_v4f_v2f_, 0, b"^{cp_frame=}"  # noqa: F821
        )
        self.assertArgHasType(simdfloat4x4cp_frame_I_C_v4f_v2f_, 1, b"I")  # noqa: F821
        self.assertArgHasType(simdfloat4x4cp_frame_I_C_v4f_v2f_, 2, b"C")  # noqa: F821
        self.assertArgHasType(
            simdfloat4x4cp_frame_I_C_v4f_v2f_, 3, b"<4f>"  # noqa: F821
        )
        self.assertArgHasType(
            simdfloat4x4cp_frame_I_C_v4f_v2f_, 4, b"<2f>"  # noqa: F821
        )

        caller = simdfloat4x4cp_frame_I_C_v4f_v2f_  # noqa: F821

        # Valid call
        rv = caller(
            None,
            42,
            21,
            objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
            objc.simd.vector_float2(0.0, 1.5),
        )
        self.assertEqual(
            rv,
            simd.simd_float4x4(
                (
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                    objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                )
            ),
        )

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 5)
        self.assertEqual(stored[0], None)
        self.assertEqual(stored[1], 42)
        self.assertEqual(stored[2], 21)
        self.assertEqual(stored[3], objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))
        self.assertEqual(stored[4], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(None, 42, 21, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5))

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(
                None,
                42,
                21,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                objc.simd.vector_float2(0.0, 1.5),
                None,
            )

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(
                3.5,
                42,
                21,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaises((TypeError, ValueError)):
            caller(
                None,
                None,
                21,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaises((TypeError, ValueError)):
            caller(
                None,
                42,
                None,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaises((TypeError, ValueError)):
            caller(None, 42, 21, None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises((TypeError, ValueError)):
            caller(None, 42, 21, objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5), None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(
                None,
                42,
                21,
                objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                objc.simd.vector_float2(0.0, 1.5),
            )

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(
                arg0=None,
                arg1=42,
                arg2=21,
                arg3=objc.simd.vector_float4(0.0, 1.5, 3.0, 4.5),
                arg4=objc.simd.vector_float2(0.0, 1.5),
            )

    def test_vcp_drawable_v2f_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(vcp_drawable_v2f_, b"v")  # noqa: F821  # noqa: F821
        self.assertArgHasType(vcp_drawable_v2f_, 0, b"^{cp_drawable=}")  # noqa: F821
        self.assertArgHasType(vcp_drawable_v2f_, 1, b"<2f>")  # noqa: F821

        caller = vcp_drawable_v2f_  # noqa: F821

        # Valid call
        rv = caller(None, objc.simd.vector_float2(0.0, 1.5))
        self.assertIs(rv, None)

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 2)
        self.assertEqual(stored[0], None)
        self.assertEqual(stored[1], objc.simd.vector_float2(0.0, 1.5))

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(None)

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(None, objc.simd.vector_float2(0.0, 1.5), None)

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(3.5, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaises((TypeError, ValueError)):
            caller(None, None)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(None, objc.simd.vector_float2(0.0, 1.5))

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0=None, arg1=objc.simd.vector_float2(0.0, 1.5))

    def test_v2fcp_drawable_(self):
        clearRaise()  # noqa: F821
        # Check that the signature is as expected
        self.assertResultHasType(v2fcp_drawable_, b"<2f>")  # noqa: F821  # noqa: F821
        self.assertArgHasType(v2fcp_drawable_, 0, b"^{cp_drawable=}")  # noqa: F821

        caller = v2fcp_drawable_  # noqa: F821

        # Valid call
        rv = caller(None)
        self.assertEqual(rv, objc.simd.vector_float2(0.0, 1.5))

        stored = storedvalue()  # noqa: F821
        self.assertIsInstance(stored, (list, tuple))
        self.assertEqual(len(stored), 1)
        self.assertEqual(stored[0], None)

        # Too few arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller()

        # Too many arguments call
        with self.assertRaisesRegex(TypeError, "expected.*arguments.*got"):
            caller(None, None)

        # Bad value for arguments
        with self.assertRaises((TypeError, ValueError)):
            caller(3.5)

        # Exception handling
        setRaise()  # noqa: F821
        with self.assertRaisesRegex(objc.error, "SimpleException"):
            caller(None)

        with self.assertRaisesRegex(TypeError, "does not accept keyword arguments"):
            caller(arg0=None)
