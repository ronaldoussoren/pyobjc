import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTFrameProcessor_OpticalFlow(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            VideoToolbox.VTOpticalFlowConfigurationQualityPrioritization
        )
        self.assertEqual(
            VideoToolbox.VTOpticalFlowConfigurationQualityPrioritizationNormal, 1
        )
        self.assertEqual(
            VideoToolbox.VTOpticalFlowConfigurationQualityPrioritizationQuality, 2
        )

        self.assertIsEnumType(VideoToolbox.VTOpticalFlowConfigurationRevision)
        self.assertEqual(VideoToolbox.VTOpticalFlowConfigurationRevision1, 1)

        self.assertIsEnumType(VideoToolbox.VTOpticalFlowParametersSubmissionMode)
        self.assertEqual(VideoToolbox.VTOpticalFlowParametersSubmissionModeRandom, 1)
        self.assertEqual(
            VideoToolbox.VTOpticalFlowParametersSubmissionModeSequential, 2
        )

    @min_os_level("15.4")
    def test_methods(self):
        self.assertResultIsBOOL(
            VideoToolbox.VTOpticalFlowConfiguration.processorSupported
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(VideoToolbox.VTOpticalFlowConfiguration.isSupported)
