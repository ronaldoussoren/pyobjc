from PyObjCTools.TestSupport import TestCase

import IOBluetoothUI


class TestIOBluetoothServiceBrowserController(TestCase):
    def test_methods(self):
        self.assertArgIsOut(
            IOBluetoothUI.IOBluetoothServiceBrowserController.discover_, 0
        )
        self.assertArgIsOut(
            IOBluetoothUI.IOBluetoothServiceBrowserController.discoverAsSheetForWindow_withRecord_,
            1,
        )
        self.assertArgIsOut(
            IOBluetoothUI.IOBluetoothServiceBrowserController.discoverWithDeviceAttributes_serviceList_serviceRecord_,
            2,
        )

        self.assertArgIsIn(
            IOBluetoothUI.IOBluetoothServiceBrowserController.setSearchAttributes_, 0
        )
