from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCIContext(TestCase):
    def testConstants(self):
        self.assertIsInstance(Quartz.kCIContextOutputColorSpace, str)
        self.assertIsInstance(Quartz.kCIContextWorkingColorSpace, str)
        self.assertIsInstance(Quartz.kCIContextUseSoftwareRenderer, str)

        self.assertIsInstance(Quartz.kCIContextWorkingFormat, str)

        self.assertIsInstance(Quartz.kCIContextOutputPremultiplied, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Quartz.kCIContextHighQualityDownsample, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Quartz.kCIContextCacheIntermediates, str)
        self.assertIsInstance(Quartz.kCIContextPriorityRequestLow, str)
        self.assertIsInstance(Quartz.kCIContextAllowLowPower, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(Quartz.kCIImageRepresentationAVDepthData, str)
        self.assertIsInstance(Quartz.kCIImageRepresentationDepthImage, str)
        self.assertIsInstance(Quartz.kCIImageRepresentationDisparityImage, str)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(Quartz.kCIImageRepresentationAVPortraitEffectsMatte, str)
        self.assertIsInstance(
            Quartz.kCIImageRepresentationPortraitEffectsMatteImage, str
        )
        self.assertIsInstance(Quartz.kCIContextName, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            Quartz.kCIImageRepresentationAVSemanticSegmentationMattes, str
        )
        self.assertIsInstance(
            Quartz.kCIImageRepresentationSemanticSegmentationSkinMatteImage, str
        )
        self.assertIsInstance(
            Quartz.kCIImageRepresentationSemanticSegmentationHairMatteImage, str
        )
        self.assertIsInstance(
            Quartz.kCIImageRepresentationSemanticSegmentationTeethMatteImage, str
        )

    @min_os_level("10.16")
    def testConstants10_16(self):
        self.assertIsInstance(
            Quartz.kCIImageRepresentationSemanticSegmentationGlassesMatteImage, str
        )

    def testMethods(self):
        self.assertArgIsOut(
            Quartz.CIContext.render_toBitmap_rowBytes_bounds_format_colorSpace_, 1
        )
        self.assertArgIsVariableSize(
            Quartz.CIContext.render_toBitmap_rowBytes_bounds_format_colorSpace_, 1
        )
        self.assertResultIsCFRetained(Quartz.CIContext.createCGLayerWithSize_info_)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBOOL(
            Quartz.CIContext.createCGImage_fromRect_format_colorSpace_deferred_, 4
        )
        self.assertResultIsCFRetained(
            Quartz.CIContext.createCGImage_fromRect_format_colorSpace_deferred_
        )

    @min_os_level("10.13.4")
    def testMethods_10_13_4(self):
        self.assertResultIsBOOL(
            Quartz.CIContext.writeHEIFRepresentationOfImage_toURL_format_colorSpace_options_error_
        )
        self.assertArgIsOut(
            Quartz.CIContext.writeHEIFRepresentationOfImage_toURL_format_colorSpace_options_error_,
            5,
        )
