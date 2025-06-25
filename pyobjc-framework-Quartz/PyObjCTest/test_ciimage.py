from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCIImage(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Quartz.CIFormat, int)
        self.assertIsTypedEnum(Quartz.CIImageAutoAdjustmentOption, str)
        self.assertIsTypedEnum(Quartz.CIImageOption, str)

    def testConstants(self):
        self.assertIsInstance(Quartz.kCIFormatARGB8, int)
        self.assertIsInstance(Quartz.kCIFormatBGRA8, int)
        self.assertIsInstance(Quartz.kCIFormatRGBA8, int)
        self.assertIsInstance(Quartz.kCIFormatRGBA16, int)
        self.assertIsInstance(Quartz.kCIFormatRGBAf, int)
        self.assertIsInstance(Quartz.kCIFormatRGBAh, int)
        self.assertIsInstance(Quartz.kCIImageColorSpace, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(Quartz.kCIImageProperties, str)
        self.assertIsInstance(Quartz.kCIImageAutoAdjustEnhance, str)
        self.assertIsInstance(Quartz.kCIImageAutoAdjustRedEye, str)
        self.assertIsInstance(Quartz.kCIImageAutoAdjustFeatures, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(Quartz.kCIImageTextureTarget, str)
        self.assertIsInstance(Quartz.kCIImageTextureFormat, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Quartz.kCIImageAutoAdjustCrop, str)
        self.assertIsInstance(Quartz.kCIImageAutoAdjustLevel, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Quartz.kCIFormatABGR8, int)
        self.assertIsInstance(Quartz.kCIFormatA8, int)
        self.assertIsInstance(Quartz.kCIFormatA16, int)
        self.assertIsInstance(Quartz.kCIFormatAh, int)
        self.assertIsInstance(Quartz.kCIFormatAf, int)
        self.assertIsInstance(Quartz.kCIFormatR8, int)
        self.assertIsInstance(Quartz.kCIFormatR16, int)
        self.assertIsInstance(Quartz.kCIFormatRh, int)
        self.assertIsInstance(Quartz.kCIFormatRf, int)
        self.assertIsInstance(Quartz.kCIFormatRG8, int)
        self.assertIsInstance(Quartz.kCIFormatRG16, int)
        self.assertIsInstance(Quartz.kCIFormatRGh, int)
        self.assertIsInstance(Quartz.kCIFormatRGf, int)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Quartz.kCIFormatL8, int)
        self.assertIsInstance(Quartz.kCIFormatL16, int)
        self.assertIsInstance(Quartz.kCIFormatLh, int)
        self.assertIsInstance(Quartz.kCIFormatLf, int)

        self.assertIsInstance(Quartz.kCIFormatLA8, int)
        self.assertIsInstance(Quartz.kCIFormatLA16, int)
        self.assertIsInstance(Quartz.kCIFormatLAh, int)
        self.assertIsInstance(Quartz.kCIFormatLAf, int)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.kCIImageNearestSampling, str)
        self.assertIsInstance(Quartz.kCIImageAuxiliaryDepth, str)
        self.assertIsInstance(Quartz.kCIImageAuxiliaryDisparity, str)
        self.assertIsInstance(Quartz.kCIImageApplyOrientationProperty, str)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(Quartz.kCIImageAuxiliaryPortraitEffectsMatte, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(Quartz.kCIImageAuxiliarySemanticSegmentationSkinMatte, str)
        self.assertIsInstance(Quartz.kCIImageAuxiliarySemanticSegmentationHairMatte, str)
        self.assertIsInstance(Quartz.kCIImageAuxiliarySemanticSegmentationTeethMatte, str)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(Quartz.kCIImageToneMapHDRtoSDR, str)
        self.assertIsInstance(
            Quartz.kCIImageAuxiliarySemanticSegmentationGlassesMatte, str
        )

    @min_os_level("11.1")
    def testConstants11_1(self):
        self.assertIsInstance(Quartz.kCIImageAuxiliarySemanticSegmentationSkyMatte, str)

    @min_os_level("14.0")
    def testConstants14_0(self):
        self.assertIsInstance(Quartz.kCIFormatRGBX16, int)
        self.assertIsInstance(Quartz.kCIFormatRGBXh, int)
        self.assertIsInstance(Quartz.kCIFormatRGBXf, int)
        self.assertIsInstance(Quartz.kCIFormatRGB10, int)

        self.assertIsInstance(Quartz.kCIImageExpandToHDR, str)
        self.assertIsInstance(Quartz.kCIImageCacheImmediately, str)
        self.assertIsInstance(Quartz.kCIImageAuxiliaryHDRGainMap, str)

    @min_os_level("15.0")
    def testConstants15_0(self):
        self.assertIsInstance(Quartz.kCIImageContentHeadroom, str)

    def testMethods(self):
        self.assertArgIsBOOL(Quartz.CIImage.imageWithTexture_size_flipped_colorSpace_, 2)
        self.assertArgIsBOOL(Quartz.CIImage.initWithTexture_size_flipped_colorSpace_, 2)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBOOL(Quartz.CIImage.imageWithTexture_size_flipped_options_, 2)
        self.assertArgIsBOOL(Quartz.CIImage.initWithTexture_size_flipped_options_, 2)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsOut(
            Quartz.CIContext.writeJPEGRepresentationOfImage_toURL_colorSpace_options_error_,
            4,
        )
        self.assertResultIsBOOL(
            Quartz.CIContext.writeJPEGRepresentationOfImage_toURL_colorSpace_options_error_
        )

        self.assertArgIsBOOL(
            Quartz.CIImage.imageByApplyingTransform_highQualityDownsample_, 1
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsOut(
            Quartz.CIContext.writePNGRepresentationOfImage_toURL_format_colorSpace_options_error_,
            5,
        )
        self.assertResultIsBOOL(
            Quartz.CIContext.writePNGRepresentationOfImage_toURL_format_colorSpace_options_error_
        )

        self.assertArgIsOut(
            Quartz.CIContext.writeHEIFRepresentationOfImage_toURL_format_colorSpace_options_error_,
            5,
        )
        self.assertResultIsBOOL(
            Quartz.CIContext.writeHEIFRepresentationOfImage_toURL_format_colorSpace_options_error_
        )

    @min_os_level("15.0")
    def testMethods15_0(self):
        self.assertResultIsBOOL(Quartz.CIImage.isOpaque)
