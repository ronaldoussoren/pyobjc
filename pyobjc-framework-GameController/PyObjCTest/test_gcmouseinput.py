from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCMouseInput(TestCase):
    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBlock(GameController.GCMouseInput.mouseMovedHandler, b"v@ff")
        self.assertArgIsBlock(
            GameController.GCMouseInput.setMouseMovedHandler_, 0, b"v@ff"
        )
