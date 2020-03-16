from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLHRElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLHRElement.noShade)
        self.assertArgIsBOOL(WebKit.DOMHTMLHRElement.setNoShade_, 0)
