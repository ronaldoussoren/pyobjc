from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCISampler(TestCase):
    def testMethods(self):
        self.assertIsNullTerminated(Quartz.CISampler.samplerWithImage_keysAndValues_)
        self.assertIsNullTerminated(Quartz.CISampler.initWithImage_keysAndValues_)

    def testConstants(self):
        self.assertIsInstance(Quartz.kCISamplerAffineMatrix, str)
        self.assertIsInstance(Quartz.kCISamplerWrapMode, str)
        self.assertIsInstance(Quartz.kCISamplerFilterMode, str)
        self.assertIsInstance(Quartz.kCISamplerWrapBlack, str)
        self.assertIsInstance(Quartz.kCISamplerWrapClamp, str)
        self.assertIsInstance(Quartz.kCISamplerFilterNearest, str)
        self.assertIsInstance(Quartz.kCISamplerFilterLinear, str)
        self.assertIsInstance(Quartz.kCISamplerColorSpace, str)
