import sys

try:
    unicode
except NameError:
    unicode = str

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
            self.assertArgIsBlock(CKContainer.fetchRecordWithID_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CKContainer.saveRecord_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CKContainer.deleteRecordWithID_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CKContainer.performQuery_inZoneWithID__completionHandler_, 2, b"v@@")
            self.assertArgIsBlock(CKContainer.fetchAllRecordZonesWithCompletionHandler_, 0, b"v@@")
            self.assertArgIsBlock(CKContainer.fetchRecordZoneWithID_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CKContainer.saveRecordZone_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CKContainer.deleteRecordZoneWithID_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CKContainer.fetchSubscriptionWithID_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CKContainer.fetchAllSubscriptionsWithCompletionHandler_, 0, b"v@@")
            self.assertArgIsBlock(CKContainer.saveSubscription_completionHandler_, 1, b"v@@")
            self.assertArgIsBlock(CKContainer.deleteSubscriptionWithID_completionHandler_, 1, b"v@@")


if __name__ == "__main__":
    main()
