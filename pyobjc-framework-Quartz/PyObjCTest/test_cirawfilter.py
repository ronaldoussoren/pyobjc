
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIRAWFilter (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCIInputDecoderVersionKey, unicode)
        self.assertIsInstance(kCISupportedDecoderVersionsKey, unicode)
        self.assertIsInstance(kCIInputBoostKey, unicode)
        self.assertIsInstance(kCIInputNeutralChromaticityXKey, unicode)
        self.assertIsInstance(kCIInputNeutralChromaticityYKey, unicode)
        self.assertIsInstance(kCIInputNeutralTemperatureKey, unicode)
        self.assertIsInstance(kCIInputNeutralTintKey, unicode)
        self.assertIsInstance(kCIInputEVKey, unicode)
        self.assertIsInstance(kCIInputNeutralLocationKey, unicode)
        self.assertIsInstance(kCIInputScaleFactorKey, unicode)
        self.assertIsInstance(kCIInputAllowDraftModeKey, unicode)
        self.assertIsInstance(kCIInputIgnoreImageOrientationKey, unicode)
        self.assertIsInstance(kCIInputImageOrientationKey, unicode)
        self.assertIsInstance(kCIInputEnableSharpeningKey, unicode)
        self.assertIsInstance(kCIInputEnableChromaticNoiseTrackingKey, unicode)
        self.assertIsInstance(kCIInputBoostShadowAmountKey, unicode)
        self.assertIsInstance(kCIInputBiasKey, unicode)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(kCIInputNoiseReductionAmountKey, unicode)
        self.assertIsInstance(kCIInputLinearSpaceFilter, unicode)
        self.assertIsInstance(kCIActiveKeys, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(kCIInputEnableVendorLensCorrectionKey, unicode)
        self.assertIsInstance(kCIInputLuminanceNoiseReductionAmountKey, unicode)
        self.assertIsInstance(kCIInputColorNoiseReductionAmountKey, unicode)
        self.assertIsInstance(kCIInputNoiseReductionSharpnessAmountKey, unicode)
        self.assertIsInstance(kCIInputNoiseReductionContrastAmountKey, unicode)
        self.assertIsInstance(kCIInputNoiseReductionDetailAmountKey, unicode)
        self.assertIsInstance(kCIOutputNativeSizeKey, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(kCIInputBaselineExposureKey, unicode)
        self.assertIsInstance(kCIInputDisableGamutMapKey, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(kCIInputMoireAmountKey, unicode)

if __name__ == "__main__":
    main()
