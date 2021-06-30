from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController
import objc


class TestGCKeyboardInput(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBlock(
            GameController.GCKeyboardInput.keyChangedHandler,
            b"v@@" + objc._C_CFIndex + objc._C_NSBOOL,
        )
        self.assertArgIsBlock(
            GameController.GCKeyboardInput.setKeyChangedHandler_,
            0,
            b"v@@" + objc._C_CFIndex + objc._C_NSBOOL,
        )

        self.assertResultIsBOOL(GameController.GCKeyboardInput.isAnyKeyPressed)
