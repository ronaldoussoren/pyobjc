from PyObjCTools.TestSupport import TestCase
import objc
from objc import simd

from .vector import OC_Vector

CASES = [
    (simd.vector_uchar16, range(16)),
    (simd.vector_float2, (0, 1)),
    (simd.vector_float2, (0.5, -2.5)),
    (simd.vector_float3, (1.5, 2.5, -4.5)),
    (simd.vector_float4, (-1.5, 2.5, -4.5, 6.5)),
    (simd.vector_double2, (1.0, 2.5)),
    (simd.vector_double3, (1.5, 2.5, 3.5)),
    (simd.vector_double4, (-1.5, 2.5, 3.5, 7.5)),
    (simd.vector_short2, (0, 2000)),
    (simd.vector_short2, (-500, 15000)),
    (simd.vector_ushort2, (55, 424)),
    (simd.vector_ushort3, (42, 55, 44)),
    (simd.vector_ushort4, (1, 2, 3, 4)),
    (simd.vector_int2, (1, 2)),
    (simd.vector_int2, (-1, -2)),
    (simd.vector_uint2, (1, 2)),
    (simd.vector_uint3, (1, 2, 3)),
]


class TestRepythonify(TestCase):
    def test_from_tuple(self):
        for simd_type, args in CASES:
            with self.subTest(type=simd_type, args=args):
                expected = simd_type(*args)
                value = objc.repythonify(args, simd_type.__typestr__)
                self.assertIsInstance(value, simd_type)
                self.assertEqual(value, expected)

    def test_from_sime_type(self):
        for simd_type, args in CASES:
            with self.subTest(type=simd_type, args=args):
                expected = simd_type(*args)
                value = objc.repythonify(expected, simd_type.__typestr__)
                self.assertIsInstance(value, simd_type)
                self.assertEqual(value, expected)


objc.registerMetaDataForSelector(
    b"OC_Vector", b"getVectorFloat3", {"full_signature": b"<3f>@:"}
)


# XXX: Add test that tries to call before overriding with 'full_signature'


class TestMethods(TestCase):
    def test_return_vector_float3(self):
        self.assertResultHasType(
            OC_Vector.getVectorFloat3, simd.vector_float3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        self.assertEqual(oc.getVectorFloat3(), simd.vector_float3(1.5, 2.5, 3.5))

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 1"):
            oc.getVectorFloat3(42)


class TestIMP(TestCase):
    def test_return_vector_float3(self):
        self.assertResultHasType(
            OC_Vector.getVectorFloat3, simd.vector_float3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        imp = oc.methodForSelector_(b"getVectorFloat3")
        self.assertEqual(imp(oc), simd.vector_float3(1.5, 2.5, 3.5))

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 1"):
            imp(oc, 42)
