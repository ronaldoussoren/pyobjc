from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCMouseInput(TestCase):
    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBlock(GameController.GCMouseInput.mouseMovedHandler, b"v@ff")
        self.assertArgIsBlock(
            GameController.GCMouseInput.setMouseMovedHandler_, 0, b"v@ff"
        )
