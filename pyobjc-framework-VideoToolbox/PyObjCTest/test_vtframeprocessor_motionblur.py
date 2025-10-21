import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTFrameProcessor_MotionBlur(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            VideoToolbox.VTMotionBlurConfigurationQualityPrioritization
        )
        self.assertEqual(
            VideoToolbox.VTMotionBlurConfigurationQualityPrioritizationNormal, 1
        )
        self.assertEqual(
            VideoToolbox.VTMotionBlurConfigurationQualityPrioritizationQuality, 2
        )

        self.assertIsEnumType(VideoToolbox.VTMotionBlurConfigurationRevision)
        self.assertEqual(VideoToolbox.VTMotionBlurConfigurationRevision1, 1)

        self.assertIsEnumType(VideoToolbox.VTMotionBlurParametersSubmissionMode)
        self.assertEqual(VideoToolbox.VTMotionBlurParametersSubmissionModeRandom, 1)
        self.assertEqual(VideoToolbox.VTMotionBlurParametersSubmissionModeSequential, 2)

    @min_os_level("15.4")
    def test_methods(self):
        self.assertResultIsBOOL(
            VideoToolbox.VTMotionBlurConfiguration.usePrecomputedFlow
        )
        self.assertResultIsBOOL(
            VideoToolbox.VTMotionBlurConfiguration.processorSupported
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(VideoToolbox.VTMotionBlurConfiguration.isSupported)
