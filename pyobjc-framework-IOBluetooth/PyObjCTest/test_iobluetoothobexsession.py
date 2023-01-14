from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestIOBluetoothOBEXSession(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothOBEXSession.isSessionTargetAMac)
        self.assertArgIsIn(
            IOBluetooth.IOBluetoothOBEXSession.sendDataToTransport_dataLength_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.IOBluetoothOBEXSession.sendDataToTransport_dataLength_, 0, 1
        )
