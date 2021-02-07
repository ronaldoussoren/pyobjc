from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKFindConfiguration(TestCase):
    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertResultIsBOOL(WebKit.WKFindConfiguration.backwards)
        self.assertArgIsBOOL(WebKit.WKFindConfiguration.setBackwards_, 0)

        self.assertResultIsBOOL(WebKit.WKFindConfiguration.caseSensitive)
        self.assertArgIsBOOL(WebKit.WKFindConfiguration.setCaseSensitive_, 0)

        self.assertResultIsBOOL(WebKit.WKFindConfiguration.wraps)
        self.assertArgIsBOOL(WebKit.WKFindConfiguration.setWraps_, 0)
