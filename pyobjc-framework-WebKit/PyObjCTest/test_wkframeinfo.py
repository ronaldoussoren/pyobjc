from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKFrameInfo(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(WebKit.WKFrameInfo.isMainFrame)
