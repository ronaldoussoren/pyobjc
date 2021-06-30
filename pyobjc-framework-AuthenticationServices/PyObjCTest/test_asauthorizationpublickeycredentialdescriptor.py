import AuthenticationServices  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestASAuthorizationPublicKeyCredentialDescriptor(TestCase):
    @min_sdk_level("12.0")
    def test_protocols(self):
        objc.protocolNamed("ASAuthorizationPublicKeyCredentialDescriptor")
