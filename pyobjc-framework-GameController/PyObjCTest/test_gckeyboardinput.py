from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController
import objc


class TestGCKeyboardInput(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
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
