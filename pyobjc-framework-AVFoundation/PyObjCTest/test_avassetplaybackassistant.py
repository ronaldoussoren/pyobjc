import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAssetPlaybackAssistant(TestCase):
    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(
            AVFoundation.AVAssetPlaybackConfigurationOptionStereoVideo, str
        )
        self.assertIsInstance(
            AVFoundation.AVAssetPlaybackConfigurationOptionStereoMultiviewVideo, str
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            AVFoundation.AVAssetPlaybackAssistant.loadPlaybackConfigurationOptionsWithCompletionHandler_,
            0,
            b"v@",
        )
