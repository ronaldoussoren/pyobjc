
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncSession (TestCase):
    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertArgIsSEL(
            ISyncSession.beginSessionInBackgroundWithClient_entityNames_target_selector_, 3, b"v@:@@")

    def testMethods(self):
        self.assertResultIsBOOL(ISyncSession.shouldPushChangesForEntityName_)
        self.assertResultIsBOOL(ISyncSession.shouldPushAllRecordsForEntityName_)
        self.assertResultIsBOOL(ISyncSession.shouldPullChangesForEntityName_)
        self.assertResultIsBOOL(ISyncSession.shouldReplaceAllRecordsOnClientForEntityName_)

        self.assertArgIsBOOL(ISyncSession.clientLostRecordWithIdentifier_shouldReplaceOnNextSync_, 1)
        self.assertResultIsBOOL(ISyncSession.prepareToPullChangesForEntityNames_beforeDate_)
        self.assertArgIsSEL(ISyncSession.prepareToPullChangesInBackgroundForEntityNames_target_selector_, 2, b"v@:@@")
        self.assertResultIsBOOL(ISyncSession.isCancelled)

    def testConstants(self):
        self.assertIsInstance(ISyncSessionCancelledException, unicode)
        self.assertIsInstance(ISyncSessionUnavailableException, unicode)
        self.assertIsInstance(ISyncInvalidRecordException, unicode)
        self.assertIsInstance(ISyncInvalidRecordIdentifiersKey, unicode)
        self.assertIsInstance(ISyncInvalidRecordReasonsKey, unicode)
        self.assertIsInstance(ISyncInvalidRecordsKey, unicode)
        self.assertIsInstance(ISyncInvalidEntityException, unicode)
        self.assertIsInstance(ISyncUnsupportedEntityException, unicode)
        self.assertIsInstance(ISyncRecordEntityNameKey, unicode)


if __name__ == "__main__":
    main()
