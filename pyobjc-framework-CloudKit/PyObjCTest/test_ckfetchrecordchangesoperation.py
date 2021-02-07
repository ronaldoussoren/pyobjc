from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKFetchRecordChangesOperation(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKServerChangeToken")
        self.assertIsInstance(CloudKit.CKServerChangeToken, objc.objc_class)
        self.assertHasAttr(CloudKit, "CKFetchRecordChangesOperation")
        self.assertIsInstance(CloudKit.CKFetchRecordChangesOperation, objc.objc_class)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            CloudKit.CKFetchRecordChangesOperation.setRecordChangedBlock_, 0, b"v@"
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordChangesOperation.recordChangedBlock, b"v@"
        )
        self.assertArgIsBlock(
            CloudKit.CKFetchRecordChangesOperation.setRecordWithIDWasDeletedBlock_,
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordChangesOperation.recordWithIDWasDeletedBlock, b"v@"
        )
        self.assertResultIsBOOL(CloudKit.CKFetchRecordChangesOperation.moreComing)
        self.assertArgIsBlock(
            CloudKit.CKFetchRecordChangesOperation.setFetchRecordChangesCompletionBlock_,
            0,
            b"v@@@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordChangesOperation.fetchRecordChangesCompletionBlock,
            b"v@@@",
        )
