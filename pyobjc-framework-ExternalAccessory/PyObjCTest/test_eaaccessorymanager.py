import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import ExternalAccessory

    class TestEAAccessoryManager (TestCase):
        def testConstants(self):
            self.assertEqual(ExternalAccessory.EABluetoothAccessoryPickerAlreadyConnected, 0)
            self.assertEqual(ExternalAccessory.EABluetoothAccessoryPickerResultNotFound, 1)
            self.assertEqual(ExternalAccessory.EABluetoothAccessoryPickerResultCancelled, 2)
            self.assertEqual(ExternalAccessory.EABluetoothAccessoryPickerResultFailed, 3)

            self.assertIsInstance(ExternalAccessory.EABluetoothAccessoryPickerErrorDomain, unicode)
            self.assertIsInstance(ExternalAccessory.EAAccessoryDidConnectNotification, unicode)
            self.assertIsInstance(ExternalAccessory.EAAccessoryDidDisconnectNotification, unicode)
            self.assertIsInstance(ExternalAccessory.EAAccessoryKey, unicode)

        def testMethods(self):
            # Not on macOS:
            #self.assertArgIsBlock(ExternalAccessory.EAAccessoryManager.showBluetoothAccessoryPickerWithNameFilter_completion_, 1, b'v@')
            pass

if __name__ == "__main__":
    main()
