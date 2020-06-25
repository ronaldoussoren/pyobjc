from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKFindResult(TestCase):
    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertResultIsBOOL(WebKit.WKFindResult.matchFound)
