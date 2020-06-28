import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioRoutingArbiter(TestCase):
    def test_constants(self):
        self.assertEqual(AVFoundation.AVAudioRoutingArbitrationCategoryPlayback, 0)
        self.assertEqual(AVFoundation.AVAudioRoutingArbitrationCategoryPlayAndRecord, 1)
        self.assertEqual(
            AVFoundation.AVAudioRoutingArbitrationCategoryPlayAndRecordVoice, 2
        )

    @min_os_level("10.16")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioRoutingArbiter.beginArbitrationWithCategory_completionHandler_,
            1,
            b"vZ@",
        )
