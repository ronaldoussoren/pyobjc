
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

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(ISyncServerDisabledReasonNone, 1000)
        self.failUnlessEqual(ISyncServerDisabledReasonByPreference, 1001)
        self.failUnlessEqual(ISyncServerDisabledReasonSharedNetworkHome, 1002)
        self.failUnlessEqual(ISyncServerDisabledReasonUnresponsive, 1003)
        self.failUnlessEqual(ISyncServerDisabledReasonUnknown, 1004)

        self.failUnlessIsInstance(ISyncInvalidSchemaException, unicode)
        self.failUnlessIsInstance(ISyncInvalidArgumentsException, unicode)


if __name__ == "__main__":
    main()
