from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVCaptureSession (TestCase):
    @min_os_level('10.7')
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVCaptureSessionRuntimeErrorNotification, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionErrorKey, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionDidStartRunningNotification, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionDidStopRunningNotification, unicode)

        self.assertEqual(AVFoundation.AVCaptureVideoOrientationPortrait, 1)
        self.assertEqual(AVFoundation.AVCaptureVideoOrientationPortraitUpsideDown, 2)
        self.assertEqual(AVFoundation.AVCaptureVideoOrientationLandscapeRight, 3)
        self.assertEqual(AVFoundation.AVCaptureVideoOrientationLandscapeLeft, 4)

        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetPhoto, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetHigh, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetMedium, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetLow, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset320x240, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset352x288, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset640x480, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset960x540, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPreset1280x720, unicode)

        self.assertEqual(AVFoundation.AVVideoFieldModeBoth, 0)
        self.assertEqual(AVFoundation.AVVideoFieldModeTopOnly, 1)
        self.assertEqual(AVFoundation.AVVideoFieldModeBottomOnly, 2)
        self.assertEqual(AVFoundation.AVVideoFieldModeDeinterlace, 3)


    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetiFrame960x540, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionPresetiFrame1280x720, unicode)

    @min_os_level('10.14')
    def testConstants10_14(self):
        self.assertIsInstance(AVFoundation.AVCaptureSessionWasInterruptedNotification, unicode)
        self.assertIsInstance(AVFoundation.AVCaptureSessionInterruptionEndedNotification, unicode)

    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession.canSetSessionPreset_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession.canAddInput_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession.canAddOutput_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession.canAddConnection_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureSession.isRunning)

        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureConnection.setEnabled_, 0)

        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.isActive)
        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.isVideoMirroringSupported)
        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.isVideoMirrored)

        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.automaticallyAdjustsVideoMirroring)
        self.assertArgIsBOOL(AVFoundation.AVCaptureConnection.setAutomaticallyAdjustsVideoMirroring_, 0)

        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.isVideoOrientationSupported)
        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.isVideoFieldModeSupported)
        self.assertResultIsBOOL(AVFoundation.AVCaptureConnection.isVideoMinFrameDurationSupported)

        self.assertResultIsBOOL(AVFoundation.AVCaptureAudioChannel.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureAudioChannel.setEnabled_, 0)


if __name__ == "__main__":
    main()
