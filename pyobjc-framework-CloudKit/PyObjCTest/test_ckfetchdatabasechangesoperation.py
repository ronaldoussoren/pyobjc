from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKFetchDatabaseChangesOperation(TestCase):
    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBlock(
            CloudKit.CKFetchDatabaseChangesOperation.setRecordZoneWithIDChangedBlock_,
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchDatabaseChangesOperation.recordZoneWithIDChangedBlock, b"v@"
        )

        self.assertArgIsBlock(
            CloudKit.CKFetchDatabaseChangesOperation.setRecordZoneWithIDWasDeletedBlock_,
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchDatabaseChangesOperation.recordZoneWithIDWasDeletedBlock,
            b"v@",
        )

        self.assertArgIsBlock(
            CloudKit.CKFetchDatabaseChangesOperation.setChangeTokenUpdatedBlock_,
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchDatabaseChangesOperation.changeTokenUpdatedBlock, b"v@"
        )

        self.assertArgIsBlock(
            CloudKit.CKFetchDatabaseChangesOperation.setFetchDatabaseChangesCompletionBlock_,  # noqa: B950
            0,
            b"v@Z@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchDatabaseChangesOperation.fetchDatabaseChangesCompletionBlock,
            b"v@Z@",
        )

        self.assertResultIsBOOL(
            CloudKit.CKFetchDatabaseChangesOperation.fetchAllChanges
        )
        self.assertArgIsBOOL(
            CloudKit.CKFetchDatabaseChangesOperation.setFetchAllChanges_, 0
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            CloudKit.CKFetchDatabaseChangesOperation.setRecordZoneWithIDWasPurgedBlock_,
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchDatabaseChangesOperation.recordZoneWithIDWasPurgedBlock,
            b"v@",
        )
