from PyObjCTools.TestSupport import TestCase

import IOBluetoothUI


class TestIOBluetoothObjectPushUIController(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            IOBluetoothUI.IOBluetoothObjectPushUIController.isTransferInProgress
        )
