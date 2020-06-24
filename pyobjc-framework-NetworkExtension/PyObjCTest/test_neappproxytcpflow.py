from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEAppProxyTCPFlow(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertArgIsBlock(
            NetworkExtension.NEAppProxyTCPFlow.readDataWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            NetworkExtension.NEAppProxyTCPFlow.writeData_withCompletionHandler_,
            1,
            b"v@",
        )
