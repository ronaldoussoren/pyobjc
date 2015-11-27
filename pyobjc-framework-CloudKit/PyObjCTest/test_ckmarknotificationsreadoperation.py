import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKMarkNotificationsReadOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKMarkNotificationsReadOperation")
            self.assertIsInstance(CloudKit.CKMarkNotificationsReadOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertResultIsBlock(CloudKit.CKMarkNotificationsReadOperation.markNotificationsReadCompletionBlock, b"v@@")
            self.assertArgIsBlock(CloudKit.CKMarkNotificationsReadOperation.setMarkNotificationsReadCompletionBlock_, 0, b"v@@")

if __name__ == "__main__":
    main()
