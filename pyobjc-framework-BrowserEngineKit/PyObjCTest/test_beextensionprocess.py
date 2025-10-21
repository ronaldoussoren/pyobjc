from PyObjCTools.TestSupport import TestCase, min_sdk_level
import BrowserEngineKit


class TestBEExtensionProcessHelper(BrowserEngineKit.NSObject):
    def makeLibXPCConnectionError_(self, a):
        return 1


class TestBEExtensionProcess(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("BEExtensionProcess")

    def test_protocol_methods(self):
        self.assertArgIsOut(TestBEExtensionProcessHelper.makeLibXPCConnectionError_, 0)
