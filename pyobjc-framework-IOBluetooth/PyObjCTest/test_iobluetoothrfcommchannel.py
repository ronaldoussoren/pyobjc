from PyObjCTools.TestSupport import TestCase

import IOBluetooth
import objc


class TestIOBluetoothRFCOMMChannelHelper(IOBluetooth.NSObject):
    def rfcommChannelData_data_length_(self, a, b, c):
        pass

    def rfcommChannelOpenComplete_status_(self, a, b):
        pass

    def rfcommChannelWriteComplete_refcon_status_(self, a, b, c):
        pass

    def rfcommChannelWriteComplete_refcon_status_bytesWritten_(self, a, b, c, d):
        pass


class TestIOBluetoothRFCOMMChannel(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("IOBluetoothRFCOMMChannelDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestIOBluetoothRFCOMMChannelHelper.rfcommChannelData_data_length_, 1, b"n^v"
        )
        self.assertArgHasType(
            TestIOBluetoothRFCOMMChannelHelper.rfcommChannelData_data_length_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestIOBluetoothRFCOMMChannelHelper.rfcommChannelData_data_length_, 1, 2
        )

        self.assertArgHasType(
            TestIOBluetoothRFCOMMChannelHelper.rfcommChannelOpenComplete_status_,
            1,
            objc._C_INT,
        )
        self.assertArgHasType(
            TestIOBluetoothRFCOMMChannelHelper.rfcommChannelWriteComplete_refcon_status_,
            2,
            objc._C_INT,
        )
        self.assertArgHasType(
            TestIOBluetoothRFCOMMChannelHelper.rfcommChannelWriteComplete_refcon_status_bytesWritten_,
            2,
            objc._C_INT,
        )
        self.assertArgHasType(
            TestIOBluetoothRFCOMMChannelHelper.rfcommChannelWriteComplete_refcon_status_bytesWritten_,
            3,
            objc._C_NSUInteger,
        )

    def test_methods(self):
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothRFCOMMChannel.isOpen)
        self.assertResultIsBOOL(
            IOBluetooth.IOBluetoothRFCOMMChannel.isTransmissionPaused
        )

        self.assertArgIsIn(IOBluetooth.IOBluetoothRFCOMMChannel.write_length_sleep_, 0)
        self.assertArgSizeInArg(
            IOBluetooth.IOBluetoothRFCOMMChannel.write_length_sleep_, 0, 1
        )
        self.assertArgIsBOOL(
            IOBluetooth.IOBluetoothRFCOMMChannel.write_length_sleep_, 2
        )

        self.assertArgIsIn(
            IOBluetooth.IOBluetoothRFCOMMChannel.writeAsync_length_refcon_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.IOBluetoothRFCOMMChannel.writeAsync_length_refcon_, 0, 1
        )

        self.assertArgIsIn(IOBluetooth.IOBluetoothRFCOMMChannel.writeSync_length_, 0)
        self.assertArgSizeInArg(
            IOBluetooth.IOBluetoothRFCOMMChannel.writeSync_length_, 0, 1
        )

        self.assertArgIsIn(
            IOBluetooth.IOBluetoothRFCOMMChannel.writeSimple_length_sleep_bytesSent_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.IOBluetoothRFCOMMChannel.writeSimple_length_sleep_bytesSent_,
            0,
            1,
        )
        self.assertArgIsBOOL(
            IOBluetooth.IOBluetoothRFCOMMChannel.writeSimple_length_sleep_bytesSent_, 2
        )
        self.assertArgIsOut(
            IOBluetooth.IOBluetoothRFCOMMChannel.writeSimple_length_sleep_bytesSent_, 3
        )

        self.assertResultIsBOOL(IOBluetooth.IOBluetoothRFCOMMChannel.isIncoming)
