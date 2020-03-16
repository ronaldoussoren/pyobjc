from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMRangeException(TestCase):
    def testConstants(self):
        self.assertIsInstance(WebKit.DOMRangeException, str)
        self.assertEqual(WebKit.DOM_BAD_BOUNDARYPOINTS_ERR, 1)
        self.assertEqual(WebKit.DOM_INVALID_NODE_TYPE_ERR, 2)
