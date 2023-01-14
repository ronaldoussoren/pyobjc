from PyObjCTools.TestSupport import TestCase

import IOBluetooth
import objc


class TestIOBluetoothDeviceHelper(IOBluetooth.NSObject):
    def remoteNameRequestComplete_status_(self, a, b):
        pass

    def connectionComplete_status_(self, a, b):
        pass

    def sdpQueryComplete_status_(self, a, b):
        pass


class TestIOBluetoothDevice(TestCase):
    def test_constants(self):
        self.assertEqual(
            IOBluetooth.kIOBluetoothDeviceNotificationNameConnected,
            "IOBluetoothDeviceConnected",
        )
        self.assertEqual(
            IOBluetooth.kIOBluetoothDeviceNotificationNameDisconnected,
            "IOBluetoothDeviceDisconnected",
        )
        self.assertEqual(
            IOBluetooth.kIOBluetoothDeviceNameChangedNotification,
            "IOBluetoothDeviceNameChanged",
        )
        self.assertEqual(
            IOBluetooth.kIOBluetoothDeviceInquiryInfoChangedNotification,
            "IOBluetoothDeviceInquiryInfoChanged",
        )
        self.assertEqual(
            IOBluetooth.kIOBluetoothDeviceServicesChangedNotification,
            "IOBluetoothDeviceServicesChanged",
        )
        self.assertEqual(
            IOBluetooth.kIOBluetoothL2CAPChannelMaxAllowedIncomingMTU,
            "MaxAllowedIncomingMTU",
        )
        self.assertEqual(
            IOBluetooth.kIOBluetoothL2CAPChannelDesiredOutgoingMTU, "DesiredOutgoingMTU"
        )

    def test_protocols(self):
        self.assertProtocolExists("IOBluetoothDeviceAsyncCallbacks")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestIOBluetoothDeviceHelper.remoteNameRequestComplete_status_,
            1,
            objc._C_INT,
        )
        self.assertArgHasType(
            TestIOBluetoothDeviceHelper.connectionComplete_status_, 1, objc._C_INT
        )
        self.assertArgHasType(
            TestIOBluetoothDeviceHelper.sdpQueryComplete_status_, 1, objc._C_INT
        )

    def test_methods(self):
        self.assertArgIsOut(
            IOBluetooth.IOBluetoothDevice.openL2CAPChannelSync_withPSM_delegate_, 0
        )
        self.assertArgIsOut(
            IOBluetooth.IOBluetoothDevice.openL2CAPChannelAsync_withPSM_delegate_, 0
        )
        self.assertArgIsOut(
            IOBluetooth.IOBluetoothDevice.openL2CAPChannel_findExisting_newChannel_, 2
        )

        self.assertArgIsIn(
            IOBluetooth.IOBluetoothDevice.sendL2CAPEchoRequest_length_, 0
        )
        self.assertArgSizeInArg(
            IOBluetooth.IOBluetoothDevice.sendL2CAPEchoRequest_length_, 0, 1
        )

        self.assertArgIsOut(IOBluetooth.IOBluetoothDevice.openRFCOMMChannel_channel_, 1)
        self.assertArgIsOut(
            IOBluetooth.IOBluetoothDevice.openRFCOMMChannelSync_withChannelID_delegate_,
            0,
        )
        self.assertArgIsOut(
            IOBluetooth.IOBluetoothDevice.openRFCOMMChannelAsync_withChannelID_delegate_,
            0,
        )

        self.assertResultIsBOOL(IOBluetooth.IOBluetoothDevice.isConnected)
        self.assertArgIsBOOL(
            IOBluetooth.IOBluetoothDevice.openConnection_withPageTimeout_authenticationRequired_,
            2,
        )
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothDevice.isIncoming)
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothDevice.isFavorite)
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothDevice.isPaired)
