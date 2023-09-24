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

    def setVertexVisibleFunctionTable_atBufferIndex_(self, a, b):
        pass

    def setVertexVisibleFunctionTables_withBufferRange_(self, a, b):
        pass

    def setVertexIntersectionFunctionTable_atBufferIndex_(self, a, b):
        pass

    def setVertexIntersectionFunctionTables_withBufferRange_(self, a, b):
        pass

    def setVertexAccelerationStructure_atBufferIndex_(self, a, b):
        pass

    def setFragmentVisibleFunctionTable_atBufferIndex_(self, a, b):
        pass

    def setFragmentVisibleFunctionTables_withBufferRange_(self, a, b):
        pass

    def setFragmentIntersectionFunctionTable_atBufferIndex_(self, a, b):
        pass

    def setFragmentIntersectionFunctionTables_withBufferRange_(self, a, b):
        pass

    def setFragmentAccelerationStructure_atBufferIndex_(self, a, b):
        pass

    def setTileVisibleFunctionTable_atBufferIndex_(self, a, b):
        pass

    def setTileVisibleFunctionTables_withBufferRange_(self, a, b):
        pass

    def setTileIntersectionFunctionTable_atBufferIndex_(self, a, b):
        pass

    def setTileIntersectionFunctionTables_withBufferRange_(self, a, b):
        pass

    def setTileAccelerationStructure_atBufferIndex_(self, a, b):
        pass

    def setStencilStoreActionOptions_(self, a):
        pass

    def setObjectBytes_length_atIndex_(self, a, b, c):
        pass

    def setObjectBuffer_offset_atIndex_(self, a, b, c):
        pass

    def setObjectBufferOffset_atIndex_(self, a, b):
        pass

    def setObjectTexture_atIndex_(self, a, b):
        pass

    def setObjectBuffers_offsets_withRange_(self, a, b, c):
        pass

    def setObjectTextures_withRange_(self, a, b):
        pass

    def setObjectSamplerState_atIndex_(self, a, b):
        pass

    def setObjectSamplerStates_withRange_(self, a, b):
        pass

    def setObjectSamplerState_lodMinClamp_lodMaxClamp_atIndex_(self, a, b, c, d):
        pass

    def setObjectSamplerStates_lodMinClamps_lodMaxClamps_withRange_(self, a, b, c, d):
        pass

    def setObjectThreadgroupMemoryLength_atIndex_(self, a, b):
        pass

    def setMeshBytes_length_atIndex_(self, a, b, c):
        pass

    def setMeshBuffer_offset_atIndex_(self, a, b, c):
        pass

    def setMeshBufferOffset_atIndex_(self, a, b):
        pass

    def setMeshBuffers_offsets_withRange_(self, a, b, c):
        pass

    def setMeshTexture_atIndex_(self, a, b):
        pass

    def setMeshTextures_withRange_(self, a, b):
        pass

    def setMeshSamplerState_atIndex_(self, a, b):
        pass

    def setMeshSamplerStates_withRange_(self, a, b):
        pass

    def setMeshSamplerState_lodMinClamp_lodMaxClamp_atIndex_(self, a, b, c, d):
        pass

    def setMeshSamplerStates_lodMinClamps_lodMaxClamps_withRange_(self, a, b, c, d):
        pass

    def drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_(
        self, a, b, c
    ):
        pass

    def drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_(
        self, a, b, c
    ):
        pass

    def drawMeshThreadgroupsWithIndirectBuffer_indirectBufferOffset_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_(
        self, a, b, c, d
    ):
        pass

    def setVertexBuffer_offset_attributeStride_atIndex_(self, a, b, c, d):
        pass

    def setVertexBuffers_offsets_attributeStrides_withRange_(self, a, b, c, d):
        pass

    def setVertexBufferOffset_attributeStride_atIndex_(self, a, b, c):
        pass

    def setVertexBytes_length_attributeStride_atIndex_(self, a, b, c, d):
        pass


class TestMTLRenderCommandEncoder(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Metal.MTLCullMode)
        self.assertIsEnumType(Metal.MTLDepthClipMode)
        self.assertIsEnumType(Metal.MTLPrimitiveType)
        self.assertIsEnumType(Metal.MTLRenderStages)
        self.assertIsEnumType(Metal.MTLTriangleFillMode)
        self.assertIsEnumType(Metal.MTLVisibilityResultMode)
        self.assertIsEnumType(Metal.MTLWinding)

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
        self.assertEqual(Metal.MTLRenderStageTile, 1 << 2)
        self.assertEqual(Metal.MTLRenderStageObject, 1 << 3)
        self.assertEqual(Metal.MTLRenderStageMesh, 1 << 4)

    def test_structs(self):
        v = Metal.MTLScissorRect()
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLViewport()
        self.assertEqual(v.originX, 0)
        self.assertEqual(v.originY, 0)
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)
        self.assertEqual(v.znear, 0)
        self.assertEqual(v.zfar, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLDrawPrimitivesIndirectArguments()
        self.assertEqual(v.vertexCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.vertexStart, 0)
        self.assertEqual(v.baseInstance, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLDrawIndexedPrimitivesIndirectArguments()
        self.assertEqual(v.indexCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.indexStart, 0)
        self.assertEqual(v.baseVertex, 0)
        self.assertEqual(v.baseInstance, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLDrawPatchIndirectArguments()
        self.assertEqual(v.patchCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.patchStart, 0)
        self.assertEqual(v.baseInstance, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLQuadTessellationFactorsHalf()
        self.assertEqual(v.edgeTessellationFactor, None)
        self.assertEqual(v.insideTessellationFactor, None)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLTriangleTessellationFactorsHalf()
        self.assertEqual(v.edgeTessellationFactor, None)
        self.assertEqual(v.insideTessellationFactor, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLVertexAmplificationViewMapping()
        self.assertEqual(v.viewportArrayIndexOffset, 0)
        self.assertEqual(v.renderTargetArrayIndexOffset, 0)
        self.assertPickleRoundTrips(v)

    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("MTLRenderCommandEncoder")

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
            TestMTLRenderCommandEncoderHelper.setVertexVisibleFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexVisibleFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexVisibleFunctionTables_withBufferRange_,
            0,
            1,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexIntersectionFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexIntersectionFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexIntersectionFunctionTables_withBufferRange_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexAccelerationStructure_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentVisibleFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentVisibleFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setFragmentVisibleFunctionTables_withBufferRange_,
            0,
            1,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentIntersectionFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentIntersectionFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setFragmentIntersectionFunctionTables_withBufferRange_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentAccelerationStructure_atBufferIndex_,
            1,
            objc._C_NSUInteger,
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

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileVisibleFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileVisibleFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileVisibleFunctionTables_withBufferRange_,
            0,
            1,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileIntersectionFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileIntersectionFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileIntersectionFunctionTables_withBufferRange_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileAccelerationStructure_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setStencilStoreActionOptions_,
            0,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBytes_length_atIndex_, 0, b"n^v"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectBytes_length_atIndex_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBytes_length_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBytes_length_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBufferOffset_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBufferOffset_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            0,
            2,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            1,
            2,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            2,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectTexture_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectTextures_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectTextures_withRange_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectTextures_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_, 0, 2
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_, 1, 2
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            2,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectTexture_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectTextures_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectTextures_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectTextures_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectSamplerState_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectSamplerStates_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectSamplerStates_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectSamplerStates_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectSamplerState_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectSamplerStates_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectSamplerStates_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectSamplerStates_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectSamplerStates_withRange_, 0, 1
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectThreadgroupMemoryLength_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectThreadgroupMemoryLength_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshBytes_length_atIndex_, 0, b"n^v"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setMeshBytes_length_atIndex_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshBytes_length_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshBytes_length_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshBufferOffset_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshBufferOffset_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshBuffers_offsets_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setMeshBuffers_offsets_withRange_, 0, 2
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshBuffers_offsets_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setMeshBuffers_offsets_withRange_, 1, 2
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshBuffers_offsets_withRange_,
            2,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshTexture_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshTextures_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setMeshTextures_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshTextures_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerState_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerStates_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerStates_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerStates_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerState_lodMinClamp_lodMaxClamp_atIndex_,
            1,
            objc._C_FLT,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerState_lodMinClamp_lodMaxClamp_atIndex_,
            2,
            objc._C_FLT,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerState_lodMinClamp_lodMaxClamp_atIndex_,
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            0,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            1,
            b"n^" + objc._C_FLT,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            1,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            2,
            b"n^" + objc._C_FLT,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            2,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setMeshSamplerStates_lodMinClamps_lodMaxClamps_withRange_,
            3,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            0,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            1,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawMeshThreadgroups_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            2,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            0,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            1,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawMeshThreads_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            2,
            Metal.MTLSize.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawMeshThreadgroupsWithIndirectBuffer_indirectBufferOffset_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawMeshThreadgroupsWithIndirectBuffer_indirectBufferOffset_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            2,
            Metal.MTLSize.__typestr__,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.drawMeshThreadgroupsWithIndirectBuffer_indirectBufferOffset_threadsPerObjectThreadgroup_threadsPerMeshThreadgroup_,
            3,
            Metal.MTLSize.__typestr__,
        )


class TestMTLRenderCommandEncoder2(TestCase):
    # XXX: Fixme, copy&paste error
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
        self.assertEqual(Metal.MTLRenderStageTile, 1 << 2)
        self.assertEqual(Metal.MTLRenderStageObject, 1 << 3)
        self.assertEqual(Metal.MTLRenderStageMesh, 1 << 4)

    def test_structs(self):
        v = Metal.MTLScissorRect()
        self.assertEqual(v.x, 0)
        self.assertEqual(v.y, 0)
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLViewport()
        self.assertEqual(v.originX, 0)
        self.assertEqual(v.originY, 0)
        self.assertEqual(v.width, 0)
        self.assertEqual(v.height, 0)
        self.assertEqual(v.znear, 0)
        self.assertEqual(v.zfar, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLDrawPrimitivesIndirectArguments()
        self.assertEqual(v.vertexCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.vertexStart, 0)
        self.assertEqual(v.baseInstance, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLDrawIndexedPrimitivesIndirectArguments()
        self.assertEqual(v.indexCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.indexStart, 0)
        self.assertEqual(v.baseVertex, 0)
        self.assertEqual(v.baseInstance, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLDrawPatchIndirectArguments()
        self.assertEqual(v.patchCount, 0)
        self.assertEqual(v.instanceCount, 0)
        self.assertEqual(v.patchStart, 0)
        self.assertEqual(v.baseInstance, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLQuadTessellationFactorsHalf()
        self.assertEqual(v.edgeTessellationFactor, None)
        self.assertEqual(v.insideTessellationFactor, None)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLTriangleTessellationFactorsHalf()
        self.assertEqual(v.edgeTessellationFactor, None)
        self.assertEqual(v.insideTessellationFactor, 0)
        self.assertPickleRoundTrips(v)

        v = Metal.MTLVertexAmplificationViewMapping()
        self.assertEqual(v.viewportArrayIndexOffset, 0)
        self.assertEqual(v.renderTargetArrayIndexOffset, 0)
        self.assertPickleRoundTrips(v)

    @min_sdk_level("10.11")
    def test_protocols(self):
        self.assertProtocolExists("MTLRenderCommandEncoder")

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
            TestMTLRenderCommandEncoderHelper.setVertexVisibleFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexVisibleFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexVisibleFunctionTables_withBufferRange_,
            0,
            1,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexIntersectionFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexIntersectionFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexIntersectionFunctionTables_withBufferRange_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexAccelerationStructure_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentVisibleFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentVisibleFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setFragmentVisibleFunctionTables_withBufferRange_,
            0,
            1,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentIntersectionFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentIntersectionFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setFragmentIntersectionFunctionTables_withBufferRange_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setFragmentAccelerationStructure_atBufferIndex_,
            1,
            objc._C_NSUInteger,
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

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileVisibleFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileVisibleFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileVisibleFunctionTables_withBufferRange_,
            0,
            1,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileIntersectionFunctionTable_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileIntersectionFunctionTables_withBufferRange_,
            1,
            Metal.NSRange.__typestr__,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setTileIntersectionFunctionTables_withBufferRange_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setTileAccelerationStructure_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setStencilStoreActionOptions_,
            0,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBytes_length_atIndex_, 0, b"n^v"
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectBytes_length_atIndex_, 0, 1
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBytes_length_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBytes_length_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBufferOffset_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBufferOffset_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            0,
            2,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            1,
            2,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectBuffers_offsets_withRange_,
            2,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectTexture_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectTextures_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setObjectTextures_withRange_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setObjectTextures_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffer_offset_attributeStride_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffer_offset_attributeStride_atIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffer_offset_attributeStride_atIndex_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffer_offset_attributeStride_atIndex_,
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_attributeStrides_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_attributeStrides_withRange_,
            0,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_attributeStrides_withRange_,
            1,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_attributeStrides_withRange_,
            1,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_attributeStrides_withRange_,
            2,
            b"n^" + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_attributeStrides_withRange_,
            2,
            3,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBuffers_offsets_attributeStrides_withRange_,
            3,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBufferOffset_attributeStride_atIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBufferOffset_attributeStride_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBufferOffset_attributeStride_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBytes_length_attributeStride_atIndex_,
            0,
            b"n^v",
        )
        self.assertArgSizeInArg(
            TestMTLRenderCommandEncoderHelper.setVertexBytes_length_attributeStride_atIndex_,
            0,
            1,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBytes_length_attributeStride_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBytes_length_attributeStride_atIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLRenderCommandEncoderHelper.setVertexBytes_length_attributeStride_atIndex_,
            3,
            objc._C_NSUInteger,
        )
