import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKAsset (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertIsInstance(CloudKit.CKAsset, objc.objc_class)
            self.assertIsInstance(CloudKit.CKContainer, objc.objc_class)

        @min_os_level("10.10")
        def testConstants(self):
            self.assertIsInstnace(CloudKit.CKOwnerDefaultName, unicode)

            self.assertEqual(CloudKit.CKAccountStatusCouldNotDetermine, 0)
            self.assertEqual(CloudKit.CKAccountStatusAvailable, 1)
            self.assertEqual(CloudKit.CKAccountStatusRestricted, 2)
            self.assertEqual(CloudKit.CKAccountStatusNoAccount, 3)
            self.assertEqual(CloudKit.CKApplicationPermissionUserDiscoverability, 1)
            self.assertEqual(CloudKit.CKApplicationPermissionStatusInitialState, 0)
            self.assertEqual(CloudKit.CKApplicationPermissionStatusCouldNotComplete, 1)
            self.assertEqual(CloudKit.CKApplicationPermissionStatusDenied, 2)
            self.assertEqual(CloudKit.CKApplicationPermissionStatusGranted, 3)

        @min_os_level("10.11")
        def testConstants(self):
            self.assertIsInstance(CloudKit.CKAccountChangedNotification, unicode)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CloudKit.CKContainer.accountStatusWithCompletionHandler_, 0,
                    b"v" + objc._C_NSInteger + b"@")
            self.assertArgIsBlock(CloudKit.CKContainer.statusForApplicationPermission_completionHandler_, 1,
                    b"v" + objc._C_NSInteger + b"@")
            self.assertArgIsBlock(CloudKit.CKContainer.requestApplicationPermission_completionHandler_, 1,
                    b"v" + objc._C_NSInteger + b"@")
            self.assertArgIsBlock(CloudKit.CKContainer.fetchUserRecordIDWithCompletionHandler_, 0,
                    b"v@@")
            self.assertArgIsBlock(CloudKit.CKContainer.discoverAllContactUserInfosWithCompletionHandler_, 0,
                    b"v@@")
            self.assertArgIsBlock(CloudKit.CKContainer.discoverUserInfoWithEmailAddress_completionHandler_, 1,
                    b"v@@")
            self.assertArgIsBlock(CloudKit.CKContainer.discoverUserInfoWithUserRecordID_completionHandler_, 1,
                    b"v@@")


if __name__ == "__main__":
    main()
