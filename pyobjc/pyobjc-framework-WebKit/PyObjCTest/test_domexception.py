
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMException (TestCase):
    def testConstants(self):
        self.assertEqual(DOM_INDEX_SIZE_ERR, 1)
        self.assertEqual(DOM_DOMSTRING_SIZE_ERR, 2)
        self.assertEqual(DOM_HIERARCHY_REQUEST_ERR, 3)
        self.assertEqual(DOM_WRONG_DOCUMENT_ERR, 4)
        self.assertEqual(DOM_INVALID_CHARACTER_ERR, 5)
        self.assertEqual(DOM_NO_DATA_ALLOWED_ERR, 6)
        self.assertEqual(DOM_NO_MODIFICATION_ALLOWED_ERR, 7)
        self.assertEqual(DOM_NOT_FOUND_ERR, 8)
        self.assertEqual(DOM_NOT_SUPPORTED_ERR, 9)
        self.assertEqual(DOM_INUSE_ATTRIBUTE_ERR, 10)
        self.assertEqual(DOM_INVALID_STATE_ERR, 11)
        self.assertEqual(DOM_SYNTAX_ERR, 12)
        self.assertEqual(DOM_INVALID_MODIFICATION_ERR, 13)
        self.assertEqual(DOM_NAMESPACE_ERR, 14)
        self.assertEqual(DOM_INVALID_ACCESS_ERR, 15)

        self.assertIsInstance(DOMException, unicode)

if __name__ == "__main__":
    main()
