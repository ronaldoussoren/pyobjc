
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncManager (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(ISyncManager.isEnabled)
        self.failUnlessResultIsBOOL(ISyncManager.registerSchemaWithBundlePath_)

    def testConstants(self):
        self.failUnlessIsInstance(ISyncAvailabilityChangedNotification, unicode)
        self.failUnlessIsInstance(ISyncServerUnavailableException, unicode)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsBOOL(ISyncManager.clientWithIdentifier_needsSyncing_, 1)

if __name__ == "__main__":
    main()
