from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebExtensionMatchPattern(TestCase):
    def test_constants(self):
        self.assertIsEnumType(WebKit.WKWebExtensionMatchPatternError)
        self.assertEqual(WebKit.WKWebExtensionMatchPatternErrorUnknown, 1)
        self.assertEqual(WebKit.WKWebExtensionMatchPatternErrorInvalidScheme, 2)
        self.assertEqual(WebKit.WKWebExtensionMatchPatternErrorInvalidHost, 3)
        self.assertEqual(WebKit.WKWebExtensionMatchPatternErrorInvalidPath, 4)

        self.assertIsEnumType(WebKit.WKWebExtensionMatchPatternOptions)
        self.assertEqual(WebKit.WKWebExtensionMatchPatternOptionsNone, 0)
        self.assertEqual(WebKit.WKWebExtensionMatchPatternOptionsIgnoreSchemes, 1 << 0)
        self.assertEqual(WebKit.WKWebExtensionMatchPatternOptionsIgnorePaths, 1 << 1)
        self.assertEqual(
            WebKit.WKWebExtensionMatchPatternOptionsMatchBidirectionally, 1 << 2
        )

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(WebKit.WKWebExtensionMatchPatternErrorDomain, str)

    @min_os_level("15.4")
    def test_methods(self):
        self.assertArgIsOut(WebKit.WKWebExtensionMatchPattern.initWithString_error_, 1)
        self.assertArgIsOut(
            WebKit.WKWebExtensionMatchPattern.initWithScheme_host_path_error_, 3
        )

        self.assertResultIsBOOL(WebKit.WKWebExtensionMatchPattern.matchesAllURLs)
        self.assertResultIsBOOL(WebKit.WKWebExtensionMatchPattern.matchesAllHosts)
        self.assertResultIsBOOL(WebKit.WKWebExtensionMatchPattern.matchesURL_)
        self.assertResultIsBOOL(WebKit.WKWebExtensionMatchPattern.matchesURL_options_)
        self.assertResultIsBOOL(WebKit.WKWebExtensionMatchPattern.matchesPattern_)
        self.assertResultIsBOOL(
            WebKit.WKWebExtensionMatchPattern.matchesPattern_options_
        )
