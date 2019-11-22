from PyObjCTools.TestSupport import *

import AuthenticationServices


class TestASAuthorizationProvider(TestCase):
    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("ASAuthorizationProvider")

    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBlock(
            AuthenticationServices.ASAuthorizationProviderExtensionAuthorizationRequest.presentAuthorizationViewControllerWithCompletion_,
            0,
            b"vZ@",
        )
