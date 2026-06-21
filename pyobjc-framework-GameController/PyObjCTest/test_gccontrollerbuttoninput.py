from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import GameController


class TestGCControllerButtonInput(TestCase):
    @min_os_level("10.9")
    def test_classes(self):
        self.assertIsInstance(GameController.GCControllerButtonInput, objc.objc_class)

    @min_os_level("10.9")
    def test_methods(self):
        self.assertResultIsBlock(
            GameController.GCControllerButtonInput.valueChangedHandler,
            b"v@f" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            GameController.GCControllerButtonInput.setValueChangedHandler_,
            0,
            b"v@f" + objc._C_NSBOOL,
        )

        self.assertResultIsBOOL(GameController.GCControllerButtonInput.isPressed)

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBlock(
            GameController.GCControllerButtonInput.pressedChangedHandler,
            b"v@f" + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            GameController.GCControllerButtonInput.setPressedChangedHandler_,
            0,
            b"v@f" + objc._C_NSBOOL,
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBlock(
            GameController.GCControllerButtonInput.touchedChangedHandler,
            b"v@f" + objc._C_NSBOOL + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            GameController.GCControllerButtonInput.setTouchedChangedHandler_,
            0,
            b"v@f" + objc._C_NSBOOL + objc._C_NSBOOL,
        )

        self.assertResultIsBOOL(GameController.GCControllerButtonInput.isTouched)
