from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMEventException(TestCase):
    def testConstants(self):
        self.assertIsInstance(WebKit.DOMEventException, str)
        self.assertEqual(WebKit.DOM_UNSPECIFIED_EVENT_TYPE_ERR, 0)
