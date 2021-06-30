from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKFindResult(TestCase):
    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(WebKit.WKFindResult.matchFound)
