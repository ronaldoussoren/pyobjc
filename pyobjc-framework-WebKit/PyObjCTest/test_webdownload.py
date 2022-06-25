from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit  # noqa: F401


class TestWebDownload(TestCase):
    @min_sdk_level("10.11")
    def testProtocols(self):
        self.assertProtocolExists("WebDownloadDelegate")
