from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc
import objc.simd

import MetalFX


class TestMTLFXFrameInterpolatorHelper(MetalFX.NSObject):
    # MTLFXFrameInterpolatorBase
    def colorTextureUsage(self):
        return 1

    def outputTextureUsage(self):
        return 1

    def depthTextureUsage(self):
        return 1

    def motionTextureUsage(self):
        return 1

    def uiTextureUsage(self):
        return 1

    def colorTextureFormat(self):
        return 1

    def depthTextureFormat(self):
        return 1

    def motionTextureFormat(self):
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

    def uiTextureFormat(self):
        return 1

    def contentWidth(self):
        return 1

    def setContentWidth_(self, a):
        pass

    def contentHeight(self):
        return 1

    def setContentHeight_(self, a):
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

    def distortionOffsetX(self):
        return 1

    def setDistortionOffsetX_(self, a):
        pass

    def distortionOffsetY(self):
        return 1

    def setDistortionOffsetY_(self, a):
        pass

    def distortionWidth(self):
        return 1

    def setDistortionWidth_(self, a):
        pass

    def distortionHeight(self):
        return 1

    def setDistortionHeight_(self, a):
        pass

    def outputOffsetX(self):
        return 1

    def setOutputOffsetX_(self, a):
        pass

    def outputOffsetY(self):
        return 1

    def setOutputOffsetY_(self, a):
        pass

    def setMotionVectorScaleX_(self, x):
        pass

    # def outputOffsetX(self):
    #    return 1

    # def setOutputOffsetX_(self, a):
    #    pass

    # def outputOffsetY(self):
    #    return 1

    def motionVectorScaleX(self):
        return 1

    # def setMotionVectorScaleX_(self, x):
    #    pass

    def motionVectorScaleY(self):
        return 1

    def setMotionVectorScaleY_(self, x):
        pass

    def deltaTime(self):
        return 1

    def setDeltaTime_(self, x):
        pass

    def nearPlane(self):
        return 1

    def setNearPlane_(self, x):
        pass

    def farPlane(self):
        return 1

    def setFarPlane_(self, x):
        pass

    def fieldOfView(self):
        return 1

    def setFieldOfView_(self, x):
        pass

    def aspectRatio(self):
        return 1

    def setAspectRatio_(self, x):
        pass

    def worldToViewMatrix(self):
        return 1

    def setWorldToViewMatrix_(self, a):
        pass

    def viewToClipMatrix(self):
        return 1

    def setViewToClipMatrix_(self, a):
        pass

    def jitterOffsetX(self):
        return 1

    def setJitterOffsetX_(self, x):
        pass

    def jitterOffsetY(self):
        return 1

    def setJitterOffsetY_(self, x):
        pass

    def isUITextureComposited(self):
        return 1

    def setIsUITextureComposited_(self, x):
        pass

    def shouldResetHistory(self):
        return 1

    def setShouldResetHistory_(self, x):
        pass

    def isDepthReversed(self):
        return 1

    def setDepthReversed_(self, x):
        pass

    # MTLFXFrameInterpolator
    # ... empty ...


class TestMTLFXFrameInterpolator(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            MetalFX.MTLFXFrameInterpolatorDescriptor.supportsMetal4FX_
        )
        self.assertResultIsBOOL(
            MetalFX.MTLFXFrameInterpolatorDescriptor.supportsDevice_
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            MetalFX.MTLFXFrameInterpolator.isDistortionTextureEnabled
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXFrameInterpolator.setDistortionTextureEnabled_, 0
        )
        self.assertResultIsBOOL(MetalFX.MTLFXFrameInterpolator.requiresPrevColorTexture)
        self.assertArgIsBOOL(
            MetalFX.MTLFXFrameInterpolator.setRequiresPrevColorTexture_, 0
        )

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLFXFrameInterpolatorBase", MetalFX)
        self.assertProtocolExists("MTLFXFrameInterpolator", MetalFX)

    def test_protocol_methods(self):

        # MTLFXFrameInterpolatorBase
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.colorTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.outputTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.depthTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.motionTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.uiTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.colorTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.depthTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.motionTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.outputTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.inputWidth, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.inputHeight, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.outputWidth, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.outputHeight, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.uiTextureFormat, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.contentWidth, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setContentWidth_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.contentHeight, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setContentHeight_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.depthContentOffsetX, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setDepthContentOffsetX_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.depthContentOffsetY, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setDepthContentOffsetY_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.motionContentOffsetX, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setMotionContentOffsetX_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.motionContentOffsetY, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setMotionContentOffsetY_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.outputOffsetX, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setOutputOffsetX_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.outputOffsetY, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setOutputOffsetY_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.distortionOffsetX, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setDistortionOffsetX_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.distortionOffsetY, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setDistortionOffsetY_,
            0,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.distortionWidth, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setDistortionWidth_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.distortionHeight, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setDistortionHeight_, 0, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.motionVectorScaleX, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setMotionVectorScaleX_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.motionVectorScaleY, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setMotionVectorScaleY_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.deltaTime, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setDeltaTime_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.nearPlane, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setNearPlane_, 0, objc._C_FLT
        )
        self.assertResultHasType(TestMTLFXFrameInterpolatorHelper.farPlane, objc._C_FLT)
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setFarPlane_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.fieldOfView, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setFieldOfView_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.aspectRatio, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setAspectRatio_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.worldToViewMatrix,
            objc.simd.simd_float4x4.__typestr__,
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setWorldToViewMatrix_,
            0,
            objc.simd.simd_float4x4.__typestr__,
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.viewToClipMatrix,
            objc.simd.simd_float4x4.__typestr__,
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setViewToClipMatrix_,
            0,
            objc.simd.simd_float4x4.__typestr__,
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.jitterOffsetX, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setJitterOffsetX_, 0, objc._C_FLT
        )
        self.assertResultHasType(
            TestMTLFXFrameInterpolatorHelper.jitterOffsetY, objc._C_FLT
        )
        self.assertArgHasType(
            TestMTLFXFrameInterpolatorHelper.setJitterOffsetY_, 0, objc._C_FLT
        )

        self.assertResultIsBOOL(TestMTLFXFrameInterpolatorHelper.isUITextureComposited)
        self.assertArgIsBOOL(
            TestMTLFXFrameInterpolatorHelper.setIsUITextureComposited_, 0
        )
        self.assertResultIsBOOL(TestMTLFXFrameInterpolatorHelper.shouldResetHistory)
        self.assertArgIsBOOL(TestMTLFXFrameInterpolatorHelper.setShouldResetHistory_, 0)
        self.assertResultIsBOOL(TestMTLFXFrameInterpolatorHelper.isDepthReversed)
        self.assertArgIsBOOL(TestMTLFXFrameInterpolatorHelper.setDepthReversed_, 0)

        # MTLFXFrameInterpolator
        # ... empty ...
