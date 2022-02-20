import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVAudioRoutingArbiter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVAudioRoutingArbitrationCategory)

    def test_constants(self):
        self.assertEqual(AVFoundation.AVAudioRoutingArbitrationCategoryPlayback, 0)
        self.assertEqual(AVFoundation.AVAudioRoutingArbitrationCategoryPlayAndRecord, 1)
        self.assertEqual(
            AVFoundation.AVAudioRoutingArbitrationCategoryPlayAndRecordVoice, 2
        )

    @min_os_level("11.0")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVAudioRoutingArbiter.beginArbitrationWithCategory_completionHandler_,
            1,
            b"vZ@",
        )
