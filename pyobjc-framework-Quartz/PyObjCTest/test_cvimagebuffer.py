from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz
import objc


class TestCVImageBuffer(TestCase):
    @expectedFailure
    def testsMissing(self):
        # FIXME
        Quartz.CVImageBufferGetColorSpace
        Quartz.CVImageBufferRef
        self.fail("Reimplement function tests using an actual buffer")

    def testConstants(self):
        self.assertIsInstance(Quartz.kCVImageBufferCGColorSpaceKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferCleanApertureKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferCleanApertureWidthKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferCleanApertureHeightKey, str)
        self.assertIsInstance(
            Quartz.kCVImageBufferCleanApertureHorizontalOffsetKey, str
        )
        self.assertIsInstance(Quartz.kCVImageBufferCleanApertureVerticalOffsetKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferPreferredCleanApertureKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferFieldCountKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferFieldDetailKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferFieldDetailTemporalTopFirst, str)
        self.assertIsInstance(Quartz.kCVImageBufferFieldDetailTemporalBottomFirst, str)
        self.assertIsInstance(
            Quartz.kCVImageBufferFieldDetailSpatialFirstLineEarly, str
        )
        self.assertIsInstance(Quartz.kCVImageBufferFieldDetailSpatialFirstLineLate, str)
        self.assertIsInstance(Quartz.kCVImageBufferPixelAspectRatioKey, str)
        self.assertIsInstance(
            Quartz.kCVImageBufferPixelAspectRatioHorizontalSpacingKey, str
        )
        self.assertIsInstance(
            Quartz.kCVImageBufferPixelAspectRatioVerticalSpacingKey, str
        )
        self.assertIsInstance(Quartz.kCVImageBufferDisplayDimensionsKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferDisplayWidthKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferDisplayHeightKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferGammaLevelKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferYCbCrMatrixKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferYCbCrMatrix_ITU_R_709_2, str)
        self.assertIsInstance(Quartz.kCVImageBufferYCbCrMatrix_ITU_R_601_4, str)
        self.assertIsInstance(Quartz.kCVImageBufferYCbCrMatrix_SMPTE_240M_1995, str)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(Quartz.kCVImageBufferColorPrimaries_ITU_R_709_2, str)
        self.assertIsInstance(Quartz.kCVImageBufferColorPrimaries_EBU_3213, str)
        self.assertIsInstance(Quartz.kCVImageBufferColorPrimaries_SMPTE_C, str)
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunctionKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_ITU_R_709_2, str)
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_EBU_3213, str)
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_SMPTE_C, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaLocationTopFieldKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaLocationBottomFieldKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaLocation_Left, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaLocation_Center, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaLocation_TopLeft, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaLocation_Top, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaLocation_BottomLeft, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaLocation_Bottom, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaLocation_DV420, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaSubsamplingKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaSubsampling_420, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaSubsampling_422, str)
        self.assertIsInstance(Quartz.kCVImageBufferChromaSubsampling_411, str)
        self.assertIsInstance(Quartz.kCVImageBufferColorPrimariesKey, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.kCVImageBufferICCProfileKey, str)
        self.assertIsInstance(
            Quartz.kCVImageBufferTransferFunction_SMPTE_240M_1995, str
        )
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_UseGamma, str)
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_EBU_3213, str)
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_SMPTE_C, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(Quartz.kCVImageBufferColorPrimaries_P22, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(Quartz.kCVImageBufferAlphaChannelIsOpaque, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(Quartz.kCVImageBufferYCbCrMatrix_ITU_R_2020, str)

        self.assertIsInstance(Quartz.kCVImageBufferColorPrimaries_DCI_P3, str)
        self.assertIsInstance(Quartz.kCVImageBufferColorPrimaries_P3_D65, str)
        self.assertIsInstance(Quartz.kCVImageBufferColorPrimaries_ITU_R_2020, str)

        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_ITU_R_2020, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_SMPTE_ST_428_1, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(
            Quartz.kCVImageBufferTransferFunction_SMPTE_ST_2084_PQ, str
        )
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_ITU_R_2100_HLG, str)
        self.assertIsInstance(Quartz.kCVImageBufferMasteringDisplayColorVolumeKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferContentLightLevelInfoKey, str)
        self.assertIsInstance(Quartz.kCVMetalTextureUsage, str)
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_sRGB, str)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(Quartz.kCVImageBufferTransferFunction_Linear, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(Quartz.kCVImageBufferAlphaChannelModeKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferAlphaChannelMode_StraightAlpha, str)
        self.assertIsInstance(
            Quartz.kCVImageBufferAlphaChannelMode_PremultipliedAlpha, str
        )

    @min_os_level("12.0")
    def testConstants12_0(self):
        self.assertIsInstance(Quartz.kCVImageBufferAmbientViewingEnvironmentKey, str)
        self.assertIsInstance(Quartz.kCVImageBufferRegionOfInterestKey, str)

    def testFunctions(self):
        self.assertResultHasType(
            Quartz.CVImageBufferGetEncodedSize, Quartz.CGSize.__typestr__
        )
        self.assertResultHasType(
            Quartz.CVImageBufferGetDisplaySize, Quartz.CGSize.__typestr__
        )
        self.assertResultHasType(
            Quartz.CVImageBufferGetCleanRect, Quartz.CGRect.__typestr__
        )
        self.assertResultHasType(Quartz.CVImageBufferIsFlipped, objc._C_NSBOOL)

    @min_os_level("10.8")
    def testFunctions10_8(self):
        self.assertResultIsCFRetained(
            Quartz.CVImageBufferCreateColorSpaceFromAttachments
        )

    @min_os_level("10.13")
    def testFunctions10_13(self):
        Quartz.CVYCbCrMatrixGetIntegerCodePointForString
        Quartz.CVColorPrimariesGetIntegerCodePointForString
        Quartz.CVTransferFunctionGetIntegerCodePointForString
        Quartz.CVYCbCrMatrixGetStringForIntegerCodePoint
        Quartz.CVColorPrimariesGetStringForIntegerCodePoint
        Quartz.CVTransferFunctionGetStringForIntegerCodePoint
