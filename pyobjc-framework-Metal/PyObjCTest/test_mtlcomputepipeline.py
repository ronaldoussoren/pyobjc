import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestMTLComputePipelineHelper(Metal.NSObject):
    def maxTotalThreadsPerThreadgroup(self):
        return 1

    def threadExecutionWidth(self):
        return 1

    def staticThreadgroupMemoryLength(self):
        return 1

    def textureWriteRoundingMode(self):
        return 1

    def newComputePipelineStateWithAdditionalBinaryFunctions_error_(self, a, b):
        return 1


class TestMTLComputePipeline(TestCase):
    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("MTLComputePipelineState")

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(
            Metal.MTLComputePipelineDescriptor.alloc()
            .init()
            .threadGroupSizeIsMultipleOfThreadExecutionWidth
        )
        self.assertArgIsBOOL(
            Metal.MTLComputePipelineDescriptor.alloc()
            .init()
            .setThreadGroupSizeIsMultipleOfThreadExecutionWidth_,
            0,
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(
            Metal.MTLComputePipelineDescriptor.alloc()
            .init()
            .supportIndirectCommandBuffers
        )

    def test_methods(self):
        self.assertResultHasType(
            TestMTLComputePipelineHelper.maxTotalThreadsPerThreadgroup,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLComputePipelineHelper.threadExecutionWidth, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLComputePipelineHelper.staticThreadgroupMemoryLength,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLComputePipelineHelper.newComputePipelineStateWithAdditionalBinaryFunctions_error_,
            1,
            b"o^@",
        )
