
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebView (TestCase):
    def testConstants(self):
        self.assertIsInstance(WebElementDOMNodeKey, unicode)
        self.assertIsInstance(WebElementFrameKey, unicode)
        self.assertIsInstance(WebElementImageAltStringKey, unicode)
        self.assertIsInstance(WebElementImageKey, unicode)
        self.assertIsInstance(WebElementImageRectKey, unicode)
        self.assertIsInstance(WebElementImageURLKey, unicode)
        self.assertIsInstance(WebElementIsSelectedKey, unicode)
        self.assertIsInstance(WebElementLinkURLKey, unicode)
        self.assertIsInstance(WebElementLinkTargetFrameKey, unicode)
        self.assertIsInstance(WebElementLinkTitleKey, unicode)
        self.assertIsInstance(WebElementLinkLabelKey, unicode)
        self.assertIsInstance(WebViewProgressStartedNotification, unicode)
        self.assertIsInstance(WebViewProgressEstimateChangedNotification, unicode)
        self.assertIsInstance(WebViewProgressFinishedNotification, unicode)
        self.assertIsInstance(WebViewDidBeginEditingNotification, unicode)
        self.assertIsInstance(WebViewDidChangeNotification, unicode)
        self.assertIsInstance(WebViewDidEndEditingNotification, unicode)
        self.assertIsInstance(WebViewDidChangeTypingStyleNotification, unicode)
        self.assertIsInstance(WebViewDidChangeSelectionNotification, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(WebView.canShowMIMEType_)
        self.assertResultIsBOOL(WebView.canShowMIMETypeAsHTML_)
        self.assertResultIsBOOL(WebView.shouldCloseWithWindow)
        self.assertArgIsBOOL(WebView.setShouldCloseWithWindow_, 0)
        self.assertArgIsBOOL(WebView.setMaintainsBackForwardList_, 0)
        self.assertResultIsBOOL(WebView.goBack)
        self.assertResultIsBOOL(WebView.goForward)
        self.assertResultIsBOOL(WebView.goToBackForwardItem_)
        self.assertResultIsBOOL(WebView.supportsTextEncoding)
        self.assertResultIsBOOL(WebView.searchFor_direction_caseSensitive_wrap_)
        self.assertArgIsBOOL(WebView.searchFor_direction_caseSensitive_wrap_, 1)
        self.assertArgIsBOOL(WebView.searchFor_direction_caseSensitive_wrap_, 2)
        self.assertArgIsBOOL(WebView.searchFor_direction_caseSensitive_wrap_, 3)
        self.assertResultIsBOOL(WebView.isLoading)
        self.assertResultIsBOOL(WebView.drawsBackground)
        self.assertArgIsBOOL(WebView.setDrawsBackground_, 0)
        self.assertResultIsBOOL(WebView.canGoBack)
        self.assertResultIsBOOL(WebView.canGoForward)
        self.assertResultIsBOOL(WebView.canMakeTextLarger)
        self.assertResultIsBOOL(WebView.canMakeTextSmaller)
        self.assertResultIsBOOL(WebView.canMakeTextStandardSize)
        self.assertResultIsBOOL(WebView.maintainsInactiveSelection)
        self.assertResultIsBOOL(WebView.isEditable)
        self.assertArgIsBOOL(WebView.setEditable_, 0)
        self.assertResultIsBOOL(WebView.smartInsertDeleteEnabled)
        self.assertArgIsBOOL(WebView.setSmartInsertDeleteEnabled_, 0)
        self.assertResultIsBOOL(WebView.isContinuousSpellCheckingEnabled)
        self.assertArgIsBOOL(WebView.setContinuousSpellCheckingEnabled_, 0)

        self.assertArgIsBOOL(WebView.setShouldUpdateWhileOffscreen_, 0)
        self.assertResultIsBOOL(WebView.shouldUpdateWhileOffscreen)



if __name__ == "__main__":
    main()
