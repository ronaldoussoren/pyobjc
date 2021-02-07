import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTLComputeCommandEncoderHelper(Metal.NSObject):
    def dispatchType(self):
        return 1

    def setBytes_length_atIndex_(self, a, b, c):
        pass

    def setBuffer_offset_atIndex_(self, a, b, c):
        pass

    def setBufferOffset_atIndex_(self, a, b):
        pass

    def setBuffers_offsets_withRange_(self, a, b, c):
        pass

    def setTexture_atIndex_(self, a, b):
        pass

    def setTextures_withRange_(self, a, b):
        pass

    def setSamplerState_atIndex_(self, a, b):
        pass

    def setSamplerStates_withRange_(self, a, b):
        pass

    def setSamplerStates_lodMinClamps_lodMaxClamps_withRange_(self, a, b, c, d):
        pass

    def setThreadgroupMemoryLength_atIndex_(self, a, b):
        pass

    def setStageInRegion_(self, a):
        pass

    def setStageInRegionWithIndirectBuffer_indirectBufferOffset_(self, a, b):
        pass

    def dispatchThreadgroups_threadsPerThreadgroup_(self, a, b):
        pass

    def dispatchThreadgroupsWithIndirectBuffer_indirectBufferOffset_threadsPerThreadgroup_(
        self, a, b, c
    ):
        pass

    def dispatchThreads_threadsPerThreadgroup_(self, a, b):
        pass

    def useResource_usage_(self, a, b):
        pass

    def useResources_count_usage_(self, a, b, c):
        pass

    def useHeaps_count_(self, a, b):
        pass

    def memoryBarrierWithScope_(self, a):
        pass

    def memoryBarrierWithResources_count_(self, a, b):
        pass

    def sampleCountersInBuffer_atSampleIndex_withBarrier_(self, a, b, c):
        pass

    def setVisibleFunctionTable_atBufferIndex_(self, a, b):
        pass

    def setVisibleFunctionTables_withBufferRange_(self, a, b):
        pass

    def setIntersectionFunctionTable_atBufferIndex_(self, a, b):
        pass

    def setIntersectionFunctionTables_withBufferRange_(self, a, b):
        pass

    def setAccelerationStructure_atBufferIndex_(self, a, b):
        pass

    def setImageblockWidth_height_(self, a, b):
        pass

    def executeCommandsInBuffer_withRange_(self, a, b):
        pass

    def executeCommandsInBuffer_inDirectBuffer_indirectBufferOffset_(self, a, b, c):
        pass

    def imageblockMemoryLengthForDimensions_(self, a):
        return 1

    def supportIndirectCommandBuffers(self):
        return 1


class TestMTLComputeCommandEncoder(TestCase):
    def test_structs(self):
        v = Metal.MTLDispatchThreadgroupsIndirectArguments()
        self.assertEqual(v.threadgroupsPerGrid, None)

        v = Metal.MTLStageInRegionIndirectArguments()
        self.assertEqual(v.stageInOrigin, None)
        self.assertEqual(v.stageInSize, None)

    @min_sdk_level("10.11")
    def test_protocols(self):
        objc.protocolNamed("MTLComputeCommandEncoder")

    def test_methods(self):
        self.assertResultHasType(
            TestMTLComputeCommandEncoderHelper.dispatchType, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setBytes_length_atIndex_,
            0,
            objc._C_IN + objc._C_PTR + objc._C_VOID,
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.setBytes_length_atIndex_, 0, 1
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setBytes_length_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setBytes_length_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setBufferOffset_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setBufferOffset_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setBuffers_offsets_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.setBuffers_offsets_withRange_, 0, 2
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setBuffers_offsets_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.setBuffers_offsets_withRange_, 1, 2
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setBuffers_offsets_withRange_,
            2,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setTexture_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setTextures_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.setTextures_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setTextures_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setSamplerState_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setSamplerStates_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.setSamplerStates_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setSamplerStates_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.setSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            0,
            3,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            1,
            b"n^f",
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.setSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            1,
            3,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            2,
            b"n^f",
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.setSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            2,
            3,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setThreadgroupMemoryLength_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setThreadgroupMemoryLength_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setStageInRegion_,
            0,
            Metal.MTLRegion.__typestr__,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setStageInRegionWithIndirectBuffer_indirectBufferOffset_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.dispatchThreadgroups_threadsPerThreadgroup_,
            0,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.dispatchThreadgroups_threadsPerThreadgroup_,
            1,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.dispatchThreadgroupsWithIndirectBuffer_indirectBufferOffset_threadsPerThreadgroup_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.dispatchThreadgroupsWithIndirectBuffer_indirectBufferOffset_threadsPerThreadgroup_,  # noqa: B950
            2,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.dispatchThreads_threadsPerThreadgroup_,
            0,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.dispatchThreads_threadsPerThreadgroup_,
            1,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.useResource_usage_, 1, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.useResources_count_usage_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.useResources_count_usage_, 0, 1
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.useResources_count_usage_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.useResources_count_usage_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.useHeaps_count_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.useHeaps_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.useHeaps_count_, 1, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.memoryBarrierWithScope_,
            0,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.memoryBarrierWithResources_count_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.memoryBarrierWithResources_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.memoryBarrierWithResources_count_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.sampleCountersInBuffer_atSampleIndex_withBarrier_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.sampleCountersInBuffer_atSampleIndex_withBarrier_,  # noqa: B950
            2,
            objc._C_NSBOOL,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setVisibleFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setVisibleFunctionTables_withBufferRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.setVisibleFunctionTables_withBufferRange_,
            0,
            1,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setVisibleFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setIntersectionFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setIntersectionFunctionTables_withBufferRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLComputeCommandEncoderHelper.setIntersectionFunctionTables_withBufferRange_,
            0,
            1,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setIntersectionFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setAccelerationStructure_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setImageblockWidth_height_,
            0,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.setImageblockWidth_height_,
            1,
            objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.executeCommandsInBuffer_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLComputeCommandEncoderHelper.executeCommandsInBuffer_inDirectBuffer_indirectBufferOffset_,
            2,
            objc._C_NSUInteger,
        )

        self.assertResultIsBOOL(
            TestMTLComputeCommandEncoderHelper.supportIndirectCommandBuffers
        )
