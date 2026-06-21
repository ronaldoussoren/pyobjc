from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLMenuElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLMenuElement.compact)
        self.assertArgIsBOOL(WebKit.DOMHTMLMenuElement.setCompact_, 0)
