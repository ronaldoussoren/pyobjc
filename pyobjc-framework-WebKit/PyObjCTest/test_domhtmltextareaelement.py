from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLTextAreaElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLTextAreaElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLTextAreaElement.setDisabled_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLTextAreaElement.readOnly)
        self.assertArgIsBOOL(WebKit.DOMHTMLTextAreaElement.setReadOnly_, 0)

        self.assertResultIsBOOL(WebKit.DOMHTMLTextAreaElement.autofocus)
        self.assertArgIsBOOL(WebKit.DOMHTMLTextAreaElement.setAutofocus_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLTextAreaElement.willValidate)
