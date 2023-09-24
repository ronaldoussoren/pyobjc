import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVPlayerLooper(TestCase):
    def testConstants(self):
        self.assertIsEnumType(AVFoundation.AVPlayerLooperStatus)
        self.assertEqual(AVFoundation.AVPlayerLooperStatusUnknown, 0)
        self.assertEqual(AVFoundation.AVPlayerLooperStatusReady, 1)
        self.assertEqual(AVFoundation.AVPlayerLooperStatusFailed, 2)
        self.assertEqual(AVFoundation.AVPlayerLooperStatusCancelled, 3)

        self.assertIsEnumType(AVFoundation.AVPlayerLooperItemOrdering)
        self.assertEqual(
            AVFoundation.AVPlayerLooperItemOrderingLoopingItemsPrecedeExistingItems, 0
        )
        self.assertEqual(
            AVFoundation.AVPlayerLooperItemOrderingLoopingItemsFollowExistingItems, 1
        )
