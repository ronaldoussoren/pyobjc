
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncManager (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(ISyncManager.isEnabled)
        self.failUnlessResultIsBOOL(ISyncManager.registerSchemaWithBundlePath_)

    def testConstants(self):
        self.failUnlessIsInstance(ISyncAvailabilityChangedNotification, unicode)
        self.failUnlessIsInstance(ISyncServerUnavailableException, unicode)


if __name__ == "__main__":
    main()
