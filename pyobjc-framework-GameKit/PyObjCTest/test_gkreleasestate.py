from PyObjCTools.TestSupport import TestCase
import GameKit


class TestGKReleaseState(TestCase):
    def test_constants(self):
        self.assertIsEnumType(GameKit.GKReleaseState)
        self.assertEqual(GameKit.GKReleaseStateUnknown, 0)
        self.assertEqual(GameKit.GKReleaseStateReleased, 1)
        self.assertEqual(GameKit.GKReleaseStatePrereleased, 2)
