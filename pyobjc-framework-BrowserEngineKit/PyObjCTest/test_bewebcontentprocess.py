import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase


class TestBEWebContentProcess(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            BrowserEngineKit.BEWebContentProcess.webContentProcessWithInterruptionHandler_completion_,
            0,
            b"v",
        )
        self.assertArgIsBlock(
            BrowserEngineKit.BEWebContentProcess.webContentProcessWithInterruptionHandler_completion_,
            1,
            b"v@@",
        )

        self.assertArgIsOut(
            BrowserEngineKit.BEWebContentProcess.makeLibXPCConnectionError_, 0
        )
