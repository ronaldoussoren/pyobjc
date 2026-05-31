import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTL4ComputeCommandEncoderHelper(Metal.NSObject):
    def setThreadgroupMemoryLength_atIndex_(self, a, b):
        pass

    def setImageblockWidth_height_(self, a, b):
        pass

    def dispatchThreadgroups_threadsPerThreadgroup_(self, a, b):
        pass

    def dispatchThreadgroupsWithIndirectBuffer_threadsPerThreadgroup_(self, a, b):
        pass

    def dispatchThreadsWithIndirectBuffer_(self, a):
        pass

    def executeCommandsInBuffer_withRange_(self, a, b):
        pass

    def executeCommandsInBuffer_indirectBuffer_(self, a, b):
        pass

    def copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_(
        self, a, b, c, d, e, f, g, h
    ):
        pass

    def copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_(  # noqa: B950
        self, a, b, c, d, e, f, g, h, i
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

    def copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size_(
        self, a, b, c, d, e
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

    def fillBuffer_range_value_(self, a, b, c):
        pass

    def optimizeContentsForGPUAccess_slice_level_(self, a, b, c):
        pass

    def optimizeContentsForCPUAccess_slice_level_(self, a, b, c):
        pass

    def resetCommandsInBuffer_withRange_(self, a, b):
        pass

    def copyIndirectCommandBuffer_sourceRange_destination_destinationIndex_(
        self, a, b, c, d
    ):
        pass

    def optimizeIndirectCommandBuffer_withRange_(self, a, b):
        pass

    def buildAccelerationStructure_descriptor_scratchBuffer_(self, a, b, c):
        pass

    def refitAccelerationStructure_descriptor_destination_scratchBuffer_(
        self, a, b, c, d
    ):
        pass

    def refitAccelerationStructure_descriptor_destination_scratchBuffer_options_(
        self, a, b, c, d, e
    ):
        pass

    def writeCompactedAccelerationStructureSize_toBuffer_(self, a, b):
        pass

    def writeTimestampWithGranularity_intoHeap_atIndex_(self, a, b, c):
        pass


class TestMTL4ComputeCommandEncoder(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4ComputeCommandEncoder")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.setThreadgroupMemoryLength_atIndex_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.setThreadgroupMemoryLength_atIndex_,
            1,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.setImageblockWidth_height_, 0, b"q"
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.setImageblockWidth_height_, 1, b"q"
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.dispatchThreadgroups_threadsPerThreadgroup_,
            0,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.dispatchThreadgroups_threadsPerThreadgroup_,
            1,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.dispatchThreadgroupsWithIndirectBuffer_threadsPerThreadgroup_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.dispatchThreadgroupsWithIndirectBuffer_threadsPerThreadgroup_,
            1,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.dispatchThreadsWithIndirectBuffer_,
            0,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.executeCommandsInBuffer_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.executeCommandsInBuffer_indirectBuffer_,
            1,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,
            4,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,
            5,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,
            6,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_toTexture_destinationSlice_destinationLevel_sliceCount_levelCount_,
            7,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            3,
            Metal.MTLOrigin.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            6,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            7,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            8,
            Metal.MTLOrigin.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,
            3,
            Metal.MTLOrigin.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,
            6,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,
            7,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,
            8,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,
            3,
            Metal.MTLOrigin.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_,
            6,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,
            7,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,
            8,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromTexture_sourceSlice_sourceLevel_sourceOrigin_sourceSize_toBuffer_destinationOffset_destinationBytesPerRow_destinationBytesPerImage_options_,
            9,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size_,
            3,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_toBuffer_destinationOffset_size_,
            4,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            3,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            6,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            7,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_,
            8,
            Metal.MTLOrigin.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,
            3,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,
            4,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,
            6,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,
            7,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,
            8,
            Metal.MTLOrigin.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyFromBuffer_sourceOffset_sourceBytesPerRow_sourceBytesPerImage_sourceSize_toTexture_destinationSlice_destinationLevel_destinationOrigin_options_,
            9,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.fillBuffer_range_value_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.fillBuffer_range_value_,
            2,
            objc._C_CHAR_AS_INT,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.optimizeContentsForGPUAccess_slice_level_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.optimizeContentsForGPUAccess_slice_level_,
            2,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.optimizeContentsForCPUAccess_slice_level_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.optimizeContentsForCPUAccess_slice_level_,
            2,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.resetCommandsInBuffer_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyIndirectCommandBuffer_sourceRange_destination_destinationIndex_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.copyIndirectCommandBuffer_sourceRange_destination_destinationIndex_,
            3,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.optimizeIndirectCommandBuffer_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.buildAccelerationStructure_descriptor_scratchBuffer_,
            2,
            Metal.MTL4BufferRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.refitAccelerationStructure_descriptor_destination_scratchBuffer_,
            3,
            Metal.MTL4BufferRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.refitAccelerationStructure_descriptor_destination_scratchBuffer_options_,
            3,
            Metal.MTL4BufferRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.writeCompactedAccelerationStructureSize_toBuffer_,
            1,
            Metal.MTL4BufferRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4ComputeCommandEncoderHelper.writeTimestampWithGranularity_intoHeap_atIndex_,
            2,
            b"Q",
        )
