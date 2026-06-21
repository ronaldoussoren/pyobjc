from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLLinkElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLLinkElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLLinkElement.setDisabled_, 0)
