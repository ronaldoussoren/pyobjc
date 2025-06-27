from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebExtensionAction(TestCase):
    @min_os_level("15.4")
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.WKWebExtensionAction.hasUnreadBadgeText)
        self.assertResultIsBOOL(WebKit.WKWebExtensionAction.isEnabled)
        self.assertResultIsBOOL(WebKit.WKWebExtensionAction.presentsPopup)
