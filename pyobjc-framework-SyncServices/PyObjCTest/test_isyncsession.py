from PyObjCTools.TestSupport import TestCase, min_os_level
import SyncServices


class TestISyncSession(TestCase):
    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsSEL(
            SyncServices.ISyncSession.beginSessionInBackgroundWithClient_entityNames_target_selector_,  # noqa: B950
            3,
            b"v@:@@",
        )

    def testMethods(self):
        self.assertResultIsBOOL(
            SyncServices.ISyncSession.shouldPushChangesForEntityName_
        )
        self.assertResultIsBOOL(
            SyncServices.ISyncSession.shouldPushAllRecordsForEntityName_
        )
        self.assertResultIsBOOL(
            SyncServices.ISyncSession.shouldPullChangesForEntityName_
        )
        self.assertResultIsBOOL(
            SyncServices.ISyncSession.shouldReplaceAllRecordsOnClientForEntityName_
        )

        self.assertArgIsBOOL(
            SyncServices.ISyncSession.clientLostRecordWithIdentifier_shouldReplaceOnNextSync_,
            1,
        )
        self.assertResultIsBOOL(
            SyncServices.ISyncSession.prepareToPullChangesForEntityNames_beforeDate_
        )
        self.assertArgIsSEL(
            SyncServices.ISyncSession.prepareToPullChangesInBackgroundForEntityNames_target_selector_,  # noqa: B950
            2,
            b"v@:@@",
        )
        self.assertResultIsBOOL(SyncServices.ISyncSession.isCancelled)

    def testConstants(self):
        self.assertIsInstance(SyncServices.ISyncSessionCancelledException, str)
        self.assertIsInstance(SyncServices.ISyncSessionUnavailableException, str)
        self.assertIsInstance(SyncServices.ISyncInvalidRecordException, str)
        self.assertIsInstance(SyncServices.ISyncInvalidRecordIdentifiersKey, str)
        self.assertIsInstance(SyncServices.ISyncInvalidRecordReasonsKey, str)
        self.assertIsInstance(SyncServices.ISyncInvalidRecordsKey, str)
        self.assertIsInstance(SyncServices.ISyncInvalidEntityException, str)
        self.assertIsInstance(SyncServices.ISyncUnsupportedEntityException, str)
        self.assertIsInstance(SyncServices.ISyncRecordEntityNameKey, str)
