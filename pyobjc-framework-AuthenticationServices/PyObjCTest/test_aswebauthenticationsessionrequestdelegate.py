from PyObjCTools.TestSupport import *

import AuthenticationServices


class TestASWebAuthenticationSessionRequestDelegate(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("ASWebAuthenticationSessionRequestDelegate")
