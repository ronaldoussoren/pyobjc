from PyObjCTools.TestSupport import TestCase

import IOBluetoothUI


class TestIOBluetoothUIUserLib(TestCase):
    def test_types(self):
        self.assertIs(
            IOBluetoothUI.IOBluetoothDeviceSelectorControllerRef,
            IOBluetoothUI.IOBluetoothObjectRef,
        )
        self.assertIs(
            IOBluetoothUI.IOBluetoothPairingControllerRef,
            IOBluetoothUI.IOBluetoothObjectRef,
        )
        self.assertIs(
            IOBluetoothUI.IOBluetoothServiceBrowserControllerRef,
            IOBluetoothUI.IOBluetoothObjectRef,
        )

    def test_constants(self):
        self.assertIsEnumType(IOBluetoothUI.IOBluetoothServiceBrowserControllerOptions)
        self.assertEqual(
            IOBluetoothUI.kIOBluetoothServiceBrowserControllerOptionsNone, 0
        )
        self.assertEqual(
            IOBluetoothUI.kIOBluetoothServiceBrowserControllerOptionsAutoStartInquiry,
            1 << 0,
        )
        self.assertEqual(
            IOBluetoothUI.kIOBluetoothServiceBrowserControllerOptionsDisconnectWhenDone,
            1 << 1,
        )

        self.assertEqual(IOBluetoothUI.kIOBluetoothUISuccess, -1000)
        self.assertEqual(IOBluetoothUI.kIOBluetoothUIUserCanceledErr, -1001)

    def test_functions(self):
        IOBluetoothUI.IOBluetoothValidateHardwareWithDescription
        IOBluetoothUI.IOBluetoothGetPairingController
        IOBluetoothUI.IOBluetoothGetDeviceSelectorController
