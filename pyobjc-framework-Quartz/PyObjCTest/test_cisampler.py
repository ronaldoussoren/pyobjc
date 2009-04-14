
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCISampler (TestCase):
    def testMethods(self):
        self.failUnlessIsNullTerminated(CISampler.samplerWithImage_keysAndValues_)
        self.failUnlessIsNullTerminated(CISampler.initWithImage_keysAndValues_)

    def testConstants(self):
        self.failUnlessIsInstance(kCISamplerAffineMatrix, unicode)
        self.failUnlessIsInstance(kCISamplerWrapMode, unicode)
        self.failUnlessIsInstance(kCISamplerFilterMode, unicode)
        self.failUnlessIsInstance(kCISamplerWrapBlack, unicode)
        self.failUnlessIsInstance(kCISamplerWrapClamp, unicode)
        self.failUnlessIsInstance(kCISamplerFilterNearest, unicode)
        self.failUnlessIsInstance(kCISamplerFilterLinear, unicode)


if __name__ == "__main__":
    main()
