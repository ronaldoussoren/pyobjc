
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIImage (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCIFormatARGB8, (int, long))
        self.assertIsInstance(kCIFormatBGRA8, (int, long))
        self.assertIsInstance(kCIFormatRGBA8, (int, long))
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

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(kCIFormatABGR8, (int, long))
        self.assertIsInstance(kCIFormatA8, (int, long))
        self.assertIsInstance(kCIFormatA16, (int, long))
        self.assertIsInstance(kCIFormatAh, (int, long))
        self.assertIsInstance(kCIFormatAf, (int, long))
        self.assertIsInstance(kCIFormatR8, (int, long))
        self.assertIsInstance(kCIFormatR16, (int, long))
        self.assertIsInstance(kCIFormatRh, (int, long))
        self.assertIsInstance(kCIFormatRf, (int, long))
        self.assertIsInstance(kCIFormatRG8, (int, long))
        self.assertIsInstance(kCIFormatRG16, (int, long))
        self.assertIsInstance(kCIFormatRGh, (int, long))
        self.assertIsInstance(kCIFormatRGf, (int, long))

    def testMethods(self):
        self.assertArgIsBOOL(CIImage.imageWithTexture_size_flipped_colorSpace_, 2)
        self.assertArgIsBOOL(CIImage.initWithTexture_size_flipped_colorSpace_, 2)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsBOOL(CIImage.imageWithTexture_size_flipped_options_, 2)
        self.assertArgIsBOOL(CIImage.initWithTexture_size_flipped_options_, 2)

if __name__ == "__main__":
    main()
