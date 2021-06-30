from PyObjCTools.TestSupport import TestCase
import IntentsUI


class TestIntentsUI(TestCase):
    def test_constants(self):
        self.assertIsInstance(IntentsUI.IntentsUIVersionNumber, float)
        self.assertIsInstance(IntentsUI.IntentsUIVersionString, bytes)
