from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMAttr(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMAttr.specified)
