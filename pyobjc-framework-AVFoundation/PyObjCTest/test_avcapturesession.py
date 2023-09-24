import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestAVCaptureSession(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVCaptureSessionInterruptionReason)
        self.assertIsEnumType(AVFoundation.AVCaptureVideoOrientation)
        self.assertIsEnumType(AVFoundation.AVVideoFieldMode)

    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(
            AVFoundation.AVCaptureSessionRuntimeErrorNotification, str
        )
        self.assertIsInstance(AVFoundation.AVCaptureSessionErrorKey, str)
        self.assertIsInstance(
            AVFoundation.AVCaptureSessionDidStartRunningNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVCaptureSessionDidStopRunningNotification, str
        )

        self.assertEqual(AVFoundation.AVCaptureVideoOrientationPortrait, 1)
        self.assertEqual(AVFoundation.AVCaptureVideoOrientationPortraitUpsideDown, 2)
        self.assertEqual(AVFoundation.AVCaptureVideoOrientationLandscapeRight, 3)
        self.assertEqual(AVFoundation.AVCaptureVideoOrientationLandscapeLeft, 4)

        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetPhoto, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetHigh, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetMedium, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetLow, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset320x240, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset352x288, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset640x480, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset960x540, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset1280x720, str)

        self.assertEqual(AVFoundation.AVVideoFieldModeBoth, 0)
        self.assertEqual(AVFoundation.AVVideoFieldModeTopOnly, 1)
        self.assertEqual(AVFoundation.AVVideoFieldModeBottomOnly, 2)
        self.assertEqual(AVFoundation.AVVideoFieldModeDeinterlace, 3)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetiFrame960x540, str)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetiFrame1280x720, str)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(
            AVFoundation.AVCaptureSessionWasInterruptedNotification, str
        )
        self.assertIsInstance(
            AVFoundation.AVCaptureSessionInterruptionEndedNotification, str
        )

    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession.canSetSessionPreset_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession.canAddInput_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession.canAddOutput_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession.canAddConnection_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession.isRunning)

        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureConnection.setEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.isActive)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection.isVideoMirroringSupported
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.isVideoMirrored)

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection.automaticallyAdjustsVideoMirroring
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureConnection.setAutomaticallyAdjustsVideoMirroring_, 0
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection.isVideoOrientationSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection.isVideoFieldModeSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection.isVideoMinFrameDurationSupported
        )

        self.assertResultIsBOOL(AVFoundation.AVCaptureAudioChannel.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureAudioChannel.setEnabled_, 0)

    @min_os_level("12.0")
    def test_methodsTundra(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureSession_Tundra.canSetSessionPreset_
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession_Tundra.canAddInput_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession_Tundra.canAddOutput_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession_Tundra.canAddConnection_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession_Tundra.isRunning)
        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection_Tundra.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureConnection_Tundra.setEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection_Tundra.isActive)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection_Tundra.isVideoMirroringSupported
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection_Tundra.isVideoMirrored)

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection_Tundra.automaticallyAdjustsVideoMirroring
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureConnection_Tundra.setAutomaticallyAdjustsVideoMirroring_,
            0,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection_Tundra.isVideoOrientationSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection_Tundra.isVideoFieldModeSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection_Tundra.isVideoMinFrameDurationSupported
        )

        self.assertResultIsBOOL(AVFoundation.AVCaptureAudioChannel_Tundra.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureAudioChannel_Tundra.setEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVCaptureAudioChannel_Tundra.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureAudioChannel_Tundra.setEnabled_, 0)

    @expectedFailure
    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection.isHighResolutionStillImageOutputEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureConnection.setHighResolutionStillImageOutputEnabled_,
            0,
        )

    @min_os_level("14.0")
    def testMethods14_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection.automaticallyAdjustsVideoMirroring
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureConnection.setAutomaticallyAdjustsVideoMirroring_,
            0,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureConnection.isVideoRotationAngleSupported_
        )
