from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKVersion(TestCase):
    def testConstants(self):
        self.assertNotHasAttr(GameplayKit, "GK_VERSION")
