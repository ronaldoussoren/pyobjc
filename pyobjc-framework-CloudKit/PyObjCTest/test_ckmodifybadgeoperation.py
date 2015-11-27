import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKModifyBadgeOperation (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKModifyBadgeOperation")
            self.assertIsInstance(CloudKit.CKModifyBadgeOperation, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            #self.assertResultIsBOOL(CloudKit.CKModifyBadgeOperation.thisDeviceOnly)
            #self.assertArgIsBOOL(CloudKit.CKModifyBadgeOperation.setThisDeviceOnly_, 0)

            self.assertResultIsBlock(CloudKit.CKModifyBadgeOperation.modifyBadgeCompletionBlock, b"v@")
            self.assertArgIsBlock(CloudKit.CKModifyBadgeOperation.setModifyBadgeCompletionBlock_, 0, b"v@")

if __name__ == "__main__":
    main()
