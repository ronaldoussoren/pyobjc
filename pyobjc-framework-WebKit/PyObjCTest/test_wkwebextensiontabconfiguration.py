from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebExtensionTabConfiguration(TestCase):
    @min_os_level("15.4")
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.WKWebExtensionTabConfiguration.shouldBeActive)
        self.assertResultIsBOOL(
            WebKit.WKWebExtensionTabConfiguration.shouldAddToSelection
        )
        self.assertResultIsBOOL(WebKit.WKWebExtensionTabConfiguration.shouldBePinned)
        self.assertResultIsBOOL(WebKit.WKWebExtensionTabConfiguration.shouldBeMuted)
        self.assertResultIsBOOL(
            WebKit.WKWebExtensionTabConfiguration.shouldReaderModeBeActive
        )
