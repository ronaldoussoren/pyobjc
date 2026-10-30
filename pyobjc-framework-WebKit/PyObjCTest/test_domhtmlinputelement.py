from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLInputElement(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.defaultChecked)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setDefaultChecked_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.checked)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setChecked_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setDisabled_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.readOnly)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setReadOnly_, 0)

        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.indeterminate)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setIndeterminate_, 0)

        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.autofocus)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setAutofocus_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.multiple)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setMultiple_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.willValidate)
