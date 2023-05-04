from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
)
import objc
import GameController


class TestGCMicroGamepad(TestCase):
    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(GameController.GCInputMicroGamepadDpad, str)
        self.assertIsInstance(GameController.GCInputMicroGamepadButtonA, str)
        self.assertIsInstance(GameController.GCInputMicroGamepadButtonX, str)
        self.assertIsInstance(GameController.GCInputMicroGamepadButtonMenu, str)

    @min_os_level("10.12")
    def testClasses(self):
        self.assertIsInstance(GameController.GCMicroGamepad, objc.objc_class)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBlock(
            GameController.GCMicroGamepad.valueChangedHandler, b"v@@"
        )
        self.assertArgIsBlock(
            GameController.GCMicroGamepad.setValueChangedHandler_, 0, b"v@@"
        )

        self.assertResultIsBOOL(GameController.GCMicroGamepad.reportsAbsoluteDpadValues)
        self.assertArgIsBOOL(
            GameController.GCMicroGamepad.setReportsAbsoluteDpadValues_, 0
        )

        self.assertResultIsBOOL(GameController.GCMicroGamepad.allowsRotation)
        self.assertArgIsBOOL(GameController.GCMicroGamepad.setAllowsRotation_, 0)
