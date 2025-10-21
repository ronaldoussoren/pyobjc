import GameKit
from PyObjCTools.TestSupport import TestCase


class TestGKGameActivityState(TestCase):
    def test_constants(self):
        self.assertIsEnumType(GameKit.GKGameActivityState)
        self.assertEqual(GameKit.GKGameActivityStateInitialized, 0)
        self.assertEqual(GameKit.GKGameActivityStateActive, 1)
        self.assertEqual(GameKit.GKGameActivityStatePaused, 2)
        self.assertEqual(GameKit.GKGameActivityStateEnded, 4)
