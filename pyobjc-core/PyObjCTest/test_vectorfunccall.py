#
# This file is generated using Tools/generate-helpers-vector.py
#
#     ** DO NOT EDIT **
#
from functools import partial  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_os_level  # noqa: F401
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


class NoObjCClass:
    @property
    def __pyobjc_object__(self):
        raise TypeError("Cannot proxy")


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
