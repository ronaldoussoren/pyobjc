import sys

try:
    unicode
except NameError:
    unicode = str

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKAsset (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKDiscoverUserInfosOperation")
            self.assertIsInstance(CloudKit.CKDiscoverUserInfosOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CloudKit.CKDiscoverUserInfosOperation.setDiscoverUserInfosCompletionBlock_, 0, b"@@@")
            self.assertResultIsBlock(CloudKit.CKDiscoverUserInfosOperation.discoverUserInfosCompletionBlock, b"@@@")

if __name__ == "__main__":
    main()
