from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKNavigationAction(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertEqual(WebKit.WKNavigationTypeLinkActivated, 0)
        self.assertEqual(WebKit.WKNavigationTypeFormSubmitted, 1)
        self.assertEqual(WebKit.WKNavigationTypeBackForward, 2)
        self.assertEqual(WebKit.WKNavigationTypeReload, 3)
        self.assertEqual(WebKit.WKNavigationTypeFormResubmitted, 4)
        self.assertEqual(WebKit.WKNavigationTypeOther, -1)
