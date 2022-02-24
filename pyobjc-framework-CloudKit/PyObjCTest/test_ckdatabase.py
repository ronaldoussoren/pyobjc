from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit
import objc


class TestCKDatabase(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CloudKit.CKDatabaseScope)

    @min_os_level("10.10")
    def testClasses(self):
        self.assertHasAttr(CloudKit, "CKDatabase")
        self.assertIsInstance(CloudKit.CKDatabase, objc.objc_class)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            CloudKit.CKDatabase.fetchRecordWithID_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.saveRecord_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.deleteRecordWithID_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.performQuery_inZoneWithID_completionHandler_, 2, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.fetchAllRecordZonesWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.fetchRecordZoneWithID_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.saveRecordZone_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.deleteRecordZoneWithID_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.fetchSubscriptionWithID_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.fetchAllSubscriptionsWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.saveSubscription_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            CloudKit.CKDatabase.deleteSubscriptionWithID_completionHandler_, 1, b"v@@"
        )

    def testConstants(self):
        self.assertEqual(CloudKit.CKDatabaseScopePublic, 1)
        self.assertEqual(CloudKit.CKDatabaseScopePrivate, 2)
        self.assertEqual(CloudKit.CKDatabaseScopeShared, 3)
