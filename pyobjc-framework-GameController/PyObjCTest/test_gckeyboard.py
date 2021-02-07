from PyObjCTools.TestSupport import TestCase, min_os_level

import GameController


class TestGCKeyboard(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertIsInstance(GameController.GCKeyboardDidConnectNotification, str)
        self.assertIsInstance(GameController.GCKeyboardDidDisconnectNotification, str)
