import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVPlayerLooper(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVPlayerLooperStatus)

    def testConstants(self):
        self.assertEqual(AVFoundation.AVPlayerLooperStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVPlayerLooperStatusReady, 1)
        self.assertEqual(AVFoundation.AVPlayerLooperStatusFailed, 2)
        self.assertEqual(AVFoundation.AVPlayerLooperStatusCancelled, 3)
