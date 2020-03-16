from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLUListElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLUListElement.compact)
        self.assertArgIsBOOL(WebKit.DOMHTMLUListElement.setCompact_, 0)
