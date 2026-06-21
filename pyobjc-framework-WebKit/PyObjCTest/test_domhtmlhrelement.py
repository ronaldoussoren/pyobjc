from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLHRElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLHRElement.noShade)
        self.assertArgIsBOOL(WebKit.DOMHTMLHRElement.setNoShade_, 0)
