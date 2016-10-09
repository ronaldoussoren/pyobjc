import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKDiscoverAllUserIdentitiesOperation (TestCase):
        @min_os_level("10.12")
        def testMethods10_12(self):
            self.assertArgIsBlock(CloudKit.CKDiscoverAllUserIdentitiesOperation.setUserIdentityDiscoveredBlock_, 0, b"v@")
            self.assertResultIsBlock(CloudKit.CKDiscoverAllUserIdentitiesOperation.userIdentityDiscoveredBlock, b"v@")

            self.assertArgIsBlock(CloudKit.CKDiscoverAllUserIdentitiesOperation.setDiscoverAllUserIdentitiesCompletionBlock_, 0, b"v@")
            self.assertResultIsBlock(CloudKit.CKDiscoverAllUserIdentitiesOperation.discoverAllUserIdentitiesCompletionBlock, b"v@")

if __name__ == "__main__":
    main()
