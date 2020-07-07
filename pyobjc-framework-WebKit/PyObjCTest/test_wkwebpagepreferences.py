from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWebPagePreferences(TestCase):
    def test_constants(self):
        self.assertEqual(WebKit.WKContentModeRecommended, 0)
        self.assertEqual(WebKit.WKContentModeMobile, 1)
        self.assertEqual(WebKit.WKContentModeDesktop, 2)

    @min_os_level("10.16")
    def test_methods10_16(self):
        self.assertResultIsBOOL(WebKit.WKWebpagePreferences.allowsContentJavaScript)
        self.assertArgIsBOOL(WebKit.WKWebpagePreferences.setAllowsContentJavaScript_, 0)
