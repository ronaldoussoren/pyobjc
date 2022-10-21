from PyObjCTools.TestSupport import TestCase
import objc

import MetalFX


class TestMTLFXSpatialScalerHelper(MetalFX.NSObject):
    def colorTextureUsage(self):
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

    def colorTextureFormat(self):
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

    def colorProcessingMode(self):
        return 1


class TestMTLFXSpatialScaler(TestCase):
    def test_constants(self):
        self.assertIsEnumType(MetalFX.MTLFXSpatialScalerColorProcessingMode)
        self.assertEqual(MetalFX.MTLFXSpatialScalerColorProcessingModePerceptual, 0)
        self.assertEqual(MetalFX.MTLFXSpatialScalerColorProcessingModeLinear, 1)
        self.assertEqual(MetalFX.MTLFXSpatialScalerColorProcessingModeHDR, 2)

    def test_protocols(self):
        self.assertProtocolExists("MTLFXSpatialScaler")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.colorTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.outputTextureUsage, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.inputContentWidth, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXSpatialScalerHelper.setInputContentWidth_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.inputContentHeight, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTLFXSpatialScalerHelper.setInputContentHeight_, 0, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.colorTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.outputTextureFormat, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.inputWidth, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.inputHeight, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.outputWidth, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.outputHeight, objc._C_NSUInteger
        )
        self.assertResultHasType(
            TestMTLFXSpatialScalerHelper.colorProcessingMode, objc._C_NSInteger
        )
