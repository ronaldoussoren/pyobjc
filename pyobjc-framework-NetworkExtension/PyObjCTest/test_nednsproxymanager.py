from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEDNSProxyManager(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(NetworkExtension.NEDNSProxyManagerError)

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(
            NetworkExtension.NEDNSProxyConfigurationDidChangeNotification, str
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
