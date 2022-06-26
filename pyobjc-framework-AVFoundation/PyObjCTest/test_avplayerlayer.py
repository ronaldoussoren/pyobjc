import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPlayerLayer(TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerLayer.isReadyForDisplay)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsCFRetained(
            AVFoundation.AVPlayerLayer.copyDisplayedPixelBuffer
        )
