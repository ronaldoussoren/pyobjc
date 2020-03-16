from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLOptionElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLOptionElement.defaultSelected)
        self.assertArgIsBOOL(WebKit.DOMHTMLOptionElement.setDefaultSelected_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLOptionElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLOptionElement.setDisabled_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLOptionElement.selected)
        self.assertArgIsBOOL(WebKit.DOMHTMLOptionElement.setSelected_, 0)
