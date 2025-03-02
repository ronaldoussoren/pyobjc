from PyObjCTools.TestSupport import TestCase, min_sdk_level
import WebKit


class TestWKWebExtensionWindowHelper(WebKit.NSObject):
    def setWindowState_forWebExtensionContext_completionHandler_(self, a, b, c):
        pass

    def isPrivateForWebExtensionContext_(self, a):
        pass

    def screenFrameForWebExtensionContext_(self, a):
        return 1

    def frameForWebExtensionContext_(self, a):
        return 1

    def setFrame_forWebExtensionContext_completionHandler_(self, a, b, c):
        pass

    def focusForWebExtensionContext_completionHandler_(self, a, b):
        pass

    def closeForWebExtensionContext_completionHandler_(self, a, b):
        pass


class TestWKWebExtensionWindow(TestCase):
    def test_constants(self):
        self.assertIsEnumType(WebKit.WKWebExtensionWindowType)
        self.assertEqual(WebKit.WKWebExtensionWindowTypeNormal, 0)
        self.assertEqual(WebKit.WKWebExtensionWindowTypePopup, 1)

        self.assertIsEnumType(WebKit.WKWebExtensionWindowState)
        self.assertEqual(WebKit.WKWebExtensionWindowStateNormal, 0)
        self.assertEqual(WebKit.WKWebExtensionWindowStateMinimized, 1)
        self.assertEqual(WebKit.WKWebExtensionWindowStateMaximized, 2)
        self.assertEqual(WebKit.WKWebExtensionWindowStateFullscreen, 3)

    @min_sdk_level("15.4")
    def test_protocols(self):
        self.assertProtocolExists("WKWebExtensionWindow")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestWKWebExtensionWindowHelper.setWindowState_forWebExtensionContext_completionHandler_,
            2,
            b"v@",
        )
        self.assertResultIsBOOL(
            TestWKWebExtensionWindowHelper.isPrivateForWebExtensionContext_
        )
        self.assertResultHasType(
            TestWKWebExtensionWindowHelper.screenFrameForWebExtensionContext_,
            WebKit.CGRect.__typestr__,
        )
        self.assertResultHasType(
            TestWKWebExtensionWindowHelper.frameForWebExtensionContext_,
            WebKit.CGRect.__typestr__,
        )

        self.assertArgHasType(
            TestWKWebExtensionWindowHelper.setFrame_forWebExtensionContext_completionHandler_,
            0,
            WebKit.CGRect.__typestr__,
        )
        self.assertArgIsBlock(
            TestWKWebExtensionWindowHelper.setFrame_forWebExtensionContext_completionHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            TestWKWebExtensionWindowHelper.focusForWebExtensionContext_completionHandler_,
            1,
            b"v@",
        )

        self.assertArgIsBlock(
            TestWKWebExtensionWindowHelper.closeForWebExtensionContext_completionHandler_,
            1,
            b"v@",
        )
