import BrowserEngineKit
from PyObjCTools.TestSupport import TestCase


class TestBERenderingProcess(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            BrowserEngineKit.BERenderingProcess.renderingProcessWithInterruptionHandler_completion_,
            0,
            b"v",
        )
        self.assertArgIsBlock(
            BrowserEngineKit.BERenderingProcess.renderingProcessWithInterruptionHandler_completion_,
            1,
            b"v@@",
        )

        self.assertArgIsOut(
            BrowserEngineKit.BERenderingProcess.makeLibXPCConnectionError_, 0
        )
