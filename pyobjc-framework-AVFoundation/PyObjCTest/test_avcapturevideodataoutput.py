import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestAVCaptureVideoDataOutput(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.alwaysDiscardsLateVideoFrames
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureVideoDataOutput.setAlwaysDiscardsLateVideoFrames_, 0
        )

    @min_sdk_level("10.7")
    def testProtocols(self):
        objc.protocolNamed("AVCaptureVideoDataOutputSampleBufferDelegate")
