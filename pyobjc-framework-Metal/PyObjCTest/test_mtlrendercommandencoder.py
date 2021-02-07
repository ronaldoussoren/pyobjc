import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTLRenderCommandEncoderHelper(Metal.NSObject):
    def setVertexBytes_length_atIndex_(self, a, b, c):
        pass

    def setVertexBuffer_offset_atIndex_(self, a, b, c):
        pass

    def setVertexBufferOffset_atIndex_(self, a, b):
        pass

    def setVertexBuffers_offsets_withRange_(self, a, b, c):
        pass

    def setVertexTexture_atIndex_(self, a, b):
        pass

    def setVertexTextures_withRange_(self, a, b):
        pass

    def setVertexSamplerState_atIndex_(self, a, b):
        pass

    def setVertexSamplerStates_withRange_(self, a, b):
        pass

    def setVertexSamplerState_lodMinClamp_lodMaxClamp_atIndex_(self, a, b, c, d):
        pass

    def setVertexSamplerStates_lodMinClamps_lodMaxClamps_withRange_(self, a, b, c, d):
        pass

    def setViewport_(self, a):
        pass

    def setViewports_count_(self, a, b):
        pass

    def setFrontFacingWinding_(self, a):
        pass

    def setVertexAmplificationCount_viewMapping_(self, a, b):
        pass

    def setCullMode_(self, a):
        pass

    def setDepthClipMode_(self, a):
        pass

    def setDepthBias_slopeScale_clamp_(self, a, b, c):
        pass

    def setScissorRect_(self, a):
        pass

    def setScissorRects_count_(self, a, b):
        pass

    def setTriangleFillMode_(self, a):
        pass

    def setFragmentBytes_length_atIndex_(self, a, b, c):
        pass

    def setFragmentBuffer_offset_atIndex_(self, a, b, c):
        pass

    def setFragmentBufferOffset_atIndex_(self, a, b):
        pass

    def setFragmentBuffers_offsets_withRange_(self, a, b, c):
        pass

    def setFragmentTexture_atIndex_(self, a, b):
        pass

    def setFragmentTextures_withRange_(self, a, b):
        pass

    def useResources_count_usage_(self, a, b, c):
        pass

    def useHeaps_count_(self, a, b):
        pass

    def useHeap_stages_(self, a, b):
        pass

    def useHeaps_count_stages_(self, a, b, c):
        pass

    def executeCommandsInBuffer_withRange_(self, a, b):
        pass

    def executeCommandsInBuffer_indirectBuffer_indirectBufferOffset_(self, a, b, c):
        pass

    def memoryBarrierWithScope_afterStages_beforeStages_(self, a, b, c):
        pass

    def memoryBarrierWithResources_count_(self, a, b):
        pass

    def sampleCountersInBuffer_atSampleIndex_withBarrier_(self, a, b, c):
        pass

    def drawIndexedPatches_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_indirectBuffer_indirectBufferOffset_(  # noqa: B950
        self, a, b, c, d, e, f, g
    ):
        pass

    def tileWidth(self):
        return 1

    def tileHeight(self):
        return 1

    def setTileBytes_length_atIndex_(self, a, b, c):
        pass

    def setTileBuffer_offset_atIndex_(self, a, b, c):
        pass

    def setTileBufferOffset_atIndex_(self, a, b):
        pass

    def setTileBuffers_offsets_withRange_(self, a, b, c):
        pass

    def setTileTexture_atIndex_(self, a, b):
        pass

    def setTileTextures_withRange_(self, a, b):
        pass

    def setTileSamplerState_atIndex_(self, a, b):
        pass

    def setTileSamplerStates_withRange_(self, a, b):
        pass

    def setTileSamplerState_lodMinClamp_lodMaxClamp_atIndex_(self, a, b, c, d):
        pass

    def setTileSamplerStates_lodMinClamps_lodMaxClamps_withRange_(self, a, b, c, d):
        pass

    def dispatchThreadsPerTile_(self, a):
        pass

    def setThreadgroupMemoryLength_offset_atIndex_(self, a, b, c):
        pass


class TestMTLRenderCommandEncoder(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLPrimitiveTypePoint, 0)
        self.assertEqual(Metal.MTLPrimitiveTypeLine, 1)
        self.assertEqual(Metal.MTLPrimitiveTypeLineStrip, 2)
        self.assertEqual(Metal.MTLPrimitiveTypeTriangle, 3)
        self.assertEqual(Metal.MTLPrimitiveTypeTriangleStrip, 4)

        self.assertEqual(Metal.MTLVisibilityResultModeDisabled, 0)
        self.assertEqual(Metal.MTLVisibilityResultModeBoolean, 1)
        self.assertEqual(Metal.MTLVisibilityResultModeCounting, 2)

        self.assertEqual(Metal.MTLCullModeNone, 0)
        self.assertEqual(Metal.MTLCullModeFront, 1)
        self.assertEqual(Metal.MTLCullModeBack, 2)

        self.assertEqual(Metal.MTLWindingClockwise, 0)
        self.assertEqual(Metal.MTLWindingCounterClockwise, 1)

        self.assertEqual(Metal.MTLDepthClipModeClip, 0)
        self.assertEqual(Metal.MTLDepthClipModeClamp, 1)

        self.assertEqual(Metal.MTLTriangleFillModeFill, 0)
        self.assertEqual(Metal.MTLTriangleFillModeLines, 1)

        self.assertEqual(Metal.MTLRenderStageVertex, 1 << 0)
        self.assertEqual(Metal.MTLRenderStageFragment, 1 << 1)

    def test_structs(self):
        v = Metal.MTLScissorRect()
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)

        v = Metal.MTLViewport()
        self.assertEqual(v.originX, 0)
        self.assertEqual(v.originY, 0)
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)
        self.assertEqual(v.znear, 0)
        self.assertEqual(v.zfar, 0)

        v = Metal.MTLDrawPrimitivesIndirectArguments()
        self.assertEqual(v.vertexCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.vertexStart, 0)
        self.assertEqual(v.baseInstance, 0)

        v = Metal.MTLDrawIndexedPrimitivesIndirectArguments()
        self.assertEqual(v.indexCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.indexStart, 0)
        self.assertEqual(v.baseVertex, 0)
        self.assertEqual(v.baseInstance, 0)

        v = Metal.MTLDrawPatchIndirectArguments()
        self.assertEqual(v.patchCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.patchStart, 0)
        self.assertEqual(v.baseInstance, 0)

        v = Metal.MTLQuadTessellationFactorsHalf()
        self.assertEqual(v.edgeTessellationFactor, None)
        self.assertEqual(v.insideTessellationFactor, None)

        v = Metal.MTLTriangleTessellationFactorsHalf()
        self.assertEqual(v.edgeTessellationFactor, None)
        self.assertEqual(v.insideTessellationFactor, 0)

        v = Metal.MTLVertexAmplificationViewMapping()
        self.assertEqual(v.viewportArrayIndexOffset, 0)
        self.assertEqual(v.renderTargetArrayIndexOffset, 0)

    @min_sdk_level("10.11")
    def test_protocols(self):
        objc.protocolNamed("MTLRenderCommandEncoder")

    def test_methods(self):
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBytes_length_atIndex_, 0, b"n^v"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexBytes_length_atIndex_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBytes_length_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBytes_length_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBufferOffset_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBufferOffset_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_withRange_, 0, 2
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_withRange_, 1, 2
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_withRange_,
            2,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexTexture_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexTextures_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexTextures_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexTextures_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerState_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerStates_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerStates_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerStates_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerState_lodMinClamp_lodMaxClamp_atIndex_,  # noqa: B950
            1,
            objc._C_FLT,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerState_lodMinClamp_lodMaxClamp_atIndex_,  # noqa: B950
            2,
            objc._C_FLT,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerState_lodMinClamp_lodMaxClamp_atIndex_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            0,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            1,
            b"n^f",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            1,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            2,
            b"n^f",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            2,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexSamplerStates_lodMinClamps_lodMaxClamps_withRange_,  # noqa: B950
            3,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setViewport_,
            0,
            Metal.MTLViewport.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setViewports_count_,
            0,
            b"n^" + Metal.MTLViewport.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setViewports_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setViewports_count_, 1, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFrontFacingWinding_,
            0,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexAmplificationCount_viewMapping_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexAmplificationCount_viewMapping_,
            1,
            Metal.MTLVertexAmplificationViewMapping.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setCullMode_, 0, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setDepthClipMode_, 0, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setDepthBias_slopeScale_clamp_,
            0,
            objc._C_FLT,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setDepthBias_slopeScale_clamp_,
            1,
            objc._C_FLT,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setDepthBias_slopeScale_clamp_,
            2,
            objc._C_FLT,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setScissorRect_,
            0,
            Metal.MTLScissorRect.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setScissorRects_count_,
            0,
            b"n^" + Metal.MTLScissorRect.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setScissorRects_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setScissorRects_count_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTriangleFillMode_,
            0,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentBytes_length_atIndex_,
            0,
            b"n^v",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setFragmentBytes_length_atIndex_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentBytes_length_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentBytes_length_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentBufferOffset_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentBufferOffset_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentBuffers_offsets_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setFragmentBuffers_offsets_withRange_,
            0,
            2,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentBuffers_offsets_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setFragmentBuffers_offsets_withRange_,
            1,
            2,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentBuffers_offsets_withRange_,
            2,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentTexture_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentTextures_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setFragmentTextures_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentTextures_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.useResources_count_usage_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.useResources_count_usage_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.useResources_count_usage_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.useResources_count_usage_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.useHeaps_count_, 0, b"n^@"
        )
        self.assertArgSizeInArg(TestMTLRenderCommandEncoderHelper.useHeaps_count_, 0, 1)
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.useHeaps_count_, 1, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.useHeap_stages_, 1, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.useHeaps_count_stages_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.useHeaps_count_stages_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.useHeaps_count_stages_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.useHeaps_count_stages_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.executeCommandsInBuffer_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.executeCommandsInBuffer_indirectBuffer_indirectBufferOffset_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.memoryBarrierWithScope_afterStages_beforeStages_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.memoryBarrierWithScope_afterStages_beforeStages_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.memoryBarrierWithScope_afterStages_beforeStages_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.memoryBarrierWithResources_count_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.memoryBarrierWithResources_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.memoryBarrierWithResources_count_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.sampleCountersInBuffer_atSampleIndex_withBarrier_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.sampleCountersInBuffer_atSampleIndex_withBarrier_,
            2,
            objc._C_NSBOOL,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawIndexedPatches_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_indirectBuffer_indirectBufferOffset_,  # noqa: B950
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawIndexedPatches_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_indirectBuffer_indirectBufferOffset_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawIndexedPatches_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_indirectBuffer_indirectBufferOffset_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawIndexedPatches_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_indirectBuffer_indirectBufferOffset_,  # noqa: B950
            6,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestMTLRenderCommandEncoderHelper.tileWidth, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestMTLRenderCommandEncoderHelper.tileHeight, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileBytes_length_atIndex_, 0, b"n^v"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileBytes_length_atIndex_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileBytes_length_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileBytes_length_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileBufferOffset_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileBufferOffset_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileBuffers_offsets_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileBuffers_offsets_withRange_, 0, 2
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileBuffers_offsets_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileBuffers_offsets_withRange_, 1, 2
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileBuffers_offsets_withRange_,
            2,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileTexture_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileTextures_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileTextures_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileTextures_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileSamplerState_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileSamplerStates_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileSamplerStates_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileSamplerStates_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileSamplerState_lodMinClamp_lodMaxClamp_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileSamplerState_lodMinClamp_lodMaxClamp_atIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileSamplerState_lodMinClamp_lodMaxClamp_atIndex_,
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            0,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            1,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            2,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            2,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            3,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.dispatchThreadsPerTile_,
            0,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setThreadgroupMemoryLength_offset_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setThreadgroupMemoryLength_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setThreadgroupMemoryLength_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )
