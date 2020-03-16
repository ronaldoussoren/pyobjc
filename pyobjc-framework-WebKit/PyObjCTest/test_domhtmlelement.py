from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMHTMLElement(TestCase):
    def testMehods(self):
        self.assertResultIsBOOL(WebKit.DOMHTMLElement.isContentEditable)
