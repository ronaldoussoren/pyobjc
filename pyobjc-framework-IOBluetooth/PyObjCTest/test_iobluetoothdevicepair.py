from PyObjCTools.TestSupport import TestCase

import IOBluetooth
import objc


class TestIOBluetoothDevicePairHelper(IOBluetooth.NSObject):
    def devicePairingUserConfirmationRequest_numericValue_(self, a, b):
        pass

    def devicePairingUserPasskeyNotification_passkey_(self, a, b):
        pass

    def devicePairingFinished_error_(self, a, b):
        pass

    def deviceSimplePairingComplete_status_(self, a, b):
        pass


class TestIOBluetoothDevicePair(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("IOBluetoothDevicePairDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestIOBluetoothDevicePairHelper.devicePairingUserConfirmationRequest_numericValue_,
            1,
            objc._C_UINT,
        )

        self.assertArgHasType(
            TestIOBluetoothDevicePairHelper.devicePairingUserPasskeyNotification_passkey_,
            1,
            objc._C_UINT,
        )

        self.assertArgHasType(
            TestIOBluetoothDevicePairHelper.devicePairingFinished_error_,
            1,
            objc._C_INT,
        )

        self.assertArgHasType(
            TestIOBluetoothDevicePairHelper.deviceSimplePairingComplete_status_,
            1,
            objc._C_UCHR,
        )

    def test_methods(self):
        self.assertArgIsIn(IOBluetooth.IOBluetoothDevicePair.replyPINCode_PINCode_, 1)

        self.assertArgIsBOOL(
            IOBluetooth.IOBluetoothDevicePair.replyUserConfirmation_, 0
        )
