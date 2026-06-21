import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestAVCaptureAudioDataOutput(TestCase):
    def test_classes(self):
        AVFoundation.AVCaptureAudioDataOutput

    @min_sdk_level("10.7")
    def test_protocols(self):
        self.assertProtocolExists(
            "AVCaptureAudioDataOutputSampleBufferDelegate", AVFoundation
        )
