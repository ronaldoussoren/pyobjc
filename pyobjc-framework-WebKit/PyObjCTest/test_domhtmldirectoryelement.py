from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLDirectoryElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLDirectoryElement.compact)
        self.assertArgIsBOOL(WebKit.DOMHTMLDirectoryElement.setCompact_, 0)
