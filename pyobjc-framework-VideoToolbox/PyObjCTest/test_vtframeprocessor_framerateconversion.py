import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTFrameProcessor_FrameRateConversion(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            VideoToolbox.VTFrameRateConversionConfigurationQualityPrioritization
        )
        self.assertEqual(
            VideoToolbox.VTFrameRateConversionConfigurationQualityPrioritizationNormal,
            1,
        )
        self.assertEqual(
            VideoToolbox.VTFrameRateConversionConfigurationQualityPrioritizationQuality,
            2,
        )

        self.assertIsEnumType(VideoToolbox.VTFrameRateConversionConfigurationRevision)
        self.assertEqual(VideoToolbox.VTFrameRateConversionConfigurationRevision1, 1)

        self.assertIsEnumType(
            VideoToolbox.VTFrameRateConversionParametersSubmissionMode
        )
        self.assertEqual(
            VideoToolbox.VTFrameRateConversionParametersSubmissionModeRandom, 1
        )
        self.assertEqual(
            VideoToolbox.VTFrameRateConversionParametersSubmissionModeSequential, 2
        )

    @min_os_level("15.4")
    def test_methods(self):
        self.assertResultIsBOOL(
            VideoToolbox.VTFrameRateConversionConfiguration.usePrecomputedFlow
        )
        self.assertResultIsBOOL(
            VideoToolbox.VTFrameRateConversionConfiguration.processorSupported
        )
