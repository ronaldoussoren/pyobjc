from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import GameController


class TestGCExtendedGamepad(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(GameController.GCExtendedGamepad, objc.objc_class)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBlock(
            GameController.GCExtendedGamepad.valueChangedHandler, b"v@@"
        )
        self.assertArgIsBlock(
            GameController.GCExtendedGamepad.setValueChangedHandler_, 0, b"v@@"
        )
