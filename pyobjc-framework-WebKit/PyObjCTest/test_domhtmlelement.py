from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLElement.isContentEditable)
