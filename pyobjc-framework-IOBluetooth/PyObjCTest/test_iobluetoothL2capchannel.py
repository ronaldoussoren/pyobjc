from PyObjCTools.TestSupport import TestCase, min_os_level

import IOBluetooth

import objc


class TestIOBluetoothL2CAPChannelHelper(IOBluetooth.NSObject):
    def l2capChannelData_data_length_(self, a, b, c):
        pass

    def l2capChannelOpenComplete_status_(slef, a, b):
        pass

    def l2capChannelWriteComplete_refcon_status_(self, a, b, c):
        pass


class TestIOBluetoothL2CAPChannel(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            IOBluetooth.IOBluetoothL2CAPChannelPublishedNotification, str
        )
        self.assertIsInstance(
            IOBluetooth.IOBluetoothL2CAPChannelTerminatedNotification, str
        )

    def test_protocols(self):
        self.assertProtocolExists("IOBluetoothL2CAPChannelDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestIOBluetoothL2CAPChannelHelper.l2capChannelData_data_length_, 1, b"n^v"
        )
        self.assertArgHasType(
            TestIOBluetoothL2CAPChannelHelper.l2capChannelData_data_length_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgSizeInArg(
            TestIOBluetoothL2CAPChannelHelper.l2capChannelData_data_length_, 1, 2
        )

        self.assertArgHasType(
            TestIOBluetoothL2CAPChannelHelper.l2capChannelOpenComplete_status_,
            1,
            objc._C_INT,
        )

        self.assertArgHasType(
            TestIOBluetoothL2CAPChannelHelper.l2capChannelWriteComplete_refcon_status_,
            1,
            b"^v",
        )
        self.assertArgHasType(
            TestIOBluetoothL2CAPChannelHelper.l2capChannelWriteComplete_refcon_status_,
            2,
            objc._C_INT,
        )

    def test_methods(self):
        self.assertArgIsIn(
            IOBluetooth.IOBluetoothL2CAPChannel.writeAsync_length_refcon_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.IOBluetoothL2CAPChannel.writeAsync_length_refcon_, 0, 1
        )

        self.assertArgIsIn(IOBluetooth.IOBluetoothL2CAPChannel.writeSync_length_, 0)
        self.assertArgSizeInArg(
            IOBluetooth.IOBluetoothL2CAPChannel.writeSync_length_, 0, 1
        )

        self.assertResultIsBOOL(IOBluetooth.IOBluetoothL2CAPChannel.isIncoming)

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertArgIsIn(
            IOBluetooth.IOBluetoothL2CAPChannel.writeAsyncTrap_length_refcon_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.IOBluetoothL2CAPChannel.writeAsyncTrap_length_refcon_, 0, 1
        )
