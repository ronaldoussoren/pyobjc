import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPlayerItemTrack(TestCase):
    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerItemTrackVideoFieldModeDeinterlaceFields, str
        )

    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerItemTrack.isEnabled)
        self.assertArgIsBOOL(AVFoundation.AVPlayerItemTrack.setEnabled_, 0)
