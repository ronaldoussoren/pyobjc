from PyObjCTools.TestSupport import TestCase
import WebKit


class TestWebFrameView(TestCase):
    def test_methods(self):
        self.assertArgIsBOOL(WebKit.WebFrameView.setAllowsScrolling_, 0)
        self.assertResultIsBOOL(WebKit.WebFrameView.allowsScrolling)
        self.assertResultIsBOOL(WebKit.WebFrameView.canPrintHeadersAndFooters)
        self.assertResultIsBOOL(WebKit.WebFrameView.documentViewShouldHandlePrint)
