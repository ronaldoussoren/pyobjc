import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetExportSession(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVAssetExportSessionStatus)
        self.assertIsEnumType(AVFoundation.AVAssetTrackGroupOutputHandling)

        self.assertIsTypedEnum(
            AVFoundation.AVAssetExportSessionResumptionFailureReason, str
        )

    @min_os_level("10.7")
    def test_constants(self):
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

        self.assertEqual(AVFoundation.AVAssetTrackGroupOutputHandlingNone, 0)
        self.assertEqual(
            AVFoundation.AVAssetTrackGroupOutputHandlingPreserveAlternateTracks, 1 << 0
        )
        self.assertEqual(
            AVFoundation.AVAssetTrackGroupOutputHandlingDefaultPolicy,
            AVFoundation.AVAssetTrackGroupOutputHandlingNone,
        )

    @min_os_level("10.8")
    def test_constants10_8(self):
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetAppleM4V1080pHD, str
        )  # noqa: B950

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPreset3840x2160, str)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPresetLowQuality, str)
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetMediumQuality, str
        )  # noqa: B950
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetHighestQuality, str
        )  # noqa: B950

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetHEVCHighestQuality, str
        )  # noqa: B950
        self.assertIsInstance(AVFoundation.AVAssetExportPresetHEVC1920x1080, str)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetHEVC3840x2160, str)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetHEVC1920x1080WithAlpha, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetHEVC3840x2160WithAlpha, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetExportPresetAppleProRes4444LPCM, str
        )  # noqa: B950

    @min_os_level("12.1")
    def test_constants12_1(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPresetHEVC7680x4320, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPresetMVHEVC960x960, str)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetMVHEVC1440x1440, str)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(AVFoundation.AVAssetExportPresetHEVC4320x2160, str)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetMVHEVC4320x4320, str)
        self.assertIsInstance(AVFoundation.AVAssetExportPresetMVHEVC7680x7680, str)

    @min_os_level("27.0")
    def test_constants27_0(self):
        self.assertIsInstance(
            AVFoundation.AVAssetExportSessionResumptionFailureReasonIncompatiblePreset,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVAssetExportSessionResumptionFailureReasonUnsupportedForPresetOnPlatform,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVAssetExportSessionResumptionFailureReasonTemporaryDirectoryDoesNotExist,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVAssetExportSessionResumptionFailureReasonIncompatibleSessionSettings,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVAssetExportSessionResumptionFailureReasonIncompatibleTemporaryDirectoryContents,
            str,
        )

    @min_os_level("10.7")
    def test_methods(self):
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
    def test_methods10_10(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetExportSession.canPerformMultiplePassesOverSourceMediaData  # noqa: B950
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetExportSession.setCanPerformMultiplePassesOverSourceMediaData_,  # noqa: B950
            0,
        )

    @min_os_level("10.15")
    def test_methods10_15(self):
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

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetExportSession.allowsParallelizedExport
        )
        self.assertArgIsBOOL(
            AVFoundation.AVAssetExportSession.setAllowsParallelizedExport_, 0
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVAssetExportSessionResumptionState.isResumptionConfigured
        )
        self.assertResultIsBOOL(
            AVFoundation.AVAssetExportSessionResumptionState.isResumingFromPreviousState
        )
        self.assertArgIsBlock(
            AVFoundation.AVAssetExportSession.configureForResumableExportWithCompletionHandler_,
            0,
            b"v@",
        )
