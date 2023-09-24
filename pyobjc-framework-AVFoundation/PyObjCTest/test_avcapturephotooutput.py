import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestAVCapturePhotoOutputHelper(AVFoundation.NSObject):
    def readinessCoordinator_captureReadinessDidChange_(self, a, b):
        pass


class TestAVCapturePhotoOutput(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AVFoundation.AVCapturePhotoOutputCaptureReadiness)
        self.assertEqual(
            AVFoundation.AVCapturePhotoOutputCaptureReadinessSessionNotRunning, 0
        )
        self.assertEqual(AVFoundation.AVCapturePhotoOutputCaptureReadinessReady, 1)
        self.assertEqual(
            AVFoundation.AVCapturePhotoOutputCaptureReadinessNotReadyMomentarily, 2
        )
        self.assertEqual(
            AVFoundation.AVCapturePhotoOutputCaptureReadinessNotReadyWaitingForCapture,
            3,
        )
        self.assertEqual(
            AVFoundation.AVCapturePhotoOutputCaptureReadinessNotReadyWaitingForProcessing,
            4,
        )

    @min_sdk_level("10.15")
    def test_protocols10_15(self):
        self.assertProtocolExists("AVCapturePhotoCaptureDelegate")

    @min_sdk_level("14.0")
    def test_protocols14_0(self):
        self.assertProtocolExists("AVCapturePhotoOutputReadinessCoordinatorDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestAVCapturePhotoOutputHelper.readinessCoordinator_captureReadinessDidChange_,
            1,
            b"q",
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCapturePhotoSettings.isHighResolutionPhotoEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCapturePhotoSettings.setHighResolutionPhotoEnabled_, 0
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCapturePhotoSettings_Tundra.isHighResolutionPhotoEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCapturePhotoSettings_Tundra.setHighResolutionPhotoEnabled_, 0
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCapturePhotoOutput.preservesLivePhotoCaptureSuspendedOnSessionStop
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCapturePhotoOutput.setPreservesLivePhotoCaptureSuspendedOnSessionStop_,
            0,
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCapturePhotoOutput.preservesLivePhotoCaptureSuspendedOnSessionStop
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCapturePhotoOutput.setPreservesLivePhotoCaptureSuspendedOnSessionStop_,
            0,
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCapturePhotoOutput.isFastCapturePrioritizationSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCapturePhotoOutput.isFastCapturePrioritizationEnabled
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCapturePhotoOutput.isZeroShutterLagEnabled
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCapturePhotoOutput.isResponsiveCaptureSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCapturePhotoOutput.isResponsiveCaptureEnabled
        )
