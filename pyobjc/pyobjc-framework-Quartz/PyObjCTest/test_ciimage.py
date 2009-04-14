
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIImage (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kCIFormatARGB8, (int, long))
        self.failUnlessIsInstance(kCIFormatRGBA16, (int, long))
        self.failUnlessIsInstance(kCIFormatRGBAf, (int, long))
        self.failUnlessIsInstance(kCIImageColorSpace, unicode)

    def testMethods(self):
        self.failUnlessArgIsBOOL(CIImage.imageWithTexture_size_flipped_colorSpace_, 2)
        self.failUnlessArgIsBOOL(CIImage.initWithTexture_size_flipped_colorSpace_, 2)

if __name__ == "__main__":
    main()
