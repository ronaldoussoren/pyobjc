from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKShareRequestAccessOperation(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBlock(
            CloudKit.CKShareRequestAccessOperation.perShareAccessRequestCompletionBlock,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKShareRequestAccessOperation.setPerShareAccessRequestCompletionBlock_,
            b"v@@",
        )

        self.assertResultIsBlock(
            CloudKit.CKShareRequestAccessOperation.shareRequestAccessCompletionBlock,
            b"v@",
        )
        self.assertArgIsBlock(
            CloudKit.CKShareRequestAccessOperation.setShareRequestAccessCompletionBlock_,
            b"v@",
        )
