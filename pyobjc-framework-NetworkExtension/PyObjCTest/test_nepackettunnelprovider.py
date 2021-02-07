from PyObjCTools.TestSupport import TestCase, min_os_level

import NetworkExtension


class TestNEPacketTunnelProvider(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertArgIsBlock(
            NetworkExtension.NEPacketTunnelProvider.startTunnelWithOptions_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEPacketTunnelProvider.stopTunnelWithReason_completionHandler_,
            1,
            b"v",
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEPacketTunnelProvider.createTCPConnectionThroughTunnelToEndpoint_enableTLS_TLSParameters_delegate_,  # noqa: B950
            1,
        )
