import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureInput(TestCase):
    @min_os_level("10.7")
    def testConstants(self):
        self.assertIsInstance(
            AVFoundation.AVCaptureInputPortFormatDescriptionDidChangeNotification, str
        )

    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureInputPort.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureInputPort.setEnabled_, 0)

        self.assertArgIsOut(
            AVFoundation.AVCaptureDeviceInput.deviceInputWithDevice_error_, 1
        )
        self.assertArgIsOut(AVFoundation.AVCaptureDeviceInput.initWithDevice_error_, 1)

        self.assertResultIsBOOL(AVFoundation.AVCaptureScreenInput.capturesMouseClicks)
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureScreenInput.setCapturesMouseClicks_, 0
        )

    @min_os_level("12.0")
    def test_methodsTundra(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureScreenInput_Tundra.capturesMouseClicks
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureScreenInput_Tundra.setCapturesMouseClicks_, 0
        )
        self.assertResultIsBOOL(AVFoundation.AVCaptureInputPort_Tundra.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVCaptureInputPort_Tundra.setEnabled_, 0)

        self.assertArgIsOut(
            AVFoundation.AVCaptureDeviceInput_Tundra.deviceInputWithDevice_error_, 1
        )
        self.assertArgIsOut(
            AVFoundation.AVCaptureDeviceInput_Tundra.initWithDevice_error_, 1
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureScreenInput.capturesCursor)
        self.assertArgIsBOOL(AVFoundation.AVCaptureScreenInput.setCapturesCursor_, 0)

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureScreenInput.removesDuplicateFrames
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureScreenInput.setRemovesDuplicateFrames_, 0
        )

    @min_os_level("12.0")
    def testMethodsTundra10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureScreenInput_Tundra.capturesCursor)
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureScreenInput_Tundra.setCapturesCursor_, 0
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureScreenInput.removesDuplicateFrames
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureScreenInput.setRemovesDuplicateFrames_, 0
        )
