from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKPaymentInformationEventExtensionHelper(PassKit.NSObject):
    def handleInformationRequest_completion_(self, a, b):
        pass

    def handleSignatureRequest_completion_(self, a, b):
        pass

    def handleConfigurationRequest_completion_(self, a, b):
        pass


class TestPKPaymentInformationEventExtension(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("PKPaymentInformationRequestHandling")

    def test_methods(self):
        self.assertArgIsBlock(
            TestPKPaymentInformationEventExtensionHelper.handleInformationRequest_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKPaymentInformationEventExtensionHelper.handleSignatureRequest_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            TestPKPaymentInformationEventExtensionHelper.handleConfigurationRequest_completion_,
            1,
            b"v",
        )
