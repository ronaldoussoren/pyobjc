from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEDNSProxyProvider(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertResultIsBOOL(
            NetworkExtension.NEDNSProxyProvider.handleNewUDPFlow_initialRemoteEndpoint_
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(
            NetworkExtension.NEDNSProxyProvider.handleNewUDPFlow_initialRemoteFlowEndpoint_
        )
