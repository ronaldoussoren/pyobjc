import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKFetchRecordZonesOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKFetchRecordZonesOperation")
            self.assertIsInstance(CloudKit.CKFetchRecordZonesOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CloudKit.CKFetchRecordZonesOperation.setFetchRecordZonesCompletionBlock_, 0, b"v@@")
            self.assertResultIsBlock(CloudKit.CKFetchRecordZonesOperation.fetchRecordZonesCompletionBlock, b"v@@")

if __name__ == "__main__":
    main()
