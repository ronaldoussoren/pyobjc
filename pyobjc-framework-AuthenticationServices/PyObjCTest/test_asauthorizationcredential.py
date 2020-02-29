import AuthenticationServices
from PyObjCTools.TestSupport import *


class TestASAuthorizationCredential(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("ASAuthorizationCredential")
