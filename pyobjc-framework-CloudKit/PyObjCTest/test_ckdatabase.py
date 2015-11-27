import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKDatabase (TestCase):
        @min_os_level("10.10")
        def testClasses(self):
            self.assertHasAttr(CloudKit, "CKDatabase")
            self.assertIsInstance(CloudKit.CKDatabase, objc.objc_class)

        @min_os_level("10.10")
        def testMethods10_10(self):
            self.assertArgIsBlock(CloudKit.CKDatabase.fetchRecordWithID_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.saveRecord_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.deleteRecordWithID_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.performQuery_inZoneWithID_completionHandler_, 2, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.fetchAllRecordZonesWithCompletionHandler_, 0, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.fetchRecordZoneWithID_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.saveRecordZone_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.deleteRecordZoneWithID_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.fetchSubscriptionWithID_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.fetchAllSubscriptionsWithCompletionHandler_, 0, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.saveSubscription_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CloudKit.CKDatabase.deleteSubscriptionWithID_completionHandler_, 1, b"v@@")


if __name__ == "__main__":
    main()
