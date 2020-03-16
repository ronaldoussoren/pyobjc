from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLStyleElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLStyleElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLStyleElement.setDisabled_, 0)
