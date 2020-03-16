from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMHTMLInputElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.defaultChecked)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setDefaultChecked_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.checked)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setChecked_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setDisabled_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.readOnly)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setReadOnly_, 0)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.indeterminate)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setIndeterminate_, 0)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.autofocus)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setAutofocus_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.multiple)
        self.assertArgIsBOOL(WebKit.DOMHTMLInputElement.setMultiple_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLInputElement.willValidate)
