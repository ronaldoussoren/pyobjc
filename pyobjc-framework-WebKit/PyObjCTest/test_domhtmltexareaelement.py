from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLTextAreaElement(TestCase):
    def testMehods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLTextAreaElement.willValidate)
