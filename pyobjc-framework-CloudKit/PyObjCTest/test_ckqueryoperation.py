from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKQueryOperation(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKQueryCursor")
        self.assertIsInstance(CloudKit.CKQueryCursor, objc.objc_class)
        self.assertHasAttr(CloudKit, "CKQueryOperation")
        self.assertIsInstance(CloudKit.CKQueryOperation, objc.objc_class)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertIsInstance(CloudKit.CKQueryOperationMaximumResults, int)

    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBlock(CloudKit.CKQueryOperation.recordFetchedBlock, b"v@")
        self.assertArgIsBlock(
            CloudKit.CKQueryOperation.setRecordFetchedBlock_, 0, b"v@"
        )
        self.assertResultIsBlock(CloudKit.CKQueryOperation.queryCompletionBlock, b"v@@")
        self.assertArgIsBlock(
            CloudKit.CKQueryOperation.setQueryCompletionBlock_, 0, b"v@@"
        )
