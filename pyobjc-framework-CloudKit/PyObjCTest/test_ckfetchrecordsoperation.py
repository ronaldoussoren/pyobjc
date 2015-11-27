import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKFetchRecordsOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKFetchRecordsOperation")
            self.assertIsInstance(CloudKit.CKFetchRecordsOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CloudKit.CKFetchRecordsOperation.setPerRecordProgressBlock_, 0, b"v@d")
            self.assertResultIsBlock(CloudKit.CKFetchRecordsOperation.perRecordProgressBlock, b"v@d")
            self.assertArgIsBlock(CloudKit.CKFetchRecordsOperation.setPerRecordCompletionBlock_, 0, b"v@@@")
            self.assertResultIsBlock(CloudKit.CKFetchRecordsOperation.perRecordCompletionBlock, b"v@@@")
            self.assertArgIsBlock(CloudKit.CKFetchRecordsOperation.setFetchRecordsCompletionBlock_, 0, b"v@@")
            self.assertResultIsBlock(CloudKit.CKFetchRecordsOperation.fetchRecordsCompletionBlock, b"v@@")

if __name__ == "__main__":
    main()
