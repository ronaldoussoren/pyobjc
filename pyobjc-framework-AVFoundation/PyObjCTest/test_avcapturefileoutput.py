import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureFileOutputHelper(AVFoundation.NSObject):
    def captureOutputShouldProvideSampleAccurateRecordingStart_(self, a):
        return 1

    def captureOutput_didStartRecordingToOutputFileAtURL_startPTS_fromConnections_(
        self, a, b, c, d
    ):
        pass


class TestAVCaptureFileOutput(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureFileOutput.isRecording)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureFileOutput.isRecordingPaused
        )  # noqa: B950

    @min_os_level("12.0")
    def test_methodsTundra(self):
        self.assertResultIsBOOL(AVFoundation.AVCaptureFileOutput_Tundra.isRecording)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureFileOutput_Tundra.isRecordingPaused
        )  # noqa: B950

    def testProtocols(self):
        self.assertProtocolExists("AVCaptureFileOutputRecordingDelegate")
        self.assertProtocolExists("AVCaptureFileOutputDelegate")

    def testProtocolMethods(self):
        self.assertResultIsBOOL(
            TestAVCaptureFileOutputHelper.captureOutputShouldProvideSampleAccurateRecordingStart_  # noqa: B950
        )
        self.assertArgHasType(
            TestAVCaptureFileOutputHelper.captureOutput_didStartRecordingToOutputFileAtURL_startPTS_fromConnections_,  # noqa: B950
            2,
            AVFoundation.CMTime.__typestr__,
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureMovieFileOutput.isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureMovieFileOutput_Tundra.isPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureMovieFileOutput.setPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled_,
            0,
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureMovieFileOutput_Tundra.setPrimaryConstituentDeviceSwitchingBehaviorForRecordingEnabled_,
            0,
        )

    @min_os_level("15.0")
    def testMethods15_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureMovieFileOutput.isSpatialVideoCaptureSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureMovieFileOutput.isSpatialVideoCaptureEnabled
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureMovieFileOutput.setSpatialVideoCaptureEnabled_,
            0,
        )
