
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIRAWFilter (TestCase):
    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(kCIInputDecoderVersionKey, unicode)
        self.failUnlessIsInstance(kCISupportedDecoderVersionsKey, unicode)
        self.failUnlessIsInstance(kCIInputBoostKey, unicode)
        self.failUnlessIsInstance(kCIInputNeutralChromaticityXKey, unicode)
        self.failUnlessIsInstance(kCIInputEVKey, unicode)
        self.failUnlessIsInstance(kCIInputNeutralChromaticityXKey, unicode)
        self.failUnlessIsInstance(kCIInputNeutralChromaticityYKey, unicode)
        self.failUnlessIsInstance(kCIInputNeutralTemperatureKey, unicode)
        self.failUnlessIsInstance(kCIInputNeutralTintKey, unicode)
        self.failUnlessIsInstance(kCIInputNeutralLocationKey, unicode)
        self.failUnlessIsInstance(kCIInputScaleFactorKey, unicode)
        self.failUnlessIsInstance(kCIInputAllowDraftModeKey, unicode)
        self.failUnlessIsInstance(kCIInputIgnoreImageOrientationKey, unicode)
        self.failUnlessIsInstance(kCIInputImageOrientationKey, unicode)
        self.failUnlessIsInstance(kCIInputEnableSharpeningKey, unicode)
        self.failUnlessIsInstance(kCIInputEnableChromaticNoiseTrackingKey, unicode)
        self.failUnlessIsInstance(kCIInputBoostShadowAmountKey, unicode)
        self.failUnlessIsInstance(kCIInputBiasKey, unicode)

if __name__ == "__main__":
    main()
