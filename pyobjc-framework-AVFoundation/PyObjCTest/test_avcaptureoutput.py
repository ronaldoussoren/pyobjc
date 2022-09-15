import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureOutputHelper(AVFoundation.NSObject):
    def captureOutputShouldProvideSampleAccurateRecordingStart_(self, a):
        return 1


class TestAVCaptureOutput(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVCaptureOutputDataDroppedReason)

    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.alwaysDiscardsLateVideoFrames
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.setAlwaysDiscardsLateVideoFrames_,
            0,  # noqa: B950
        )

        self.assertResultIsBOOL(AVFoundation.AVCaptureFileOutput.isRecording)
        self.assertResultIsBOOL(AVFoundation.AVCaptureFileOutput.isRecordingPaused)

        self.assertResultIsBOOL(
            TestAVCaptureOutputHelper.captureOutputShouldProvideSampleAccurateRecordingStart_  # noqa: B950
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureStillImageOutput.isCapturingStillImage
        )
        self.assertArgIsBlock(
            AVFoundation.AVCaptureStillImageOutput.captureStillImageAsynchronouslyFromConnection_completionHandler_,  # noqa: B950
            1,
            b"v^{opaqueCMSampleBuffer=}@",
        )

    @min_os_level("12.0")
    def test_methodsTundra(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput_Tundra.alwaysDiscardsLateVideoFrames
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput_Tundra.setAlwaysDiscardsLateVideoFrames_,
            0,  # noqa: B950
        )

        self.assertResultIsBOOL(AVFoundation.AVCaptureFileOutput_Tundra.isRecording)
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureFileOutput_Tundra.isRecordingPaused
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureStillImageOutput_Tundra.isCapturingStillImage
        )
        self.assertArgIsBlock(
            AVFoundation.AVCaptureStillImageOutput_Tundra.captureStillImageAsynchronouslyFromConnection_completionHandler_,  # noqa: B950
            1,
            b"v^{opaqueCMSampleBuffer=}@",
        )

    def testProtocols(self):
        self.assertProtocolExists("AVCaptureVideoDataOutputSampleBufferDelegate")
        self.assertProtocolExists("AVCaptureAudioDataOutputSampleBufferDelegate")
        self.assertProtocolExists("AVCaptureFileOutputRecordingDelegate")
        self.assertProtocolExists("AVCaptureFileOutputDelegate")
        self.assertProtocolExists("AVCaptureMetadataOutputObjectsDelegate")
