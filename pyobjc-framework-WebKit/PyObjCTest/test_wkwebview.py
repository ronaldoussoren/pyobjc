from PyObjCTools.TestSupport import *
from WebKit import *


class TestWKWebView(TestCase):
    @onlyOn64Bit
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(WKWebView.isLoading)
        self.assertResultIsBOOL(WKWebView.hasOnlySecureContent)
        self.assertResultIsBOOL(WKWebView.canGoBack)
        self.assertResultIsBOOL(WKWebView.canGoForward)
        self.assertResultIsBOOL(WKWebView.allowsBackForwardNavigationGestures)
        self.assertArgIsBOOL(WKWebView.setAllowsBackForwardNavigationGestures_, 0)
        self.assertResultIsBOOL(WKWebView.allowsMagnification)
        self.assertArgIsBOOL(WKWebView.setAllowsMagnification_, 0)
        self.assertArgIsBlock(
            WKWebView.evaluateJavaScript_completionHandler_, 1, b"v@@"
        )

    @onlyOn64Bit
    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(WKWebView.allowsLinkPreview)
        self.assertArgIsBOOL(WKWebView.setAllowsLinkPreview_, 0)

    @onlyOn64Bit
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            WKWebView.takeSnapshotWithConfiguration_completionHandler_, 1, b"v@@"
        )
        self.assertResultIsBOOL(WKWebView.handlesURLScheme_)

    @onlyOn64Bit
    @min_os_level("10.15.4")
    def testMethods10_15_4(self):
        self.assertArgIsBlock(
            WKWebView.createPDFWithConfiguration_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            WKWebView.createWebArchiveDataWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            WKWebView.findString_withConfiguration_completionHandler_, 2, b"v@"
        )


if __name__ == "__main__":
    main()
