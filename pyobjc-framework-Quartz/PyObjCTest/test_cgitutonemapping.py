from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGITUToneMapping(TestCase):
    @min_os_level("15.2")
    def test_constants(self):
        self.assertIsInstance(Quartz.kCGUse100nitsHLGOOTF, str)
        self.assertIsInstance(Quartz.kCGUseBT1886ForCoreVideoGamma, str)
        self.assertIsInstance(Quartz.kCGSkipBoostToHDR, str)
        self.assertIsInstance(Quartz.kCGUseLegacyHDREcosystem, str)
