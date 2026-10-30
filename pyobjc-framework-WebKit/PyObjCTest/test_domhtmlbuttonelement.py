from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLButtonElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLButtonElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLButtonElement.setDisabled_, 0)

        self.assertResultIsBOOL(WebKit.DOMHTMLButtonElement.willValidate)
        self.assertResultIsBOOL(WebKit.DOMHTMLButtonElement.autofocus)
        self.assertArgIsBOOL(WebKit.DOMHTMLButtonElement.setAutofocus_, 0)
