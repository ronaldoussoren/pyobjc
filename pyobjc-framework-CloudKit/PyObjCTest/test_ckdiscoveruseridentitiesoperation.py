import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKDiscoverUserIdentitiesOperation (TestCase):
        @min_os_level("10.12")
        def testMethods(self):
            self.assertResultIsBlock(CloudKit.CKDiscoverUserIdentitiesOperation.userIdentityDiscoveredBlock, b'v@@')
            self.assertArgIsBlock(CloudKit.CKDiscoverUserIdentitiesOperation.setUserIdentityDiscoveredBlock_, 0, b'v@@')

            self.assertResultIsBlock(CloudKit.CKDiscoverUserIdentitiesOperation.discoverUserIdentitiesCompletionBlock, b'v@')
            self.assertArgIsBlock(CloudKit.CKDiscoverUserIdentitiesOperation.setDiscoverUserIdentitiesCompletionBlock_, 0, b'v@')

if __name__ == "__main__":
    main()
