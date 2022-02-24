import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLResourceStateCommandEncoderHelper(Metal.NSObject):
    def updateTextureMappings_mode_regions_mipLevels_slices_numRegions_(
        self, a, b, c, d, e, f
    ):
        pass

    def updateTextureMapping_mode_region_mipLevel_slice_(self, a, b, c, d, e):
        pass

    def updateTextureMapping_mode_indirectBuffer_indirectBufferOffset_(
        self, a, b, c, d
    ):
        pass


class TestMTLResourceStateCommandEncoder(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLSparseTextureMappingMode)

    def test_constants(self):
        self.assertEqual(Metal.MTLSparseTextureMappingModeMap, 0)
        self.assertEqual(Metal.MTLSparseTextureMappingModeUnmap, 1)

    def test_structs(self):
        self.assertNotHasAttr(Metal, "MTLMapIndirectBufferFormat")
        # v = Metal.MTLMapIndirectBufferFormat()  # XXX: Needs work!
        # self.assertIsInstance(v.numMappings, int)
        # self.assertIs(v.mappings, None)

        v = Metal.MTLMapIndirectArguments()
        self.assertIsInstance(v.regionOriginX, int)
        self.assertIsInstance(v.regionOriginY, int)
        self.assertIsInstance(v.regionOriginZ, int)
        self.assertIsInstance(v.regionSizeWidth, int)
        self.assertIsInstance(v.regionSizeHeight, int)
        self.assertIsInstance(v.regionSizeDepth, int)
        self.assertIsInstance(v.mipMapLevel, int)
        self.assertIsInstance(v.sliceId, int)
        self.assertPickleRoundTrips(v)

    @min_sdk_level("11.0")
    def test_protocols11_0(self):
        objc.protocolNamed("MTLResourceStateCommandEncoder")

    def test_methods(self):
        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMappings_mode_regions_mipLevels_slices_numRegions_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMappings_mode_regions_mipLevels_slices_numRegions_,  # noqa: B950
            2,
            b"n^" + Metal.MTLRegion.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMappings_mode_regions_mipLevels_slices_numRegions_,  # noqa: B950
            2,
            5,
        )
        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMappings_mode_regions_mipLevels_slices_numRegions_,  # noqa: B950
            3,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMappings_mode_regions_mipLevels_slices_numRegions_,  # noqa: B950
            3,
            5,
        )
        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMappings_mode_regions_mipLevels_slices_numRegions_,  # noqa: B950
            4,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMappings_mode_regions_mipLevels_slices_numRegions_,  # noqa: B950
            4,
            5,
        )
        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMappings_mode_regions_mipLevels_slices_numRegions_,  # noqa: B950
            5,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMapping_mode_region_mipLevel_slice_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMapping_mode_region_mipLevel_slice_,  # noqa: B950
            2,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMapping_mode_region_mipLevel_slice_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMapping_mode_region_mipLevel_slice_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMapping_mode_indirectBuffer_indirectBufferOffset_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLResourceStateCommandEncoderHelper.updateTextureMapping_mode_indirectBuffer_indirectBufferOffset_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
