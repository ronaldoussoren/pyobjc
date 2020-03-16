from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMCSSStyleDeclaration(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(WebKit.DOMCSSStyleDeclaration.isPropertyImplicit_)
