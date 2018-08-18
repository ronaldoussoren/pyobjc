
from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVImageBuffer (TestCase):


    @expectedFailure
    def testsMissing(self):
        # FIXME
        CVImageBufferGetColorSpace
        CVImageBufferRef
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

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCVImageBufferICCProfileKey, unicode)
        self.assertIsInstance(kCVImageBufferTransferFunction_SMPTE_240M_1995, unicode)
        self.assertIsInstance(kCVImageBufferTransferFunction_UseGamma, unicode)
        self.assertIsInstance(kCVImageBufferTransferFunction_EBU_3213, unicode)
        self.assertIsInstance(kCVImageBufferTransferFunction_SMPTE_C, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(kCVImageBufferColorPrimaries_P22, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(kCVImageBufferAlphaChannelIsOpaque, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(kCVImageBufferYCbCrMatrix_ITU_R_2020, unicode)

        self.assertIsInstance(kCVImageBufferColorPrimaries_DCI_P3, unicode)
        self.assertIsInstance(kCVImageBufferColorPrimaries_P3_D65, unicode)
        self.assertIsInstance(kCVImageBufferColorPrimaries_ITU_R_2020, unicode)

        self.assertIsInstance(kCVImageBufferTransferFunction_ITU_R_2020, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(kCVImageBufferTransferFunction_SMPTE_ST_428_1, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(kCVImageBufferTransferFunction_SMPTE_ST_2084_PQ, unicode)
        self.assertIsInstance(kCVImageBufferTransferFunction_ITU_R_2100_HLG, unicode)
        self.assertIsInstance(kCVImageBufferMasteringDisplayColorVolumeKey, unicode)
        self.assertIsInstance(kCVImageBufferContentLightLevelInfoKey, unicode)
        self.assertIsInstance(kCVMetalTextureUsage, unicode)
        self.assertIsInstance(kCVImageBufferTransferFunction_sRGB, unicode)

    @min_os_level('10.14')
    def testConstants10_14(self):
        self.assertIsInstance(kCVImageBufferTransferFunction_Linear, unicode)

    def testFunctions(self):
        self.assertResultHasType(CVImageBufferGetEncodedSize, CGSize.__typestr__)
        self.assertResultHasType(CVImageBufferGetDisplaySize, CGSize.__typestr__)
        self.assertResultHasType(CVImageBufferGetCleanRect, CGRect.__typestr__)
        self.assertResultHasType(CVImageBufferIsFlipped, objc._C_NSBOOL)

    @min_os_level('10.8')
    def testFunctions10_8(self):
        self.assertResultIsCFRetained(CVImageBufferCreateColorSpaceFromAttachments)

    @min_os_level('10.13')
    def testFunctions10_13(self):
        CVYCbCrMatrixGetIntegerCodePointForString
        CVColorPrimariesGetIntegerCodePointForString
        CVTransferFunctionGetIntegerCodePointForString
        CVYCbCrMatrixGetStringForIntegerCodePoint
        CVColorPrimariesGetStringForIntegerCodePoint
        CVTransferFunctionGetStringForIntegerCodePoint


if __name__ == "__main__":
    main()
