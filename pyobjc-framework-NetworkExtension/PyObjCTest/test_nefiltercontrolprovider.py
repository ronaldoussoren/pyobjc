from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEFilterControlProvider(TestCase):
    @min_os_level("10.11")
    def testMethods(self):
        self.assertArgIsBlock(
            NetworkExtension.NEFilterControlProvider.handleRemediationForFlow_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEFilterControlProvider.handleNewFlow_completionHandler_,
            1,
            b"v@",
        )

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            NetworkExtension.NEFilterControlProvider.handleNewFlow_completionHandler_,
            1,
            b"v@",
        )
