import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVError(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVFoundationErrorDomain, str)

        self.assertIsInstance(AVFoundation.AVErrorDeviceKey, str)
        self.assertIsInstance(AVFoundation.AVErrorTimeKey, str)
        self.assertIsInstance(AVFoundation.AVErrorFileSizeKey, str)
        self.assertIsInstance(AVFoundation.AVErrorPIDKey, str)
        self.assertIsInstance(AVFoundation.AVErrorRecordingSuccessfullyFinishedKey, str)
        self.assertIsInstance(AVFoundation.AVErrorMediaTypeKey, str)
        self.assertIsInstance(AVFoundation.AVErrorMediaSubTypeKey, str)

        self.assertIsInstance(AVFoundation.AVErrorDiscontinuityFlagsKey, str)

        self.assertEqual(AVFoundation.AVErrorUnknown, -11800)
        self.assertEqual(AVFoundation.AVErrorOutOfMemory, -11801)
        self.assertEqual(AVFoundation.AVErrorSessionNotRunning, -11803)
        self.assertEqual(AVFoundation.AVErrorDeviceAlreadyUsedByAnotherSession, -11804)
        self.assertEqual(AVFoundation.AVErrorNoDataCaptured, -11805)
        self.assertEqual(AVFoundation.AVErrorSessionConfigurationChanged, -11806)
        self.assertEqual(AVFoundation.AVErrorDiskFull, -11807)
        self.assertEqual(AVFoundation.AVErrorDeviceWasDisconnected, -11808)
        self.assertEqual(AVFoundation.AVErrorMediaChanged, -11809)
        self.assertEqual(AVFoundation.AVErrorMaximumDurationReached, -11810)
        self.assertEqual(AVFoundation.AVErrorMaximumFileSizeReached, -11811)
        self.assertEqual(AVFoundation.AVErrorMediaDiscontinuity, -11812)
        self.assertEqual(
            AVFoundation.AVErrorMaximumNumberOfSamplesForFileFormatReached, -11813
        )
        self.assertEqual(AVFoundation.AVErrorDeviceNotConnected, -11814)
        self.assertEqual(AVFoundation.AVErrorDeviceInUseByAnotherApplication, -11815)
        self.assertEqual(
            AVFoundation.AVErrorDeviceLockedForConfigurationByAnotherProcess, -11817
        )
        self.assertEqual(AVFoundation.AVErrorExportFailed, -11820)
        self.assertEqual(AVFoundation.AVErrorDecodeFailed, -11821)
        self.assertEqual(AVFoundation.AVErrorInvalidSourceMedia, -11822)
        self.assertEqual(AVFoundation.AVErrorFileAlreadyExists, -11823)
        self.assertEqual(
            AVFoundation.AVErrorCompositionTrackSegmentsNotContiguous, -11824
        )
        self.assertEqual(
            AVFoundation.AVErrorInvalidCompositionTrackSegmentDuration, -11825
        )
        self.assertEqual(
            AVFoundation.AVErrorInvalidCompositionTrackSegmentSourceStartTime, -11826
        )
        self.assertEqual(
            AVFoundation.AVErrorInvalidCompositionTrackSegmentSourceDuration, -11827
        )
        self.assertEqual(AVFoundation.AVErrorFileFormatNotRecognized, -11828)
        self.assertEqual(AVFoundation.AVErrorFileFailedToParse, -11829)
        self.assertEqual(
            AVFoundation.AVErrorMaximumStillImageCaptureRequestsExceeded, -11830
        )
        self.assertEqual(AVFoundation.AVErrorContentIsProtected, -11831)
        self.assertEqual(AVFoundation.AVErrorNoImageAtTime, -11832)
        self.assertEqual(AVFoundation.AVErrorDecoderNotFound, -11833)
        self.assertEqual(AVFoundation.AVErrorEncoderNotFound, -11834)
        self.assertEqual(AVFoundation.AVErrorContentIsNotAuthorized, -11835)
        self.assertEqual(AVFoundation.AVErrorApplicationIsNotAuthorized, -11836)
        self.assertEqual(AVFoundation.AVErrorOperationNotSupportedForAsset, -11838)
        self.assertEqual(AVFoundation.AVErrorDecoderTemporarilyUnavailable, -11839)
        self.assertEqual(AVFoundation.AVErrorEncoderTemporarilyUnavailable, -11840)
        self.assertEqual(AVFoundation.AVErrorInvalidVideoComposition, -11841)
        self.assertEqual(
            AVFoundation.AVErrorReferenceForbiddenByReferencePolicy, -11842
        )
        self.assertEqual(AVFoundation.AVErrorInvalidOutputURLPathExtension, -11843)
        self.assertEqual(AVFoundation.AVErrorScreenCaptureFailed, -11844)
        self.assertEqual(AVFoundation.AVErrorDisplayWasDisabled, -11845)
        self.assertEqual(AVFoundation.AVErrorTorchLevelUnavailable, -11846)
        self.assertEqual(AVFoundation.AVErrorIncompatibleAsset, -11848)
        self.assertEqual(AVFoundation.AVErrorFailedToLoadMediaData, -11849)
        self.assertEqual(AVFoundation.AVErrorServerIncorrectlyConfigured, -11850)
        self.assertEqual(
            AVFoundation.AVErrorApplicationIsNotAuthorizedToUseDevice, -11852
        )
        self.assertEqual(AVFoundation.AVErrorFailedToParse, -11853)
        self.assertEqual(
            AVFoundation.AVErrorFileTypeDoesNotSupportSampleReferences, -11854
        )
        self.assertEqual(AVFoundation.AVErrorUndecodableMediaData, -11855)
        self.assertEqual(AVFoundation.AVErrorAirPlayControllerRequiresInternet, -11856)
        self.assertEqual(AVFoundation.AVErrorAirPlayReceiverRequiresInternet, -11857)
        self.assertEqual(AVFoundation.AVErrorVideoCompositorFailed, -11858)
        self.assertEqual(AVFoundation.AVErrorCreateContentKeyRequestFailed, -11860)
        self.assertEqual(AVFoundation.AVErrorUnsupportedOutputSettings, -11861)
        self.assertEqual(AVFoundation.AVErrorOperationNotAllowed, -11862)
        self.assertEqual(AVFoundation.AVErrorContentIsUnavailable, -11863)
        self.assertEqual(AVFoundation.AVErrorFormatUnsupported, -11864)
        self.assertEqual(AVFoundation.AVErrorMalformedDepth, -11865)
        self.assertEqual(AVFoundation.AVErrorContentNotUpdated, -11866)
        self.assertEqual(AVFoundation.AVErrorNoLongerPlayable, -11867)
        self.assertEqual(
            AVFoundation.AVErrorNoCompatibleAlternatesForExternalDisplay, -11868
        )
        self.assertEqual(AVFoundation.AVErrorNoSourceTrack, -11869)
        self.assertEqual(
            AVFoundation.AVErrorExternalPlaybackNotSupportedForAsset, -11870
        )
        self.assertEqual(AVFoundation.AVErrorOperationNotSupportedForPreset, -11871)
        self.assertEqual(AVFoundation.AVErrorIncorrectlyConfigured, -11875)
        self.assertEqual(AVFoundation.AVErrorSegmentStartedWithNonSyncSample, -11876)
        self.assertEqual(AVFoundation.AVErrorRosettaNotInstalled, -11877)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AVFoundation.AVErrorPresentationTimeStampKey, str)
        self.assertIsInstance(AVFoundation.AVErrorPersistentTrackIDKey, str)
        self.assertIsInstance(AVFoundation.AVErrorFileTypeKey, str)
