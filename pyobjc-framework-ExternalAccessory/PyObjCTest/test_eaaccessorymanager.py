from PyObjCTools.TestSupport import TestCase

import ExternalAccessory


class TestEAAccessoryManager(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(ExternalAccessory.EABluetoothAccessoryPickerErrorCode)

    def test_constants(self):
        self.assertEqual(
            ExternalAccessory.EABluetoothAccessoryPickerAlreadyConnected, 0
        )
        self.assertEqual(ExternalAccessory.EABluetoothAccessoryPickerResultNotFound, 1)
        self.assertEqual(ExternalAccessory.EABluetoothAccessoryPickerResultCancelled, 2)
        self.assertEqual(ExternalAccessory.EABluetoothAccessoryPickerResultFailed, 3)

        self.assertIsInstance(
            ExternalAccessory.EABluetoothAccessoryPickerErrorDomain, str
        )
        self.assertIsInstance(ExternalAccessory.EAAccessoryDidConnectNotification, str)
        self.assertIsInstance(
            ExternalAccessory.EAAccessoryDidDisconnectNotification, str
        )
        self.assertIsInstance(ExternalAccessory.EAAccessoryKey, str)

    def test_methods(self):
        # Not on macOS:
        # self.assertArgIsBlock(ExternalAccessory.EAAccessoryManager.showBluetoothAccessoryPickerWithNameFilter_completion_, 1, b'v@')   # noqa: B950
        pass
