from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLOListElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLOListElement.compact)
        self.assertArgIsBOOL(WebKit.DOMHTMLOListElement.setCompact_, 0)
