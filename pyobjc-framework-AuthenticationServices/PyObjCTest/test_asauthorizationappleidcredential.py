from PyObjCTools.TestSupport import *

import AuthenticationServices


class TestASAuthorizationAppleIDCredential(TestCase):
    def test_constants(self):
        self.assertEqual(AuthenticationServices.ASUserDetectionStatusUnsupported, 0)
        self.assertEqual(AuthenticationServices.ASUserDetectionStatusUnknown, 1)
        self.assertEqual(AuthenticationServices.ASUserDetectionStatusLikelyReal, 2)
