
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMXPathException (TestCase):
    def testConstants(self):
        self.assertIsInstance(DOMXPathException, unicode)

        self.assertEqual(DOM_INVALID_EXPRESSION_ERR, 51)
        self.assertEqual(DOM_TYPE_ERR, 52)


if __name__ == "__main__":
    main()
