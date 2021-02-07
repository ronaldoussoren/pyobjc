from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKFetchWebAuthTokenOperation(TestCase):
    @min_os_level("10.11")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKFetchWebAuthTokenOperation")

        self.assertResultIsBlock(
            CloudKit.CKFetchWebAuthTokenOperation.fetchWebAuthTokenCompletionBlock,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKFetchWebAuthTokenOperation.setFetchWebAuthTokenCompletionBlock_,
            0,
            b"v@@",
        )
