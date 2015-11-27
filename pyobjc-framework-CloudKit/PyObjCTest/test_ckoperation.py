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

if __name__ == "__main__":
    main()
