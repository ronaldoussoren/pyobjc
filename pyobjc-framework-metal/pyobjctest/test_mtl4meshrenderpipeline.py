import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestMTL4MeshRenderPipeline(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Metal.MTL4MeshRenderPipelineDescriptor.objectThreadgroupSizeIsMultipleOfThreadExecutionWidth
        )
        self.assertArgIsBOOL(
            Metal.MTL4MeshRenderPipelineDescriptor.setObjectThreadgroupSizeIsMultipleOfThreadExecutionWidth_,
            0,
        )

        self.assertResultIsBOOL(
            Metal.MTL4MeshRenderPipelineDescriptor.meshThreadgroupSizeIsMultipleOfThreadExecutionWidth
        )
        self.assertArgIsBOOL(
            Metal.MTL4MeshRenderPipelineDescriptor.setMeshThreadgroupSizeIsMultipleOfThreadExecutionWidth_,
            0,
        )

        self.assertResultIsBOOL(
            Metal.MTL4MeshRenderPipelineDescriptor.supportObjectBinaryLinking
        )
        self.assertArgIsBOOL(
            Metal.MTL4MeshRenderPipelineDescriptor.setSupportObjectBinaryLinking_, 0
        )

        self.assertResultIsBOOL(
            Metal.MTL4MeshRenderPipelineDescriptor.supportMeshBinaryLinking
        )
        self.assertArgIsBOOL(
            Metal.MTL4MeshRenderPipelineDescriptor.setSupportMeshBinaryLinking_, 0
        )

        self.assertResultIsBOOL(
            Metal.MTL4MeshRenderPipelineDescriptor.supportFragmentBinaryLinking
        )
        self.assertArgIsBOOL(
            Metal.MTL4MeshRenderPipelineDescriptor.setSupportFragmentBinaryLinking_, 0
        )
