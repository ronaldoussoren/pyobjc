from WebKit import *
from PyObjCTools.TestSupport import *

class TestDOMRange (TestCase):
    def testConstants(self):
        self.failUnlessEqual(DOM_START_TO_START, 0)
        self.failUnlessEqual(DOM_START_TO_END, 1)
        self.failUnlessEqual(DOM_END_TO_END, 2)
        self.failUnlessEqual(DOM_END_TO_START, 3)
        self.failUnlessEqual(DOM_NODE_BEFORE, 0)
        self.failUnlessEqual(DOM_NODE_AFTER, 1)
        self.failUnlessEqual(DOM_NODE_BEFORE_AND_AFTER, 2)
        self.failUnlessEqual(DOM_NODE_INSIDE, 3)

    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMRange.collapsed)
        self.failUnlessArgIsBOOL(DOMRange.collapse_, 0)

if __name__ == "__main__":
    main()
