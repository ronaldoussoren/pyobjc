from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit  # noqa: F401


class TestWKScriptMessageHandler(TestCase):
    @min_os_level("10.10")
    def testProtocols10_10(self):
        self.assertProtocolExists("WKScriptMessageHandler")
