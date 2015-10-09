
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
        self.assertIsInstance(kCIFormatRGBAh, (int, long))
        self.assertIsInstance(kCIImageColorSpace, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(kCIImageProperties, unicode)
        self.assertIsInstance(kCIImageAutoAdjustEnhance, unicode)
        self.assertIsInstance(kCIImageAutoAdjustRedEye, unicode)
        self.assertIsInstance(kCIImageAutoAdjustFeatures, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(kCIImageTextureTarget, unicode)
        self.assertIsInstance(kCIImageTextureFormat, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(kCIImageAutoAdjustCrop, unicode)
        self.assertIsInstance(kCIImageAutoAdjustLevel, unicode)

    def testMethods(self):
        self.assertArgIsBOOL(CIImage.imageWithTexture_size_flipped_colorSpace_, 2)
        self.assertArgIsBOOL(CIImage.initWithTexture_size_flipped_colorSpace_, 2)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsBOOL(CIImage.imageWithTexture_size_flipped_options_, 2)
        self.assertArgIsBOOL(CIImage.initWithTexture_size_flipped_options_, 2)

if __name__ == "__main__":
    main()
