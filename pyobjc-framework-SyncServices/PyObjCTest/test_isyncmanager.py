from PyObjCTools.TestSupport import TestCase
import SyncServices


class TestISyncManager(TestCase):
    def test_constants(self):
        self.assertIsInstance(SyncServices.ISyncAvailabilityChangedNotification, str)
        self.assertIsInstance(SyncServices.ISyncServerUnavailableException, str)

    def test_methods(self):
        self.assertResultIsBOOL(SyncServices.ISyncManager.isEnabled)
        self.assertResultIsBOOL(SyncServices.ISyncManager.registerSchemaWithBundlePath_)

        self.assertArgIsBOOL(
            SyncServices.ISyncManager.clientWithIdentifier_needsSyncing_, 1
        )
