from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit
import WebKit


class TestWKNavigationResponse(TestCase):
    @onlyOn64Bit
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(WebKit.WKNavigationResponse.isForMainFrame)
        self.assertResultIsBOOL(WebKit.WKNavigationResponse.canShowMIMEType)
