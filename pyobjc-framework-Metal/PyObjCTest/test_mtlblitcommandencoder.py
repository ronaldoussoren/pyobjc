import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTLBlitCommandEncoderHelper(Metal.NSObject):
    def synchronizeTexture_slice_level_(self, a, b, c):
        pass

    def copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_(  # noqa: B950
        self, a, b, c, d, e, f, g, h, i
    ):
        pass

    def copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_(  # noqa: B950
        self, a, b, c, d, e, f, g, h, i
    ):
        pass

    def copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_(  # noqa: B950
        self, a, b, c, d, e, f, g, h, i, j
    ):
        pass

    def copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_(  # noqa: B950
        self, a, b, c, d, e, f, g, h, i
    ):
        pass

    def copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_(  # noqa: B950
        self, a, b, c, d, e, f, g, h, i, j
    ):
        pass

    def fillBuffer_range_value_(self, a, b, c):
        pass

    def copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_(  # noqa: B950
        self, a, b, c, d, e, f, g, h
    ):
        pass

    def copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size_(
        self, a, b, c, d, e
    ):
        pass

    def optimizeContentsForGPUAccess_slice_level_(self, a, b, c):
        pass

    def optimizeContentsForCPUAccess_slice_level_(self, a, b, c):
        pass

    def resetCommandsInBuffer_withRange_(self, a, b):
        pass

    def optimizeIndirectCommandBuffer_withRange_(self, a, b):
        pass

    def sampleCountersInBuffer_atSampleIndex_withBarrier_(self, a, b, c):
        pass

    def resolveCounters_inRange_destinationBuffer_destinationOffset_(self, a, b, c, d):
        pass

    def getTextureAccessCounters_region_mipLevel_slice_resetCounters_countersBuffer_countersBufferOffset_(
        self, a, b, c, d, e, f, g
    ):
        pass

    def resetTextureAccessCounters_region_mipLevel_slice_(self, a, b, c, d):
        pass


class TestMTLBlitCommandEncoder(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLBlitOption)

    def test_constants(self):
        self.assertEqual(Metal.MTLBlitOptionNone, 0)
        self.assertEqual(Metal.MTLBlitOptionDepthFromDepthStencil, 1 << 0)
        self.assertEqual(Metal.MTLBlitOptionStencilFromDepthStencil, 1 << 1)
        self.assertEqual(Metal.MTLBlitOptionRowLinearPVRTC, 1 << 2)

    @min_sdk_level("10.11")
    def test_protocols10_11(self):
        objc.protocolNamed("MTLBlitCommandEncoder")

    def test_methods(self):
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.synchronizeTexture_slice_level_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.synchronizeTexture_slice_level_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            3,
            Metal.MTLOrigin.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            7,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            8,
            Metal.MTLOrigin.__typestr__,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            7,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            8,
            Metal.MTLOrigin.__typestr__,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            7,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,  # noqa: B950
            8,
            Metal.MTLOrigin.__typestr__,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,  # noqa: B950
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,  # noqa: B950
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,  # noqa: B950
            7,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,  # noqa: B950
            8,
            Metal.MTLOrigin.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,  # noqa: B950
            9,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,  # noqa: B950
            3,
            Metal.MTLOrigin.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,  # noqa: B950
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,  # noqa: B950
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,  # noqa: B950
            7,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,  # noqa: B950
            8,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,  # noqa: B950
            3,
            Metal.MTLOrigin.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,  # noqa: B950
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,  # noqa: B950
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,  # noqa: B950
            7,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,  # noqa: B950
            8,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,  # noqa: B950
            9,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.fillBuffer_range_value_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.fillBuffer_range_value_,
            2,
            objc._C_CHAR_AS_INT,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,  # noqa: B950
            5,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,  # noqa: B950
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,  # noqa: B950
            7,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.optimizeContentsForGPUAccess_slice_level_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.optimizeContentsForGPUAccess_slice_level_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.optimizeContentsForCPUAccess_slice_level_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.optimizeContentsForCPUAccess_slice_level_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.resetCommandsInBuffer_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.optimizeIndirectCommandBuffer_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.sampleCountersInBuffer_atSampleIndex_withBarrier_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.sampleCountersInBuffer_atSampleIndex_withBarrier_,  # noqa: B950
            2,
            objc._C_NSBOOL,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.resolveCounters_inRange_destinationBuffer_destinationOffset_,  # noqa: B950
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.resolveCounters_inRange_destinationBuffer_destinationOffset_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.getTextureAccessCounters_region_mipLevel_slice_resetCounters_countersBuffer_countersBufferOffset_,  # noqa: B950
            1,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.getTextureAccessCounters_region_mipLevel_slice_resetCounters_countersBuffer_countersBufferOffset_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.getTextureAccessCounters_region_mipLevel_slice_resetCounters_countersBuffer_countersBufferOffset_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgIsBOOL(
            TestMTLBlitCommandEncoderHelper.getTextureAccessCounters_region_mipLevel_slice_resetCounters_countersBuffer_countersBufferOffset_,  # noqa: B950
            4,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.getTextureAccessCounters_region_mipLevel_slice_resetCounters_countersBuffer_countersBufferOffset_,  # noqa: 6950
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.resetTextureAccessCounters_region_mipLevel_slice_,  # noqa: B950
            1,
            Metal.MTLRegion.__typestr__,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.resetTextureAccessCounters_region_mipLevel_slice_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBlitCommandEncoderHelper.resetTextureAccessCounters_region_mipLevel_slice_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
