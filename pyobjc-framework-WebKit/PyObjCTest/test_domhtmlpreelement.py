from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLPreElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLPreElement.wrap)
        self.assertArgIsBOOL(WebKit.DOMHTMLPreElement.setWrap_, 0)
