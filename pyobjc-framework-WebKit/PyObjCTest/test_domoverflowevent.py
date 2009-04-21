
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMOverflowEvent (TestCase):
    def testConstants(self):
        self.failUnlessEqual(DOM_HORIZONTAL, 0)
        self.failUnlessEqual(DOM_VERTICAL, 1)
        self.failUnlessEqual(DOM_BOTH, 2)

    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMOverflowEvent.horizontalOverflow)
        self.failUnlessResultIsBOOL(DOMOverflowEvent.verticalOverflow)

        self.failUnlessArgIsBOOL(DOMOverflowEvent.initOverflowEvent_horizontalOverflow_verticalOverflow_, 1)
        self.failUnlessArgIsBOOL(DOMOverflowEvent.initOverflowEvent_horizontalOverflow_verticalOverflow_, 2)


if __name__ == "__main__":
    main()
