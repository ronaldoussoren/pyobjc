from PyObjCTools.TestSupport import TestCase, min_os_level
import SyncServices


class TestISyncManager(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(SyncServices.ISyncManager.isEnabled)
        self.assertResultIsBOOL(SyncServices.ISyncManager.registerSchemaWithBundlePath_)

    def test_constants(self):
        self.assertIsInstance(SyncServices.ISyncAvailabilityChangedNotification, str)
        self.assertIsInstance(SyncServices.ISyncServerUnavailableException, str)

    @min_os_level("10.6")
    def test_methods10_6(self):
        self.assertArgIsBOOL(
            SyncServices.ISyncManager.clientWithIdentifier_needsSyncing_, 1
        )
