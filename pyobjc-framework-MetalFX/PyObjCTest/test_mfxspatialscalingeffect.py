from PyObjCTools.TestSupport import TestCase
import MetalFX
import objc


class TestMFXSpatialScalingEffectHelper(MetalFX.NSObject):
    def colorTextureUsage(self):
        return 1

    def outputTextureUsage(self):
        return 1

    def inputContentWidth(self):
        return 1

    def setInputContentWidth_(self, a):
        return 1

    def inputContentHeight(self):
        return 1

    def setInputContentHeight_(self, a):
        return 1

    def colorTextureFormat(self):
        return 1

    def outputTextureFormat(self):
        return 1

    def inputWidth(self):
        return 1

    def inputHeigh(self):
        return 1

    def outputWidth(self):
        return 1

    def outputHeight(self):
        return 1

    def colorProcessingMode(self):
        return 1


class TestMFXSpatialScalingEffect(TestCase):
    def test_constants(self):
        self.assertEqual(MetalFX.MFXSpatialScalingEffectVersionStart, 0x10000)

        self.assertIsEnumType(MetalFX.MFXSpatialScalingEffectVersion)
        self.assertEqual(
            MetalFX.MFXSpatialScalingEffectVersion_1,
            MetalFX.MFXSpatialScalingEffectVersionStart,
        )

        self.assertIsEnumType(MetalFX.MFXSpatialScalingColorProcessingMode)
        self.assertEqual(MetalFX.MFXSpatialScalingColorProcessingMode_Perceptual, 0)
        self.assertEqual(MetalFX.MFXSpatialScalingColorProcessingMode_Linear, 1)
        self.assertEqual(MetalFX.MFXSpatialScalingColorProcessingMode_HDR, 2)

    def test_protocols(self):
        objc.protocolNamed("MFXSpatialScalingEffect")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMFXSpatialScalingEffectHelper.colorTextureUsage, b"@"
        )
        self.assertResultHasType(
            TestMFXSpatialScalingEffectHelper.outputTextureUsage, b"@"
        )

        self.assertResultHasType(
            TestMFXSpatialScalingEffectHelper.inputContentWidth, b"Q"
        )
        self.assertArgHasType(
            TestMFXSpatialScalingEffectHelper.setInputContentWidth_, 0, b"Q"
        )
        self.assertResultHasType(
            TestMFXSpatialScalingEffectHelper.inputContentHeight, b"Q"
        )
        self.assertArgHasType(
            TestMFXSpatialScalingEffectHelper.setInputContentHeight_, 0, b"Q"
        )

        self.assertResultHasType(
            TestMFXSpatialScalingEffectHelper.colorTextureFormat, b"Q"
        )
        self.assertResultHasType(
            TestMFXSpatialScalingEffectHelper.outputTextureFormat, b"Q"
        )
        self.assertResultHasType(TestMFXSpatialScalingEffectHelper.inputWidth, b"Q")
        self.assertResultHasType(TestMFXSpatialScalingEffectHelper.inputHeigh, b"Q")
        self.assertResultHasType(TestMFXSpatialScalingEffectHelper.outputWidth, b"Q")
        self.assertResultHasType(TestMFXSpatialScalingEffectHelper.outputHeight, b"Q")
        self.assertResultHasType(
            TestMFXSpatialScalingEffectHelper.colorProcessingMode, b"Q"
        )
