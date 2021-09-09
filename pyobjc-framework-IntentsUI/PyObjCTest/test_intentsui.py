from PyObjCTools.TestSupport import TestCase
import IntentsUI


class TestIntentsUI(TestCase):
    def test_constants(self):
        self.assertIsInstance(IntentsUI.IntentsUIVersionNumber, float)
        self.assertNotHasAttr(IntentsUI, "IntentsUIVersionString")
