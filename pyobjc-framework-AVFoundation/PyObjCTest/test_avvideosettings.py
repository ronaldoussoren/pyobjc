
from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVVideoSettings (TestCase):
    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(AVFoundation.AVVideoCodecKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCodecH264, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCodecJPEG, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCodecAppleProRes4444, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCodecAppleProRes422, unicode)
        self.assertIsInstance(AVFoundation.AVVideoWidthKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoHeightKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoPixelAspectRatioKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoPixelAspectRatioHorizontalSpacingKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoPixelAspectRatioVerticalSpacingKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCleanApertureKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCleanApertureWidthKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCleanApertureHeightKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCleanApertureHorizontalOffsetKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCleanApertureVerticalOffsetKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoScalingModeKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoScalingModeFit, unicode)
        self.assertIsInstance(AVFoundation.AVVideoScalingModeResize, unicode)
        self.assertIsInstance(AVFoundation.AVVideoScalingModeResizeAspect, unicode)
        self.assertIsInstance(AVFoundation.AVVideoScalingModeResizeAspectFill, unicode)
        self.assertIsInstance(AVFoundation.AVVideoColorPropertiesKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoColorPrimariesKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoColorPrimaries_ITU_R_709_2, unicode)
        self.assertIsInstance(AVFoundation.AVVideoColorPrimaries_EBU_3213, unicode)
        self.assertIsInstance(AVFoundation.AVVideoColorPrimaries_SMPTE_C, unicode)
        self.assertIsInstance(AVFoundation.AVVideoTransferFunctionKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoTransferFunction_ITU_R_709_2, unicode)
        self.assertIsInstance(AVFoundation.AVVideoTransferFunction_SMPTE_240M_1995, unicode)
        self.assertIsInstance(AVFoundation.AVVideoYCbCrMatrixKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoYCbCrMatrix_ITU_R_709_2, unicode)
        self.assertIsInstance(AVFoundation.AVVideoYCbCrMatrix_ITU_R_601_4, unicode)
        self.assertIsInstance(AVFoundation.AVVideoYCbCrMatrix_SMPTE_240M_1995, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCompressionPropertiesKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoAverageBitRateKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoQualityKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoMaxKeyFrameIntervalKey, unicode)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Baseline30, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Baseline31, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Baseline41, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Main30, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Main31, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Main32, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264Main41, unicode)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264BaselineAutoLevel, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264MainAutoLevel, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264High40, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264High41, unicode)
        self.assertIsInstance(AVFoundation.AVVideoProfileLevelH264HighAutoLevel, unicode)
        self.assertIsInstance(AVFoundation.AVVideoMaxKeyFrameIntervalDurationKey, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVVideoAllowFrameReorderingKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoH264EntropyModeKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoH264EntropyModeCAVLC, unicode)
        self.assertIsInstance(AVFoundation.AVVideoH264EntropyModeCABAC, unicode)
        self.assertIsInstance(AVFoundation.AVVideoExpectedSourceFrameRateKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoAverageNonDroppableFrameRateKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoEncoderSpecificationKey, unicode)

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(AVFoundation.AVVideoColorPrimaries_P3_D65, unicode)
        self.assertIsInstance(AVFoundation.AVVideoAllowWideColorKey, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeHEVC, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeH264, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeJPEG, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeAppleProRes4444, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCodecTypeAppleProRes422, unicode)
        self.assertIsInstance(AVFoundation.AVVideoColorPrimaries_ITU_R_2020, unicode)
        self.assertIsInstance(AVFoundation.AVVideoTransferFunction_SMPTE_ST_2084_PQ, unicode)
        self.assertIsInstance(AVFoundation.AVVideoTransferFunction_ITU_R_2100_HLG, unicode)
        self.assertIsInstance(AVFoundation.AVVideoYCbCrMatrix_ITU_R_2020, unicode)
        self.assertIsInstance(AVFoundation.AVVideoCodecHEVC, unicode)
        self.assertIsInstance(AVFoundation.AVVideoDecompressionPropertiesKey, unicode)
        self.assertIsInstance(AVFoundation.AVVideoApertureModeCleanAperture, unicode)
        self.assertIsInstance(AVFoundation.AVVideoApertureModeProductionAperture, unicode)
        self.assertIsInstance(AVFoundation.AVVideoApertureModeEncodedPixels, unicode)

if __name__ == "__main__":
    main()
