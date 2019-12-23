from PyObjCTools.TestSupport import *

import Metal


class TestMTLComputePipelineHelper(Metal.NSObject):
    def maxTotalThreadsPerThreadgroup(self):
        return 1

    def threadExecutionWidth(self):
        return 1

    def staticThreadgroupMemoryLength(self):
        return 1


class TestMTLComputePipeline(TestCase):
    @min_sdk_level("10.11")
    def test_protocols(self):
        objc.protocolNamed("MTLComputePipelineState")

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
