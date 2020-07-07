from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCMouse(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(GameController.GCMouseDidConnectNotification, str)
        self.assertIsInstance(GameController.GCMouseDidDisconnectNotification, str)

        self.assertIsInstance(GameController.GCMouseDidBecomeCurrentNotification, str)
        self.assertIsInstance(
            GameController.GCMouseDidStopBeingCurrentNotification, str
        )
