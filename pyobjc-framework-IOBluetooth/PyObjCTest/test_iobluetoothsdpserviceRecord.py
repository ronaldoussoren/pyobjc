from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestIOBluetoothSDPServiceRecord(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothSDPServiceRecord.matchesUUID16_)
        self.assertResultIsBOOL(
            IOBluetooth.IOBluetoothSDPServiceRecord.matchesUUIDArray_
        )
        self.assertResultIsBOOL(
            IOBluetooth.IOBluetoothSDPServiceRecord.matchesSearchArray_
        )
        self.assertResultIsBOOL(
            IOBluetooth.IOBluetoothSDPServiceRecord.hasServiceFromArray_
        )
