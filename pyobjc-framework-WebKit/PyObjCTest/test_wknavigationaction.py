from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKNavigationAction(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WKNavigationType)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertEqual(WebKit.WKNavigationTypeLinkActivated, 0)
        self.assertEqual(WebKit.WKNavigationTypeFormSubmitted, 1)
        self.assertEqual(WebKit.WKNavigationTypeBackForward, 2)
        self.assertEqual(WebKit.WKNavigationTypeReload, 3)
        self.assertEqual(WebKit.WKNavigationTypeFormResubmitted, 4)
        self.assertEqual(WebKit.WKNavigationTypeOther, -1)

    @min_os_level("11.3")
    def test_methods11_3(self):
        self.assertResultIsBOOL(WebKit.WKNavigationAction.shouldPerformDownload)

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultIsBOOL(WebKit.WKNavigationAction.isContentRuleListRedirect)
