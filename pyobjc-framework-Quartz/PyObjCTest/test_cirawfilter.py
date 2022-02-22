from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCIRAWFilter(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Quartz.CIRAWDecoderVersion, str)
        self.assertIsTypedEnum(Quartz.CIRAWFilterOption, str)

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

    @min_os_level("11.1")
    def testConstants11_1(self):
        self.assertIsInstance(Quartz.kCIInputLocalToneMapAmountKey, str)

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(Quartz.CIRAWDecoderVersionNone, str)
        self.assertIsInstance(Quartz.CIRAWDecoderVersion8, str)
        self.assertIsInstance(Quartz.CIRAWDecoderVersion8DNG, str)
        self.assertIsInstance(Quartz.CIRAWDecoderVersion7, str)
        self.assertIsInstance(Quartz.CIRAWDecoderVersion7DNG, str)
        self.assertIsInstance(Quartz.CIRAWDecoderVersion6, str)
        self.assertIsInstance(Quartz.CIRAWDecoderVersion6DNG, str)

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(Quartz.CIRAWFilter.isGamutMappingEnabled)
        self.assertArgIsBOOL(Quartz.CIRAWFilter.setGamutMappingEnabled_, 0)

        self.assertResultIsBOOL(Quartz.CIRAWFilter.isLensCorrectionSupported)

        self.assertResultIsBOOL(Quartz.CIRAWFilter.isLensCorrectionEnabled)
        self.assertArgIsBOOL(Quartz.CIRAWFilter.setLensCorrectionEnabled_, 0)

        self.assertResultIsBOOL(Quartz.CIRAWFilter.isLuminanceNoiseReductionSupported)

        self.assertResultIsBOOL(Quartz.CIRAWFilter.isColorNoiseReductionSupported)

        self.assertResultIsBOOL(Quartz.CIRAWFilter.isSharpnessSupported)

        self.assertResultIsBOOL(Quartz.CIRAWFilter.isContrastSupported)

        self.assertResultIsBOOL(Quartz.CIRAWFilter.isDetailSupported)

        self.assertResultIsBOOL(Quartz.CIRAWFilter.isMoireReductionSupported)

        self.assertResultIsBOOL(Quartz.CIRAWFilter.isLocalToneMapSupported)
