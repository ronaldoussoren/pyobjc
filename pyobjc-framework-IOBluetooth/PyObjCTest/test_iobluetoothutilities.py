from PyObjCTools.TestSupport import TestCase, min_os_level

import IOBluetooth


class TestIOBluetoothUtilities(TestCase):
    def test_functions(self):
        self.assertArgIsOut(IOBluetooth.IOBluetoothNSStringToDeviceAddress, 1)
        self.assertArgIsIn(IOBluetooth.IOBluetoothNSStringFromDeviceAddress, 0)
        self.assertResultIsBOOL(IOBluetooth.IOBluetoothIsFileAppleDesignatedPIMData, 1)
        IOBluetooth.IOBluetoothGetUniqueFileNameAndPath

        if 0:
            # These functions are only available in C code, not ObjC
            self.assertArgIsOut(IOBluetooth.IOBluetoothCFStringToDeviceAddress, 1)
            self.assertArgIsIn(IOBluetooth.IOBluetoothCFStringFromDeviceAddress, 1)
            self.assertResultIsBOOL(
                IOBluetooth.IOBluetoothIsFileAppleDesignatedPIMDataAtCFStringPath, 1
            )
            IOBluetooth.IOBluetoothGetUniqueFileNameAndWithCFStringPath

        # XXX: Needs manual binding:
        self.assertNotHasAttr(IOBluetooth, "IOBluetoothPackData")

        self.assertNotHasAttr(IOBluetooth, "IOBluetoothPackDataList")  # va_list

        # XXX: Needs manual binding:
        self.assertNotHasAttr(IOBluetooth, "IOBluetoothUnpackData")

        self.assertNotHasAttr(IOBluetooth, "IOBluetoothUnpackDataList")  # va_list

        IOBluetooth.IOBluetoothNumberOfAvailableHIDDevices
        IOBluetooth.IOBluetoothNumberOfPointingHIDDevices
        IOBluetooth.IOBluetoothNumberOfKeyboardHIDDevices
        IOBluetooth.IOBluetoothNumberOfTabletHIDDevices

        self.assertArgIsIn(
            IOBluetooth.IOBluetoothFindNumberOfRegistryEntriesOfClassName, 0
        )
        self.assertArgIsNullTerminated(
            IOBluetooth.IOBluetoothFindNumberOfRegistryEntriesOfClassName, 0
        )

    @min_os_level("10.10")
    def test_functions10_10(self):
        self.assertArgIsIn(IOBluetooth.IOBluetoothNSStringFromDeviceAddressColon, 0)
