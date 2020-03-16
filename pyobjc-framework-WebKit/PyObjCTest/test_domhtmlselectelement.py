from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMHTMLSelectElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLSelectElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLSelectElement.setDisabled_, 0)
        self.assertResultIsBOOL(WebKit.DOMHTMLSelectElement.multiple)
        self.assertArgIsBOOL(WebKit.DOMHTMLSelectElement.setMultiple_, 0)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLSelectElement.willValidate)
        self.assertResultIsBOOL(WebKit.DOMHTMLSelectElement.autofocus)
        self.assertArgIsBOOL(WebKit.DOMHTMLSelectElement.setAutofocus_, 0)
