import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTFrameProcessor_SuperResolutionScaler(TestCase):
    def test_constants(self):
        self.assertIsEnumType(
            VideoToolbox.VTSuperResolutionScalerConfigurationQualityPrioritization
        )
        self.assertEqual(
            VideoToolbox.VTSuperResolutionScalerConfigurationQualityPrioritizationNormal,
            1,
        )

        self.assertIsEnumType(VideoToolbox.VTSuperResolutionScalerConfigurationRevision)
        self.assertEqual(VideoToolbox.VTSuperResolutionScalerConfigurationRevision1, 1)

        self.assertIsEnumType(
            VideoToolbox.VTSuperResolutionScalerConfigurationInputType
        )
        self.assertEqual(
            VideoToolbox.VTSuperResolutionScalerConfigurationInputTypeVideo, 1
        )
        self.assertEqual(
            VideoToolbox.VTSuperResolutionScalerConfigurationInputTypeImage, 2
        )

        self.assertIsEnumType(
            VideoToolbox.VTSuperResolutionScalerConfigurationModelStatus
        )
        self.assertEqual(
            VideoToolbox.VTSuperResolutionScalerConfigurationModelStatusDownloadRequired,
            0,
        )
        self.assertEqual(
            VideoToolbox.VTSuperResolutionScalerConfigurationModelStatusDownloading, 1
        )
        self.assertEqual(
            VideoToolbox.VTSuperResolutionScalerConfigurationModelStatusReady, 2
        )

        self.assertIsEnumType(
            VideoToolbox.VTSuperResolutionScalerParametersSubmissionMode
        )
        self.assertEqual(
            VideoToolbox.VTSuperResolutionScalerParametersSubmissionModeRandom, 1
        )
        self.assertEqual(
            VideoToolbox.VTSuperResolutionScalerParametersSubmissionModeSequential, 2
        )

    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            VideoToolbox.VTSuperResolutionScalerConfiguration.usesPrecomputedFlow
        )
        self.assertResultIsBOOL(
            VideoToolbox.VTSuperResolutionScalerConfiguration.isSupported
        )

        self.assertArgIsBlock(
            VideoToolbox.VTSuperResolutionScalerConfiguration.downloadConfigurationModelWithCompletionHandler_,
            0,
            b"v@",
        )
