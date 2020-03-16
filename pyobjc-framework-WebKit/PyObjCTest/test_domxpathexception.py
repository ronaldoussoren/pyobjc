from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMXPathException(TestCase):
    def testConstants(self):
        self.assertIsInstance(WebKit.DOMXPathException, str)

        self.assertEqual(WebKit.DOM_INVALID_EXPRESSION_ERR, 51)
        self.assertEqual(WebKit.DOM_TYPE_ERR, 52)
