from PyObjCTools.TestSupport import TestCase
import SyncServices


class TestSyncServicesErrors(TestCase):
    def test_enums(self):
        # Unnamed enum:
        self.assertEqual(SyncServices.ISyncSessionClientAlreadySyncingError, 100)
        self.assertEqual(SyncServices.ISyncSessionUserCanceledSessionError, 101)
        self.assertEqual(SyncServices.ISyncSessionDriverRegistrationError, 200)
        self.assertEqual(SyncServices.ISyncSessionDriverPullFailureError, 201)
        self.assertEqual(SyncServices.ISyncSessionDriverFatalError, 300)

        # Unnamed enum:
        self.assertEqual(SyncServices.ISyncServerDisabledReasonNone, 1000)
        self.assertEqual(SyncServices.ISyncServerDisabledReasonByPreference, 1001)
        self.assertEqual(SyncServices.ISyncServerDisabledReasonSharedNetworkHome, 1002)
        self.assertEqual(SyncServices.ISyncServerDisabledReasonUnresponsive, 1003)
        self.assertEqual(SyncServices.ISyncServerDisabledReasonUnknown, 1004)

    def test_constants(self):
        self.assertIsInstance(SyncServices.ISyncErrorDomain, str)

        self.assertIsInstance(SyncServices.ISyncInvalidSchemaException, str)
        self.assertIsInstance(SyncServices.ISyncInvalidArgumentsException, str)
