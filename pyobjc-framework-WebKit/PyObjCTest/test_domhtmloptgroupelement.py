from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLOptGroupElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLOptGroupElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLOptGroupElement.setDisabled_, 0)
