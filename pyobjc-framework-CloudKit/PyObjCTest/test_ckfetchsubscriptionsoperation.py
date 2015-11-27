import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKFetchSubscriptionsOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(CloudKit.CKFetchSubscriptionsOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CloudKit.CKFetchSubscriptionsOperation.setFetchSubscriptionCompletionBlock_, 0, b"v@@")
            self.assertResultIsBlock(CloudKit.CKFetchSubscriptionsOperation.fetchSubscriptionCompletionBlock, b"v@@")

if __name__ == "__main__":
    main()
