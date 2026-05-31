import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTL4ComputePipeline(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Metal.MTL4ComputePipelineDescriptor.threadGroupSizeIsMultipleOfThreadExecutionWidth
        )
        self.assertArgIsBOOL(
            Metal.MTL4ComputePipelineDescriptor.setThreadGroupSizeIsMultipleOfThreadExecutionWidth_,
            0,
        )

        self.assertResultIsBOOL(
            Metal.MTL4ComputePipelineDescriptor.supportBinaryLinking
        )
        self.assertArgIsBOOL(
            Metal.MTL4ComputePipelineDescriptor.setSupportBinaryLinking_, 0
        )
