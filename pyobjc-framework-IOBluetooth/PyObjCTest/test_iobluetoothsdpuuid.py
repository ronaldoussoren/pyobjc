from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestIOBluetoothSDPUUID(TestCase):
    def test_methods(self):
        self.assertArgIsIn(IOBluetooth.IOBluetoothSDPUUID.uuidWithBytes_length_, 0)
        self.assertArgSizeInArg(
            IOBluetooth.IOBluetoothSDPUUID.uuidWithBytes_length_, 0, 1
        )
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothSDPUUID.isEqualToUUID_)
