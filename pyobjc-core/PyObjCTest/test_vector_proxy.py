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
objc.registerMetaDataForSelector(
    b"OC_Vector", b"calcId:andFloat2:", {"full_signature": b"@@:@<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"calcId:andFloat3:", {"full_signature": b"@@:@<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"calcId:andFloat4:", {"full_signature": b"@@:@<4f>"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"setVectorFloat2:", {"full_signature": b"v@:<2f>"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"setVectorFloat3:", {"full_signature": b"v@:<3f>"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"setVectorFloat4:", {"full_signature": b"v@:<4f>"}
)

objc.registerMetaDataForSelector(
    b"OC_Vector", b"getVectorUChar16", {"full_signature": b"<16C>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"getVectorDouble2", {"full_signature": b"<2d>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"getVectorFloat2", {"full_signature": b"<2f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"getVectorFloat3", {"full_signature": b"<3f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"getVectorFloat4", {"full_signature": b"<4f>@:"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"getVectorInt2", {"full_signature": b"<2i>@:"}
)

"""
GET_VALUE(getGKBox, GKBox, ((GKBox){{1.5, 2.5, 3.5}, {4.5, 5.5, 6.5}}))
GET_VALUE(getGKQuad, GKQuad, ((GKQuad){{7.5, 8.5}, {9.5, 10.5}}))
GET_VALUE(getMDLAxisAlignedBoundingBox, MDLAxisAlignedBoundingBox,
GET_VALUE(getMDLVoxelIndexExtent, MDLVoxelIndexExtent,
GET_VALUE(getMPSAxisAlignedBoundingBox, MPSAxisAlignedBoundingBox,
GET_VALUE(getMPSImageHistogramInfo, MPSImageHistogramInfo,
GET_VALUE(getMatrixDouble4x4, matrix_double4x4,
GET_VALUE(getMatrixFloat2x2, matrix_float2x2,
GET_VALUE(getMatrixFloat3x3, matrix_float3x3,
GET_VALUE(getMatrixFloat4x4, matrix_float4x4,
GET_VALUE(getSimdFloat4x4, simd_float4x4,
GET_VALUE(getSimdQautf, simd_quatf, ((simd_quatf){{-420.5, -421.5, -422.5}}))
"""


# XXX: Add test that tries to call before overriding with 'full_signature'


class TestMethods(TestCase):
    def test_return_vector_float3(self):
        self.assertResultHasType(
            OC_Vector.getVectorFloat3, simd.vector_float3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        self.assertEqual(oc.getVectorFloat3(), simd.vector_float3(-8.5, 9.5, 12.5))

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 1"):
            oc.getVectorFloat3(42)

    def test_calcId_andFloat2(self):
        self.assertArgHasType(
            OC_Vector.calcId_andFloat2_, 1, simd.vector_float2.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.calcId_andFloat2_("hello", (1.5, 2.5))
        self.assertEqual(result, (("hello", simd.vector_float2(1.5, 2.5))))

    def test_calcId_andFloat3(self):
        self.assertArgHasType(
            OC_Vector.calcId_andFloat3_, 1, simd.vector_float3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.calcId_andFloat3_("hello2", (1.5, 2.5, 3.5))
        self.assertEqual(result, (("hello2", simd.vector_float3(1.5, 2.5, 3.5))))

    def test_calcId_andFloat4(self):
        self.assertArgHasType(
            OC_Vector.calcId_andFloat4_, 1, simd.vector_float4.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.calcId_andFloat4_("hello2", (-1.5, -2.5, -3.5, -4.5))
        self.assertEqual(
            result, (("hello2", simd.vector_float4(-1.5, -2.5, -3.5, -4.5)))
        )

    def test_setVectorFloat2(self):
        self.assertArgHasType(
            OC_Vector.setVectorFloat2_, 0, simd.vector_float2.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.setVectorFloat2_((-1.5, -2.5))
        self.assertIs(result, None)

        value = oc.getAndResetValues()
        self.assertEqual(value, simd.vector_float2(-1.5, -2.5))

    def test_setVectorFloat3(self):
        self.assertArgHasType(
            OC_Vector.setVectorFloat3_, 0, simd.vector_float3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.setVectorFloat3_((-1.5, -2.5, 4.5))
        self.assertIs(result, None)

        value = oc.getAndResetValues()
        self.assertEqual(value, simd.vector_float3(-1.5, -2.5, 4.5))

    def test_setVectorFloat4(self):
        self.assertArgHasType(
            OC_Vector.setVectorFloat4_, 0, simd.vector_float4.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.setVectorFloat4_((-1.5, -2.5, 4.5, 99.5))
        self.assertIs(result, None)

        value = oc.getAndResetValues()
        self.assertEqual(value, simd.vector_float4(-1.5, -2.5, 4.5, 99.5))

    def test_getVectorUChar16(self):
        self.assertResultHasType(
            OC_Vector.getVectorUChar16, simd.vector_uchar16.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getVectorUChar16()
        self.assertEqual(
            result,
            simd.vector_uchar16(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 16),
        )

    def test_getVectorDouble2(self):
        self.assertResultHasType(
            OC_Vector.getVectorDouble2, simd.vector_double2.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getVectorDouble2()
        self.assertEqual(result, simd.vector_double2(-42.9, 42.8))

    def test_getVectorFloat2(self):
        self.assertResultHasType(
            OC_Vector.getVectorFloat2, simd.vector_float2.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getVectorFloat2()
        self.assertEqual(result, simd.vector_float2(-9.5, 10.5))

    def test_getVectorFloat3(self):
        self.assertResultHasType(
            OC_Vector.getVectorFloat3, simd.vector_float3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getVectorFloat3()
        self.assertEqual(result, simd.vector_float3(-8.5, 9.5, 12.5))

    def test_getVectorFloat4(self):
        self.assertResultHasType(
            OC_Vector.getVectorFloat4, simd.vector_float4.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getVectorFloat4()
        self.assertEqual(result, simd.vector_float4(-7.5, 13.5, 14.5, 16.5))

    def test_getVectorInt2(self):
        self.assertResultHasType(OC_Vector.getVectorInt2, simd.vector_int2.__typestr__)
        oc = OC_Vector.alloc().init()
        result = oc.getVectorInt2()
        self.assertEqual(result, simd.vector_int2(42, 43))


"""
GET_VALUE(getGKBox, GKBox, ((GKBox){{1.5, 2.5, 3.5}, {4.5, 5.5, 6.5}}))
GET_VALUE(getGKQuad, GKQuad, ((GKQuad){{7.5, 8.5}, {9.5, 10.5}}))
GET_VALUE(getMDLAxisAlignedBoundingBox, MDLAxisAlignedBoundingBox,
          ((MDLAxisAlignedBoundingBox){{11.5, 12.5, 13.5}, {14.5, 15.5, 16.5}}))
GET_VALUE(getMDLVoxelIndexExtent, MDLVoxelIndexExtent,
          ((MDLVoxelIndexExtent){{-1, -2, -3, -4}, {-5, -6, -7, -8}}))
GET_VALUE(getMPSAxisAlignedBoundingBox, MPSAxisAlignedBoundingBox,
          ((MPSAxisAlignedBoundingBox){{-1.5, -2.5, -3.5}, {-5.5, -6.5, -7.5}}))
GET_VALUE(getMPSImageHistogramInfo, MPSImageHistogramInfo,
          ((MPSImageHistogramInfo){
              1ULL << 40, YES, {-8.5, -9.5, -10.5, -11.5}, {-12.5, -13.5, -14.5, -15.5}}))
GET_VALUE(getMatrixDouble4x4, matrix_double4x4,
          ((matrix_double4x4){{{-20.5, -21.5, -22.5, -23.5},
                               {-30.5, -31.5, -32.5, -33.5},
                               {-40.5, -41.5, -42.5, -43.5},
                               {-50.5, -51.5, -52.5, -53.5}}}))
GET_VALUE(getMatrixFloat2x2, matrix_float2x2,
          ((matrix_float2x2){{{-20.5, -21.5}, {-30.5, -31.5}}}))
GET_VALUE(getMatrixFloat3x3, matrix_float3x3,
          ((matrix_float3x3){{{-120.5, -121.5, -122.5},
                              {-130.5, -131.5, -132.5},
                              {-140.5, -141.5, -142.5}}}))
GET_VALUE(getMatrixFloat4x4, matrix_float4x4,
          ((matrix_float4x4){{{-220.5, -221.5, -222.5},
                              {-230.5, -231.5, -232.5},
                              {-240.5, -241.5, -242.5},
                              {-250.5, -251.5, -252.5}}}))
GET_VALUE(getSimdFloat4x4, simd_float4x4,
          ((simd_float4x4){{{-320.5, -321.5, -322.5},
                            {-330.5, -331.5, -332.5},
                            {-340.5, -341.5, -342.5},
                            {-350.5, -351.5, -352.5}}}))
GET_VALUE(getSimdQautf, simd_quatf, ((simd_quatf){{-420.5, -421.5, -422.5}}))
"""


class TestIMP(TestCase):
    # Similar to TestMethods, but using method IMPs.

    def test_return_vector_float3(self):
        self.assertResultHasType(
            OC_Vector.getVectorFloat3, simd.vector_float3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        imp = oc.methodForSelector_(b"getVectorFloat3")
        self.assertEqual(imp(oc), simd.vector_float3(-8.5, 9.5, 12.5))

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 1"):
            imp(oc, 42)

    # XXX: All tests in the class above should be here as well.
