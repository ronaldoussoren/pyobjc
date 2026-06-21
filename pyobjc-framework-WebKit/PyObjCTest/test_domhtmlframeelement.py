from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLFrameElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLFrameElement.noResize)
        self.assertArgIsBOOL(WebKit.DOMHTMLFrameElement.setNoResize_, 0)
