
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncClient (TestCase):
    def testConstants(self):
        self.failUnlessEqual(ISyncStatusRunning, 1)
        self.failUnlessEqual(ISyncStatusSuccess, 2)
        self.failUnlessEqual(ISyncStatusWarnings, 3)
        self.failUnlessEqual(ISyncStatusErrors, 4)
        self.failUnlessEqual(ISyncStatusCancelled, 5)
        self.failUnlessEqual(ISyncStatusFailed, 6)
        self.failUnlessEqual(ISyncStatusNever, 7)

        self.failUnlessIsInstance(ISyncClientTypeApplication, unicode)
        self.failUnlessIsInstance(ISyncClientTypeDevice, unicode)
        self.failUnlessIsInstance(ISyncClientTypeServer, unicode)
        self.failUnlessIsInstance(ISyncClientTypePeer, unicode)


    def testMethods(self):
        self.failUnlessResultIsBOOL(ISyncClient.canPushChangesForEntityName_)
        self.failUnlessResultIsBOOL(ISyncClient.canPullChangesForEntityName_)
        self.failUnlessResultIsBOOL(ISyncClient.isEnabledForEntityName_)
        self.failUnlessArgIsBOOL(ISyncClient.setEnabled_forEntityNames_, 0)
        self.failUnlessResultIsBOOL(ISyncClient.shouldReplaceClientRecordsForEntityName_)
        self.failUnlessArgIsBOOL(ISyncClient.setShouldReplaceClientRecords_forEntityNames_, 0)
        self.failUnlessResultIsBOOL(ISyncClient.shouldSynchronizeWithClientsOfType_)
        self.failUnlessArgIsBOOL(ISyncClient.setShouldSynchronize_withClientsOfType_, 0)

if __name__ == "__main__":
    main()
