from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEFilterDataProvider(TestCase):
    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            NetworkExtension.NEFilterDataProvider.applySettings_completionHandler_,
            1,
            b"v@",
        )
