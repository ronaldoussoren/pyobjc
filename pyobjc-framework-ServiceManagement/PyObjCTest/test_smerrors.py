from PyObjCTools.TestSupport import TestCase
import ServiceManagement


class TestSMErrors(TestCase):
    def test_enums(self):
        # Unnamed enum:
        self.assertEqual(ServiceManagement.kSMErrorInternalFailure, 2)
        self.assertEqual(ServiceManagement.kSMErrorInvalidSignature, 3)
        self.assertEqual(ServiceManagement.kSMErrorAuthorizationFailure, 4)
        self.assertEqual(ServiceManagement.kSMErrorToolNotValid, 5)
        self.assertEqual(ServiceManagement.kSMErrorJobNotFound, 6)
        self.assertEqual(ServiceManagement.kSMErrorServiceUnavailable, 7)
        self.assertEqual(ServiceManagement.kSMErrorJobPlistNotFound, 8)
        self.assertEqual(ServiceManagement.kSMErrorJobMustBeEnabled, 9)
        self.assertEqual(ServiceManagement.kSMErrorInvalidPlist, 10)
        self.assertEqual(ServiceManagement.kSMErrorLaunchDeniedByUser, 11)
        self.assertEqual(ServiceManagement.kSMErrorAlreadyRegistered, 12)

    def test_constants(self):
        self.assertIsInstance(ServiceManagement.kSMErrorDomainIPC, str)
        self.assertIsInstance(ServiceManagement.kSMErrorDomainFramework, str)
        self.assertIsInstance(ServiceManagement.kSMErrorDomainLaunchd, str)
