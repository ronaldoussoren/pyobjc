
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

class TestWebUIDelegate (TestCase):
    def testConstants(self):
        self.failUnlessEqual(WebMenuItemTagOpenLinkInNewWindow, 1)
        self.failUnlessEqual(WebMenuItemTagDownloadLinkToDisk, 2)
        self.failUnlessEqual(WebMenuItemTagCopyLinkToClipboard, 3)
        self.failUnlessEqual(WebMenuItemTagOpenImageInNewWindow, 4)
        self.failUnlessEqual(WebMenuItemTagDownloadImageToDisk, 5)
        self.failUnlessEqual(WebMenuItemTagCopyImageToClipboard, 6)
        self.failUnlessEqual(WebMenuItemTagOpenFrameInNewWindow, 7)
        self.failUnlessEqual(WebMenuItemTagCopy, 8)
        self.failUnlessEqual(WebMenuItemTagGoBack, 9)
        self.failUnlessEqual(WebMenuItemTagGoForward, 10)
        self.failUnlessEqual(WebMenuItemTagStop, 11)
        self.failUnlessEqual(WebMenuItemTagReload, 12)
        self.failUnlessEqual(WebMenuItemTagCut, 13)
        self.failUnlessEqual(WebMenuItemTagPaste, 14)
        self.failUnlessEqual(WebMenuItemTagSpellingGuess, 15)
        self.failUnlessEqual(WebMenuItemTagNoGuessesFound, 16)
        self.failUnlessEqual(WebMenuItemTagIgnoreSpelling, 17)
        self.failUnlessEqual(WebMenuItemTagLearnSpelling, 18)
        self.failUnlessEqual(WebMenuItemTagOther, 19)
        self.failUnlessEqual(WebMenuItemTagSearchInSpotlight, 20)
        self.failUnlessEqual(WebMenuItemTagSearchWeb, 21)
        self.failUnlessEqual(WebMenuItemTagLookUpInDictionary, 22)
        self.failUnlessEqual(WebMenuItemTagOpenWithDefaultApplication, 23)
        self.failUnlessEqual(WebMenuItemPDFActualSize, 24)
        self.failUnlessEqual(WebMenuItemPDFZoomIn, 25)
        self.failUnlessEqual(WebMenuItemPDFZoomOut, 26)
        self.failUnlessEqual(WebMenuItemPDFAutoSize, 27)
        self.failUnlessEqual(WebMenuItemPDFSinglePage, 28)
        self.failUnlessEqual(WebMenuItemPDFFacingPages, 29)
        self.failUnlessEqual(WebMenuItemPDFContinuous, 30)
        self.failUnlessEqual(WebMenuItemPDFNextPage, 31)
        self.failUnlessEqual(WebMenuItemPDFPreviousPage, 32)

        self.failUnlessEqual(WebDragDestinationActionNone, 0)
        self.failUnlessEqual(WebDragDestinationActionDHTML, 1)
        self.failUnlessEqual(WebDragDestinationActionEdit, 2)
        self.failUnlessEqual(WebDragDestinationActionLoad, 4)
        self.failUnlessEqual(WebDragDestinationActionAny, UINT_MAX)

        self.failUnlessEqual(WebDragSourceActionNone, 0)
        self.failUnlessEqual(WebDragSourceActionDHTML, 1)
        self.failUnlessEqual(WebDragSourceActionImage, 2)
        self.failUnlessEqual(WebDragSourceActionLink, 4)
        self.failUnlessEqual(WebDragSourceActionSelection, 8)
        self.failUnlessEqual(WebDragSourceActionAny, UINT_MAX)


    def testMethods(self):
        self.failUnlessResultIsBOOL(TestWebUIDelegateHelper.webViewAreToolbarsVisible_)
        self.failUnlessArgIsBOOL(TestWebUIDelegateHelper.webView_setToolbarsVisible_, 1)
        self.failUnlessResultIsBOOL(TestWebUIDelegateHelper.webViewIsStatusBarVisible_)
        self.failUnlessArgIsBOOL(TestWebUIDelegateHelper.webView_setStatusBarVisible_, 1)
        self.failUnlessResultIsBOOL(TestWebUIDelegateHelper.webViewIsResizable_)
        self.failUnlessArgIsBOOL(TestWebUIDelegateHelper.webView_setResizable_, 1)
        self.failUnlessResultIsBOOL(TestWebUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_initiatedByFrame_)
        self.failUnlessResultIsBOOL(TestWebUIDelegateHelper.webView_runBeforeUnloadConfirmPanelWithMessage_initiatedByFrame_)
        self.failUnlessArgHasType(TestWebUIDelegateHelper.webView_mouseDidMoveOverElement_modifierFlags_, 2, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestWebUIDelegateHelper.webView_validateUserInterfaceItem_defaultValidation_)
        self.failUnlessArgIsBOOL(TestWebUIDelegateHelper.webView_validateUserInterfaceItem_defaultValidation_, 2)
        self.failUnlessResultIsBOOL(TestWebUIDelegateHelper.webView_shouldPerformAction_fromSender_)
        self.failUnlessResultHasType(TestWebUIDelegateHelper.webView_dragDestinationActionMaskForDraggingInfo_, objc._C_NSUInteger)
        self.failUnlessResultHasType(TestWebUIDelegateHelper.webView_dragSourceActionMaskForPoint_, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestWebUIDelegateHelper.webView_willPerformDragSourceAction_fromPoint_withPasteboard_, 1, objc._C_NSInteger)
        self.failUnlessArgHasType(TestWebUIDelegateHelper.webView_willPerformDragSourceAction_fromPoint_withPasteboard_, 2, NSPoint.__typestr__)
        self.failUnlessResultHasType(TestWebUIDelegateHelper.webViewHeaderHeight_, objc._C_FLT)
        self.failUnlessResultHasType(TestWebUIDelegateHelper.webViewFooterHeight_, objc._C_FLT)
        self.failUnlessArgHasType(TestWebUIDelegateHelper.webView_drawHeaderInRect_, 1, NSRect.__typestr__)
        self.failUnlessArgHasType(TestWebUIDelegateHelper.webView_drawFooterInRect_, 1, NSRect.__typestr__)
        self.failUnlessResultIsBOOL(TestWebUIDelegateHelper.webView_runJavaScriptConfirmPanelWithMessage_)
        self.failUnlessArgHasType(TestWebUIDelegateHelper.webView_setContentRect_, 1, NSRect.__typestr__)
        self.failUnlessResultHasType(TestWebUIDelegateHelper.webViewContentRect_, NSRect.__typestr__)


if __name__ == "__main__":
    main()
