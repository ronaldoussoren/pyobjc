from PyObjCTools.TestSupport import TestCase, min_os_level
import CloudKit


class TestCKSyncEngineState(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CloudKit.CKSyncEnginePendingRecordZoneChangeType)
        self.assertEqual(CloudKit.CKSyncEnginePendingRecordZoneChangeTypeSave, 0)
        self.assertEqual(CloudKit.CKSyncEnginePendingRecordZoneChangeTypeDelete, 1)

        self.assertIsEnumType(CloudKit.CKSyncEnginePendingDatabaseChangeType)
        self.assertEqual(CloudKit.CKSyncEnginePendingDatabaseChangeTypeSave, 0)
        self.assertEqual(CloudKit.CKSyncEnginePendingDatabaseChangeTypeDelete, 1)

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertResultIsBOOL(CloudKit.CKSyncEngineState.hasPendingUntrackedChanges)
        self.assertArgIsBOOL(
            CloudKit.CKSyncEngineState.setHasPendingUntrackedChanges_, 0
        )
