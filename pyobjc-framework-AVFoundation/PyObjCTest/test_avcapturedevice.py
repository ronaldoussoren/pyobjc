import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestAVCaptureDevice(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVAuthorizationStatus)
        self.assertIsEnumType(AVFoundation.AVCaptureAutoFocusRangeRestriction)
        self.assertIsEnumType(AVFoundation.AVCaptureAutoFocusSystem)
        self.assertIsEnumType(AVFoundation.AVCaptureCenterStageControlMode)
        self.assertIsEnumType(AVFoundation.AVCaptureColorSpace)
        self.assertIsEnumType(AVFoundation.AVCaptureDevicePosition)
        self.assertIsEnumType(AVFoundation.AVCaptureDeviceTransportControlsPlaybackMode)
        self.assertIsEnumType(AVFoundation.AVCaptureExposureMode)
        self.assertIsEnumType(AVFoundation.AVCaptureFlashMode)
        self.assertIsEnumType(AVFoundation.AVCaptureFocusMode)
        self.assertIsEnumType(AVFoundation.AVCaptureMicrophoneMode)
        self.assertIsEnumType(
            AVFoundation.AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions
        )
        self.assertIsEnumType(
            AVFoundation.AVCapturePrimaryConstituentDeviceSwitchingBehavior
        )
        self.assertIsEnumType(AVFoundation.AVCaptureSystemUserInterface)
        self.assertIsEnumType(AVFoundation.AVCaptureTorchMode)
        self.assertIsEnumType(AVFoundation.AVCaptureVideoStabilizationMode)
        self.assertIsEnumType(AVFoundation.AVCaptureWhiteBalanceMode)

    @min_os_level("10.7")
    def test_constants(self):
        self.assertEqual(AVFoundation.AVCaptureColorSpace_sRGB, 0)
        self.assertEqual(AVFoundation.AVCaptureColorSpace_P3_D65, 1)

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

        self.assertEqual(AVFoundation.AVCaptureMicrophoneModeStandard, 0)
        self.assertEqual(AVFoundation.AVCaptureMicrophoneModeWideSpectrum, 1)
        self.assertEqual(AVFoundation.AVCaptureMicrophoneModeVoiceIsolation, 2)

        self.assertEqual(AVFoundation.AVCaptureSystemUserInterfaceVideoEffects, 1)
        self.assertEqual(AVFoundation.AVCaptureSystemUserInterfaceMicrophoneModes, 2)

        self.assertEqual(AVFoundation.AVCaptureCenterStageControlModeUser, 0)
        self.assertEqual(AVFoundation.AVCaptureCenterStageControlModeApp, 1)
        self.assertEqual(AVFoundation.AVCaptureCenterStageControlModeCooperative, 2)

        self.assertEqual(AVFoundation.AVCaptureAutoFocusSystemNone, 0)
        self.assertEqual(AVFoundation.AVCaptureAutoFocusSystemContrastDetection, 1)
        self.assertEqual(AVFoundation.AVCaptureAutoFocusSystemPhaseDetection, 2)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(AVFoundation.AVCaptureDeviceTypeExternalUnknown, str)
        self.assertIsInstance(AVFoundation.AVCaptureDeviceTypeBuiltInMicrophone, str)
        self.assertIsInstance(
            AVFoundation.AVCaptureDeviceTypeBuiltInWideAngleCamera, str
        )

        self.assertIsInstance(AVFoundation.AVCaptureMaxAvailableTorchLevel, float)

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertEqual(
            AVFoundation.AVCapturePrimaryConstituentDeviceSwitchingBehaviorUnsupported,
            0,
        )
        self.assertEqual(
            AVFoundation.AVCapturePrimaryConstituentDeviceSwitchingBehaviorAuto, 1
        )
        self.assertEqual(
            AVFoundation.AVCapturePrimaryConstituentDeviceSwitchingBehaviorRestricted, 2
        )
        self.assertEqual(
            AVFoundation.AVCapturePrimaryConstituentDeviceSwitchingBehaviorLocked, 3
        )

        self.assertEqual(
            AVFoundation.AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionNone,
            0,
        )
        self.assertEqual(
            AVFoundation.AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionVideoZoomChanged,
            1 << 0,
        )
        self.assertEqual(
            AVFoundation.AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionFocusModeChanged,
            1 << 1,
        )
        self.assertEqual(
            AVFoundation.AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionExposureModeChanged,
            1 << 2,
        )

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(AVFoundation.AVCaptureDeviceTypeDeskViewCamera, str)

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

    @min_os_level("12.0")
    def testMethods_Clones(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.hasMediaType_)

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.lockForConfiguration_
        )
        self.assertArgIsOut(
            AVFoundation.AVCaptureDevice_Tundra.lockForConfiguration_, 0
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.supportsAVCaptureSessionPreset_
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.isConnected)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isInUseByAnotherApplication
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.isSuspended)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.hasFlash)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isFlashModeSupported_
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.hasTorch)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isTorchModeSupported_
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isFocusModeSupported_
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isFocusPointOfInterestSupported
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.isAdjustingFocus)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isExposureModeSupported_
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isExposurePointOfInterestSupported
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.isAdjustingExposure)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isWhiteBalanceModeSupported_
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isAdjustingWhiteBalance
        )

    @expectedFailure  # XXX
    @min_os_level("10.7")
    def testMethods_error_on_11(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.transportControlsSupported)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.transportControlsSupported
        )

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptureDevice.requestAccessForMediaType_completionHandler_,
            1,
            b"vZ",
        )

    @min_os_level("12.0")
    def testMethodsTundra10_14(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptureDevice_Tundra.requestAccessForMediaType_completionHandler_,
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

    @min_os_level("12.0")
    def testMethodsTundra10_15(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.isFlashAvailable)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.isTorchAvailable)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.isTorchActive)

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.setTorchModeOnWithLevel_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVCaptureDevice_Tundra.setTorchModeOnWithLevel_error_, 1
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeviceFormat.isHighPhotoQualitySupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeviceFormat_Tundra.isHighPhotoQualitySupported
        )

        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isPortraitEffectEnabled)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isPortraitEffectEnabled
        )

        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isPortraitEffectActive)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isPortraitEffectActive
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeviceFormat.isPortraitEffectSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeviceFormat_Tundra.isPortraitEffectSupported
        )

    @min_os_level("12.3")
    def test_methods12_3(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isCenterStageEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureDevice.setCenterStageEnabled_, 0)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isCenterStageEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.setCenterStageEnabled_, 0
        )

        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isCenterStageActive)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.isCenterStageActive)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeviceFormat.isCenterStageSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeviceFormat_Tundra.isCenterStageSupported
        )

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isContinuityCamera)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.isContinuityCamera)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isStudioLightEnabled)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDevice_Tundra.isStudioLightEnabled
        )
        # self.assertArgIsBOOL(AVFoundation.AVCaptureDevice.setStudioLightEnabled_, 0)
        # self.assertArgIsBOOL(
        #    AVFoundation.AVCaptureDevice_Tundra.setStudioLightEnabled_, 0
        # )
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.isStudioLightActive)
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice_Tundra.isStudioLightActive)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeviceFormat.isStudioLightSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeviceFormat_Tundra.isStudioLightSupported
        )

    @min_os_level("14.0")
    def testMethods14_0(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureDevice.reactionEffectsEnabled)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeviceFormat.reactionEffectsSupported
        )

    @min_os_level("14.2")
    def testMethods14_2(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeviceFormat.zoomFactorsOutsideOfVideoZoomRangesForDepthDeliverySupported
        )
