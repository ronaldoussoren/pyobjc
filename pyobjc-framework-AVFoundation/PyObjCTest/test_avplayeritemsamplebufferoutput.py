import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level


class TestAVPlayerItemSampleBufferOutput(TestCase):
    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists(
            "AVPlayerItemSampleBufferOutputDelegate", AVFoundation
        )

    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsCFRetained(
            AVFoundation.AVPlayerItemSampleBufferOutput.copyNextSampleBuffer
        )
