from PyObjCTools.TestSupport import TestCase

import IOBluetoothUI


class TestIOBluetoothPairingController(TestCase):
    def test_methods(self):
        self.assertArgIsIn(
            IOBluetoothUI.IOBluetoothPairingController.setSearchAttributes_, 0
        )
