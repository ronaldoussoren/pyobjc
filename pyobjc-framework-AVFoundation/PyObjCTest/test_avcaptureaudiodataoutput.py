import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVCaptureAudioDataOutput(TestCase):
    def test_classes(self):
        AVFoundation.AVCaptureAudioDataOutput

    def test_protocols(self):
        self.assertProtocolExists(
            "AVCaptureAudioDataOutputSampleBufferDelegate", AVFoundation
        )
