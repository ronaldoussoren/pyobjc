
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMOverflowEvent (TestCase):
    def testConstants(self):
        self.assertEqual(DOM_HORIZONTAL, 0)
        self.assertEqual(DOM_VERTICAL, 1)
        self.assertEqual(DOM_BOTH, 2)

    def testMethods(self):
        self.assertResultIsBOOL(DOMOverflowEvent.horizontalOverflow)
        self.assertResultIsBOOL(DOMOverflowEvent.verticalOverflow)

        self.assertArgIsBOOL(DOMOverflowEvent.initOverflowEvent_horizontalOverflow_verticalOverflow_, 1)
        self.assertArgIsBOOL(DOMOverflowEvent.initOverflowEvent_horizontalOverflow_verticalOverflow_, 2)


if __name__ == "__main__":
    main()
