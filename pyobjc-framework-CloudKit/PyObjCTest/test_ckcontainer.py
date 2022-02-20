from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKContainer(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CloudKit.CKAccountStatus)
        self.assertIsEnumType(CloudKit.CKApplicationPermissionStatus)
        self.assertIsEnumType(CloudKit.CKApplicationPermissions)

    @min_os_level("10.10")
    def testClasses(self):
        self.assertIsInstance(CloudKit.CKAsset, objc.objc_class)
        self.assertIsInstance(CloudKit.CKContainer, objc.objc_class)

    @min_os_level("10.10")
    def testConstants(self):
        self.assertIsInstance(CloudKit.CKOwnerDefaultName, str)

        self.assertEqual(CloudKit.CKAccountStatusCouldNotDetermine, 0)
        self.assertEqual(CloudKit.CKAccountStatusAvailable, 1)
        self.assertEqual(CloudKit.CKAccountStatusRestricted, 2)
        self.assertEqual(CloudKit.CKAccountStatusNoAccount, 3)
        self.assertEqual(CloudKit.CKAccountStatusTemporarilyUnavailable, 4)
        self.assertEqual(CloudKit.CKApplicationPermissionUserDiscoverability, 1)
        self.assertEqual(CloudKit.CKApplicationPermissionStatusInitialState, 0)
        self.assertEqual(CloudKit.CKApplicationPermissionStatusCouldNotComplete, 1)
        self.assertEqual(CloudKit.CKApplicationPermissionStatusDenied, 2)
        self.assertEqual(CloudKit.CKApplicationPermissionStatusGranted, 3)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertIsInstance(CloudKit.CKAccountChangedNotification, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(CloudKit.CKCurrentUserDefaultName, str)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            CloudKit.CKContainer.accountStatusWithCompletionHandler_,
            0,
            b"v" + objc._C_NSInteger + b"@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.statusForApplicationPermission_completionHandler_,
            1,
            b"v" + objc._C_NSInteger + b"@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.requestApplicationPermission_completionHandler_,
            1,
            b"v" + objc._C_NSInteger + b"@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.fetchUserRecordIDWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.discoverAllContactUserInfosWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.discoverUserInfoWithEmailAddress_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.discoverUserInfoWithUserRecordID_completionHandler_,
            1,
            b"v@@",
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBlock(
            CloudKit.CKContainer.fetchShareParticipantWithEmailAddress_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.fetchShareParticipantWithPhoneNumber_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.fetchShareParticipantWithUserRecordID_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.fetchShareMetadataWithURL_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.acceptShareMetadata_completionHandler_, 1, b"v@@"
        )

        self.assertArgIsBlock(
            CloudKit.CKContainer.fetchAllLongLivedOperationIDsWithCompletionHandler_,
            0,
            b"v@@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.fetchLongLivedOperationWithID_completionHandler_,
            1,
            b"v@@",
        )

        self.assertArgIsBlock(
            CloudKit.CKContainer.discoverAllIdentitiesWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.discoverUserIdentityWithEmailAddress_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.discoverUserIdentityWithPhoneNumber_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            CloudKit.CKContainer.discoverUserIdentityWithUserRecordID_completionHandler_,
            1,
            b"v@@",
        )
