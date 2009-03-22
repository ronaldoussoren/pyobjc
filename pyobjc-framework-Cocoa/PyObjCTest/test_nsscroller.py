
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSScroller (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSScrollerArrowsMaxEnd, 0)
        self.failUnlessEqual(NSScrollerArrowsMinEnd, 1)
        self.failUnlessEqual(NSScrollerArrowsDefaultSetting, 0)
        self.failUnlessEqual(NSScrollerArrowsNone, 2)
        self.failUnlessEqual(NSNoScrollerParts, 0)
        self.failUnlessEqual(NSOnlyScrollerArrows, 1)
        self.failUnlessEqual(NSAllScrollerParts, 2)
        self.failUnlessEqual(NSScrollerNoPart, 0)
        self.failUnlessEqual(NSScrollerDecrementPage, 1)
        self.failUnlessEqual(NSScrollerKnob, 2)
        self.failUnlessEqual(NSScrollerIncrementPage, 3)
        self.failUnlessEqual(NSScrollerDecrementLine, 4)
        self.failUnlessEqual(NSScrollerIncrementLine, 5)
        self.failUnlessEqual(NSScrollerKnobSlot, 6)
        self.failUnlessEqual(NSScrollerIncrementArrow, 0)
        self.failUnlessEqual(NSScrollerDecrementArrow, 1)

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSScroller.drawArrow_highlight_, 1)
        self.failUnlessArgIsBOOL(NSScroller.drawKnobSlotInRect_highlight_, 1)
        self.failUnlessArgIsBOOL(NSScroller.highlight_, 0)


if __name__ == "__main__":
    main()
