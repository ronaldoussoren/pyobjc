from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebExtensionWindowConfiguration(TestCase):
    @min_os_level("15.4")
    def test_methods(self):
        self.assertResultIsBOOL(
            WebKit.WKWebExtensionWindowConfiguration.shouldBeFocused
        )
        self.assertResultIsBOOL(
            WebKit.WKWebExtensionWindowConfiguration.shouldBePrivate
        )
