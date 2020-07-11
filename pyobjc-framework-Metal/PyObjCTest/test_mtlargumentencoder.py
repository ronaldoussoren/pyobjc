import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTLArgumentEncoderHelper(Metal.NSObject):
    def encodedLength(self):
        return 1

    def alignment(self):
        return 1

    def setArgumentBuffer_offset_(self, a, b):
        pass

    def setArgumentBuffer_startOffset_arrayElement_(self, a, b, c):
        pass

    def setBuffer_offset_atIndex_(self, a, b, c):
        pass

    def setBuffers_offsets_withRange_(self, a, b, c):
        pass

    def setTexture_atIndex_(self, a, b):
        pass

    def setTextures_withRange_(self, a, b):
        pass

    def setSamplerState_atIndex_(self, a, b):
        pass

    def setSamplerStates_withRange_(self, a, b):
        pass

    def constantDataAtIndex_(self, a):
        pass

    def setRenderPipelineState_atIndex_(self, a, b):
        pass

    def setRenderPipelineStates_withRange_(self, a, b):
        pass

    def setIndirectCommandBuffer_atIndex_(self, a, b):
        pass

    def setIndirectCommandBuffers_withRange_(self, a, b):
        pass

    def newArgumentEncoderForBufferAtIndex_(self, a):
        pass

    def setAccelerationStructure_atIndex_(self, a, b):
        pass

    def setVisibleFunctionTable_atIndex_(self, a, b):
        pass

    def setVisibleFunctionTables_withRange_(self, a, b):
        pass

    def setIntersectionFunctionTable_atIndex_(self, a, b):
        pass

    def setIntersectionFunctionTables_withRange_(self, a, b):
        pass


class TestMTLArgumentEncoder(TestCase):
    @min_sdk_level("10.13")
    def test_protocols10_13(self):
        objc.protocolNamed("MTLArgumentEncoder")

    def test_methods(self):
        self.assertResultHasType(
            TestMTLArgumentEncoderHelper.encodedLength, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestMTLArgumentEncoderHelper.alignment, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setArgumentBuffer_offset_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setArgumentBuffer_startOffset_arrayElement_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setArgumentBuffer_startOffset_arrayElement_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setBuffer_offset_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setBuffer_offset_atIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgIsIn(
            TestMTLArgumentEncoderHelper.setBuffers_offsets_withRange_, 0
        )
        self.assertArgSizeInArg(
            TestMTLArgumentEncoderHelper.setBuffers_offsets_withRange_, 0, 2
        )
        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setBuffers_offsets_withRange_,
            1,
            objc._C_IN + objc._C_PTR + objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestMTLArgumentEncoderHelper.setBuffers_offsets_withRange_, 1, 2
        )
        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setBuffers_offsets_withRange_,
            2,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setTexture_atIndex_, 1, objc._C_NSUInteger
        )

        self.assertArgIsIn(TestMTLArgumentEncoderHelper.setTextures_withRange_, 0)
        self.assertArgSizeInArg(
            TestMTLArgumentEncoderHelper.setTextures_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setTextures_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setSamplerState_atIndex_, 1, objc._C_NSUInteger
        )

        self.assertArgIsIn(TestMTLArgumentEncoderHelper.setSamplerStates_withRange_, 0)
        self.assertArgSizeInArg(
            TestMTLArgumentEncoderHelper.setSamplerStates_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setSamplerStates_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.constantDataAtIndex_, 0, objc._C_NSUInteger
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setRenderPipelineState_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgIsIn(
            TestMTLArgumentEncoderHelper.setRenderPipelineStates_withRange_, 0
        )
        self.assertArgSizeInArg(
            TestMTLArgumentEncoderHelper.setRenderPipelineStates_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setRenderPipelineStates_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setIndirectCommandBuffer_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgIsIn(
            TestMTLArgumentEncoderHelper.setIndirectCommandBuffers_withRange_, 0
        )
        self.assertArgSizeInArg(
            TestMTLArgumentEncoderHelper.setIndirectCommandBuffers_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setIndirectCommandBuffers_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.newArgumentEncoderForBufferAtIndex_,
            0,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setAccelerationStructure_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setVisibleFunctionTable_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setVisibleFunctionTables_withRange_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTLArgumentEncoderHelper.setVisibleFunctionTables_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setVisibleFunctionTables_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setIntersectionFunctionTable_atIndex_,
            1,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setIntersectionFunctionTables_withRange_,
            0,
            b"n^@",
        )
        self.assertArgSizeInArg(
            TestMTLArgumentEncoderHelper.setIntersectionFunctionTables_withRange_, 0, 1
        )
        self.assertArgHasType(
            TestMTLArgumentEncoderHelper.setIntersectionFunctionTables_withRange_,
            1,
            Metal.NSRange.__typestr__,
        )
