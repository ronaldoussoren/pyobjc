from PyObjCTools.TestSupport import TestCase, min_os_level
import SyncServices


class TestISyncManager(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(SyncServices.ISyncManager.isEnabled)
        self.assertResultIsBOOL(SyncServices.ISyncManager.registerSchemaWithBundlePath_)

    def testConstants(self):
        self.assertIsInstance(SyncServices.ISyncAvailabilityChangedNotification, str)
        self.assertIsInstance(SyncServices.ISyncServerUnavailableException, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBOOL(
            SyncServices.ISyncManager.clientWithIdentifier_needsSyncing_, 1
        )
