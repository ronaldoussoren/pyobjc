from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEDNSProxyManager(TestCase):
        @min_os_level("10.15")
        def test_constants10_15(self):
            self.assertIsInstance(
                NetworkExtension.NEDNSProxyConfigurationDidChangeNotification, unicode
            )

        @min_os_level("10.15")
        def test_methods10_15(self):
            self.assertArgIsBlock(
                NetworkExtension.NEDNSProxyManager.loadFromPreferencesWithCompletionHandler_,
                0,
                b"v@",
            )
            self.assertArgIsBlock(
                NetworkExtension.NEDNSProxyManager.removeFromPreferencesWithCompletionHandler_,
                0,
                b"v@",
            )
            self.assertArgIsBlock(
                NetworkExtension.NEDNSProxyManager.saveToPreferencesWithCompletionHandler_,
                0,
                b"v@",
            )

            self.assertResultIsBOOL(NetworkExtension.NEDNSProxyManager.isEnabled)
            self.assertArgIsBOOL(NetworkExtension.NEDNSProxyManager.setEnabled_, 0)

            # self.assertArgIsBlock(NetworkExtension.NEDNSProxyManager.startProxyWithOptions_completionHandler_, 1, b'v@')
            # self.assertArgIsBlock(NetworkExtension.NEDNSProxyManager.stopProxyWithReason_completionHandler_, 1, b'v')
            # self.assertResultIsBOOL(NetworkExtension.NEDNSProxyManager.handleNewFlow_)
            # self.assertResultIsBOOL(NetworkExtension.NEDNSProxyManager.handleNewUDPFlow_initialRemoteEndpoint_)


if __name__ == "__main__":
    main()
