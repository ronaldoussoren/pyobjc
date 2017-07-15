import sys

from PyObjCTools.TestSupport import *
import objc

if sys.maxsize > 2 ** 32:
    import ExternalAccessory

    class TestEAWiFiUnconfiguredAccessoryBrowser (TestCase):
        def testProtocols(self):
            objc.protocolNamed('EAWiFiUnconfiguredAccessoryBrowserDelegate')

        def testConstants(self):
            self.assertEqual(ExternalAccessory.EAWiFiUnconfiguredAccessoryBrowserStateWiFiUnavailable, 0)
            self.assertEqual(ExternalAccessory.EAWiFiUnconfiguredAccessoryBrowserStateStopped, 1)
            self.assertEqual(ExternalAccessory.EAWiFiUnconfiguredAccessoryBrowserStateSearching, 2)
            self.assertEqual(ExternalAccessory.EAWiFiUnconfiguredAccessoryBrowserStateConfiguring, 3)

            self.assertEqual(ExternalAccessory.EAWiFiUnconfiguredAccessoryConfigurationStatusSuccess, 0)
            self.assertEqual(ExternalAccessory.EAWiFiUnconfiguredAccessoryConfigurationStatusUserCancelledConfiguration, 1)
            self.assertEqual(ExternalAccessory.EAWiFiUnconfiguredAccessoryConfigurationStatusFailed, 2)

        def testMethods(self):
            # Not on macOS:
            #self.assertArgIsBlock(ExternalAccessory.EAAccessoryManager.showBluetoothAccessoryPickerWithNameFilter_completion_, 1, b'v@')
            pass

if __name__ == "__main__":
    main()
