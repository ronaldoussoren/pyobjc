from PyObjCTools.TestSupport import TestCase
import objc
import GameController


class TestGCControllerAxisInput(TestCase):
    def test_classes(self):
        self.assertIsInstance(GameController.GCControllerAxisInput, objc.objc_class)

    def test_methods(self):
        self.assertResultIsBlock(
            GameController.GCControllerAxisInput.valueChangedHandler, b"v@f"
        )
        self.assertArgIsBlock(
            GameController.GCControllerAxisInput.setValueChangedHandler_, 0, b"v@f"
        )
