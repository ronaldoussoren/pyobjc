from PyObjCTools.TestSupport import TestCase
import GameplayKit


class TestGKVersion(TestCase):
    def test_constants(self):
        self.assertNotHasAttr(GameplayKit, "GK_VERSION")
