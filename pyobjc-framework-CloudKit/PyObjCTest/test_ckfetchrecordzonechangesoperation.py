import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CloudKit

    class TestCKFetchRecordZoneChangesOperation (TestCase):
        @min_os_level("10.12")
        def testMethods10_12(self):
            self.assertArgIsBlock(CloudKit.CKFetchRecordZoneChangesOperation.setRecordChangedBlock_, 0, b"v@")
            self.assertResultIsBlock(CloudKit.CKFetchRecordZoneChangesOperation.recordChangedBlock, b"v@")

            self.assertArgIsBlock(CloudKit.CKFetchRecordZoneChangesOperation.setRecordWithIDWasDeletedBlock_, 0, b"v@@")
            self.assertResultIsBlock(CloudKit.CKFetchRecordZoneChangesOperation.recordWithIDWasDeletedBlock, b"v@@")

            self.assertArgIsBlock(CloudKit.CKFetchRecordZoneChangesOperation.setRecordZoneChangeTokensUpdatedBlock_, 0, b"v@@@")
            self.assertResultIsBlock(CloudKit.CKFetchRecordZoneChangesOperation.recordZoneChangeTokensUpdatedBlock, b"v@@@")

            self.assertArgIsBlock(CloudKit.CKFetchRecordZoneChangesOperation.setRecordZoneFetchCompletionBlock_, 0, b"v@@@Z@")
            self.assertResultIsBlock(CloudKit.CKFetchRecordZoneChangesOperation.recordZoneFetchCompletionBlock, b"v@@@Z@")

            self.assertArgIsBlock(CloudKit.CKFetchRecordZoneChangesOperation.setFetchRecordZoneChangesCompletionBlock_, 0, b"v@")
            self.assertResultIsBlock(CloudKit.CKFetchRecordZoneChangesOperation.fetchRecordZoneChangesCompletionBlock, b"v@")

            self.assertResultIsBOOL(CloudKit.CKFetchRecordZoneChangesOperation.fetchAllChanges)
            self.assertArgIsBOOL(CloudKit.CKFetchRecordZoneChangesOperation.setFetchAllChanges_, 0)

if __name__ == "__main__":
    main()
