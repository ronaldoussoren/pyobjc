from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKFetchRecordZoneChangesOperation(TestCase):
    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.setRecordChangedBlock_, 0, b"v@"
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.recordChangedBlock, b"v@"
        )

        self.assertArgIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.setRecordWithIDWasDeletedBlock_,
            0,
            b"v@@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.recordWithIDWasDeletedBlock,
            b"v@@",
        )

        self.assertArgIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.setRecordZoneChangeTokensUpdatedBlock_,  # noqa: B950
            0,
            b"v@@@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.recordZoneChangeTokensUpdatedBlock,
            b"v@@@",
        )

        self.assertArgIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.setRecordZoneFetchCompletionBlock_,
            0,
            b"v@@@Z@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.recordZoneFetchCompletionBlock,
            b"v@@@Z@",
        )

        self.assertArgIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.setFetchRecordZoneChangesCompletionBlock_,  # noqa: B950
            0,
            b"v@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.fetchRecordZoneChangesCompletionBlock,  # noqa: B950
            b"v@",
        )

        self.assertResultIsBOOL(
            CloudKit.CKFetchRecordZoneChangesOperation.fetchAllChanges
        )
        self.assertArgIsBOOL(
            CloudKit.CKFetchRecordZoneChangesOperation.setFetchAllChanges_, 0
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.setRecordWasChangedBlock_,
            0,
            b"v@@@",
        )
        self.assertResultIsBlock(
            CloudKit.CKFetchRecordZoneChangesOperation.recordWasChangedBlock, b"v@@@"
        )
