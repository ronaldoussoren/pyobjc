from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGEXRToneMappingGamma(TestCase):
    @min_os_level("15.0")
    def test_constants(self):
        self.assertIsInstance(Quartz.kCGEXRToneMappingGammaDefog, str)
        self.assertIsInstance(Quartz.kCGEXRToneMappingGammaExposure, str)
        self.assertIsInstance(Quartz.kCGEXRToneMappingGammaKneeLow, str)
        self.assertIsInstance(Quartz.kCGEXRToneMappingGammaKneeHigh, str)
