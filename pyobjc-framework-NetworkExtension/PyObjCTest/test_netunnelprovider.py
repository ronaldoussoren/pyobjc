from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEAppProxyFlow(TestCase):
    def test_enums(self):
        self.assertIsEnumType(NetworkExtension.NETunnelProviderError)
        self.assertEqual(
            NetworkExtension.NETunnelProviderErrorNetworkSettingsInvalid, 1
        )
        self.assertEqual(
            NetworkExtension.NETunnelProviderErrorNetworkSettingsCanceled, 2
        )
        self.assertEqual(NetworkExtension.NETunnelProviderErrorNetworkSettingsFailed, 3)

        self.assertIsEnumType(NetworkExtension.NETunnelProviderRoutingMethod)
        self.assertEqual(NetworkExtension.NETunnelProviderRoutingMethodDestinationIP, 1)
        self.assertEqual(
            NetworkExtension.NETunnelProviderRoutingMethodSourceApplication, 2
        )
        self.assertEqual(NetworkExtension.NETunnelProviderRoutingMethodNetworkRule, 3)

    @min_os_level("10.11")
    def test_constants(self):
        self.assertIsInstance(NetworkExtension.NETunnelProviderErrorDomain, str)

    @min_os_level("10.11")
    def test_methods(self):
        self.assertArgIsBlock(
            NetworkExtension.NETunnelProvider.handleAppMessage_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NETunnelProvider.setTunnelNetworkSettings_completionHandler_,
            1,
            b"v@",
        )
        self.assertResultIsBOOL(NetworkExtension.NETunnelProvider.reasserting)
        self.assertArgIsBOOL(NetworkExtension.NETunnelProvider.setReasserting_, 0)
