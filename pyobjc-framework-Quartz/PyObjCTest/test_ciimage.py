
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

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(kCIFormatL8, (int, long))
        self.assertIsInstance(kCIFormatL16, (int, long))
        self.assertIsInstance(kCIFormatLh, (int, long))
        self.assertIsInstance(kCIFormatLf, (int, long))

        self.assertIsInstance(kCIFormatLA8, (int, long))
        self.assertIsInstance(kCIFormatLA16, (int, long))
        self.assertIsInstance(kCIFormatLAh, (int, long))
        self.assertIsInstance(kCIFormatLAf, (int, long))

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(kCIImageNearestSampling, unicode)
        self.assertIsInstance(kCIImageAuxiliaryDepth, unicode)
        self.assertIsInstance(kCIImageAuxiliaryDisparity, unicode)
        self.assertIsInstance(kCIImageApplyOrientationProperty, unicode)

    @min_os_level('10.14')
    def testConstants10_14(self):
        self.assertIsInstance(kCIImageAuxiliaryPortraitEffectsMatte, unicode)

    def testMethods(self):
        self.assertArgIsBOOL(CIImage.imageWithTexture_size_flipped_colorSpace_, 2)
        self.assertArgIsBOOL(CIImage.initWithTexture_size_flipped_colorSpace_, 2)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertArgIsBOOL(CIImage.imageWithTexture_size_flipped_options_, 2)
        self.assertArgIsBOOL(CIImage.initWithTexture_size_flipped_options_, 2)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertArgIsOut(CIContext.writeJPEGRepresentationOfImage_toURL_colorSpace_options_error_, 4)
        self.assertResultIsBOOL(CIContext.writeJPEGRepresentationOfImage_toURL_colorSpace_options_error_)

    @min_os_level('10.13')
    def testMethods10_13(self):
        self.assertArgIsOut(CIContext.writePNGRepresentationOfImage_toURL_format_colorSpace_options_error_, 5)
        self.assertResultIsBOOL(CIContext.writePNGRepresentationOfImage_toURL_format_colorSpace_options_error_)

        self.assertArgIsOut(CIContext.writeHEIFRepresentationOfImage_toURL_format_colorSpace_options_error_, 5)
        self.assertResultIsBOOL(CIContext.writeHEIFRepresentationOfImage_toURL_format_colorSpace_options_error_)

if __name__ == "__main__":
    main()
