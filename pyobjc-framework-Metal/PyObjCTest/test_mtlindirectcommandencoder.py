from PyObjCTools.TestSupport import *

import Metal


class TestMTLIndirectCommandEncoderHelper(Metal.NSObject):
    def setVertexBuffer_offset_atIndex_(self, a, b, c):
        pass

    def setFragmentBuffer_offset_atIndex_(self, a, b, c):
        pass

    def drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_(
        self, a, b, c, d, e, f, g, h, i, j
    ):
        pass

    def drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_(
        self, a, b, c, d, e, f, g, h, i, j, k, l
    ):
        pass

    def drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_(
        self, a, b, c, d, e
    ):
        pass

    def drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_(
        self, a, b, c, d, e, f, g, h
    ):
        pass


class TestMTLIndirectCommandEncoder(TestCase):
    @min_sdk_level("10.14")
    def test_protocols(self):
        objc.protocolNamed("MTLIndirectRenderCommand")

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
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            5,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            8,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            9,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            6,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            7,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            8,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            10,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPatches_patchStart_patchCount_patchIndexBuffer_patchIndexBufferOffset_controlPointIndexBuffer_controlPointIndexBufferOffset_instanceCount_baseInstance_tessellationFactorBuffer_tessellationFactorBufferOffset_tessellationFactorBufferInstanceStride_,
            11,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawPrimitives_vertexStart_vertexCount_instanceCount_baseInstance_,
            4,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,
            4,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,
            5,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLIndirectCommandEncoderHelper.drawIndexedPrimitives_indexCount_indexType_indexBuffer_indexBufferOffset_instanceCount_baseVertex_baseInstance_,
            6,
            objc._C_NSInteger,
        )
