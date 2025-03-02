from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestWKWebExtensionContext(TestCase):
    def test_constants(self):
        self.assertIsEnumType(WebKit.WKWebExtensionContextError)
        self.assertEqual(WebKit.WKWebExtensionContextErrorUnknown, 1)
        self.assertEqual(WebKit.WKWebExtensionContextErrorAlreadyLoaded, 2)
        self.assertEqual(WebKit.WKWebExtensionContextErrorNotLoaded, 3)
        self.assertEqual(WebKit.WKWebExtensionContextErrorBaseURLAlreadyInUse, 4)
        self.assertEqual(WebKit.WKWebExtensionContextErrorNoBackgroundContent, 5)
        self.assertEqual(
            WebKit.WKWebExtensionContextErrorBackgroundContentFailedToLoad, 6
        )

        self.assertIsEnumType(WebKit.WKWebExtensionContextPermissionStatus)
        self.assertEqual(
            WebKit.WKWebExtensionContextPermissionStatusDeniedExplicitly, -3
        )
        self.assertEqual(
            WebKit.WKWebExtensionContextPermissionStatusDeniedImplicitly, -2
        )
        self.assertEqual(
            WebKit.WKWebExtensionContextPermissionStatusRequestedImplicitly, -1
        )
        self.assertEqual(WebKit.WKWebExtensionContextPermissionStatusUnknown, 0)
        self.assertEqual(
            WebKit.WKWebExtensionContextPermissionStatusRequestedExplicitly, 1
        )
        self.assertEqual(
            WebKit.WKWebExtensionContextPermissionStatusGrantedImplicitly, 2
        )
        self.assertEqual(
            WebKit.WKWebExtensionContextPermissionStatusGrantedExplicitly, 3
        )

        self.assertIsTypedEnum(WebKit.WKWebExtensionContextNotificationUserInfoKey, str)

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(
            WebKit.WKWebExtensionContextErrorsDidUpdateNotification, str
        )
        self.assertIsInstance(
            WebKit.WKWebExtensionContextPermissionsWereGrantedNotification, str
        )
        self.assertIsInstance(
            WebKit.WKWebExtensionContextPermissionsWereDeniedNotification, str
        )
        self.assertIsInstance(
            WebKit.WKWebExtensionContextGrantedPermissionsWereRemovedNotification, str
        )
        self.assertIsInstance(
            WebKit.WKWebExtensionContextDeniedPermissionsWereRemovedNotification, str
        )
        self.assertIsInstance(
            WebKit.WKWebExtensionContextPermissionMatchPatternsWereGrantedNotification,
            str,
        )
        self.assertIsInstance(
            WebKit.WKWebExtensionContextPermissionMatchPatternsWereDeniedNotification,
            str,
        )
        self.assertIsInstance(
            WebKit.WKWebExtensionContextGrantedPermissionMatchPatternsWereRemovedNotification,
            str,
        )
        self.assertIsInstance(
            WebKit.WKWebExtensionContextDeniedPermissionMatchPatternsWereRemovedNotification,
            str,
        )
        self.assertIsInstance(
            WebKit.WKWebExtensionContextNotificationUserInfoKeyMatchPatterns, str
        )

    @min_os_level("15.4")
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.isLoaded)
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.isInspectable)
        self.assertResultIsBOOL(
            WebKit.WKWebExtensionContext.hasRequestedOptionalAccessToAllHosts
        )
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.hasAccessToPrivateData)
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.hasPermission_)
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.hasPermission_inTab_)
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.hasAccessToURL_)
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.hasAccessToURL_inTab_)
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.hasAccessToAllURLs)
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.hasAccessToAllHosts)
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.hasInjectedContent)
        self.assertResultIsBOOL(
            WebKit.WKWebExtensionContext.hasContentModificationRules
        )

        self.assertArgIsBlock(
            WebKit.WKWebExtensionContext.loadBackgroundContentWithCompletionHandler_,
            0,
            b"v@",
        )

        self.assertResultIsBOOL(
            WebKit.WKWebExtensionContext.performCommandForKeyCommand_
        )
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.performCommandForEvent_)
        self.assertResultIsBOOL(WebKit.WKWebExtensionContext.hasActiveUserGestureInTab_)

        self.assertArgIsBOOL(
            WebKit.WKWebExtensionContext.didCloseTab_windowIsClosing_, 1
        )
