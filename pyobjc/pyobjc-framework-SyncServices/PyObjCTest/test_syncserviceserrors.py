
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestSyncServicesErrors (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(ISyncErrorDomain, unicode)

        self.failUnlessEqual(ISyncSessionClientAlreadySyncingError, 100)
        self.failUnlessEqual(ISyncSessionUserCanceledSessionError, 101)
        self.failUnlessEqual(ISyncSessionDriverRegistrationError, 200)
        self.failUnlessEqual(ISyncSessionDriverPullFailureError, 201)
        self.failUnlessEqual(ISyncSessionDriverFatalError, 300)

if __name__ == "__main__":
    main()
