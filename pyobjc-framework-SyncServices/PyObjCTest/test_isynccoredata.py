from PyObjCTools.TestSupport import TestCase, min_os_level
import SyncServices
import objc


class TestISyncCoreDataHelper(SyncServices.NSObject):
    def persistentStoreCoordinatorShouldStartSyncing_(self, v):
        return True

    def persistentStoreCoordinator_willDeleteRecordWithIdentifier_inSyncSession_(
        self, c, i, s
    ):
        return True


class TestISyncCoreData(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(
            SyncServices.NSPersistentStoreCoordinator.syncWithClient_inBackground_handler_error_  # noqa: B950
        )
        self.assertArgIsBOOL(
            SyncServices.NSPersistentStoreCoordinator.syncWithClient_inBackground_handler_error_,  # noqa: B950
            1,
        )
        self.assertArgIsOut(
            SyncServices.NSPersistentStoreCoordinator.syncWithClient_inBackground_handler_error_,  # noqa: B950
            3,
        )

    def testProtocols(self):
        objc.protocolNamed("NSPersistentStoreCoordinatorSyncing")
        self.assertResultIsBOOL(
            TestISyncCoreDataHelper.persistentStoreCoordinatorShouldStartSyncing_
        )
        self.assertResultIsBOOL(
            TestISyncCoreDataHelper.persistentStoreCoordinator_willDeleteRecordWithIdentifier_inSyncSession_  # noqa: B950
        )
