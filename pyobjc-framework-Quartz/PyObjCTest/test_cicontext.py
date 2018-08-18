from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIContext (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCIContextOutputColorSpace, unicode)
        self.assertIsInstance(kCIContextWorkingColorSpace, unicode)
        self.assertIsInstance(kCIContextUseSoftwareRenderer, unicode)

        self.assertIsInstance(kCIContextWorkingFormat, unicode)

        self.assertIsInstance(kCIContextOutputPremultiplied, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(kCIContextHighQualityDownsample, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(kCIContextCacheIntermediates, unicode)
        self.assertIsInstance(kCIContextPriorityRequestLow, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(kCIImageRepresentationAVDepthData, unicode)
        self.assertIsInstance(kCIImageRepresentationDepthImage, unicode)
        self.assertIsInstance(kCIImageRepresentationDisparityImage, unicode)

    @min_os_level('10.14')
    def testConstants10_14(self):
        self.assertIsInstance(kCIImageRepresentationAVPortraitEffectsMatte, unicode)
        self.assertIsInstance(kCIImageRepresentationPortraitEffectsMatteImage, unicode)

    def testMethods(self):
        self.assertArgIsOut(CIContext.render_toBitmap_rowBytes_bounds_format_colorSpace_, 1)
        self.assertArgIsVariableSize(CIContext.render_toBitmap_rowBytes_bounds_format_colorSpace_, 1)
        self.assertResultIsCFRetained(CIContext.createCGLayerWithSize_info_)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertArgIsBOOL(CIContext.createCGImage_fromRect_format_colorSpace_deferred_, 4)
        self.assertResultIsCFRetained(CIContext.createCGImage_fromRect_format_colorSpace_deferred_)

    @min_os_level('10.13.4')
    def testMethods_10_13_4(self):
        self.assertResultIsBOOL(CIContext.writeHEIFRepresentationOfImage_toURL_format_colorSpace_options_error_)
        self.assertArgIsOut(CIContext.writeHEIFRepresentationOfImage_toURL_format_colorSpace_options_error_, 5)


if __name__ == "__main__":
    main()
