from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestIOBluetoothHostController(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            IOBluetooth.IOBluetoothHostControllerPoweredOnNotification, str
        )
        self.assertIsInstance(
            IOBluetooth.IOBluetoothHostControllerPoweredOffNotification, str
        )
