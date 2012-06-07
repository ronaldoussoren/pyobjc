
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

try:
    unicode
except NameError:
    unicode = str

class TestCIRAWFilter (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCIInputDecoderVersionKey, unicode)
        self.assertIsInstance(kCISupportedDecoderVersionsKey, unicode)
        self.assertIsInstance(kCIInputBoostKey, unicode)
        self.assertIsInstance(kCIInputNeutralChromaticityXKey, unicode)
        self.assertIsInstance(kCIInputEVKey, unicode)
        self.assertIsInstance(kCIInputNeutralChromaticityXKey, unicode)
        self.assertIsInstance(kCIInputNeutralChromaticityYKey, unicode)
        self.assertIsInstance(kCIInputNeutralTemperatureKey, unicode)
        self.assertIsInstance(kCIInputNeutralTintKey, unicode)
        self.assertIsInstance(kCIInputNeutralLocationKey, unicode)
        self.assertIsInstance(kCIInputScaleFactorKey, unicode)
        self.assertIsInstance(kCIInputAllowDraftModeKey, unicode)
        self.assertIsInstance(kCIInputIgnoreImageOrientationKey, unicode)
        self.assertIsInstance(kCIInputImageOrientationKey, unicode)
        self.assertIsInstance(kCIInputEnableSharpeningKey, unicode)
        self.assertIsInstance(kCIInputEnableChromaticNoiseTrackingKey, unicode)
        self.assertIsInstance(kCIInputBoostShadowAmountKey, unicode)
        self.assertIsInstance(kCIInputBiasKey, unicode)

if __name__ == "__main__":
    main()
