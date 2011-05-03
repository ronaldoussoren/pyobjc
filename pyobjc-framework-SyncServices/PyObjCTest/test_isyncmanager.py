
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncManager (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(ISyncManager.isEnabled)
        self.assertResultIsBOOL(ISyncManager.registerSchemaWithBundlePath_)

    def testConstants(self):
        self.assertIsInstance(ISyncAvailabilityChangedNotification, unicode)
        self.assertIsInstance(ISyncServerUnavailableException, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBOOL(ISyncManager.clientWithIdentifier_needsSyncing_, 1)

if __name__ == "__main__":
    main()
