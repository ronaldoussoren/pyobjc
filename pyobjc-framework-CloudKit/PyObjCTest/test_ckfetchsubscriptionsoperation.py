import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKFetchSubscriptionsOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "TestCKFetchSubscriptionsOperation")
            self.assertIsInstance(CloudKit.TestCKFetchSubscriptionsOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CloudKit.TestCKFetchSubscriptionsOperation.setFetchSubscriptionCompletionBlock_, 0, b"v@@")
            self.assertResultIsBlock(CloudKit.TestCKFetchSubscriptionsOperation.fetchSubscriptionCompletionBlock, b"v@@")

if __name__ == "__main__":
    main()
