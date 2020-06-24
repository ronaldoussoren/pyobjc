from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCIRAWFilter(TestCase):
    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(Quartz.kCIInputDecoderVersionKey, str)
        self.assertIsInstance(Quartz.kCISupportedDecoderVersionsKey, str)
        self.assertIsInstance(Quartz.kCIInputBoostKey, str)
        self.assertIsInstance(Quartz.kCIInputNeutralChromaticityXKey, str)
        self.assertIsInstance(Quartz.kCIInputNeutralChromaticityYKey, str)
        self.assertIsInstance(Quartz.kCIInputNeutralTemperatureKey, str)
        self.assertIsInstance(Quartz.kCIInputNeutralTintKey, str)
        self.assertIsInstance(Quartz.kCIInputEVKey, str)
        self.assertIsInstance(Quartz.kCIInputNeutralLocationKey, str)
        self.assertIsInstance(Quartz.kCIInputScaleFactorKey, str)
        self.assertIsInstance(Quartz.kCIInputAllowDraftModeKey, str)
        self.assertIsInstance(Quartz.kCIInputIgnoreImageOrientationKey, str)
        self.assertIsInstance(Quartz.kCIInputImageOrientationKey, str)
        self.assertIsInstance(Quartz.kCIInputEnableSharpeningKey, str)
        self.assertIsInstance(Quartz.kCIInputEnableChromaticNoiseTrackingKey, str)
        self.assertIsInstance(Quartz.kCIInputBoostShadowAmountKey, str)
        self.assertIsInstance(Quartz.kCIInputBiasKey, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(Quartz.kCIInputNoiseReductionAmountKey, str)
        self.assertIsInstance(Quartz.kCIInputLinearSpaceFilter, str)
        self.assertIsInstance(Quartz.kCIActiveKeys, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Quartz.kCIInputEnableVendorLensCorrectionKey, str)
        self.assertIsInstance(Quartz.kCIInputLuminanceNoiseReductionAmountKey, str)
        self.assertIsInstance(Quartz.kCIInputColorNoiseReductionAmountKey, str)
        self.assertIsInstance(Quartz.kCIInputNoiseReductionSharpnessAmountKey, str)
        self.assertIsInstance(Quartz.kCIInputNoiseReductionContrastAmountKey, str)
        self.assertIsInstance(Quartz.kCIInputNoiseReductionDetailAmountKey, str)
        self.assertIsInstance(Quartz.kCIOutputNativeSizeKey, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Quartz.kCIInputBaselineExposureKey, str)
        self.assertIsInstance(Quartz.kCIInputDisableGamutMapKey, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.kCIInputMoireAmountKey, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(Quartz.kCIInputEnableEDRModeKey, str)
