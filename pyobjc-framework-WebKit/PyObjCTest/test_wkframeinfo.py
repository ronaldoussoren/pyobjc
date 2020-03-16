from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit
import WebKit


class TestWKFrameInfo(TestCase):
    @onlyOn64Bit
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(WebKit.WKFrameInfo.isMainFrame)
