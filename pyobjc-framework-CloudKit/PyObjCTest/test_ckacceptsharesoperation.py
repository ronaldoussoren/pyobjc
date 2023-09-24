from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKSyncEngineState(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CloudKit.CKSyncEnginePendingRecordZoneChangeType)
        self.assertEqual(CloudKit.CKSyncEnginePendingRecordZoneChangeTypeSaveRecord, 0)
        self.assertEqual(
            CloudKit.CKSyncEnginePendingRecordZoneChangeTypeDeleteRecord, 1
        )

        self.assertIsEnumType(CloudKit.CKSyncEnginePendingDatabaseChangeType)
        self.assertEqual(CloudKit.CKSyncEnginePendingDatabaseChangeTypeSaveZone, 0)
        self.assertEqual(CloudKit.CKSyncEnginePendingDatabaseChangeTypeDeleteZone, 1)

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(CloudKit.CKSyncEngineState.hasPendingUntrackedChanges)
        self.assertArgIsBOOL(
            CloudKit.CKSyncEngineState.setHasPendingUntrackedChanges_, 0
        )
