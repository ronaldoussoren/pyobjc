from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMCSSStyleDeclaration(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(WebKit.DOMCSSStyleDeclaration.isPropertyImplicit_)
