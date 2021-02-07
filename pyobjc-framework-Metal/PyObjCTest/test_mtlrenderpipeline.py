import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestMTLRenderPipelineHelper(Metal.NSObject):
    def supportIndirectCommandBuffers(self):
        return 1

    def textureWriteRoundingMode(self):
        return 1

    def maxTotalThreadsPerThreadgroup(self):
        return 1

    def threadgroupSizeMatchesTileSize(self):
        return 1

    def imageblockSampleLength(self):
        return 1

    def imageblockMemoryLengthForDimensions_(self, a):
        return 1


class TestMTLRenderPipeline(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLBlendFactorZero, 0)
        self.assertEqual(Metal.MTLBlendFactorOne, 1)
        self.assertEqual(Metal.MTLBlendFactorSourceColor, 2)
        self.assertEqual(Metal.MTLBlendFactorOneMinusSourceColor, 3)
        self.assertEqual(Metal.MTLBlendFactorSourceAlpha, 4)
        self.assertEqual(Metal.MTLBlendFactorOneMinusSourceAlpha, 5)
        self.assertEqual(Metal.MTLBlendFactorDestinationColor, 6)
        self.assertEqual(Metal.MTLBlendFactorOneMinusDestinationColor, 7)
        self.assertEqual(Metal.MTLBlendFactorDestinationAlpha, 8)
        self.assertEqual(Metal.MTLBlendFactorOneMinusDestinationAlpha, 9)
        self.assertEqual(Metal.MTLBlendFactorSourceAlphaSaturated, 10)
        self.assertEqual(Metal.MTLBlendFactorBlendColor, 11)
        self.assertEqual(Metal.MTLBlendFactorOneMinusBlendColor, 12)
        self.assertEqual(Metal.MTLBlendFactorBlendAlpha, 13)
        self.assertEqual(Metal.MTLBlendFactorOneMinusBlendAlpha, 14)
        self.assertEqual(Metal.MTLBlendFactorSource1Color, 15)
        self.assertEqual(Metal.MTLBlendFactorOneMinusSource1Color, 16)
        self.assertEqual(Metal.MTLBlendFactorSource1Alpha, 17)
        self.assertEqual(Metal.MTLBlendFactorOneMinusSource1Alpha, 18)

        self.assertEqual(Metal.MTLBlendOperationAdd, 0)
        self.assertEqual(Metal.MTLBlendOperationSubtract, 1)
        self.assertEqual(Metal.MTLBlendOperationReverseSubtract, 2)
        self.assertEqual(Metal.MTLBlendOperationMin, 3)
        self.assertEqual(Metal.MTLBlendOperationMax, 4)

        self.assertEqual(Metal.MTLColorWriteMaskNone, 0)
        self.assertEqual(Metal.MTLColorWriteMaskRed, 0x1 << 3)
        self.assertEqual(Metal.MTLColorWriteMaskGreen, 0x1 << 2)
        self.assertEqual(Metal.MTLColorWriteMaskBlue, 0x1 << 1)
        self.assertEqual(Metal.MTLColorWriteMaskAlpha, 0x1 << 0)
        self.assertEqual(Metal.MTLColorWriteMaskAll, 0xF)

        self.assertEqual(Metal.MTLPrimitiveTopologyClassUnspecified, 0)
        self.assertEqual(Metal.MTLPrimitiveTopologyClassPoint, 1)
        self.assertEqual(Metal.MTLPrimitiveTopologyClassLine, 2)
        self.assertEqual(Metal.MTLPrimitiveTopologyClassTriangle, 3)

        self.assertEqual(Metal.MTLTessellationPartitionModePow2, 0)
        self.assertEqual(Metal.MTLTessellationPartitionModeInteger, 1)
        self.assertEqual(Metal.MTLTessellationPartitionModeFractionalOdd, 2)
        self.assertEqual(Metal.MTLTessellationPartitionModeFractionalEven, 3)

        self.assertEqual(Metal.MTLTessellationFactorStepFunctionConstant, 0)
        self.assertEqual(Metal.MTLTessellationFactorStepFunctionPerPatch, 1)
        self.assertEqual(Metal.MTLTessellationFactorStepFunctionPerInstance, 2)
        self.assertEqual(
            Metal.MTLTessellationFactorStepFunctionPerPatchAndPerInstance, 3
        )

        self.assertEqual(Metal.MTLTessellationFactorFormatHalf, 0)

        self.assertEqual(Metal.MTLTessellationControlPointIndexTypeNone, 0)
        self.assertEqual(Metal.MTLTessellationControlPointIndexTypeUInt16, 1)
        self.assertEqual(Metal.MTLTessellationControlPointIndexTypeUInt32, 2)

    @min_sdk_level("10.11")
    def test_protocols(self):
        objc.protocolNamed("MTLRenderPipelineState")

    def test_methods(self):
        self.assertResultIsBOOL(
            TestMTLRenderPipelineHelper.supportIndirectCommandBuffers
        )

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(
            Metal.MTLRenderPipelineColorAttachmentDescriptor.alloc()
            .init()
            .isBlendingEnabled
        )
        self.assertArgIsBOOL(
            Metal.MTLRenderPipelineColorAttachmentDescriptor.alloc()
            .init()
            .setBlendingEnabled_,
            0,
        )

        self.assertResultIsBOOL(
            Metal.MTLRenderPipelineDescriptor.alloc().init().isAlphaToCoverageEnabled
        )
        self.assertArgIsBOOL(
            Metal.MTLRenderPipelineDescriptor.alloc().init().setAlphaToCoverageEnabled_,
            0,
        )
        self.assertResultIsBOOL(
            Metal.MTLRenderPipelineDescriptor.alloc().init().isAlphaToOneEnabled
        )
        self.assertArgIsBOOL(
            Metal.MTLRenderPipelineDescriptor.alloc().init().setAlphaToOneEnabled_, 0
        )
        self.assertResultIsBOOL(
            Metal.MTLRenderPipelineDescriptor.alloc().init().isRasterizationEnabled
        )
        self.assertArgIsBOOL(
            Metal.MTLRenderPipelineDescriptor.alloc().init().setRasterizationEnabled_, 0
        )
        self.assertResultIsBOOL(
            Metal.MTLRenderPipelineDescriptor.alloc()
            .init()
            .isTessellationFactorScaleEnabled
        )
        self.assertArgIsBOOL(
            Metal.MTLRenderPipelineDescriptor.alloc()
            .init()
            .setTessellationFactorScaleEnabled_,
            0,
        )
        self.assertResultIsBOOL(
            Metal.MTLRenderPipelineDescriptor.alloc()
            .init()
            .supportIndirectCommandBuffers
        )
        self.assertArgIsBOOL(
            Metal.MTLRenderPipelineDescriptor.alloc()
            .init()
            .setSupportIndirectCommandBuffers_,
            0,
        )
