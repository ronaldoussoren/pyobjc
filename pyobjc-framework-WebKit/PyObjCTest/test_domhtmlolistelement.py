from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLOListElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLOListElement.compact)
        self.assertArgIsBOOL(WebKit.DOMHTMLOListElement.setCompact_, 0)
