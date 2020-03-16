from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMHTMLButtonElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLButtonElement.disabled)
        self.assertArgIsBOOL(WebKit.DOMHTMLButtonElement.setDisabled_, 0)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLButtonElement.willValidate)
        self.assertResultIsBOOL(WebKit.DOMHTMLButtonElement.autofocus)
        self.assertArgIsBOOL(WebKit.DOMHTMLButtonElement.setAutofocus_, 0)
