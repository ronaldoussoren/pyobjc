import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTL4RenderCommandEncoderHelper(Metal.NSObject):
    def tileWidth(self):
        return 1

    def tileHeight(self):
        return 1

    def setViewport_(self, a):
        pass

    def setViewports_count_(self, a, b):
        pass

    def setVertexAmplificationCount_viewMappings_(self, a, b):
        pass

    def setCullMode_(self, a):
        pass

    def setDepthClipMode_(self, a):
        pass

    def setDepthBias_slopeScale_clamp_(self, a, b, c):
        pass

    def setDepthTestMinBound_maxBound_(self, a, b):
        pass

    def setScissorRect_(self, a):
        pass

    def setScissorRects_count_(self, a, b):
        pass

    def setTriangleFillMode_(self, a):
        pass

    def setBlendColorRed_green_blue_alpha_(self, a, b, c, d):
        pass

    def setStencilReferenceValue_(self, a):
        pass

    def setStencilFrontReferenceValue_backReferenceValue_(self, a, b):
        pass

    def setVisibilityResultMode_offset_(self, a, b):
        pass

    def setColorStoreAction_atIndex_(self, a, b):
        pass

    def setDepthStoreAction_(self, a):
        pass

    def setStencilStoreAction_(self, a):
        pass

    def drawPrimitives_vertexStart_vertexCount_(self, a, b, c):
        pass

    def drawPrimitives_vertexStart_vertexCount_instanceCount_(self, a, b, c, d):
        pass

    def drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_(
        self, a, b, c, d, e
    ):
        pass

    def drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_(
        self, a, b, c, d, e
    ):
        pass

    def drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_(
        self, a, b, c, d, e, f
    ):
        pass

    def drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_baseVertex_baseInstance_(
        self, a, b, c, d, e, f, g, h
    ):
        pass

    def drawPrimitives_indirectBuffer_(self, a, b):
        pass

    def drawIndexedPrimitives_indexType_indexBuffer_indexBufferLength_indirectBuffer_(
        self, a, b, c, d, e
    ):
        pass

    def executeCommandsInBuffer_withRange_(self, a, b):
        pass

    def executeCommandsInBuffer_indirectBuffer_(self, a, b):
        pass

    def setObjectThreadgroupMemoryLength_atIndex_(self, a, b):
        pass

    def drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_(
        self, a, b, c
    ):
        pass

    def drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_(
        self, a, b, c
    ):
        pass

    def drawMeshThreadgroupsWithIndirectBuffer_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_(
        self, a, b, c
    ):
        pass

    def dispatchThreadsPerTile_(self, a):
        pass

    def setThreadgroupMemoryLength_offset_atIndex_(self, a, b, c):
        pass

    def setArgumentTable_atStages_(self, a, b):
        pass

    def writeTimestampWithGranularity_afterStage_intoHeap_atIndex_(self, a, b, c, d):
        pass


class TestMTL4RenderCommandEncoder(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTL4RenderEncoderOptions)
        self.assertEqual(Metal.MTL4RenderEncoderOptionNone, 0)
        self.assertEqual(Metal.MTL4RenderEncoderOptionSuspending, 1 << 0)
        self.assertEqual(Metal.MTL4RenderEncoderOptionResuming, 1 << 1)

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4RenderCommandEncoder")

    def test_protocol_methods(self):
        self.assertResultHasType(TestMTL4RenderCommandEncoderHelper.tileWidth, b"Q")
        self.assertResultHasType(TestMTL4RenderCommandEncoderHelper.tileHeight, b"Q")

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setViewport_,
            0,
            Metal.MTLViewport.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setViewports_count_,
            0,
            b"n^" + Metal.MTLViewport.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTL4RenderCommandEncoderHelper.setViewports_count_, 0, 1
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setViewports_count_, 1, b"Q"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setVertexAmplificationCount_viewMappings_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setVertexAmplificationCount_viewMappings_,
            1,
            b"n^" + Metal.MTLVertexAmplificationViewMapping.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTL4RenderCommandEncoderHelper.setVertexAmplificationCount_viewMappings_,
            1,
            0,
        )

        self.assertArgHasType(TestMTL4RenderCommandEncoderHelper.setCullMode_, 0, b"Q")
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setDepthClipMode_, 0, b"Q"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setDepthBias_slopeScale_clamp_, 0, b"f"
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setDepthBias_slopeScale_clamp_, 1, b"f"
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setDepthBias_slopeScale_clamp_, 2, b"f"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setDepthTestMinBound_maxBound_, 0, b"f"
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setDepthTestMinBound_maxBound_, 1, b"f"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setScissorRect_,
            0,
            Metal.MTLScissorRect.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setScissorRects_count_,
            0,
            b"n^" + Metal.MTLScissorRect.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setScissorRects_count_, 1, b"Q"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setTriangleFillMode_, 0, b"Q"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setBlendColorRed_green_blue_alpha_,
            0,
            b"f",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setBlendColorRed_green_blue_alpha_,
            1,
            b"f",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setBlendColorRed_green_blue_alpha_,
            2,
            b"f",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setBlendColorRed_green_blue_alpha_,
            3,
            b"f",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setStencilReferenceValue_, 0, b"I"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setStencilFrontReferenceValue_backReferenceValue_,
            0,
            b"I",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setStencilFrontReferenceValue_backReferenceValue_,
            1,
            b"I",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setVisibilityResultMode_offset_, 0, b"Q"
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setVisibilityResultMode_offset_, 1, b"Q"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setColorStoreAction_atIndex_, 0, b"Q"
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setColorStoreAction_atIndex_, 1, b"Q"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setDepthStoreAction_, 0, b"Q"
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setStencilStoreAction_, 0, b"Q"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_,
            2,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_,
            3,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,
            3,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,
            4,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_,
            3,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_,
            3,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_,
            4,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_baseVertex_baseInstance_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_baseVertex_baseInstance_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_baseVertex_baseInstance_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_baseVertex_baseInstance_,
            3,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_baseVertex_baseInstance_,
            4,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_baseVertex_baseInstance_,
            5,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferLength_instanceCount_baseVertex_baseInstance_,
            6,
            b"q",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_indirectBuffer_, 0, b"Q"
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawPrimitives_indirectBuffer_, 1, b"Q"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexType_indexBuffer_indexBufferLength_indirectBuffer_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexType_indexBuffer_indexBufferLength_indirectBuffer_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexType_indexBuffer_indexBufferLength_indirectBuffer_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexType_indexBuffer_indexBufferLength_indirectBuffer_,
            3,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexType_indexBuffer_indexBufferLength_indirectBuffer_,
            4,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.executeCommandsInBuffer_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.executeCommandsInBuffer_indirectBuffer_,
            1,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setObjectThreadgroupMemoryLength_atIndex_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawIndexedPrimitives_indexType_indexBuffer_indexBufferLength_indirectBuffer_,
            1,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            0,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            1,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            2,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            0,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            1,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            2,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawMeshThreadgroupsWithIndirectBuffer_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawMeshThreadgroupsWithIndirectBuffer_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            1,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.drawMeshThreadgroupsWithIndirectBuffer_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            2,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.dispatchThreadsPerTile_,
            0,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setThreadgroupMemoryLength_offset_atIndex_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setThreadgroupMemoryLength_offset_atIndex_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setThreadgroupMemoryLength_offset_atIndex_,
            2,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.setArgumentTable_atStages_, 1, b"Q"
        )

        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.writeTimestampWithGranularity_afterStage_intoHeap_atIndex_,
            0,
            b"q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.writeTimestampWithGranularity_afterStage_intoHeap_atIndex_,
            1,
            b"Q",
        )
        self.assertArgHasType(
            TestMTL4RenderCommandEncoderHelper.writeTimestampWithGranularity_afterStage_intoHeap_atIndex_,
            3,
            b"Q",
        )
