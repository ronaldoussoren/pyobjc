from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKFetchNotificationChangesOperation(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(
            CloudKit.CKFetchNotificationChangesOperation, objc.objc_class
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            CloudKit.CKFetchNotificationChangesOperation.setNotificationChangedBlock_,
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchNotificationChangesOperation.notificationChangedBlock, b"v@"
        )

        self.assertArgIsBlock(
            CloudKit.CKFetchNotificationChangesOperation.setFetchNotificationChangesCompletionBlock_,  # noqa: B950
            0,
            b"v@@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchNotificationChangesOperation.fetchNotificationChangesCompletionBlock,  # noqa: B950
            b"v@@",
        )

        self.assertResultIsBOOL(CloudKit.CKFetchNotificationChangesOperation.moreComing)
        # self.assertArgIsBOOL(CloudKit.CKFetchNotificationChangesOperation.setMoreComing_, 0)   # noqa: B950
