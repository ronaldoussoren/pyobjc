from PyObjCTools.TestSupport import TestCase
import WebKit


class TestDOMException(TestCase):
    def testConstants(self):
        self.assertEqual(WebKit.DOM_INDEX_SIZE_ERR, 1)
        self.assertEqual(WebKit.DOM_DOMSTRING_SIZE_ERR, 2)
        self.assertEqual(WebKit.DOM_HIERARCHY_REQUEST_ERR, 3)
        self.assertEqual(WebKit.DOM_WRONG_DOCUMENT_ERR, 4)
        self.assertEqual(WebKit.DOM_INVALID_CHARACTER_ERR, 5)
        self.assertEqual(WebKit.DOM_NO_DATA_ALLOWED_ERR, 6)
        self.assertEqual(WebKit.DOM_NO_MODIFICATION_ALLOWED_ERR, 7)
        self.assertEqual(WebKit.DOM_NOT_FOUND_ERR, 8)
        self.assertEqual(WebKit.DOM_NOT_SUPPORTED_ERR, 9)
        self.assertEqual(WebKit.DOM_INUSE_ATTRIBUTE_ERR, 10)
        self.assertEqual(WebKit.DOM_INVALID_STATE_ERR, 11)
        self.assertEqual(WebKit.DOM_SYNTAX_ERR, 12)
        self.assertEqual(WebKit.DOM_INVALID_MODIFICATION_ERR, 13)
        self.assertEqual(WebKit.DOM_NAMESPACE_ERR, 14)
        self.assertEqual(WebKit.DOM_INVALID_ACCESS_ERR, 15)

        self.assertIsInstance(WebKit.DOMException, str)
