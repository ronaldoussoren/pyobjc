from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEFailureHandlerProvider(TestCase):
    @min_os_level("10.14")
    def testMethods(self):
        self.assertArgIsBlock(
            NetworkExtension.NEFailureHandlerProvider.handleFailure_completionHandler_,
            1,
            b"v",
        )
