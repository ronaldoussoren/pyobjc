from PyObjCTools.TestSupport import TestCase, os_level_between
import NetworkExtension


class TestNEFailureHandlerProvider(TestCase):
    @os_level_between("14.0", "14.1")
    def testMethods(self):
        self.assertArgIsBlock(
            NetworkExtension.NEFailureHandlerProvider.handleFailure_completionHandler_,
            1,
            b"v",
        )
