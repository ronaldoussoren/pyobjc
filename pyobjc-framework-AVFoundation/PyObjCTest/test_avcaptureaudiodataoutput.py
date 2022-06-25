import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestAVCaptureAudioDataOutput(TestCase):
    def testClasses(self):
        AVFoundation.AVCaptureAudioDataOutput

    @min_sdk_level("10.7")
    def testProtocols(self):
        self.assertProtocolExists("AVCaptureAudioDataOutputSampleBufferDelegate")
