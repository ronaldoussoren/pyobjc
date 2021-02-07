import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLAccelerationStructureCommandEncoderHelper(Metal.NSObject):
    def buildAccelerationStructure_descriptor_scratchBuffer_scratchBufferOffset_(
        self, a, b, c, d
    ):
        pass

    def refitAccelerationStructure_descriptor_destination_scratchBuffer_scratchBufferOffset_(
        self, a, b, c, d, e
    ):
        pass

    def writeCompactedAccelerationStructureSize_toBuffer_offset_(self, a, b, c):
        pass

    def useResource_usage_(self, a, b):
        pass

    def useResources_count_usage_(self, a, b, c):
        pass

    def useHeaps_count_(self, a, b):
        pass

    def sampleCountersInBuffer_atSampleIndex_withBarrier_(self, a, b, c):
        pass


class TestMTLAccelerationStructureCommandEncoder(TestCase):
    @min_sdk_level("10.16")
    def test_protocols(self):
        objc.protocolNamed("MTLAccelerationStructureCommandEncoder")

    def test_methods(self):
        self.assertArgHasType(
            TestMTLAccelerationStructureCommandEncoderHelper.buildAccelerationStructure_descriptor_scratchBuffer_scratchBufferOffset_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLAccelerationStructureCommandEncoderHelper.refitAccelerationStructure_descriptor_destination_scratchBuffer_scratchBufferOffset_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLAccelerationStructureCommandEncoderHelper.writeCompactedAccelerationStructureSize_toBuffer_offset_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLAccelerationStructureCommandEncoderHelper.useResource_usage_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgIsIn(
            TestMTLAccelerationStructureCommandEncoderHelper.useResources_count_usage_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLAccelerationStructureCommandEncoderHelper.useResources_count_usage_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLAccelerationStructureCommandEncoderHelper.useResources_count_usage_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLAccelerationStructureCommandEncoderHelper.useResources_count_usage_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgIsIn(
            TestMTLAccelerationStructureCommandEncoderHelper.useHeaps_count_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLAccelerationStructureCommandEncoderHelper.useHeaps_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTLAccelerationStructureCommandEncoderHelper.useHeaps_count_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgIsBOOL(
            TestMTLAccelerationStructureCommandEncoderHelper.sampleCountersInBuffer_atSampleIndex_withBarrier_,
            2,
        )
