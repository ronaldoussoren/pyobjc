
from PyObjCTools.TestSupport import *
from WebKit import *

import sys
UINT_MAX = -1

class TestWebUIDelegateHelper (NSObject):
    def webViewAreToolbarsVisible_(self, a): return 1
    def webView_setToolbarsVisible_(self, a, b): pass
    def webViewIsStatusBarVisible_(self, a): return 1
    def webView_setStatusBarVisible_(self, a, b): pass
    def webViewIsResizable_(self, a): return 1
    def webView_setResizable_(self, a, b): pass
    def webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_(self, a, b, c): return 1
    def webView_runBeforeUnloadConfirmPanelWithMessage_initiatedByFrame_(self, a, b, c): return 1
    def webView_mouseDidMoveOverElement_modifierFlags_(self, a, b, c): pass
    def webView_validateUserInterfaceItem_defaultValidation_(self, a, b, c): return 1
    def webView_shouldPerformAction_fromSender_(self, a, b, c): return 1
    def webView_dragDestinationActionMaskForDraggingInfo_(self, a, b): return 1
    def webView_dragSourceActionMaskForPoint_(self, a, b): return 1
    def webView_willPerformDragSourceAction_fromPoint_withPasteboard_(self, a, b, c, d): pass
    def webView_printFrameView_(self, a, b): pass
    def webViewHeaderHeight_(self, a): return 1
    def webViewFooterHeight_(self, a): return 1
    def webView_drawHeaderInRect_(self, a, b): pass
    def webView_drawFooterInRect_(self, a, b): pass
    def webView_runJavaScriptConfirmPanelWithMessage_(self, a, b): return 1
    def webView_setContentRect_(self, a, b): pass
    def webViewContentRect_(self, a): return 1

    def webView_runOpenPanelForFileButtonWithResultListener_allowMultipleFiles_(self, a, b, c): pass
    def webView_runJavaScriptConfirmPanelWithMessage_(self, a, b): return 1


class TestWebUIDelegate (TestCase):
    def testConstants(self):
        self.assertEqual(WebMenuItemTagOpenLinkInNewWindow, 1)
        self.assertEqual(WebMenuItemTagDownloadLinkToDisk, 2)
        self.assertEqual(WebMenuItemTagCopyLinkToClipboard, 3)
        self.assertEqual(WebMenuItemTagOpenImageInNewWindow, 4)
        self.assertEqual(WebMenuItemTagDownloadImageToDisk, 5)
        self.assertEqual(WebMenuItemTagCopyImageToClipboard, 6)
        self.assertEqual(WebMenuItemTagOpenFrameInNewWindow, 7)
        self.assertEqual(WebMenuItemTagCopy, 8)
        self.assertEqual(WebMenuItemTagGoBack, 9)
        self.assertEqual(WebMenuItemTagGoForward, 10)
        self.assertEqual(WebMenuItemTagStop, 11)
        self.assertEqual(WebMenuItemTagReload, 12)
        self.assertEqual(WebMenuItemTagCut, 13)
        self.assertEqual(WebMenuItemTagPaste, 14)
        self.assertEqual(WebMenuItemTagSpellingGuess, 15)
        self.assertEqual(WebMenuItemTagNoGuessesFound, 16)
        self.assertEqual(WebMenuItemTagIgnoreSpelling, 17)
        self.assertEqual(WebMenuItemTagLearnSpelling, 18)
        self.assertEqual(WebMenuItemTagOther, 19)
        self.assertEqual(WebMenuItemTagSearchInSpotlight, 20)
        self.assertEqual(WebMenuItemTagSearchWeb, 21)
        self.assertEqual(WebMenuItemTagLookUpInDictionary, 22)
        self.assertEqual(WebMenuItemTagOpenWithDefaultApplication, 23)
        self.assertEqual(WebMenuItemPDFActualSize, 24)
        self.assertEqual(WebMenuItemPDFZoomIn, 25)
        self.assertEqual(WebMenuItemPDFZoomOut, 26)
        self.assertEqual(WebMenuItemPDFAutoSize, 27)
        self.assertEqual(WebMenuItemPDFSinglePage, 28)
        self.assertEqual(WebMenuItemPDFFacingPages, 29)
        self.assertEqual(WebMenuItemPDFContinuous, 30)
        self.assertEqual(WebMenuItemPDFNextPage, 31)
        self.assertEqual(WebMenuItemPDFPreviousPage, 32)

        self.assertEqual(WebDragDestinationActionNone, 0)
        self.assertEqual(WebDragDestinationActionDHTML, 1)
        self.assertEqual(WebDragDestinationActionEdit, 2)
        self.assertEqual(WebDragDestinationActionLoad, 4)
        self.assertEqual(WebDragDestinationActionAny, UINT_MAX)

        self.assertEqual(WebDragSourceActionNone, 0)
        self.assertEqual(WebDragSourceActionDHTML, 1)
        self.assertEqual(WebDragSourceActionImage, 2)
        self.assertEqual(WebDragSourceActionLink, 4)
        self.assertEqual(WebDragSourceActionSelection, 8)
        self.assertEqual(WebDragSourceActionAny, UINT_MAX)


    def testMethods(self):
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webViewAreToolbarsVisible_)
        self.assertArgIsBOOL(TestWebUIDelegateHelper.webView_setToolbarsVisible_, 1)
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webViewIsStatusBarVisible_)
        self.assertArgIsBOOL(TestWebUIDelegateHelper.webView_setStatusBarVisible_, 1)
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webViewIsResizable_)
        self.assertArgIsBOOL(TestWebUIDelegateHelper.webView_setResizable_, 1)
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_)
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webView_runBeforeUnloadConfirmPanelWithMessage_initiatedByFrame_)
        self.assertArgHasType(TestWebUIDelegateHelper.webView_mouseDidMoveOverElement_modifierFlags_, 2, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webView_validateUserInterfaceItem_defaultValidation_)
        self.assertArgIsBOOL(TestWebUIDelegateHelper.webView_validateUserInterfaceItem_defaultValidation_, 2)
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webView_shouldPerformAction_fromSender_)
        self.assertResultHasType(TestWebUIDelegateHelper.webView_dragDestinationActionMaskForDraggingInfo_, objc._C_NSUInteger)
        self.assertResultHasType(TestWebUIDelegateHelper.webView_dragSourceActionMaskForPoint_, objc._C_NSUInteger)
        self.assertArgHasType(TestWebUIDelegateHelper.webView_willPerformDragSourceAction_fromPoint_withPasteboard_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestWebUIDelegateHelper.webView_willPerformDragSourceAction_fromPoint_withPasteboard_, 2, NSPoint.__typestr__)
        self.assertResultHasType(TestWebUIDelegateHelper.webViewHeaderHeight_, objc._C_FLT)
        self.assertResultHasType(TestWebUIDelegateHelper.webViewFooterHeight_, objc._C_FLT)
        self.assertArgHasType(TestWebUIDelegateHelper.webView_drawHeaderInRect_, 1, NSRect.__typestr__)
        self.assertArgHasType(TestWebUIDelegateHelper.webView_drawFooterInRect_, 1, NSRect.__typestr__)
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_)
        self.assertArgHasType(TestWebUIDelegateHelper.webView_setContentRect_, 1, NSRect.__typestr__)
        self.assertResultHasType(TestWebUIDelegateHelper.webViewContentRect_, NSRect.__typestr__)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBOOL(TestWebUIDelegateHelper.webView_runOpenPanelForFileButtonWithResultListener_allowMultipleFiles_, 2)
        self.assertResultIsBOOL(TestWebUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_)
if __name__ == "__main__":
    main()
