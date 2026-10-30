from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMEventException(TestCase):
    def test_constants(self):
        self.assertIsInstance(WebKit.DOMEventException, str)
        self.assertEqual(WebKit.DOM_UNSPECIFIED_EVENT_TYPE_ERR, 0)
