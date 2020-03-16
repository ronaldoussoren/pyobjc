from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLScriptElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLScriptElement.defer)
        self.assertArgIsBOOL(WebKit.DOMHTMLScriptElement.setDefer_, 0)
