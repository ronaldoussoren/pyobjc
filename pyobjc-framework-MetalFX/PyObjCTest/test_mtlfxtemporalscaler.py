from PyObjCTools.TestSupport import TestCase

import MetalFX
import objc


class TestMTLFXTemporalScalerHelper(MetalFX.NSObject):
    def colorTextureUsage(self):
        return 1

    def depthTextureUsage(self):
        return 1

    def motionTextureUsage(self):
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

    def jitterOffset(self):
        return 1

    def setJitterOffset_(self, a):
        pass

    def motionVectorScale(self):
        return 1

    def setMotionVectorScale_(self, a):
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

    def isDepthReversed(self):
        return 1

    def setDepthReversed_(self, a):
        pass


class TestMTLFXTemporalScaler(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MTLFXTemporalScaler")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.colorTextureUsage, objc._C_NSUInteger
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
            TestMTLFXTemporalScalerHelper.jitterOffset, MetalFX.NSPoint.__typestr__
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setJitterOffset_,
            0,
            MetalFX.NSPoint.__typestr__,
        )
        self.assertResultHasType(
            TestMTLFXTemporalScalerHelper.motionVectorScale, MetalFX.NSPoint.__typestr__
        )
        self.assertArgHasType(
            TestMTLFXTemporalScalerHelper.setMotionVectorScale_,
            0,
            MetalFX.NSPoint.__typestr__,
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
        self.assertResultIsBOOL(
            MetalFX.MTLFXTemporalScalerDescriptor.enableInputContentProperties
        )
        self.assertArgIsBOOL(
            MetalFX.MTLFXTemporalScalerDescriptor.setEnableInputContentProperties_, 0
        )
