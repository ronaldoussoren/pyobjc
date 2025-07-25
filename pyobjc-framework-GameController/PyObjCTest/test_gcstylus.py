from PyObjCTools.TestSupport import TestCase, min_os_level
import GameController


class TestGCStylus(TestCase):
    @min_os_level("26.0")
    def test_constants(self):
        self.assertIsInstance(GameController.GCStylusDidConnectNotification, str)
        self.assertIsInstance(GameController.GCStylusDidDisconnectNotification, str)
