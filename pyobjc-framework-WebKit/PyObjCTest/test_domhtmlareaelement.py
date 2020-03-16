from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLAreaElement(TestCase):
    def testMehods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLAreaElement.noHref)
        self.assertArgIsBOOL(WebKit.DOMHTMLAreaElement.setNoHref_, 0)
