from PyObjCTools.TestSupport import TestCase
import CloudKit


class TestCKSyncEngineEvent(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CloudKit.CKSyncEngineEventType)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeStateUpdate, 0)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeAccountChange, 1)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeFetchedDatabaseChanges, 2)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeFetchedRecordZoneChanges, 3)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeSentDatabaseChanges, 4)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeSentRecordZoneChanges, 5)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeWillFetchChanges, 6)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeWillFetchRecordZoneChanges, 7)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeDidFetchRecordZoneChanges, 8)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeDidFetchChanges, 9)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeWillSendChanges, 10)
        self.assertEqual(CloudKit.CKSyncEngineEventTypeDidSendChanges, 11)

        self.assertIsEnumType(CloudKit.CKSyncEngineAccountChangeType)
        self.assertEqual(CloudKit.CKSyncEngineAccountChangeTypeSignIn, 0)
        self.assertEqual(CloudKit.CKSyncEngineAccountChangeTypeSignOut, 1)
        self.assertEqual(CloudKit.CKSyncEngineAccountChangeTypeSwitchAccounts, 2)

        self.assertIsEnumType(CloudKit.CKSyncEngineZoneDeletionReason)
        self.assertEqual(CloudKit.CKSyncEngineZoneDeletionReasonDeleted, 0)
        self.assertEqual(CloudKit.CKSyncEngineZoneDeletionReasonPurged, 1)
        self.assertEqual(CloudKit.CKSyncEngineZoneDeletionReasonEncryptedDataReset, 2)
