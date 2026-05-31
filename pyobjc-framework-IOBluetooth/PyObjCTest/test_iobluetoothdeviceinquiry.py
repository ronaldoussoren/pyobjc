from PyObjCTools.TestSupport import TestCase

import IOBluetooth
import objc


class TestIOBluetoothDeviceInquiryHelper(IOBluetooth.NSObject):
    def deviceInquiryUpdatingDeviceNamesStarted_devicesRemaining_(self, a, b):
        pass

    def deviceInquiryDeviceNameUpdated_device_devicesRemaining_(self, a, b, c):
        pass

    def deviceInquiryComplete_error_aborted_(self, a, b, c):
        pass


class TestIOBluetoothDeviceInquiry(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("IOBluetoothDeviceInquiryDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestIOBluetoothDeviceInquiryHelper.deviceInquiryUpdatingDeviceNamesStarted_devicesRemaining_,
            1,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestIOBluetoothDeviceInquiryHelper.deviceInquiryDeviceNameUpdated_device_devicesRemaining_,
            2,
            objc._C_UINT,
        )
        self.assertArgHasType(
            TestIOBluetoothDeviceInquiryHelper.deviceInquiryComplete_error_aborted_,
            1,
            objc._C_INT,
        )
        self.assertArgIsBOOL(
            TestIOBluetoothDeviceInquiryHelper.deviceInquiryComplete_error_aborted_, 2
        )

    def test_methods(self):
        self.assertResultIsBOOL(
            IOBluetooth.IOBluetoothDeviceInquiry.updateNewDeviceNames
        )
        self.assertArgIsBOOL(
            IOBluetooth.IOBluetoothDeviceInquiry.setUpdateNewDeviceNames_, 0
        )
