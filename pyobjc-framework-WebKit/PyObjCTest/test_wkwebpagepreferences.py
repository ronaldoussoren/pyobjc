from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebPagePreferences(TestCase):
    def test_constants(self):
        self.assertEqual(WebKit.WKContentModeRecommended, 0)
        self.assertEqual(WebKit.WKContentModeMobile, 1)
        self.assertEqual(WebKit.WKContentModeDesktop, 2)
