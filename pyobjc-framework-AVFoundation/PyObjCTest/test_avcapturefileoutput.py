import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase


class TestAVCaptureFileOutputHelper(AVFoundation.NSObject):
    def captureOutputShouldProvideSampleAccurateRecordingStart_(self, a):
        return 1


class TestAVCaptureFileOutput(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureFileOutput.isRecording)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureFileOutput.isRecordingPaused
        )  # noqa: B950

    def testProtocols(self):
        objc.protocolNamed("AVCaptureFileOutputRecordingDelegate")
        objc.protocolNamed("AVCaptureFileOutputDelegate")

    def testProtocolMethods(self):
        self.assertResultIsBOOL(
            TestAVCaptureFileOutputHelper.captureOutputShouldProvideSampleAccurateRecordingStart_  # noqa: B950
        )
