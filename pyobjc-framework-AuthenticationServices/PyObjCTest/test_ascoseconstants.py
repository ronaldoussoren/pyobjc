import AuthenticationServices
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestASCOSEConstants(TestCase):
    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertEqual(AuthenticationServices.ASCOSEAlgorithmIdentifierES256, -7)

        self.assertEqual(AuthenticationServices.ASCOSEEllipticCurveIdentifierP256, 1)
