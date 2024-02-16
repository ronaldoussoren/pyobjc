import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase, expectedFailure


class TestBEProcessHelper(BrowserEngineKit.NSObject):
    def isValid(self):
        return 1


class TestBEProcess(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("BEProcessCapabilityGrant")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestBEProcessHelper.isValid)

    @expectedFailure
    def test_methods(self):
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
