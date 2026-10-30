from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLUListElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLUListElement.compact)
        self.assertArgIsBOOL(WebKit.DOMHTMLUListElement.setCompact_, 0)
