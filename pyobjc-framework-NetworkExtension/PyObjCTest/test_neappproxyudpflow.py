from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEAppProxyUDPFlow(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
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
