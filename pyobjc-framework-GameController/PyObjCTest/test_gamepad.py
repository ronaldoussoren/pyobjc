from PyObjCTools.TestSupport import TestCase
import objc

import GameController


class TestGCGamePad(TestCase):
    def test_classes(self):
        self.assertIsInstance(GameController.GCGamepad, objc.objc_class)

    def test_methods(self):
        self.assertResultIsBlock(GameController.GCGamepad.valueChangedHandler, b"v@@")
        self.assertArgIsBlock(
            GameController.GCGamepad.setValueChangedHandler_, 0, b"v@@"
        )
