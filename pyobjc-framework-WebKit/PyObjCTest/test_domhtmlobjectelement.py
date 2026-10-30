from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLObjectElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLObjectElement.declare)
        self.assertArgIsBOOL(WebKit.DOMHTMLObjectElement.setDeclare_, 0)
