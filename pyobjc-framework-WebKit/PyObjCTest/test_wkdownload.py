from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKDownload(TestCase):
    @min_os_level("10.16")
    def testMethods(self):
        self.assertArgIsBlock(
            WebKit.WKDownload.cancel_,
            0,
            b"v@",
        )
