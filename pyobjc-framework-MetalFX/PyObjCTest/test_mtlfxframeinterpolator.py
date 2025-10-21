from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc

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

    def motionVectorScaleX(self):
        return 1

    def setMotionVectorScaleX_(self, x):
        pass

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

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLFXFrameInterpolatorBase")
        self.assertProtocolExists("MTLFXFrameInterpolator")

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
