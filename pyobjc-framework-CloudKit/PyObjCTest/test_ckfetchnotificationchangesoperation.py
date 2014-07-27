import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKFetchNotificationChangesOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "TestCKFetchNotificationChangesOperation")
            self.assertIsInstance(CloudKit.TestCKFetchNotificationChangesOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CloudKit.TestCKFetchNotificationChangesOperation.setNotificationChangedBlock_, 0, b"v@")
            self.assertResultIsBlock(CloudKit.TestCKFetchNotificationChangesOperation.notificationChangedBlock, b"v@")

            self.assertArgIsBlock(CloudKit.TestCKFetchNotificationChangesOperation.setFetchNotificationChangesCompletionBlock_, 0, b"v@@")
            self.assertResultIsBlock(CloudKit.TestCKFetchNotificationChangesOperation.fetchNotificationChangesCompletionBlock, b"v@@")

if __name__ == "__main__":
    main()
