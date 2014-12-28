from PyObjCTools.TestSupport import *
from WebKit import *

try:
    unicode
except NameError:
    unicode = str


class TestWKWebView (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(WKWebView.isLoading)
        self.assertResultIsBOOL(WKWebView.hasOnlySecureContent)
        self.assertResultIsBOOL(WKWebView.canGoBack)
        self.assertResultIsBOOL(WKWebView.canGoForward)
        self.assertResultIsBOOL(WKWebView.allowsBackForwardNavigationGestures)
        self.assertArgIsBOOL(WKWebView.setAllowsBackForwardNavigationGestures_, 0)
        self.assertResultIsBOOL(WKWebView.allowsMagnification)
        self.assertArgIsBOOL(WKWebView.setAllowsMagnification_, 0)
        self.assertArgIsBlock(WKWebView.evaluateJavaScript_completionHandler_, 1, b"v@@")


if __name__ == "__main__":
    main()
