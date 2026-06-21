from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMHTMLTextAreaElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLTextAreaElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLTextAreaElement.setDisabled_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLTextAreaElement.readOnly)
        self.assertArgIsBOOL(WebKit.DOMHTMLTextAreaElement.setReadOnly_, 0)

    @min_os_level("10.6")
    def test_methods10_6(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLTextAreaElement.autofocus)
        self.assertArgIsBOOL(WebKit.DOMHTMLTextAreaElement.setAutofocus_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLTextAreaElement.willValidate)
