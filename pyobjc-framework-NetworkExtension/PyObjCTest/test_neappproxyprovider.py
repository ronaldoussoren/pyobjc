from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEAppProxyProvider(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertArgIsBlock(
            NetworkExtension.NEAppProxyProvider.startProxyWithOptions_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEAppProxyProvider.stopProxyWithReason_completionHandler_,
            1,
            b"v",
        )
        self.assertResultIsBOOL(NetworkExtension.NEAppProxyProvider.handleNewFlow_)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(
            NetworkExtension.NEAppProxyProvider.handleNewUDPFlow_initialRemoteEndpoint_
        )

    @min_os_level("15.0")
    def testMethods15_0(self):
        self.assertResultIsBOOL(NetworkExtension.NEAppProxyProvider.handleNewFlow_)
        self.assertResultIsBOOL(
            NetworkExtension.NEAppProxyProvider.handleNewUDPFlow_initialRemoteFlowEndpoint_
        )
