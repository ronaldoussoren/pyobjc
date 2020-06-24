from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKVersion(TestCase):
    def testConstants(self):
        self.assertEqual(GameplayKit.GK_VERSION, 80_000_000)
