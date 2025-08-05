import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTL4TileRenderPipeline(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Metal.MTL4TileRenderPipelineDescriptor.threadgroupSizeMatchesTileSize
        )
        self.assertArgIsBOOL(
            Metal.MTL4TileRenderPipelineDescriptor.setThreadgroupSizeMatchesTileSize_, 0
        )

        self.assertResultIsBOOL(
            Metal.MTL4TileRenderPipelineDescriptor.supportBinaryLinking
        )
        self.assertArgIsBOOL(
            Metal.MTL4TileRenderPipelineDescriptor.setSupportBinaryLinking_, 0
        )
