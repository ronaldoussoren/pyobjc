import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase


class TestBEProcessHelper(BrowserEngineKit.NSObject):
    def isValid(self):
        return 1


class TestBEProcess(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("BEProcessCapabilityGrant")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestBEProcessHelper.isValid)

    def test_methods(self):
        self.assertArgIsOut(
            BrowserEngineKit.BEMediaEnvironment.initWithXPCRepresentation_error_, 1
        )

        self.assertResultIsBOOL(BrowserEngineKit.BEMediaEnvironment.activateWithError_)
        self.assertArgIsOut(BrowserEngineKit.BEMediaEnvironment.activateWithError_, 0)

        self.assertResultIsBOOL(BrowserEngineKit.BEMediaEnvironment.suspendWithError_)
        self.assertArgIsOut(BrowserEngineKit.BEMediaEnvironment.suspendWithError_, 0)

        self.assertArgIsOut(
            BrowserEngineKit.BEMediaEnvironment.makeCaptureSessionWithError_, 0
        )

        self.assertArgIsOut(BrowserEngineKit.BEProcessCapability.requestWithError_, 0)

        self.assertArgIsOut(
            BrowserEngineKit.BEWebContentProcess.grantCapability_error_, 1
        )
        self.assertArgIsOut(
            BrowserEngineKit.BERenderingProcess.grantCapability_error_, 1
        )
        self.assertArgIsOut(
            BrowserEngineKit.BENetworkingProcess.grantCapability_error_, 1
        )
