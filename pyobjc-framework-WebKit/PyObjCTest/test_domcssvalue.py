from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMCSSValue(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_CSS_INHERIT, 0)
        self.assertEqual(WebKit.DOM_CSS_PRIMITIVE_VALUE, 1)
        self.assertEqual(WebKit.DOM_CSS_VALUE_LIST, 2)
        self.assertEqual(WebKit.DOM_CSS_CUSTOM, 3)
