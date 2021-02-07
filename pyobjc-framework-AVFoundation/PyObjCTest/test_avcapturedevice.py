import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestAVCaptureDevice(TestCase):
    @expectedFailure
    def testMissingConstants(self):
        # Present in header files, but not actually exposed
        self.assertIsInstance(AVFoundation.AVCaptureMaxAvailableTorchLevel, float)

    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(AVFoundation.AVCaptureDeviceWasConnectedNotification, str)
        self.assertIsInstance(
            AVFoundation.AVCaptureDeviceWasDisconnectedNotification, str
        )

        self.assertEqual(AVFoundation.AVCaptureDevicePositionUnspecified, 0)
        self.assertEqual(AVFoundation.AVCaptureDevicePositionBack, 1)
        self.assertEqual(AVFoundation.AVCaptureDevicePositionFront, 2)

        self.assertEqual(AVFoundation.AVCaptureFlashModeOff, 0)
        self.assertEqual(AVFoundation.AVCaptureFlashModeOn, 1)
        self.assertEqual(AVFoundation.AVCaptureFlashModeAuto, 2)

        self.assertEqual(AVFoundation.AVCaptureTorchModeOff, 0)
        self.assertEqual(AVFoundation.AVCaptureTorchModeOn, 1)
        self.assertEqual(AVFoundation.AVCaptureTorchModeAuto, 2)

        self.assertEqual(AVFoundation.AVCaptureFocusModeLocked, 0)
        self.assertEqual(AVFoundation.AVCaptureFocusModeAutoFocus, 1)
        self.assertEqual(AVFoundation.AVCaptureFocusModeContinuousAutoFocus, 2)

        self.assertEqual(AVFoundation.AVCaptureAutoFocusRangeRestrictionNone, 0)
        self.assertEqual(AVFoundation.AVCaptureAutoFocusRangeRestrictionNear, 1)
        self.assertEqual(AVFoundation.AVCaptureAutoFocusRangeRestrictionFar, 2)

        self.assertEqual(AVFoundation.AVCaptureExposureModeLocked, 0)
        self.assertEqual(AVFoundation.AVCaptureExposureModeAutoExpose, 1)
        self.assertEqual(AVFoundation.AVCaptureExposureModeContinuousAutoExposure, 2)
        self.assertEqual(AVFoundation.AVCaptureExposureModeCustom, 3)

        self.assertEqual(AVFoundation.AVCaptureWhiteBalanceModeLocked, 0)
        self.assertEqual(AVFoundation.AVCaptureWhiteBalanceModeAutoWhiteBalance, 1)
        self.assertEqual(
            AVFoundation.AVCaptureWhiteBalanceModeContinuousAutoWhiteBalance, 2
        )

        self.assertEqual(AVFoundation.AVCaptureDeviceTransportControlsNotPlayingMode, 0)
        self.assertEqual(AVFoundation.AVCaptureDeviceTransportControlsPlayingMode, 1)

        self.assertEqual(AVFoundation.AVAuthorizationStatusNotDetermined, 0)
        self.assertEqual(AVFoundation.AVAuthorizationStatusRestricted, 1)
        self.assertEqual(AVFoundation.AVAuthorizationStatusDenied, 2)
        self.assertEqual(AVFoundation.AVAuthorizationStatusAuthorized, 3)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(AVFoundation.AVCaptureDeviceTypeExternalUnknown, str)
        self.assertIsInstance(AVFoundation.AVCaptureDeviceTypeBuiltInMicrophone, str)
        self.assertIsInstance(
            AVFoundation.AVCaptureDeviceTypeBuiltInWideAngleCamera, str
        )

        self.assertIsInstance(AVFoundation.AVCaptureMaxAvailableTorchLevel, float)

    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.hasMediaType_)

        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.lockForConfiguration_)
        self.assertArgIsOut(AVFoundation.AVCaptureDevice.lockForConfiguration_, 0)

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice.supportsAVCaptureSessionPreset_
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isConnected)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice.isInUseByAnotherApplication
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isSuspended)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.hasFlash)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isFlashModeSupported_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.hasTorch)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isTorchModeSupported_)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isFocusModeSupported_)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice.isFocusPointOfInterestSupported
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isAdjustingFocus)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isExposureModeSupported_)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice.isExposurePointOfInterestSupported
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isAdjustingExposure)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice.isWhiteBalanceModeSupported_
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isAdjustingWhiteBalance)

    @expectedFailure  # XXX
    @min_os_level("10.7")
    def testMethods_error_on_11(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.transportControlsSupported)

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptureDevice.requestAccessForMediaType_completionHandler_,
            1,
            b"vZ",
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isFlashAvailable)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isTorchAvailable)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isTorchActive)

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice.setTorchModeOnWithLevel_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVCaptureDevice.setTorchModeOnWithLevel_error_, 1
        )
