from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLSelectElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLSelectElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLSelectElement.setDisabled_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLSelectElement.multiple)
        self.assertArgIsBOOL(WebKit.DOMHTMLSelectElement.setMultiple_, 0)

        self.assertResultIsBOOL(WebKit.DOMHTMLSelectElement.willValidate)
        self.assertResultIsBOOL(WebKit.DOMHTMLSelectElement.autofocus)
        self.assertArgIsBOOL(WebKit.DOMHTMLSelectElement.setAutofocus_, 0)
