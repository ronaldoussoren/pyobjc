from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEAppProxyUDPFlow(TestCase):
    @min_os_level("10.11")
    def test_methods(self):
        self.assertArgIsBlock(
            NetworkExtension.NEAppProxyUDPFlow.readDatagramsWithCompletionHandler_,
            0,
            b"v@@@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEAppProxyUDPFlow.writeDatagrams_sentByEndpoints_completionHandler_,
            2,
            b"v@",
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertArgIsBlock(
            NetworkExtension.NEAppProxyUDPFlow.readDatagramsAndFlowEndpointsWithCompletionHandler_,
            0,
            b"v@@@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEAppProxyUDPFlow.readDatagramsWithCompletionHandler_,
            0,
            b"v@@@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEAppProxyUDPFlow.writeDatagrams_sentByFlowEndpoints_completionHandler_,
            2,
            b"v@",
        )
