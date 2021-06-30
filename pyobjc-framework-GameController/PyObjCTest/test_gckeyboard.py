from PyObjCTools.TestSupport import TestCase, min_os_level

import GameController


class TestGCKeyboard(TestCase):
    @min_os_level("11.0")
    def test_constants11_0(self):
        self.assertIsInstance(GameController.GCKeyboardDidConnectNotification, str)
        self.assertIsInstance(GameController.GCKeyboardDidDisconnectNotification, str)
