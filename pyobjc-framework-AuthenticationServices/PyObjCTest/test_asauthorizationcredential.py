import AuthenticationServices  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestASAuthorizationCredential(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("ASAuthorizationCredential")
