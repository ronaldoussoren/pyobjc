import AuthenticationServices
from PyObjCTools.TestSupport import TestCase


class TestASAuthorizationAppleIDCredential(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AuthenticationServices.ASUserDetectionStatus)
        self.assertEqual(AuthenticationServices.ASUserDetectionStatusUnsupported, 0)
        self.assertEqual(AuthenticationServices.ASUserDetectionStatusUnknown, 1)
        self.assertEqual(AuthenticationServices.ASUserDetectionStatusLikelyReal, 2)

        self.assertIsEnumType(AuthenticationServices.ASUserAgeRange)
        self.assertEqual(AuthenticationServices.ASUserAgeRangeUnknown, 0)
        self.assertEqual(AuthenticationServices.ASUserAgeRangeChild, 1)
        self.assertEqual(AuthenticationServices.ASUserAgeRangeNotChild, 2)
