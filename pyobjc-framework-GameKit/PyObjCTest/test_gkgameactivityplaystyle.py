from PyObjCTools.TestSupport import TestCase
import GameKit


class TestGKGameActivityPlayStyle(TestCase):
    def test_constants(self):
        self.assertIsEnumType(GameKit.GKGameActivityPlayStyle)
        self.assertEqual(GameKit.GKGameActivityPlayStyleUnspecified, 0)
        self.assertEqual(GameKit.GKGameActivityPlayStyleSynchronous, 1)
        self.assertEqual(GameKit.GKGameActivityPlayStyleAsynchronous, 2)
