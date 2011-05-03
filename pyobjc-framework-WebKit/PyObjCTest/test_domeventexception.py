
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMEventException (TestCase):
    def testConstants(self):
        self.assertIsInstance(DOMEventException, unicode)
        self.assertEqual(DOM_UNSPECIFIED_EVENT_TYPE_ERR, 0)

if __name__ == "__main__":
    main()
