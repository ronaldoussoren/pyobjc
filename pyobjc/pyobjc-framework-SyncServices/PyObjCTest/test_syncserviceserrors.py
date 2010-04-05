
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestSyncServicesErrors (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(ISyncErrorDomain, unicode)

        self.assertEqual(ISyncSessionClientAlreadySyncingError, 100)
        self.assertEqual(ISyncSessionUserCanceledSessionError, 101)
        self.assertEqual(ISyncSessionDriverRegistrationError, 200)
        self.assertEqual(ISyncSessionDriverPullFailureError, 201)
        self.assertEqual(ISyncSessionDriverFatalError, 300)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(ISyncServerDisabledReasonNone, 1000)
        self.assertEqual(ISyncServerDisabledReasonByPreference, 1001)
        self.assertEqual(ISyncServerDisabledReasonSharedNetworkHome, 1002)
        self.assertEqual(ISyncServerDisabledReasonUnresponsive, 1003)
        self.assertEqual(ISyncServerDisabledReasonUnknown, 1004)

        self.assertIsInstance(ISyncInvalidSchemaException, unicode)
        self.assertIsInstance(ISyncInvalidArgumentsException, unicode)


if __name__ == "__main__":
    main()
