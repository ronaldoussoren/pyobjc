
from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVImageBuffer (TestCase):
    def testFunctions(self):
        self.assertResultHasType(CVImageBufferGetEncodedSize, CGSize.__typestr__)
        self.assertResultHasType(CVImageBufferGetDisplaySize, CGSize.__typestr__)
        self.assertResultHasType(CVImageBufferGetCleanRect, CGRect.__typestr__)

        # FIXME
        CVImageBufferGetColorSpace
        self.fail("Reimplement function tests using an actual buffer")

    def testConstants(self):
        self.assertIsInstance(kCVImageBufferCGColorSpaceKey, unicode)
        self.assertIsInstance(kCVImageBufferCleanApertureKey, unicode)
        self.assertIsInstance(kCVImageBufferCleanApertureWidthKey, unicode)
        self.assertIsInstance(kCVImageBufferCleanApertureHeightKey, unicode)
        self.assertIsInstance(kCVImageBufferCleanApertureHorizontalOffsetKey, unicode)
        self.assertIsInstance(kCVImageBufferCleanApertureVerticalOffsetKey, unicode)
        self.assertIsInstance(kCVImageBufferPreferredCleanApertureKey, unicode)
        self.assertIsInstance(kCVImageBufferFieldCountKey, unicode)
        self.assertIsInstance(kCVImageBufferFieldDetailKey, unicode)
        self.assertIsInstance(kCVImageBufferFieldDetailTemporalTopFirst, unicode)
        self.assertIsInstance(kCVImageBufferFieldDetailTemporalBottomFirst, unicode)
        self.assertIsInstance(kCVImageBufferFieldDetailSpatialFirstLineEarly, unicode)
        self.assertIsInstance(kCVImageBufferFieldDetailSpatialFirstLineLate, unicode)
        self.assertIsInstance(kCVImageBufferPixelAspectRatioKey, unicode)
        self.assertIsInstance(kCVImageBufferPixelAspectRatioHorizontalSpacingKey, unicode)
        self.assertIsInstance(kCVImageBufferPixelAspectRatioVerticalSpacingKey, unicode)
        self.assertIsInstance(kCVImageBufferDisplayDimensionsKey, unicode)
        self.assertIsInstance(kCVImageBufferDisplayWidthKey, unicode)
        self.assertIsInstance(kCVImageBufferDisplayHeightKey, unicode)
        self.assertIsInstance(kCVImageBufferGammaLevelKey, unicode)
        self.assertIsInstance(kCVImageBufferYCbCrMatrixKey, unicode)
        self.assertIsInstance(kCVImageBufferYCbCrMatrix_ITU_R_709_2, unicode)
        self.assertIsInstance(kCVImageBufferYCbCrMatrix_ITU_R_601_4, unicode)
        self.assertIsInstance(kCVImageBufferYCbCrMatrix_SMPTE_240M_1995, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(kCVImageBufferColorPrimaries_ITU_R_709_2, unicode)
        self.assertIsInstance(kCVImageBufferColorPrimaries_EBU_3213, unicode)
        self.assertIsInstance(kCVImageBufferColorPrimaries_SMPTE_C, unicode)
        self.assertIsInstance(kCVImageBufferTransferFunctionKey, unicode)
        self.assertIsInstance(kCVImageBufferTransferFunction_ITU_R_709_2, unicode)
        self.assertIsInstance(kCVImageBufferTransferFunction_EBU_3213, unicode)
        self.assertIsInstance(kCVImageBufferTransferFunction_SMPTE_C, unicode)
        self.assertIsInstance(kCVImageBufferChromaLocationTopFieldKey, unicode)
        self.assertIsInstance(kCVImageBufferChromaLocationBottomFieldKey, unicode)
        self.assertIsInstance(kCVImageBufferChromaLocation_Left, unicode)
        self.assertIsInstance(kCVImageBufferChromaLocation_Center, unicode)
        self.assertIsInstance(kCVImageBufferChromaLocation_TopLeft, unicode)
        self.assertIsInstance(kCVImageBufferChromaLocation_Top, unicode)
        self.assertIsInstance(kCVImageBufferChromaLocation_BottomLeft, unicode)
        self.assertIsInstance(kCVImageBufferChromaLocation_Bottom, unicode)
        self.assertIsInstance(kCVImageBufferChromaLocation_DV420, unicode)
        self.assertIsInstance(kCVImageBufferChromaSubsamplingKey, unicode)
        self.assertIsInstance(kCVImageBufferChromaSubsampling_420, unicode)
        self.assertIsInstance(kCVImageBufferChromaSubsampling_422, unicode)
        self.assertIsInstance(kCVImageBufferChromaSubsampling_411, unicode)
        self.assertIsInstance(kCVImageBufferColorPrimariesKey, unicode)

if __name__ == "__main__":
    main()
