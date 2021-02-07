import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTLIndirectCommandEncoderHelper(Metal.NSObject):
    def setVertexBuffer_offset_atIndex_(self, a, b, c):
        pass

    def setFragmentBuffer_offset_atIndex_(self, a, b, c):
        pass

    def drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_(  # noqa: B950
        self, a, b, c, d, e, f, g, h, i, j
    ):
        pass

    def drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_(  # noqa: B950
        self, a, b, c, d, e, f, g, h, i, j, k, x
    ):
        pass

    def drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_(
        self, a, b, c, d, e
    ):
        pass

    def drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_(  # noqa: B950
        self, a, b, c, d, e, f, g, h
    ):
        pass

    def setKernelBuffer_offset_atIndex_(self, a, b, c):
        pass

    def concurrentDispatchThreadgroups_threadsPerThreadgroup_(self, a, b):
        pass

    def concurrentDispatchThreads_threadsPerThreadgroup_(self, a, b):
        pass

    def setImageblockWidth_height_(self, a, b):
        pass


class TestMTLIndirectCommandEncoder(TestCase):
    @min_sdk_level("10.14")
    def test_protocols(self):
        objc.protocolNamed("MTLIndirectRenderCommand")
        objc.protocolNamed("MTLIndirectComputeCommand")

    def test_methods(self):
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.setVertexBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.setVertexBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.setFragmentBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.setFragmentBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            5,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            8,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            9,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            7,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            8,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            10,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,  # noqa: B950
            11,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,  # noqa: B950
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,  # noqa: B950
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,  # noqa: B950
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,  # noqa: B950
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,  # noqa: B950
            5,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,  # noqa: B950
            6,
            objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.setKernelBuffer_offset_atIndex_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.concurrentDispatchThreadgroups_threadsPerThreadgroup_,  # noqa: B950
            0,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.concurrentDispatchThreadgroups_threadsPerThreadgroup_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.concurrentDispatchThreads_threadsPerThreadgroup_,  # noqa: B950
            0,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.concurrentDispatchThreads_threadsPerThreadgroup_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.setImageblockWidth_height_,  # noqa: B950
            0,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.setImageblockWidth_height_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )
