from PyObjCTools.TestSupport import TestCase, min_os_level
import WebKit


class TestDOMHTMLPreElement(TestCase):
    @min_os_level("10.6")
    def testMehods10_6(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLPreElement.wrap)
        self.assertArgIsBOOL(WebKit.DOMHTMLPreElement.setWrap_, 0)
