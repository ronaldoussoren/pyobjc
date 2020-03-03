import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetExportSession(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPreset640x480, str)
        self.assertIsInstance(AVFoundation.AVAssetExportPreset960x540, str)
        self.assertIsInstance(AVFoundation.AVAssetExportPreset1280x720, str)
        self.assertIsInstance(AVFoundation.AVAssetExportPreset1920x1080, str)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4A, str)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetPassthrough, str)
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetAppleM4VCellular, str
        )  # noqa: B950
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4ViPod, str)
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetAppleM4V480pSD, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetAppleM4VAppleTV, str
        )  # noqa: B950
        self.assertIsInstance(AVFoundation.AVAssetExportPresetAppleM4VWiFi, str)
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetAppleM4V720pHD, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetAppleProRes422LPCM, str
        )  # noqa: B950

        self.assertEqual(AVFoundation.AVAssetExportSessionStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusWaiting, 1)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusExporting, 2)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusCompleted, 3)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusFailed, 4)
        self.assertEqual(AVFoundation.AVAssetExportSessionStatusCancelled, 5)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetAppleM4V1080pHD, str
        )  # noqa: B950

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPreset3840x2160, str)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPresetLowQuality, str)
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetMediumQuality, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetHighestQuality, str
        )  # noqa: B950

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetHEVCHighestQuality, str
        )  # noqa: B950
        self.assertIsInstance(AVFoundation.AVAssetExportPresetHEVC1920x1080, str)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetHEVC3840x2160, str)

    @min_os_level("10.15")
    def testConstants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetHEVC1920x1080WithAlpha, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetHEVC3840x2160WithAlpha, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetAppleProRes4444LPCM, str
        )  # noqa: B950

    @min_os_level("10.7")
    def testMethods(self):
        self.assertArgIsBlock(
            AVFoundation.AVAssetExportSession.determineCompatibilityOfExportPreset_withAsset_outputFileType_completionHandler_,  # noqa: B950
            3,
            b"vZ",
        )
        self.assertResultIsBOOL(
            AVFoundation.AVAssetExportSession.shouldOptimizeForNetworkUse
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetExportSession.setShouldOptimizeForNetworkUse_, 0
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetExportSession.determineCompatibleFileTypesWithCompletionHandler_,  # noqa: B950
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetExportSession.exportAsynchronouslyWithCompletionHandler_,  # noqa: B950
            0,
            b"v",
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetExportSession.canPerformMultiplePassesOverSourceMediaData  # noqa: B950
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetExportSession.setCanPerformMultiplePassesOverSourceMediaData_,  # noqa: B950
            0,
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            AVFoundation.AVAssetExportSession.estimateMaximumDurationWithCompletionHandler_,  # noqa: B950
            0,
            b"v" + AVFoundation.CMTime.__typestr__ + b"@",
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetExportSession.estimateOutputFileLengthWithCompletionHandler_,  # noqa: B950
            0,
            b"vQ@",
        )
