from PyObjCTools.TestSupport import TestCase

import IOBluetooth

IOBluetoothOBEXSessionOpenConnectionCallback = b"v^{OpaqueOBEXSessionRef=}i^v"


class TestOBEXBluetooth(TestCase):
    def test_functions(self):
        self.assertArgIsOut(
            IOBluetooth.IOBluetoothOBEXSessionCreateWithIOBluetoothSDPServiceRecordRef,
            1,
        )
        self.assertArgIsOut(
            IOBluetooth.IOBluetoothOBEXSessionCreateWithIOBluetoothDeviceRefAndChannelNumber,
            2,
        )

        if 1:
            self.assertNotHasAttr(
                IOBluetooth,
                "IOBluetoothOBEXSessionCreateWithIncomingIOBluetoothRFCOMMChannel",
            )
        else:
            self.assertArgIsOut(
                IOBluetooth.IOBluetoothOBEXSessionCreateWithIncomingIOBluetoothRFCOMMChannel,
                3,
            )
        self.assertArgIsFunction(
            IOBluetooth.IOBluetoothOBEXSessionOpenTransportConnection,
            1,
            IOBluetoothOBEXSessionOpenConnectionCallback,
            True,
        )
