from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKQueryOperation(TestCase):
    @min_os_level("10.10")
    def test_classes(self):
        self.assertHasAttr(CloudKit, "CKQueryCursor")
        self.assertIsInstance(CloudKit.CKQueryCursor, objc.objc_class)
        self.assertHasAttr(CloudKit, "CKQueryOperation")
        self.assertIsInstance(CloudKit.CKQueryOperation, objc.objc_class)

    @min_os_level("10.10")
    def test_constants(self):
        self.assertIsInstance(CloudKit.CKQueryOperationMaximumResults, int)

    @min_os_level("10.10")
    def test_methods(self):
        self.assertResultIsBlock(CloudKit.CKQueryOperation.recordFetchedBlock, b"v@")
        self.assertArgIsBlock(
            CloudKit.CKQueryOperation.setRecordFetchedBlock_, 0, b"v@"
        )
        self.assertResultIsBlock(CloudKit.CKQueryOperation.queryCompletionBlock, b"v@@")
        self.assertArgIsBlock(
            CloudKit.CKQueryOperation.setQueryCompletionBlock_, 0, b"v@@"
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBlock(CloudKit.CKQueryOperation.recordMatchedBlock, b"v@@@")
        self.assertArgIsBlock(
            CloudKit.CKQueryOperation.setRecordMatchedBlock_, 0, b"v@@@"
        )
