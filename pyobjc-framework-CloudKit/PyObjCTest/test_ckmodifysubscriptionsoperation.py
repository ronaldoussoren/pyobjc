from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKModifySubscriptionsOperation(TestCase):
    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBlock(
            CloudKit.CKModifySubscriptionsOperation.perSubscriptionSaveBlock, b"v@@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKModifySubscriptionsOperation.setPerSubscriptionSaveBlock_,
            0,
            b"v@@@",
        )

        self.assertResultIsBlock(
            CloudKit.CKModifySubscriptionsOperation.perSubscriptionDeleteBlock, b"v@@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKModifySubscriptionsOperation.setPerSubscriptionDeleteBlock_,
            0,
            b"v@@@",
        )

        self.assertResultIsBlock(
            CloudKit.CKModifySubscriptionsOperation.modifySubscriptionsCompletionBlock,
            b"v@@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKModifySubscriptionsOperation.setModifySubscriptionsCompletionBlock_,
            0,
            b"v@@@",
        )
