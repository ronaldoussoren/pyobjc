from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLDirectoryElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLDirectoryElement.compact)
        self.assertArgIsBOOL(WebKit.DOMHTMLDirectoryElement.setCompact_, 0)
