import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase


class TestBENetworkingProcess(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            BrowserEngineKit.BENetworkingProcess.networkProcessWithInterruptionHandler_completion_,
            0,
            b"v",
        )
        self.assertArgIsBlock(
            BrowserEngineKit.BENetworkingProcess.networkProcessWithInterruptionHandler_completion_,
            1,
            b"v@@",
        )

        self.assertArgIsOut(
            BrowserEngineKit.BENetworkingProcess.makeLibXPCConnectionError_, 0
        )
