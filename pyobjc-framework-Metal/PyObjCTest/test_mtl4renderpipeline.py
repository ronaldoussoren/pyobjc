import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTL4RenderPipeline(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTL4LogicalToPhysicalColorAttachmentMappingState)
        self.assertEqual(
            Metal.MTL4LogicalToPhysicalColorAttachmentMappingStateIdentity, 0
        )
        self.assertEqual(
            Metal.MTL4LogicalToPhysicalColorAttachmentMappingStateInherited, 1
        )

    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Metal.MTL4RenderPipelineDescriptor.isRasterizationEnabled
        )
        self.assertArgIsBOOL(
            Metal.MTL4RenderPipelineDescriptor.setRasterizationEnabled_, 0
        )

        self.assertResultIsBOOL(
            Metal.MTL4RenderPipelineDescriptor.supportVertexBinaryLinking
        )
        self.assertArgIsBOOL(
            Metal.MTL4RenderPipelineDescriptor.setSupportVertexBinaryLinking_, 0
        )

        self.assertResultIsBOOL(
            Metal.MTL4RenderPipelineDescriptor.supportFragmentBinaryLinking
        )
        self.assertArgIsBOOL(
            Metal.MTL4RenderPipelineDescriptor.setSupportFragmentBinaryLinking_, 0
        )
