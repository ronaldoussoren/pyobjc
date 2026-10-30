from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLStyleElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLStyleElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLStyleElement.setDisabled_, 0)
