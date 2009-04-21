
from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *
from Quartz import *

class TestCVImageBuffer (TestCase):
    def testFunctions(self):
        self.failUnlessResultHasType(CVImageBufferGetEncodedSize, CGSize.__typestr__)
        self.failUnlessResultHasType(CVImageBufferGetDisplaySize, CGSize.__typestr__)
        self.failUnlessResultHasType(CVImageBufferGetCleanRect, CGRect.__typestr__)

        # FIXME
        CVImageBufferGetColorSpace
        self.fail("Reimplement function tests using an actual buffer")

    def testConstants(self):
        self.failUnlessIsInstance(kCVImageBufferCGColorSpaceKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferCleanApertureKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferCleanApertureWidthKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferCleanApertureHeightKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferCleanApertureHorizontalOffsetKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferCleanApertureVerticalOffsetKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferPreferredCleanApertureKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferFieldCountKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferFieldDetailKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferFieldDetailTemporalTopFirst, unicode)
        self.failUnlessIsInstance(kCVImageBufferFieldDetailTemporalBottomFirst, unicode)
        self.failUnlessIsInstance(kCVImageBufferFieldDetailSpatialFirstLineEarly, unicode)
        self.failUnlessIsInstance(kCVImageBufferFieldDetailSpatialFirstLineLate, unicode)
        self.failUnlessIsInstance(kCVImageBufferPixelAspectRatioKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferPixelAspectRatioHorizontalSpacingKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferPixelAspectRatioVerticalSpacingKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferDisplayDimensionsKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferDisplayWidthKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferDisplayHeightKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferGammaLevelKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferYCbCrMatrixKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferYCbCrMatrix_ITU_R_709_2, unicode)
        self.failUnlessIsInstance(kCVImageBufferYCbCrMatrix_ITU_R_601_4, unicode)
        self.failUnlessIsInstance(kCVImageBufferYCbCrMatrix_SMPTE_240M_1995, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(kCVImageBufferColorPrimaries_ITU_R_709_2, unicode)
        self.failUnlessIsInstance(kCVImageBufferColorPrimaries_EBU_3213, unicode)
        self.failUnlessIsInstance(kCVImageBufferColorPrimaries_SMPTE_C, unicode)
        self.failUnlessIsInstance(kCVImageBufferTransferFunctionKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferTransferFunction_ITU_R_709_2, unicode)
        self.failUnlessIsInstance(kCVImageBufferTransferFunction_EBU_3213, unicode)
        self.failUnlessIsInstance(kCVImageBufferTransferFunction_SMPTE_C, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaLocationTopFieldKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaLocationBottomFieldKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaLocation_Left, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaLocation_Center, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaLocation_TopLeft, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaLocation_Top, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaLocation_BottomLeft, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaLocation_Bottom, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaLocation_DV420, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaSubsamplingKey, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaSubsampling_420, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaSubsampling_422, unicode)
        self.failUnlessIsInstance(kCVImageBufferChromaSubsampling_411, unicode)
        self.failUnlessIsInstance(kCVImageBufferColorPrimariesKey, unicode)

if __name__ == "__main__":
    main()
