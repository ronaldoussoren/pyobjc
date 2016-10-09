import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKCKDiscoverAllContactsOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKDiscoverAllContactsOperation")
            self.assertIsInstance(CloudKit.CKDiscoverAllContactsOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CloudKit.CKDiscoverAllContactsOperation.setDiscoverAllContactsCompletionBlock_, 0, b"@@")
            self.assertResultIsBlock(CloudKit.CKDiscoverAllContactsOperation.discoverAllContactsCompletionBlock, b"@@")

if __name__ == "__main__":
    main()
