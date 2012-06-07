
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str

class TestCIImage (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCIFormatARGB8, (int, long))
        self.assertIsInstance(kCIFormatRGBA16, (int, long))
        self.assertIsInstance(kCIFormatRGBAf, (int, long))
        self.assertIsInstance(kCIImageColorSpace, unicode)

    def testMethods(self):
        self.assertArgIsBOOL(CIImage.imageWithTexture_size_flipped_colorSpace_, 2)
        self.assertArgIsBOOL(CIImage.initWithTexture_size_flipped_colorSpace_, 2)

if __name__ == "__main__":
    main()
