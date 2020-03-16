from PyObjCTools.TestSupport import TestCase, min_os_level
import SyncServices


class TestISyncClient(TestCase):
    def testConstants(self):
        self.assertEqual(SyncServices.ISyncStatusRunning, 1)
        self.assertEqual(SyncServices.ISyncStatusSuccess, 2)
        self.assertEqual(SyncServices.ISyncStatusWarnings, 3)
        self.assertEqual(SyncServices.ISyncStatusErrors, 4)
        self.assertEqual(SyncServices.ISyncStatusCancelled, 5)
        self.assertEqual(SyncServices.ISyncStatusFailed, 6)
        self.assertEqual(SyncServices.ISyncStatusNever, 7)

        self.assertIsInstance(SyncServices.ISyncClientTypeApplication, str)
        self.assertIsInstance(SyncServices.ISyncClientTypeDevice, str)
        self.assertIsInstance(SyncServices.ISyncClientTypeServer, str)
        self.assertIsInstance(SyncServices.ISyncClientTypePeer, str)

    def testMethods(self):
        self.assertResultIsBOOL(SyncServices.ISyncClient.canPushChangesForEntityName_)
        self.assertResultIsBOOL(SyncServices.ISyncClient.canPullChangesForEntityName_)
        self.assertResultIsBOOL(SyncServices.ISyncClient.isEnabledForEntityName_)
        self.assertArgIsBOOL(SyncServices.ISyncClient.setEnabled_forEntityNames_, 0)
        self.assertResultIsBOOL(
            SyncServices.ISyncClient.shouldReplaceClientRecordsForEntityName_
        )
        self.assertArgIsBOOL(
            SyncServices.ISyncClient.setShouldReplaceClientRecords_forEntityNames_, 0
        )
        self.assertResultIsBOOL(
            SyncServices.ISyncClient.shouldSynchronizeWithClientsOfType_
        )
        self.assertArgIsBOOL(
            SyncServices.ISyncClient.setShouldSynchronize_withClientsOfType_, 0
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(SyncServices.ISyncClient.formatsRelationships)
        self.assertArgIsBOOL(SyncServices.ISyncClient.setFormatsRelationships_, 0)
