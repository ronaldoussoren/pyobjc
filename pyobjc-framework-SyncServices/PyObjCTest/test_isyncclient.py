
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncClient (TestCase):
    def testConstants(self):
        self.assertEqual(ISyncStatusRunning, 1)
        self.assertEqual(ISyncStatusSuccess, 2)
        self.assertEqual(ISyncStatusWarnings, 3)
        self.assertEqual(ISyncStatusErrors, 4)
        self.assertEqual(ISyncStatusCancelled, 5)
        self.assertEqual(ISyncStatusFailed, 6)
        self.assertEqual(ISyncStatusNever, 7)

        self.assertIsInstance(ISyncClientTypeApplication, unicode)
        self.assertIsInstance(ISyncClientTypeDevice, unicode)
        self.assertIsInstance(ISyncClientTypeServer, unicode)
        self.assertIsInstance(ISyncClientTypePeer, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(ISyncClient.canPushChangesForEntityName_)
        self.assertResultIsBOOL(ISyncClient.canPullChangesForEntityName_)
        self.assertResultIsBOOL(ISyncClient.isEnabledForEntityName_)
        self.assertArgIsBOOL(ISyncClient.setEnabled_forEntityNames_, 0)
        self.assertResultIsBOOL(ISyncClient.shouldReplaceClientRecordsForEntityName_)
        self.assertArgIsBOOL(ISyncClient.setShouldReplaceClientRecords_forEntityNames_, 0)
        self.assertResultIsBOOL(ISyncClient.shouldSynchronizeWithClientsOfType_)
        self.assertArgIsBOOL(ISyncClient.setShouldSynchronize_withClientsOfType_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(ISyncClient.formatsRelationships)
        self.assertArgIsBOOL(ISyncClient.setFormatsRelationships_, 0)

if __name__ == "__main__":
    main()
