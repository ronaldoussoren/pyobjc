
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncSession (TestCase):
    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessArgIsSEL(
            ISyncSession.beginSessionInBackgroundWithClient_entityNames_target_selector_, 3, "v@:@@")

    def testMethods(self):
        self.failUnlessResultIsBOOL(ISyncSession.shouldPushChangesForEntityName_)
        self.failUnlessResultIsBOOL(ISyncSession.shouldPushAllRecordsForEntityName_)
        self.failUnlessResultIsBOOL(ISyncSession.shouldPullChangesForEntityName_)
        self.failUnlessResultIsBOOL(ISyncSession.shouldReplaceAllRecordsOnClientForEntityName_)

        self.failUnlessArgIsBOOL(ISyncSession.clientLostRecordWithIdentifier_shouldReplaceOnNextSync_, 1)
        self.failUnlessResultIsBOOL(ISyncSession.prepareToPullChangesForEntityNames_beforeDate_)
        self.failUnlessArgIsSEL(ISyncSession.prepareToPullChangesInBackgroundForEntityNames_target_selector_, 2, "v@:@@")
        self.failUnlessResultIsBOOL(ISyncSession.isCancelled)

    def testConstants(self):
        self.failUnlessIsInstance(ISyncSessionCancelledException, unicode)
        self.failUnlessIsInstance(ISyncSessionUnavailableException, unicode)
        self.failUnlessIsInstance(ISyncInvalidRecordException, unicode)
        self.failUnlessIsInstance(ISyncInvalidRecordIdentifiersKey, unicode)
        self.failUnlessIsInstance(ISyncInvalidRecordReasonsKey, unicode)
        self.failUnlessIsInstance(ISyncInvalidRecordsKey, unicode)
        self.failUnlessIsInstance(ISyncInvalidEntityException, unicode)
        self.failUnlessIsInstance(ISyncUnsupportedEntityException, unicode)
        self.failUnlessIsInstance(ISyncRecordEntityNameKey, unicode)


if __name__ == "__main__":
    main()
