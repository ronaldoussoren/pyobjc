import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level


class TestAVCaptureVideoDataOutput(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.alwaysDiscardsLateVideoFrames
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.setAlwaysDiscardsLateVideoFrames_, 0
        )

    @min_os_level("12.0")
    def testMethodsTundra(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput_Tundra.alwaysDiscardsLateVideoFrames
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput_Tundra.setAlwaysDiscardsLateVideoFrames_,
            0,
        )

    @min_sdk_level("10.7")
    def testProtocols(self):
        self.assertProtocolExists("AVCaptureVideoDataOutputSampleBufferDelegate")
