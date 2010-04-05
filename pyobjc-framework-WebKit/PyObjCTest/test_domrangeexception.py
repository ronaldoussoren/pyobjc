
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMRangeException (TestCase):
    def testConstants(self):
        self.assertIsInstance(DOMRangeException, unicode)
        self.assertEqual(DOM_BAD_BOUNDARYPOINTS_ERR, 1)
        self.assertEqual(DOM_INVALID_NODE_TYPE_ERR, 2)

if __name__ == "__main__":
    main()
