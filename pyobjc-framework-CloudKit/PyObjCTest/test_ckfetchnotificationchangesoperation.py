import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKFetchNotificationChangesOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(CloudKit.CKFetchNotificationChangesOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CloudKit.CKFetchNotificationChangesOperation.setNotificationChangedBlock_, 0, b"v@")
            self.assertResultIsBlock(CloudKit.CKFetchNotificationChangesOperation.notificationChangedBlock, b"v@")

            self.assertArgIsBlock(CloudKit.CKFetchNotificationChangesOperation.setFetchNotificationChangesCompletionBlock_, 0, b"v@@")
            self.assertResultIsBlock(CloudKit.CKFetchNotificationChangesOperation.fetchNotificationChangesCompletionBlock, b"v@@")

            self.assertResultIsBOOL(CloudKit.CKFetchNotificationChangesOperation.moreComing)
            #self.assertArgIsBOOL(CloudKit.CKFetchNotificationChangesOperation.setMoreComing_, 0)

if __name__ == "__main__":
    main()
