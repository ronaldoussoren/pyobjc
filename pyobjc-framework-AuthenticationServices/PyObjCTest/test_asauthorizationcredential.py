from PyObjCTools.TestSupport import *

import AuthenticationServices

class TestASAuthorizationCredential (TestCase):

    @min_sdk_version('10.15')
    def test_protocols(self):
        objc.protocolNamed('ASAuthorizationCredential')
