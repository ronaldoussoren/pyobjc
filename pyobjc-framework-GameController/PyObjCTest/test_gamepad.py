from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import GameController


class TestGCGamePad(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(GameController.GCGamepad, objc.objc_class)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBlock(GameController.GCGamepad.valueChangedHandler, b"v@@")
        self.assertArgIsBlock(
            GameController.GCGamepad.setValueChangedHandler_, 0, b"v@@"
        )
