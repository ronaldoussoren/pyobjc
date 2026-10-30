from PyObjCTools.TestSupport import TestCase
import objc
import GameController


class TestGCExtendedGamepad(TestCase):
    def test_classes(self):
        self.assertIsInstance(GameController.GCExtendedGamepad, objc.objc_class)

    def test_methods(self):
        self.assertResultIsBlock(
            GameController.GCExtendedGamepad.valueChangedHandler, b"v@@"
        )
        self.assertArgIsBlock(
            GameController.GCExtendedGamepad.setValueChangedHandler_, 0, b"v@@"
        )
