from PyObjCTools.TestSupport import TestCase, min_os_level

import NetworkExtension


class TestNEPacketTunnelFlow(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertArgIsBlock(
            NetworkExtension.NEPacketTunnelFlow.readPacketsWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertResultIsBOOL(
            NetworkExtension.NEPacketTunnelFlow.writePackets_withProtocols_
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBlock(
            NetworkExtension.NEPacketTunnelFlow.readPacketObjectsWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertResultIsBOOL(NetworkExtension.NEPacketTunnelFlow.writePacketObjects_)
