import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKDiscoverUserInfosOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKDiscoveredUserInfo")
            self.assertIsInstance(CloudKit.CKDiscoveredUserInfo, objc.objc_class)

            self.assertResultIsBlock(CloudKit.CKDiscoverUserInfosOperation.discoverUserInfosCompletionBlock, b'v@@@')
            self.assertArgIsBlock(CloudKit.CKDiscoverUserInfosOperation.setDiscoverUserInfosCompletionBlock_, 0, b'v@@@')

if __name__ == "__main__":
    main()
