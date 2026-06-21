from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLTextAreaElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLTextAreaElement.willValidate)
