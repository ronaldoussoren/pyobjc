from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebExtensionPermission(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(WebKit.WKWebExtensionPermission, str)

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(WebKit.WKWebExtensionPermissionActiveTab, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionAlarms, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionClipboardWrite, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionContextMenus, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionCookies, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionDeclarativeNetRequest, str)
        self.assertIsInstance(
            WebKit.WKWebExtensionPermissionDeclarativeNetRequestFeedback, str
        )
        self.assertIsInstance(
            WebKit.WKWebExtensionPermissionDeclarativeNetRequestWithHostAccess, str
        )
        self.assertIsInstance(WebKit.WKWebExtensionPermissionMenus, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionNativeMessaging, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionScripting, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionStorage, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionTabs, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionUnlimitedStorage, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionWebNavigation, str)
        self.assertIsInstance(WebKit.WKWebExtensionPermissionWebRequest, str)
