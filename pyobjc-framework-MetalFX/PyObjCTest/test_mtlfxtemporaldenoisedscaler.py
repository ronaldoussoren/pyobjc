from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc
import objc.simd

import MetalFX  # noqa: F401


class TestMTLFXTemporalDenoisedScalerHelper(MetalFX.NSObject):
    def colorTextureUsage(self):
        return 1

    def depthTextureUsage(self):
        return 1

    def motionTextureUsage(self):
        return 1

    def reactiveTextureUsage(self):
        return 1

    def diffuseAlbedoTextureUsage(self):
        return 1

    def specularAlbedoTextureUsage(self):
        return 1

    def normalTextureUsage(self):
        return 1

    def roughnessTextureUsage(self):
        return 1

    def specularHitDistanceTextureUsage(self):
        return 1

    def denoiseStrengthMaskTextureUsage(self):
        return 1

    def outputTextureUsage(self):
        return 1

    def colorTextureFormat(self):
        return 1

    def depthTextureFormat(self):
        return 1

    def motionTextureFormat(self):
        return 1

    def diffuseAlbedoTextureFormat(self):
        return 1

    def specularAlbedoTextureFormat(self):
        return 1

    def normalTextureFormat(self):
        return 1

    def roughnessTextureFormat(self):
        return 1

    def specularHitDistanceTextureFormat(self):
        return 1

    def denoiseStrengthMaskTextureFormat(self):
        return 1

    def transparencyOverlayTextureFormat(self):
        return 1

    def reactiveMaskTextureFormat(self):
        return 1

    def outputTextureFormat(self):
        return 1

    def inputWidth(self):
        return 1

    def inputHeight(self):
        return 1

    def outputWidth(self):
        return 1

    def outputHeight(self):
        return 1

    def preExposure(self):
        return 1

    def setPreExposure_(self, a):
        pass

    def jitterOffsetX(self):
        return 1

    def setJitterOffsetX_(self, a):
        pass

    def jitterOffsetY(self):
        return 1

    def setJitterOffsetY_(self, a):
        pass

    def motionVectorScaleX(self):
        return 1

    def setMotionVectorScaleX_(self, a):
        pass

    def motionVectorScaleY(self):
        return 1

    def setMotionVectorScaleY_(self, a):
        pass

    def inputContentMinScale(self):
        return 1

    def inputContentMaxScale(self):
        return 1

    def shouldResetHistory(self):
        return 1

    def setShouldResetHistory_(self, a):
        pass

    def isDepthReversed(self):
        return 1

    def setDepthReversed_(self, a):
        pass

    def viewToClipMatrix(self):
        return 1

    def setViewToClipMatrix_(self, a):
        pass


class TestMTLFXTemporalDenoisedScaler(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLFXTemporalDenoisedScalerBase")
        self.assertProtocolExists("MTLFXTemporalDenoisedScaler")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.colorTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.depthTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.motionTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.reactiveTextureUsage,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.diffuseAlbedoTextureUsage,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.specularAlbedoTextureUsage,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.normalTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.roughnessTextureUsage,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.specularHitDistanceTextureUsage,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.denoiseStrengthMaskTextureUsage,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.outputTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.colorTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.depthTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.motionTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.diffuseAlbedoTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.specularAlbedoTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.normalTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.roughnessTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.specularHitDistanceTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.denoiseStrengthMaskTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.transparencyOverlayTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.reactiveMaskTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.outputTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.inputWidth, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.inputHeight, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.outputWidth, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.outputHeight, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.preExposure, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXTemporalDenoisedScalerHelper.setPreExposure_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.jitterOffsetX, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXTemporalDenoisedScalerHelper.setJitterOffsetX_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.jitterOffsetY, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXTemporalDenoisedScalerHelper.setJitterOffsetY_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.motionVectorScaleX, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXTemporalDenoisedScalerHelper.setMotionVectorScaleX_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.motionVectorScaleY, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXTemporalDenoisedScalerHelper.setMotionVectorScaleY_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.inputContentMinScale, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.inputContentMaxScale, objc._C_FLT
        )

        self.assertResultIsBOOL(
            TestMTLFXTemporalDenoisedScalerHelper.shouldResetHistory
        )
        self.assertArgIsBOOL(
            TestMTLFXTemporalDenoisedScalerHelper.setShouldResetHistory_, 0
        )
        self.assertResultIsBOOL(TestMTLFXTemporalDenoisedScalerHelper.isDepthReversed)
        self.assertArgIsBOOL(TestMTLFXTemporalDenoisedScalerHelper.setDepthReversed_, 0)

        self.assertResultHasType(
            TestMTLFXTemporalDenoisedScalerHelper.viewToClipMatrix,
            objc.simd.simd_float4x4.__typestr__,
        )
        self.assertArgHasType(
            TestMTLFXTemporalDenoisedScalerHelper.setViewToClipMatrix_,
            0,
            objc.simd.simd_float4x4.__typestr__,
        )

    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalDenoisedScalerDescriptor.requiresSynchronousInitialization
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXTemporalDenoisedScalerDescriptor.setRequiresSynchronousInitialization_,
            0,
        )

        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalDenoisedScalerDescriptor.isAutoExposureEnabled
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXTemporalDenoisedScalerDescriptor.setAutoExposureEnabled_, 0
        )

        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalDenoisedScalerDescriptor.isTransparencyOverlayTextureEnabled
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXTemporalDenoisedScalerDescriptor.setTransparencyOverlayTextureEnabled_,
            0,
        )

        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalDenoisedScalerDescriptor.supportsMetal4FX_
        )
        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalDenoisedScalerDescriptor.supportsDevice_
        )
