import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVVideoSettings(TestCase):
    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AVFoundation.AVVideoCodecKey, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecH264, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecJPEG, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecAppleProRes4444, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecAppleProRes422, str)
        self.assertIsInstance(AVFoundation.AVVideoWidthKey, str)
        self.assertIsInstance(AVFoundation.AVVideoHeightKey, str)
        self.assertIsInstance(AVFoundation.AVVideoPixelAspectRatioKey, str)
        self.assertIsInstance(
            AVFoundation.AVVideoPixelAspectRatioHorizontalSpacingKey, str
        )
        self.assertIsInstance(
            AVFoundation.AVVideoPixelAspectRatioVerticalSpacingKey, str
        )
        self.assertIsInstance(AVFoundation.AVVideoCleanApertureKey, str)
        self.assertIsInstance(AVFoundation.AVVideoCleanApertureWidthKey, str)
        self.assertIsInstance(AVFoundation.AVVideoCleanApertureHeightKey, str)
        self.assertIsInstance(AVFoundation.AVVideoCleanApertureHorizontalOffsetKey, str)
        self.assertIsInstance(AVFoundation.AVVideoCleanApertureVerticalOffsetKey, str)
        self.assertIsInstance(AVFoundation.AVVideoScalingModeKey, str)
        self.assertIsInstance(AVFoundation.AVVideoScalingModeFit, str)
        self.assertIsInstance(AVFoundation.AVVideoScalingModeResize, str)
        self.assertIsInstance(AVFoundation.AVVideoScalingModeResizeAspect, str)
        self.assertIsInstance(AVFoundation.AVVideoScalingModeResizeAspectFill, str)
        self.assertIsInstance(AVFoundation.AVVideoColorPropertiesKey, str)
        self.assertIsInstance(AVFoundation.AVVideoColorPrimariesKey, str)
        self.assertIsInstance(AVFoundation.AVVideoColorPrimaries_ITU_R_709_2, str)
        self.assertIsInstance(AVFoundation.AVVideoColorPrimaries_EBU_3213, str)
        self.assertIsInstance(AVFoundation.AVVideoColorPrimaries_SMPTE_C, str)
        self.assertIsInstance(AVFoundation.AVVideoTransferFunctionKey, str)
        self.assertIsInstance(AVFoundation.AVVideoTransferFunction_ITU_R_709_2, str)
        self.assertIsInstance(AVFoundation.AVVideoTransferFunction_SMPTE_240M_1995, str)
        self.assertIsInstance(AVFoundation.AVVideoYCbCrMatrixKey, str)
        self.assertIsInstance(AVFoundation.AVVideoYCbCrMatrix_ITU_R_709_2, str)
        self.assertIsInstance(AVFoundation.AVVideoYCbCrMatrix_ITU_R_601_4, str)
        self.assertIsInstance(AVFoundation.AVVideoYCbCrMatrix_SMPTE_240M_1995, str)
        self.assertIsInstance(AVFoundation.AVVideoCompressionPropertiesKey, str)
        self.assertIsInstance(AVFoundation.AVVideoAverageBitRateKey, str)
        self.assertIsInstance(AVFoundation.AVVideoQualityKey, str)
        self.assertIsInstance(AVFoundation.AVVideoMaxKeyFrameIntervalKey, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelKey, str)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Baseline30, str)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Baseline31, str)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Baseline41, str)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Main30, str)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Main31, str)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Main32, str)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Main41, str)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(
            AVFoundation.AVVideoProfileLevelH264BaselineAutoLevel, str
        )
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264MainAutoLevel, str)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264High40, str)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264High41, str)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264HighAutoLevel, str)
        self.assertIsInstance(AVFoundation.AVVideoMaxKeyFrameIntervalDurationKey, str)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVVideoAllowFrameReorderingKey, str)
        self.assertIsInstance(AVFoundation.AVVideoH264EntropyModeKey, str)
        self.assertIsInstance(AVFoundation.AVVideoH264EntropyModeCAVLC, str)
        self.assertIsInstance(AVFoundation.AVVideoH264EntropyModeCABAC, str)
        self.assertIsInstance(AVFoundation.AVVideoExpectedSourceFrameRateKey, str)
        self.assertIsInstance(AVFoundation.AVVideoAverageNonDroppableFrameRateKey, str)
        self.assertIsInstance(AVFoundation.AVVideoEncoderSpecificationKey, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AVFoundation.AVVideoColorPrimaries_P3_D65, str)
        self.assertIsInstance(AVFoundation.AVVideoAllowWideColorKey, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeHEVC, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeH264, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeJPEG, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeAppleProRes4444, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeAppleProRes422, str)
        self.assertIsInstance(AVFoundation.AVVideoColorPrimaries_ITU_R_2020, str)
        self.assertIsInstance(
            AVFoundation.AVVideoTransferFunction_SMPTE_ST_2084_PQ, str
        )
        self.assertIsInstance(AVFoundation.AVVideoTransferFunction_ITU_R_2100_HLG, str)
        self.assertIsInstance(AVFoundation.AVVideoYCbCrMatrix_ITU_R_2020, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecHEVC, str)
        self.assertIsInstance(AVFoundation.AVVideoDecompressionPropertiesKey, str)
        self.assertIsInstance(AVFoundation.AVVideoApertureModeCleanAperture, str)
        self.assertIsInstance(AVFoundation.AVVideoApertureModeProductionAperture, str)
        self.assertIsInstance(AVFoundation.AVVideoApertureModeEncodedPixels, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeAppleProRes422HQ, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeAppleProRes422LT, str)
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeAppleProRes422Proxy, str)
