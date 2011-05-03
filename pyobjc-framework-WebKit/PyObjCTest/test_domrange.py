from WebKit import *
from PyObjCTools.TestSupport import *

class TestDOMRange (TestCase):
    def testConstants(self):
        self.assertEqual(DOM_START_TO_START, 0)
        self.assertEqual(DOM_START_TO_END, 1)
        self.assertEqual(DOM_END_TO_END, 2)
        self.assertEqual(DOM_END_TO_START, 3)
        self.assertEqual(DOM_NODE_BEFORE, 0)
        self.assertEqual(DOM_NODE_AFTER, 1)
        self.assertEqual(DOM_NODE_BEFORE_AND_AFTER, 2)
        self.assertEqual(DOM_NODE_INSIDE, 3)

    def testMethods(self):
        self.assertResultIsBOOL(DOMRange.collapsed)
        self.assertArgIsBOOL(DOMRange.collapse_, 0)

        self.assertResultIsBOOL(DOMRange.intersectsNode_)
        self.assertResultIsBOOL(DOMRange.isPointInRange_offset_)

if __name__ == "__main__":
    main()
