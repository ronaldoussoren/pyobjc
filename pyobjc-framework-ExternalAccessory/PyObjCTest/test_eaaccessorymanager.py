from PyObjCTools.TestSupport import TestCase

import ExternalAccessory


class TestEAAccessoryManager(TestCase):
    def test_enums(self):
        self.assertIsEnumType(ExternalAccessory.EABluetoothAccessoryPickerErrorCode)
        self.assertEqual(
            ExternalAccessory.EABluetoothAccessoryPickerAlreadyConnected, 0
        )
        self.assertEqual(ExternalAccessory.EABluetoothAccessoryPickerResultNotFound, 1)
        self.assertEqual(ExternalAccessory.EABluetoothAccessoryPickerResultCancelled, 2)
        self.assertEqual(ExternalAccessory.EABluetoothAccessoryPickerResultFailed, 3)

    def test_constants(self):
        self.assertIsInstance(
            ExternalAccessory.EABluetoothAccessoryPickerErrorDomain, str
        )
        self.assertIsInstance(ExternalAccessory.EAAccessoryDidConnectNotification, str)
        self.assertIsInstance(
            ExternalAccessory.EAAccessoryDidDisconnectNotification, str
        )
        self.assertIsInstance(ExternalAccessory.EAAccessoryKey, str)
