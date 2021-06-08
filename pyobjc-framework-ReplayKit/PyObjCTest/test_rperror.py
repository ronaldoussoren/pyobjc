from PyObjCTools.TestSupport import TestCase

import ReplayKit


class TestRPError(TestCase):
    def test_constants(self):

        self.assertEqual(ReplayKit.RPRecordingErrorUnknown, -5800)
        self.assertEqual(ReplayKit.RPRecordingErrorUserDeclined, -5801)
        self.assertEqual(ReplayKit.RPRecordingErrorDisabled, -5802)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedToStart, -5803)
        self.assertEqual(ReplayKit.RPRecordingErrorFailed, -5804)
        self.assertEqual(ReplayKit.RPRecordingErrorInsufficientStorage, -5805)
        self.assertEqual(ReplayKit.RPRecordingErrorInterrupted, -5806)
        self.assertEqual(ReplayKit.RPRecordingErrorContentResize, -5807)
        self.assertEqual(ReplayKit.RPRecordingErrorBroadcastInvalidSession, -5808)
        self.assertEqual(ReplayKit.RPRecordingErrorSystemDormancy, -5809)
        self.assertEqual(ReplayKit.RPRecordingErrorEntitlements, -5810)
        self.assertEqual(ReplayKit.RPRecordingErrorActivePhoneCall, -5811)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedToSave, -5812)
        self.assertEqual(ReplayKit.RPRecordingErrorCarPlay, -5813)
        self.assertEqual(
            ReplayKit.RPRecordingErrorFailedApplicationConnectionInvalid, -5814
        )
        self.assertEqual(
            ReplayKit.RPRecordingErrorFailedApplicationConnectionInterrupted, -5815
        )
        self.assertEqual(
            ReplayKit.RPRecordingErrorFailedNoMatchingApplicationContext, -5816
        )
        self.assertEqual(ReplayKit.RPRecordingErrorFailedMediaServicesFailure, -5817)
        self.assertEqual(ReplayKit.RPRecordingErrorVideoMixingFailure, -5818)
        self.assertEqual(ReplayKit.RPRecordingErrorBroadcastSetupFailed, -5819)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedToObtainURL, -5820)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedIncorrectTimeStamps, -5821)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedToProcessFirstSample, -5822)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedAssetWriterFailedToSave, -5823)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedNoAssetWriter, -5824)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedAssetWriterInWrongState, -5825)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedAssetWriterExportFailed, -5826)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedToRemoveFile, -5827)
        self.assertEqual(
            ReplayKit.RPRecordingErrorFailedAssetWriterExportCanceled, -5828
        )
        self.assertEqual(ReplayKit.RPRecordingErrorAttemptToStopNonRecording, -5829)
        self.assertEqual(
            ReplayKit.RPRecordingErrorAttemptToStartInRecordingState, -5830
        )
        self.assertEqual(ReplayKit.RPRecordingErrorPhotoFailure, -5831)
        self.assertEqual(ReplayKit.RPRecordingErrorRecordingInvalidSession, -5832)
        self.assertEqual(ReplayKit.RPRecordingErrorFailedToStartCaptureStack, -5833)
        self.assertEqual(ReplayKit.RPRecordingErrorInvalidParameter, -5834)
        self.assertEqual(ReplayKit.RPRecordingErrorFilePermissions, -5835)
        self.assertEqual(ReplayKit.RPRecordingErrorExportClipToURLInProgress, -5836)
        self.assertEqual(ReplayKit.RPRecordingErrorCodeSuccessful, 0)
