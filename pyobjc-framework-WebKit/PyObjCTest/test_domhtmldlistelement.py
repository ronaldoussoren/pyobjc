from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLDListElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLDListElement.compact)
        self.assertArgIsBOOL(WebKit.DOMHTMLDListElement.setCompact_, 0)
