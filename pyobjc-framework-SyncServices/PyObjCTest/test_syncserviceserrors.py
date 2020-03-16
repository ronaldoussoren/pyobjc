from PyObjCTools.TestSupport import TestCase, min_os_level
import SyncServices


class TestSyncServicesErrors(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(SyncServices.ISyncErrorDomain, str)

        self.assertEqual(SyncServices.ISyncSessionClientAlreadySyncingError, 100)
        self.assertEqual(SyncServices.ISyncSessionUserCanceledSessionError, 101)
        self.assertEqual(SyncServices.ISyncSessionDriverRegistrationError, 200)
        self.assertEqual(SyncServices.ISyncSessionDriverPullFailureError, 201)
        self.assertEqual(SyncServices.ISyncSessionDriverFatalError, 300)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(SyncServices.ISyncServerDisabledReasonNone, 1000)
        self.assertEqual(SyncServices.ISyncServerDisabledReasonByPreference, 1001)
        self.assertEqual(SyncServices.ISyncServerDisabledReasonSharedNetworkHome, 1002)
        self.assertEqual(SyncServices.ISyncServerDisabledReasonUnresponsive, 1003)
        self.assertEqual(SyncServices.ISyncServerDisabledReasonUnknown, 1004)

        self.assertIsInstance(SyncServices.ISyncInvalidSchemaException, str)
        self.assertIsInstance(SyncServices.ISyncInvalidArgumentsException, str)
