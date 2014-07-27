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
            self.assertHasAttr(CloudKit, "CKContainer")
            self.assertIsInstance(CloudKit.CKContainer, objc.objc_class)

        @min_os_level("10.10")
        def testConstants(self):
            self.assertIsInstance(CloudKit.CKAsset, unicode)

            self.assertEqual(CloudKit.CKAccountStatusCouldNotDetermine, 0)
            self.assertEqual(CloudKit.CKAccountStatusAvailable, 1)
            self.assertEqual(CloudKit.CKAccountStatusRestricted, 2)
            self.assertEqual(CloudKit.CKAccountStatusNoAccount, 3)
            self.assertEqual(CloudKit.CKApplicationPermissionUserDiscoverability, 1)
            self.assertEqual(CloudKit.CKApplicationPermissionStatusInitialState, 0)
            self.assertEqual(CloudKit.CKApplicationPermissionStatusCouldNotComplete, 1)
            self.assertEqual(CloudKit.CKApplicationPermissionStatusDenied, 2)
            self.assertEqual(CloudKit.CKApplicationPermissionStatusGranted, 3)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CKContainer.accountStatusWithCompletionHandler_, 0,
                    b"v" + objc._C_NSInteger + b"@")
            self.assertArgIsBlock(CKContainer.statusForApplicationPermission_completionHandler_, 1,
                    b"v" + objc._C_NSInteger + b"@")
            self.assertArgIsBlock(CKContainer.requestApplicationPermission_completionHandler_, 1,
                    b"v" + objc._C_NSInteger + b"@")
            self.assertArgIsBlock(CKContainer.fetchUserRecordIDWithCompletionHandler_, 0,
                    b"v@@")
            self.assertArgIsBlock(CKContainer.discoverAllContactUserInfosWithCompletionHandler_, 0,
                    b"v@@")
            self.assertArgIsBlock(CKContainer.discoverUserInfoWithEmailAddress_completionHandler_, 1,
                    b"v@@")
            self.assertArgIsBlock(CKContainer.discoverUserInfoWithUserRecordID_completionHandler_, 1,
                    b"v@@")


if __name__ == "__main__":
    main()
