from PyObjCTools.TestSupport import TestCase
import MetalFX


class TestMFXTemporalScalingEffectHelper(MetalFX.NSObject):
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

    def reset(self):
        return 1

    def setReset_(self, a):
        pass

    def reversedDepth(self):
        return 1

    def setReversedDepth_(self, a):
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


class TestMFXTemporalScalingEffect(TestCase):
    def test_constants(self):
        self.assertEqual(MetalFX.MFXTemporalScalingEffectVersionStart, 0x10000)

        self.assertIsEnumType(MetalFX.MFXTemporalScalingEffectVersion)
        self.assertEqual(
            MetalFX.MFXTemporalScalingEffectVersion_1,
            MetalFX.MFXTemporalScalingEffectVersionStart,
        )

    def test_protocols(self):
        self.assertProtocolExists("MFXTemporalScalingEffect")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.colorTextureUsage, b"Q"
        )
        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.depthTextureUsage, b"Q"
        )
        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.motionTextureUsage, b"Q"
        )
        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.outputTextureUsage, b"Q"
        )

        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.inputContentWidth, b"Q"
        )
        self.assertArgHasType(
            TestMFXTemporalScalingEffectHelper.setInputContentWidth_, 0, b"Q"
        )
        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.inputContentHeight, b"Q"
        )
        self.assertArgHasType(
            TestMFXTemporalScalingEffectHelper.setInputContentHeight_, 0, b"Q"
        )

        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.jitterOffset, MetalFX.NSPoint.__typestr__
        )
        self.assertArgHasType(
            TestMFXTemporalScalingEffectHelper.setJitterOffset_,
            0,
            MetalFX.NSPoint.__typestr__,
        )

        self.assertResultIsBOOL(TestMFXTemporalScalingEffectHelper.reset)
        self.assertArgIsBOOL(TestMFXTemporalScalingEffectHelper.setReset_, 0)
        self.assertResultIsBOOL(TestMFXTemporalScalingEffectHelper.reversedDepth)
        self.assertArgIsBOOL(TestMFXTemporalScalingEffectHelper.setReversedDepth_, 0)

        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.colorTextureFormat, b"Q"
        )
        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.depthTextureFormat, b"Q"
        )
        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.motionTextureFormat, b"Q"
        )
        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.outputTextureFormat, b"Q"
        )
        self.assertResultHasType(TestMFXTemporalScalingEffectHelper.inputWidth, b"Q")
        self.assertResultHasType(TestMFXTemporalScalingEffectHelper.inputHeight, b"Q")
        self.assertResultHasType(TestMFXTemporalScalingEffectHelper.outputWidth, b"Q")
        self.assertResultHasType(TestMFXTemporalScalingEffectHelper.outputHeight, b"Q")
        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.inputContentMinScale, b"f"
        )
        self.assertResultHasType(
            TestMFXTemporalScalingEffectHelper.inputContentMaxScale, b"f"
        )

    def test_methods(self):
        self.assertResultIsBOOL(
            MetalFX.MFXTemporalScalingEffectDescriptor.enableInputContentProperties
        )
        self.assertArgIsBOOL(
            MetalFX.MFXTemporalScalingEffectDescriptor.setEnableInputContentProperties_,
            0,
        )
