import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKOperation")
            self.assertIsInstance(CloudKit.CKOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods(self):
            self.assertResultIsBOOL(CloudKit.CKOperation.usesBackgroundSession)
            self.assertArgIsBOOL(CloudKit.CKOperation.setUsesBackgroundSession_, 0)
            self.assertResultIsBOOL(CloudKit.CKOperation.allowsCellularAccess)
            self.assertArgIsBOOL(CloudKit.CKOperation.setAllowsCellularAccess_, 0)

        @min_os_level("10.12")
        def testMethods10_12(self):
            self.assertResultIsBOOL(CloudKit.CKOperation.isLongLived)
            self.assertArgIsBOOL(CloudKit.CKOperation.setLongLived_, 0)

            self.assertArgIsBlock(CloudKit.CKOperation.setLongLivedOperationWasPersistedBlock_, 0, b'v')
            self.assertResultIsBlock(CloudKit.CKOperation.longLivedOperationWasPersistedBlock, b'v')

if __name__ == "__main__":
    main()
