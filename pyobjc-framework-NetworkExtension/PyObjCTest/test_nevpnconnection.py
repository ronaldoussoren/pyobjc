from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEVPNConnection (TestCase):
        @min_os_level('10.11')
        def testConstants(self):
            self.assertEqual(NetworkExtension.NEVPNStatusInvalid, 0)
            self.assertEqual(NetworkExtension.NEVPNStatusDisconnected, 1)
            self.assertEqual(NetworkExtension.NEVPNStatusConnecting, 2)
            self.assertEqual(NetworkExtension.NEVPNStatusConnected, 3)
            self.assertEqual(NetworkExtension.NEVPNStatusReasserting, 4)
            self.assertEqual(NetworkExtension.NEVPNStatusDisconnecting, 5)

            self.assertIsInstance(NetworkExtension.NEVPNStatusDidChangeNotification, unicode)
            self.assertIsInstance(NetworkExtension.NEVPNConnectionStartOptionUsername, unicode)
            self.assertIsInstance(NetworkExtension.NEVPNConnectionStartOptionPassword, unicode)

        @min_os_level('10.11')
        def testMethods(self):
            self.assertResultIsBOOL(NetworkExtension.NEVPNConnection.startVPNTunnelAndReturnError_)
            self.assertArgIsOut(NetworkExtension.NEVPNConnection.startVPNTunnelAndReturnError_, 0)

            self.assertResultIsBOOL(NetworkExtension.NEVPNConnection.startVPNTunnelWithOptions_andReturnError_)
            self.assertArgIsOut(NetworkExtension.NEVPNConnection.startVPNTunnelWithOptions_andReturnError_, 1)


if __name__ == "__main__":
    main()
