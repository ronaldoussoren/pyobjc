from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level, cast_uint
import WebKit
import objc

UINT_MAX = cast_uint(-1)


class TestWebUIDelegateHelper(WebKit.NSObject):
    def webView_willPerformDragDestinationAction_forDraggingInfo_(self, wv, a, i):
        pass

    def webViewAreToolbarsVisible_(self, a):
        return 1

    def webView_setToolbarsVisible_(self, a, b):
        pass

    def webViewIsStatusBarVisible_(self, a):
        return 1

    def webView_setStatusBarVisible_(self, a, b):
        pass

    def webViewIsResizable_(self, a):
        return 1

    def webView_setResizable_(self, a, b):
        pass

    def webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_(self, a, b, c):
        return 1

    def webView_runBeforeUnloadConfirmPanelWithMessage_initiatedByFrame_(self, a, b, c):
        return 1

    def webView_mouseDidMoveOverElement_modifierFlags_(self, a, b, c):
        pass

    def webView_validateUserInterfaceItem_defaultValidation_(self, a, b, c):
        return 1

    def webView_shouldPerformAction_fromSender_(self, a, b, c):
        return 1

    def webView_dragDestinationActionMaskForDraggingInfo_(self, a, b):
        return 1

    def webView_dragSourceActionMaskForPoint_(self, a, b):
        return 1

    def webView_willPerformDragSourceAction_fromPoint_withPasteboard_(self, a, b, c, d):
        pass

    def webView_printFrameView_(self, a, b):
        pass

    def webViewHeaderHeight_(self, a):
        return 1

    def webViewFooterHeight_(self, a):
        return 1

    def webView_drawHeaderInRect_(self, a, b):
        pass

    def webView_drawFooterInRect_(self, a, b):
        pass

    def webView_runJavaScriptConfirmPanelWithMessage_(self, a, b):
        return 1

    def webView_setContentRect_(self, a, b):
        pass

    def webViewContentRect_(self, a):
        return 1

    def webView_runOpenPanelForFileButtonWithResultListener_allowMultipleFiles_(
        self, a, b, c
    ):
        pass


class TestWebUIDelegate(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(WebKit.WebDragDestinationAction)
        self.assertIsEnumType(WebKit.WebDragSourceAction)

    def testConstants(self):
        self.assertEqual(WebKit.WebMenuItemTagOpenLinkInNewWindow, 1)
        self.assertEqual(WebKit.WebMenuItemTagDownloadLinkToDisk, 2)
        self.assertEqual(WebKit.WebMenuItemTagCopyLinkToClipboard, 3)
        self.assertEqual(WebKit.WebMenuItemTagOpenImageInNewWindow, 4)
        self.assertEqual(WebKit.WebMenuItemTagDownloadImageToDisk, 5)
        self.assertEqual(WebKit.WebMenuItemTagCopyImageToClipboard, 6)
        self.assertEqual(WebKit.WebMenuItemTagOpenFrameInNewWindow, 7)
        self.assertEqual(WebKit.WebMenuItemTagCopy, 8)
        self.assertEqual(WebKit.WebMenuItemTagGoBack, 9)
        self.assertEqual(WebKit.WebMenuItemTagGoForward, 10)
        self.assertEqual(WebKit.WebMenuItemTagStop, 11)
        self.assertEqual(WebKit.WebMenuItemTagReload, 12)
        self.assertEqual(WebKit.WebMenuItemTagCut, 13)
        self.assertEqual(WebKit.WebMenuItemTagPaste, 14)
        self.assertEqual(WebKit.WebMenuItemTagSpellingGuess, 15)
        self.assertEqual(WebKit.WebMenuItemTagNoGuessesFound, 16)
        self.assertEqual(WebKit.WebMenuItemTagIgnoreSpelling, 17)
        self.assertEqual(WebKit.WebMenuItemTagLearnSpelling, 18)
        self.assertEqual(WebKit.WebMenuItemTagOther, 19)
        self.assertEqual(WebKit.WebMenuItemTagSearchInSpotlight, 20)
        self.assertEqual(WebKit.WebMenuItemTagSearchWeb, 21)
        self.assertEqual(WebKit.WebMenuItemTagLookUpInDictionary, 22)
        self.assertEqual(WebKit.WebMenuItemTagOpenWithDefaultApplication, 23)
        self.assertEqual(WebKit.WebMenuItemPDFActualSize, 24)
        self.assertEqual(WebKit.WebMenuItemPDFZoomIn, 25)
        self.assertEqual(WebKit.WebMenuItemPDFZoomOut, 26)
        self.assertEqual(WebKit.WebMenuItemPDFAutoSize, 27)
        self.assertEqual(WebKit.WebMenuItemPDFSinglePage, 28)
        self.assertEqual(WebKit.WebMenuItemPDFFacingPages, 29)
        self.assertEqual(WebKit.WebMenuItemPDFContinuous, 30)
        self.assertEqual(WebKit.WebMenuItemPDFNextPage, 31)
        self.assertEqual(WebKit.WebMenuItemPDFPreviousPage, 32)

        self.assertEqual(WebKit.WebDragDestinationActionNone, 0)
        self.assertEqual(WebKit.WebDragDestinationActionDHTML, 1)
        self.assertEqual(WebKit.WebDragDestinationActionEdit, 2)
        self.assertEqual(WebKit.WebDragDestinationActionLoad, 4)
        self.assertEqual(WebKit.WebDragDestinationActionAny, UINT_MAX)

        self.assertEqual(WebKit.WebDragSourceActionNone, 0)
        self.assertEqual(WebKit.WebDragSourceActionDHTML, 1)
        self.assertEqual(WebKit.WebDragSourceActionImage, 2)
        self.assertEqual(WebKit.WebDragSourceActionLink, 4)
        self.assertEqual(WebKit.WebDragSourceActionSelection, 8)
        self.assertEqual(WebKit.WebDragSourceActionAny, UINT_MAX)

    def testProtocols(self):
        objc.protocolNamed("WebOpenPanelResultListener")

    @min_sdk_level("10.11")
    def testProtocols10_11(self):
        objc.protocolNamed("WebUIDelegate")

    def testMethods(self):
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webViewAreToolbarsVisible_)
        self.assertArgIsBOOL(TestWebUIDelegateHelper.webView_setToolbarsVisible_, 1)
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webViewIsStatusBarVisible_)
        self.assertArgIsBOOL(TestWebUIDelegateHelper.webView_setStatusBarVisible_, 1)
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webViewIsResizable_)
        self.assertArgIsBOOL(TestWebUIDelegateHelper.webView_setResizable_, 1)
        self.assertResultIsBOOL(
            TestWebUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_  # noqa: B950
        )
        self.assertResultIsBOOL(
            TestWebUIDelegateHelper.webView_runBeforeUnloadConfirmPanelWithMessage_initiatedByFrame_  # noqa: B950
        )
        self.assertArgHasType(
            TestWebUIDelegateHelper.webView_mouseDidMoveOverElement_modifierFlags_,
            2,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestWebUIDelegateHelper.webView_validateUserInterfaceItem_defaultValidation_
        )
        self.assertArgIsBOOL(
            TestWebUIDelegateHelper.webView_validateUserInterfaceItem_defaultValidation_,
            2,
        )
        self.assertResultIsBOOL(
            TestWebUIDelegateHelper.webView_shouldPerformAction_fromSender_
        )
        self.assertResultHasType(
            TestWebUIDelegateHelper.webView_dragDestinationActionMaskForDraggingInfo_,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestWebUIDelegateHelper.webView_dragSourceActionMaskForPoint_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestWebUIDelegateHelper.webView_willPerformDragSourceAction_fromPoint_withPasteboard_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestWebUIDelegateHelper.webView_willPerformDragSourceAction_fromPoint_withPasteboard_,  # noqa: B950
            2,
            WebKit.NSPoint.__typestr__,
        )
        self.assertResultHasType(
            TestWebUIDelegateHelper.webViewHeaderHeight_, objc._C_FLT
        )
        self.assertResultHasType(
            TestWebUIDelegateHelper.webViewFooterHeight_, objc._C_FLT
        )
        self.assertArgHasType(
            TestWebUIDelegateHelper.webView_drawHeaderInRect_,
            1,
            WebKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestWebUIDelegateHelper.webView_drawFooterInRect_,
            1,
            WebKit.NSRect.__typestr__,
        )
        self.assertResultIsBOOL(
            TestWebUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_
        )
        self.assertArgHasType(
            TestWebUIDelegateHelper.webView_setContentRect_,
            1,
            WebKit.NSRect.__typestr__,
        )
        self.assertResultHasType(
            TestWebUIDelegateHelper.webViewContentRect_, WebKit.NSRect.__typestr__
        )
        self.assertArgHasType(
            TestWebUIDelegateHelper.webView_willPerformDragDestinationAction_forDraggingInfo_,
            1,
            objc._C_NSUInteger,
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgIsBOOL(
            TestWebUIDelegateHelper.webView_runOpenPanelForFileButtonWithResultListener_allowMultipleFiles_,  # noqa: B950
            2,
        )
        self.assertResultIsBOOL(
            TestWebUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_
        )
