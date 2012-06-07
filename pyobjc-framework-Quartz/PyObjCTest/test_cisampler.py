
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

try:
    unicode
except NameError:
    unicode = str

class TestCISampler (TestCase):
    def testMethods(self):
        self.assertIsNullTerminated(CISampler.samplerWithImage_keysAndValues_)
        self.assertIsNullTerminated(CISampler.initWithImage_keysAndValues_)

    def testConstants(self):
        self.assertIsInstance(kCISamplerAffineMatrix, unicode)
        self.assertIsInstance(kCISamplerWrapMode, unicode)
        self.assertIsInstance(kCISamplerFilterMode, unicode)
        self.assertIsInstance(kCISamplerWrapBlack, unicode)
        self.assertIsInstance(kCISamplerWrapClamp, unicode)
        self.assertIsInstance(kCISamplerFilterNearest, unicode)
        self.assertIsInstance(kCISamplerFilterLinear, unicode)


if __name__ == "__main__":
    main()
