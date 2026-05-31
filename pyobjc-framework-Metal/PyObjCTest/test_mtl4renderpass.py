import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTL4RenderPass(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertArgIsIn(Metal.MTL4RenderPassDescriptor.setSamplePositions_count_, 0)
        self.assertArgSizeInArg(
            Metal.MTL4RenderPassDescriptor.setSamplePositions_count_, 0, 1
        )

        self.assertArgIsOut(Metal.MTL4RenderPassDescriptor.getSamplePositions_count_, 0)
        self.assertArgSizeInArg(
            Metal.MTL4RenderPassDescriptor.getSamplePositions_count_, 0, 1
        )
