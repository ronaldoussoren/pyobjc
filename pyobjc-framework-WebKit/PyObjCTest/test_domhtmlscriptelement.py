from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLScriptElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLScriptElement.defer)
        self.assertArgIsBOOL(WebKit.DOMHTMLScriptElement.setDefer_, 0)
