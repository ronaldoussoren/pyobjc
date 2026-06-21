from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import MetalFX
import objc


class TestMTLFXTemporalScalerHelper(MetalFX.NSObject):
    # MTLFXTemporalScalerBase
    def colorTextureUsage(self):
        return 1

    def depthTextureUsage(self):
        return 1

    def motionTextureUsage(self):
        return 1

    def reactiveMaskTextureUsage(self):
        return 1

    def reactiveTextureUsage(self):
        return 1

    def outputTextureUsage(self):
        return 1

    def inputContentWidth(self):
        return 1

    def setInputContentWidth_(self, a):
        pass

    def inputContentHeight(self):
        return 1

    def setInputContentHeight_(self, a):
        pass

    def colorContentOffsetX(self):
        return 1

    def setColorContentOffsetX_(self, a):
        pass

    def colorContentOffsetY(self):
        return 1

    def setColorContentOffsetY_(self, a):
        pass

    def depthContentOffsetX(self):
        return 1

    def setDepthContentOffsetX_(self, a):
        pass

    def depthContentOffsetY(self):
        return 1

    def setDepthContentOffsetY_(self, a):
        pass

    def motionContentOffsetX(self):
        return 1

    def setMotionContentOffsetX_(self, a):
        pass

    def motionContentOffsetY(self):
        return 1

    def setMotionContentOffsetY_(self, a):
        pass

    def reactiveMaskContentOffsetX(self):
        return 1

    def setReactiveMaskContentOffsetX_(self, a):
        pass

    def reactiveMaskContentOffsetY(self):
        return 1

    def setReactiveMaskContentOffsetY_(self, a):
        pass

    def outputOffsetX(self):
        return 1

    def setOutputOffsetX_(self, a):
        pass

    def outputOffsetY(self):
        return 1

    def setOutputOffsetY_(self, a):
        pass

    def jitterOffsetX(self):
        return 1

    def jitterOffsetY(self):
        return 1

    def setJitterOffsetX_(self, a):
        pass

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

    def reset(self):
        return 1

    def setReset_(self, a):
        pass

    def colorTextureFormat(self):
        return 1

    def depthTextureFormat(self):
        return 1

    def motionTextureFormat(self):
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

    def inputContentMinScale(self):
        return 1

    def inputContentMaxScale(self):
        return 1

    def isOutputResolutionMotionVectorsEnabled(self):
        return 1

    def setOutputResolutionMotionVectorsEnabled_(self, a):
        pass

    def isJitteredMotionVectorsEnabled(self):
        return 1

    def setJitteredMotionVectorsEnabled_(self, a):
        pass

    def isDepthReversed(self):
        return 1

    def setDepthReversed_(self, a):
        pass

    # MTLFXTemporalScaler
    # ... empty ...


class TestMTLFXTemporalScaler(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MTLFXTemporalScaler", MetalFX)

    @min_sdk_level("26.0")
    def test_protocols26_0(self):
        self.assertProtocolExists("MTLFXTemporalScalerBase", MetalFX)

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.colorTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.depthTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.motionTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.reactiveMaskTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.reactiveTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.outputTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.inputContentWidth, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setInputContentWidth_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.inputContentHeight, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setInputContentHeight_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.colorContentOffsetX, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setColorContentOffsetX_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.colorContentOffsetY, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setColorContentOffsetY_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.depthContentOffsetX, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setDepthContentOffsetX_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.depthContentOffsetY, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setDepthContentOffsetY_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.motionContentOffsetX, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setMotionContentOffsetX_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.motionContentOffsetY, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setMotionContentOffsetY_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.reactiveMaskContentOffsetX, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setReactiveMaskContentOffsetX_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.reactiveMaskContentOffsetY, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setReactiveMaskContentOffsetY_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.outputOffsetX, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setOutputOffsetX_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.outputOffsetY, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setOutputOffsetY_, 0, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.jitterOffsetX, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.jitterOffsetY, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setJitterOffsetX_, 0, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setJitterOffsetY_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.motionVectorScaleX, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setMotionVectorScaleX_,
            0,
            objc._C_FLT,
        )

        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.motionVectorScaleY, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setMotionVectorScaleY_,
            0,
            objc._C_FLT,
        )

        self.assertResultIsBOOL(TestMTLFXTemporalScalerHelper.reset)
        self.assertArgIsBOOL(TestMTLFXTemporalScalerHelper.setReset_, 0)

        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.colorTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.depthTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.motionTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.reactiveMaskTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.outputTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.inputWidth, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.inputHeight, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.outputWidth, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.outputHeight, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.inputContentMinScale, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.inputContentMaxScale, objc._C_FLT
        )

        self.assertResultIsBOOL(TestMTLFXTemporalScalerHelper.isDepthReversed)
        self.assertArgIsBOOL(TestMTLFXTemporalScalerHelper.setDepthReversed_, 0)

    def test_methods(self):
        self.assertResultIsBOOL(MetalFX.MTLFXTemporalScalerDescriptor.supportsDevice_)
        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalScalerDescriptor.isAutoExposureEnabled
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXTemporalScalerDescriptor.setAutoExposureEnabled_, 0
        )
        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalScalerDescriptor.requiresSynchronousInitialization
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXTemporalScalerDescriptor.setRequiresSynchronousInitialization_,
            0,
        )
        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalScalerDescriptor.isInputContentPropertiesEnabled
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXTemporalScalerDescriptor.setInputContentPropertiesEnabled_, 0
        )

    @min_os_level("14.3")
    def test_methods14_3(self):
        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalScalerDescriptor.isReactiveMaskTextureEnabled
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXTemporalScalerDescriptor.setReactiveMaskTextureEnabled_, 0
        )

        self.assertResultHasType(
            MetalFX.MTLFXTemporalScalerDescriptor.reactiveMaskTextureFormat,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            MetalFX.MTLFXTemporalScalerDescriptor.setReactiveMaskTextureFormat_,
            0,
            objc._C_NSUInteger,
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(MetalFX.MTLFXTemporalScalerDescriptor.supportsMetal4FX_)

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalScaler.isOutputResolutionMotionVectorsEnabled
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXTemporalScaler.setOutputResolutionMotionVectorsEnabled_, 0
        )
        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalScaler.isJitteredMotionVectorsEnabled
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXTemporalScaler.setJitteredMotionVectorsEnabled_, 0
        )
