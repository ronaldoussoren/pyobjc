from PyObjCTools.TestSupport import TestCase, min_sdk_level
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
    (simd.vector_int3, (1, 2, 3)),
    (simd.vector_int4, (1, 2, 3, 4)),
    (simd.vector_int2, (-1, -2)),
    (simd.vector_uint2, (1, 2)),
    (simd.vector_uint3, (1, 2, 3)),
]


class Fake:
    @property
    def __pyobjc_object__(self):
        raise TypeError("Cannot proxy")


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


GKBox = objc.createStructType("GKBox", b"{GKBox=<3f><3f>}", ["boxMax", "boxMin"])
GKQuad = objc.createStructType("GKQuad", b"{GKQuad=<2f><2f>}", ["quadMax", "quadMin"])
MDLAxisAlignedBoundingBox = objc.createStructType(
    "MDLAxisAlignedBoundingBox",
    b"{MDLAxisAlignedBoundingBox=<3f><3f>}",
    ["maxBounds", "minBounds"],
)
MDLVoxelIndexExtent = objc.createStructType(
    "MDLVoxelIndexExtent",
    b"{MDLVoxelIndexExtent=<4i><4i>}",
    ["maximumExtent", "minimumExtent"],
)
MPSAxisAlignedBoundingBox = objc.createStructType(
    "MPSAxisAlignedBoundingBox",
    b"{_MPSAxisAlignedBoundingBox=<3f><3f>}",
    ["max", "min"],
)
MPSImageHistogramInfo = objc.createStructType(
    "MPSImageHistogramInfo",
    b"{MPSImageHistogramInfo=QZ<4f><4f>}",
    ["numberOfHistogramEntries", "histogramForAlpha", "minPixelValue", "maxPixelValue"],
)

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
objc.registerMetaDataForSelector(
    b"OC_Vector", b"getGKBox", {"full_signature": GKBox.__typestr__ + b"@:"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector", b"getGKQuad", {"full_signature": GKQuad.__typestr__ + b"@:"}
)
objc.registerMetaDataForSelector(
    b"OC_Vector",
    b"getMDLAxisAlignedBoundingBox",
    {"full_signature": MDLAxisAlignedBoundingBox.__typestr__ + b"@:"},
)
objc.registerMetaDataForSelector(
    b"OC_Vector",
    b"getMDLVoxelIndexExtent",
    {"full_signature": MDLVoxelIndexExtent.__typestr__ + b"@:"},
)
objc.registerMetaDataForSelector(
    b"OC_Vector",
    b"getMPSAxisAlignedBoundingBox",
    {"full_signature": MPSAxisAlignedBoundingBox.__typestr__ + b"@:"},
)
objc.registerMetaDataForSelector(
    b"OC_Vector",
    b"getMPSImageHistogramInfo",
    {"full_signature": MPSImageHistogramInfo.__typestr__ + b"@:"},
)
objc.registerMetaDataForSelector(
    b"OC_Vector",
    b"getMatrixDouble4x4",
    {"full_signature": simd.simd_double4x4.__typestr__ + b"@:"},
)
objc.registerMetaDataForSelector(
    b"OC_Vector",
    b"getMatrixFloat2x2",
    {"full_signature": simd.simd_float2x2.__typestr__ + b"@:"},
)
objc.registerMetaDataForSelector(
    b"OC_Vector",
    b"getMatrixFloat3x3",
    {"full_signature": simd.simd_float3x3.__typestr__ + b"@:"},
)
objc.registerMetaDataForSelector(
    b"OC_Vector",
    b"getMatrixFloat4x4",
    {"full_signature": simd.simd_float4x4.__typestr__ + b"@:"},
)
objc.registerMetaDataForSelector(
    b"OC_Vector",
    b"getSimdFloat4x4",
    {"full_signature": simd.simd_float4x4.__typestr__ + b"@:"},
)
objc.registerMetaDataForSelector(
    b"OC_Vector",
    b"getSimdQuatf",
    {"full_signature": simd.simd_quatf.__typestr__ + b"@:"},
)


# XXX: Add test that tries to call before overriding with 'full_signature'
# XXX: Add tests that use a class method instead of an instance method


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

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 1"):
            oc.calcId_andFloat2_(42)

        with self.assertRaisesRegex(TypeError, "must be real number, not str"):
            oc.calcId_andFloat2_("", "aa")

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            oc.calcId_andFloat2_(Fake(), (42.0, 42.5))

    def test_calcId_andFloat3(self):
        self.assertArgHasType(
            OC_Vector.calcId_andFloat3_, 1, simd.vector_float3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.calcId_andFloat3_("hello2", (1.5, 2.5, 3.5))
        self.assertEqual(result, (("hello2", simd.vector_float3(1.5, 2.5, 3.5))))

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 1"):
            oc.calcId_andFloat3_(42)

        with self.assertRaisesRegex(ValueError, "Expecting value with 3 elements"):
            oc.calcId_andFloat3_("", "aa")

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            oc.calcId_andFloat3_(Fake(), (42.0, 42.5, 99.0))

    def test_calcId_andFloat4(self):
        self.assertArgHasType(
            OC_Vector.calcId_andFloat4_, 1, simd.vector_float4.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.calcId_andFloat4_("hello2", (-1.5, -2.5, -3.5, -4.5))
        self.assertEqual(
            result, (("hello2", simd.vector_float4(-1.5, -2.5, -3.5, -4.5)))
        )

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 1"):
            oc.calcId_andFloat4_(42)

        with self.assertRaisesRegex(ValueError, "Expecting value with 4 elements"):
            oc.calcId_andFloat4_("", "aa")

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            oc.calcId_andFloat4_(Fake(), (42.0, 42.5, 99.0, 99.5))

    def test_setVectorFloat2(self):
        self.assertArgHasType(
            OC_Vector.setVectorFloat2_, 0, simd.vector_float2.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.setVectorFloat2_((-1.5, -2.5))
        self.assertIs(result, None)

        value = oc.getAndResetValues()
        self.assertEqual(value, simd.vector_float2(-1.5, -2.5))

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 2"):
            oc.setVectorFloat2_(44, 42)

        with self.assertRaisesRegex(ValueError, "Expecting value with 2 elements"):
            oc.setVectorFloat2_("aaa")

    def test_setVectorFloat3(self):
        self.assertArgHasType(
            OC_Vector.setVectorFloat3_, 0, simd.vector_float3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.setVectorFloat3_((-1.5, -2.5, 4.5))
        self.assertIs(result, None)

        value = oc.getAndResetValues()
        self.assertEqual(value, simd.vector_float3(-1.5, -2.5, 4.5))

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 2"):
            oc.setVectorFloat3_(44, 42)

        with self.assertRaisesRegex(ValueError, "Expecting value with 3 elements"):
            oc.setVectorFloat3_("aa")

    def test_setVectorFloat4(self):
        self.assertArgHasType(
            OC_Vector.setVectorFloat4_, 0, simd.vector_float4.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.setVectorFloat4_((-1.5, -2.5, 4.5, 99.5))
        self.assertIs(result, None)

        value = oc.getAndResetValues()
        self.assertEqual(value, simd.vector_float4(-1.5, -2.5, 4.5, 99.5))

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 2"):
            oc.setVectorFloat4_(44, 42)

        with self.assertRaisesRegex(ValueError, "Expecting value with 4 elements"):
            oc.setVectorFloat4_("aa")

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

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getVectorUChar16(44, 42)

    def test_getVectorDouble2(self):
        self.assertResultHasType(
            OC_Vector.getVectorDouble2, simd.vector_double2.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getVectorDouble2()
        self.assertEqual(result, simd.vector_double2(-42.9, 42.8))

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getVectorDouble2(44, 42)

    def test_getVectorFloat2(self):
        self.assertResultHasType(
            OC_Vector.getVectorFloat2, simd.vector_float2.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getVectorFloat2()
        self.assertEqual(result, simd.vector_float2(-9.5, 10.5))

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getVectorFloat2(44, 42)

    def test_getVectorFloat3(self):
        self.assertResultHasType(
            OC_Vector.getVectorFloat3, simd.vector_float3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getVectorFloat3()
        self.assertEqual(result, simd.vector_float3(-8.5, 9.5, 12.5))

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getVectorFloat3(44, 42)

    def test_getVectorFloat4(self):
        self.assertResultHasType(
            OC_Vector.getVectorFloat4, simd.vector_float4.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getVectorFloat4()
        self.assertEqual(result, simd.vector_float4(-7.5, 13.5, 14.5, 16.5))

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getVectorFloat4(44, 42)

    def test_getVectorInt2(self):
        self.assertResultHasType(OC_Vector.getVectorInt2, simd.vector_int2.__typestr__)
        oc = OC_Vector.alloc().init()
        result = oc.getVectorInt2()
        self.assertEqual(result, simd.vector_int2(42, 43))

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getVectorInt2(44, 42)

    @min_sdk_level("10.12")
    def test_getGKBox(self):
        self.assertResultHasType(OC_Vector.getGKBox, GKBox.__typestr__)
        oc = OC_Vector.alloc().init()
        result = oc.getGKBox()
        self.assertEqual(
            result,
            GKBox(simd.vector_float3(1.5, 2.5, 3.5), simd.vector_float3(4.5, 5.5, 6.5)),
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getGKBox(44, 42)

    @min_sdk_level("10.12")
    def test_getGKQuad(self):
        self.assertResultHasType(OC_Vector.getGKQuad, GKQuad.__typestr__)
        oc = OC_Vector.alloc().init()
        result = oc.getGKQuad()
        self.assertEqual(
            result, GKQuad(simd.vector_float2(7.5, 8.5), simd.vector_float2(9.5, 10.5))
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getGKQuad(44, 42)

    @min_sdk_level("10.11")
    def test_getMDLAxisAlignedBoundingBox(self):
        self.assertResultHasType(
            OC_Vector.getMDLAxisAlignedBoundingBox,
            MDLAxisAlignedBoundingBox.__typestr__,
        )
        oc = OC_Vector.alloc().init()
        result = oc.getMDLAxisAlignedBoundingBox()
        self.assertEqual(
            result,
            MDLAxisAlignedBoundingBox(
                simd.vector_float3(11.5, 12.5, 13.5),
                simd.vector_float3(14.5, 15.5, 16.5),
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getMDLAxisAlignedBoundingBox(44, 42)

    @min_sdk_level("10.11")
    def test_getMDLVoxelIndexExtent(self):
        self.assertResultHasType(
            OC_Vector.getMDLVoxelIndexExtent, MDLVoxelIndexExtent.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getMDLVoxelIndexExtent()
        self.assertEqual(
            result,
            MDLVoxelIndexExtent(
                simd.vector_int4(-1, -2, -3, -4), simd.vector_int4(-5, -6, -7, -8)
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getMDLVoxelIndexExtent(44, 42)

    @min_sdk_level("10.14")
    def test_getMPSAxisAlignedBoundingBox(self):
        self.assertResultHasType(
            OC_Vector.getMPSAxisAlignedBoundingBox,
            MPSAxisAlignedBoundingBox.__typestr__,
        )
        oc = OC_Vector.alloc().init()
        result = oc.getMPSAxisAlignedBoundingBox()
        self.assertEqual(
            result,
            MPSAxisAlignedBoundingBox(
                simd.vector_float3(-1.5, -2.5, -3.5),
                simd.vector_float3(-5.5, -6.5, -7.5),
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getMPSAxisAlignedBoundingBox(44, 42)

    @min_sdk_level("10.13")
    def test_getMPSImageHistogramInfo(self):
        self.assertResultHasType(
            OC_Vector.getMPSImageHistogramInfo, MPSImageHistogramInfo.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getMPSImageHistogramInfo()
        self.assertEqual(
            result,
            MPSImageHistogramInfo(
                1 << 40,
                True,
                simd.vector_float4(-8.5, -9.5, -10.5, -11.5),
                simd.vector_float4(-12.5, -13.5, -14.5, -15.5),
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getMPSImageHistogramInfo(44, 42)

    def test_getMatrixDouble4x4(self):
        self.assertResultHasType(
            OC_Vector.getMatrixDouble4x4, simd.simd_double4x4.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getMatrixDouble4x4()
        self.assertEqual(
            result,
            simd.simd_double4x4(
                (
                    simd.vector_double4(-20.5, -21.5, -22.5, -23.5),
                    simd.vector_double4(-30.5, -31.5, -32.5, -33.5),
                    simd.vector_double4(-40.5, -41.5, -42.5, -43.5),
                    simd.vector_double4(-50.5, -51.5, -52.5, -53.5),
                )
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getMatrixDouble4x4(44, 42)

    def test_getMatrixFloat2x2(self):
        self.assertResultHasType(
            OC_Vector.getMatrixFloat2x2, simd.simd_float2x2.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getMatrixFloat2x2()
        self.assertEqual(
            result,
            simd.simd_float2x2(
                (
                    simd.vector_float2(-20.5, -21.5),
                    simd.vector_float2(-30.5, -31.5),
                )
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getMatrixFloat2x2(44, 42)

    def test_getMatrixFloat3x3(self):
        self.assertResultHasType(
            OC_Vector.getMatrixFloat3x3, simd.simd_float3x3.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getMatrixFloat3x3()
        self.assertEqual(
            result,
            simd.simd_float3x3(
                (
                    simd.vector_float3(-120.5, -121.5, -122.5),
                    simd.vector_float3(-130.5, -131.5, -132.5),
                    simd.vector_float3(-140.5, -141.5, -142.5),
                )
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getMatrixFloat3x3(44, 42)

    def test_getMatrixFloat4x4(self):
        self.assertResultHasType(
            OC_Vector.getMatrixFloat4x4, simd.simd_float4x4.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getMatrixFloat4x4()
        self.assertEqual(
            result,
            simd.simd_float4x4(
                (
                    simd.vector_float4(-220.5, -221.5, -222.5, 10.5),
                    simd.vector_float4(-230.5, -231.5, -232.5, 11.5),
                    simd.vector_float4(-240.5, -241.5, -242.5, 12.5),
                    simd.vector_float4(-250.5, -251.5, -252.5, 13.5),
                )
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getMatrixFloat4x4(44, 42)

    @min_sdk_level("10.13")
    def test_getSimdFloat4x4(self):
        self.assertResultHasType(
            OC_Vector.getSimdFloat4x4, simd.simd_float4x4.__typestr__
        )
        oc = OC_Vector.alloc().init()
        result = oc.getSimdFloat4x4()
        self.assertEqual(
            result,
            simd.simd_float4x4(
                (
                    simd.vector_float4(-320.5, -321.5, -322.5, 1.5),
                    simd.vector_float4(-330.5, -331.5, -332.5, 2.5),
                    simd.vector_float4(-340.5, -341.5, -342.5, 3.5),
                    simd.vector_float4(-350.5, -351.5, -352.5, 4.5),
                )
            ),
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getSimdFloat4x4(44, 42)

    @min_sdk_level("10.13")
    def test_getSimdQuatf(self):
        self.assertResultHasType(OC_Vector.getSimdQuatf, simd.simd_quatf.__typestr__)
        oc = OC_Vector.alloc().init()
        result = oc.getSimdQuatf()
        self.assertEqual(
            result, simd.simd_quatf(simd.vector_float4(-420.5, -421.5, -422.5, 0))
        )

        with self.assertRaisesRegex(TypeError, "expected no arguments, got 2"):
            oc.getSimdQuatf(44, 42)

    def test_with_unsupported_vector_type(self):
        with self.assertRaisesRegex(
            NotImplementedError, "Cannot generate IMP for mymethodWithA:b:c:"
        ):

            class OC_VectorProxyUnsupportedA(objc.lookUpClass("NSObject")):
                @objc.objc_method(signature=b"<3f>@:<4f><3f><2f>")
                def mymethodWithA_b_c_(self, a, b, c):
                    return 1

        with self.assertRaisesRegex(
            NotImplementedError, "Cannot generate IMP for mymethodWithA:b:c:"
        ):

            class OC_VectorProxyUnsupportedB(objc.lookUpClass("NSObject")):
                @objc.objc_method(signature=b"<3f>@:<4f><3f><2f>", isclass=True)
                def mymethodWithA_b_c_(self, a, b, c):
                    return 1


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
