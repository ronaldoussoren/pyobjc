from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLImageElement(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLImageElement.isMap)
        self.assertArgIsBOOL(WebKit.DOMHTMLImageElement.setIsMap_, 0)

        self.assertResultIsBOOL(WebKit.DOMHTMLImageElement.complete)
