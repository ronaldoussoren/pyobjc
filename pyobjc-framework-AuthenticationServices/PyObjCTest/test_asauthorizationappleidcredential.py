import AuthenticationServices
from PyObjCTools.TestSupport import TestCase


class TestASAuthorizationAppleIDCredential(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AuthenticationServices.ASUserDetectionStatus)

    def test_constants(self):
        self.assertEqual(AuthenticationServices.ASUserDetectionStatusUnsupported, 0)
        self.assertEqual(AuthenticationServices.ASUserDetectionStatusUnknown, 1)
        self.assertEqual(AuthenticationServices.ASUserDetectionStatusLikelyReal, 2)
