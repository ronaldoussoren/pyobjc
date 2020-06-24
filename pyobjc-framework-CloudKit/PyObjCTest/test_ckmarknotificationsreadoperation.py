from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKMarkNotificationsReadOperation(TestCase):
    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKMarkNotificationsReadOperation")
        self.assertIsInstance(
            CloudKit.CKMarkNotificationsReadOperation, objc.objc_class
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBlock(
            CloudKit.CKMarkNotificationsReadOperation.markNotificationsReadCompletionBlock,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKMarkNotificationsReadOperation.setMarkNotificationsReadCompletionBlock_,  # noqa: B950
            0,
            b"v@@",
        )
