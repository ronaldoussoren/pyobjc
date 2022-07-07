from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWebPagePreferences(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WKContentMode)

    def test_constants(self):
        self.assertEqual(WebKit.WKContentModeRecommended, 0)
        self.assertEqual(WebKit.WKContentModeMobile, 1)
        self.assertEqual(WebKit.WKContentModeDesktop, 2)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(WebKit.WKWebpagePreferences.allowsContentJavaScript)
        self.assertArgIsBOOL(WebKit.WKWebpagePreferences.setAllowsContentJavaScript_, 0)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(WebKit.WKWebpagePreferences.isLockdownModeEnabled)
        self.assertArgIsBOOL(WebKit.WKWebpagePreferences.setLockdownModeEnabled_, 0)
