from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKDownload(TestCase):
    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertArgIsBlock(
            WebKit.WKDownload.cancel_,
            0,
            b"v@",
        )

    @min_os_level("15.2")
    def testMethods15_2(self):
        self.assertResultIsBOOL(WebKit.WKDownload.isUserInitiated)
