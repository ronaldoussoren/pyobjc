
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebView (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(WebElementDOMNodeKey, unicode)
        self.failUnlessIsInstance(WebElementFrameKey, unicode)
        self.failUnlessIsInstance(WebElementImageAltStringKey, unicode)
        self.failUnlessIsInstance(WebElementImageKey, unicode)
        self.failUnlessIsInstance(WebElementImageRectKey, unicode)
        self.failUnlessIsInstance(WebElementImageURLKey, unicode)
        self.failUnlessIsInstance(WebElementIsSelectedKey, unicode)
        self.failUnlessIsInstance(WebElementLinkURLKey, unicode)
        self.failUnlessIsInstance(WebElementLinkTargetFrameKey, unicode)
        self.failUnlessIsInstance(WebElementLinkTitleKey, unicode)
        self.failUnlessIsInstance(WebElementLinkLabelKey, unicode)
        self.failUnlessIsInstance(WebViewProgressStartedNotification, unicode)
        self.failUnlessIsInstance(WebViewProgressEstimateChangedNotification, unicode)
        self.failUnlessIsInstance(WebViewProgressFinishedNotification, unicode)
        self.failUnlessIsInstance(WebViewDidBeginEditingNotification, unicode)
        self.failUnlessIsInstance(WebViewDidChangeNotification, unicode)
        self.failUnlessIsInstance(WebViewDidEndEditingNotification, unicode)
        self.failUnlessIsInstance(WebViewDidChangeTypingStyleNotification, unicode)
        self.failUnlessIsInstance(WebViewDidChangeSelectionNotification, unicode)


    def testMethods(self):
        self.failUnlessResultIsBOOL(WebView.canShowMIMEType_)
        self.failUnlessResultIsBOOL(WebView.canShowMIMETypeAsHTML_)
        self.failUnlessResultIsBOOL(WebView.shouldCloseWithWindow)
        self.failUnlessArgIsBOOL(WebView.setShouldCloseWithWindow_, 0)
        self.failUnlessArgIsBOOL(WebView.setMaintainsBackForwardList_, 0)
        self.failUnlessResultIsBOOL(WebView.goBack)
        self.failUnlessResultIsBOOL(WebView.goForward)
        self.failUnlessResultIsBOOL(WebView.goToBackForwardItem_)
        self.failUnlessResultIsBOOL(WebView.supportsTextEncoding)
        self.failUnlessResultIsBOOL(WebView.searchFor_direction_caseSensitive_wrap_)
        self.failUnlessArgIsBOOL(WebView.searchFor_direction_caseSensitive_wrap_, 1)
        self.failUnlessArgIsBOOL(WebView.searchFor_direction_caseSensitive_wrap_, 2)
        self.failUnlessArgIsBOOL(WebView.searchFor_direction_caseSensitive_wrap_, 3)
        self.failUnlessResultIsBOOL(WebView.isLoading)
        self.failUnlessResultIsBOOL(WebView.drawsBackground)
        self.failUnlessArgIsBOOL(WebView.setDrawsBackground_, 0)
        self.failUnlessResultIsBOOL(WebView.canGoBack)
        self.failUnlessResultIsBOOL(WebView.canGoForward)
        self.failUnlessResultIsBOOL(WebView.canMakeTextLarger)
        self.failUnlessResultIsBOOL(WebView.canMakeTextSmaller)
        self.failUnlessResultIsBOOL(WebView.canMakeTextStandardSize)
        self.failUnlessResultIsBOOL(WebView.maintainsInactiveSelection)
        self.failUnlessResultIsBOOL(WebView.isEditable)
        self.failUnlessArgIsBOOL(WebView.setEditable_, 0)
        self.failUnlessResultIsBOOL(WebView.smartInsertDeleteEnabled)
        self.failUnlessArgIsBOOL(WebView.setSmartInsertDeleteEnabled_, 0)
        self.failUnlessResultIsBOOL(WebView.isContinuousSpellCheckingEnabled)
        self.failUnlessArgIsBOOL(WebView.setContinuousSpellCheckingEnabled_, 0)



if __name__ == "__main__":
    main()
