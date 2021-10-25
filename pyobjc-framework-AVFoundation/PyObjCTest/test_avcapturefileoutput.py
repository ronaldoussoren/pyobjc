import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


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

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureMovieFileOutput.isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureMovieFileOutput.setPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled_,
            0,
        )
