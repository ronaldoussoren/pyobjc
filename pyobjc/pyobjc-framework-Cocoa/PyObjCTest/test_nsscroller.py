
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSScroller (TestCase):
    def testConstants(self):
        self.assertEqual(NSScrollerArrowsMaxEnd, 0)
        self.assertEqual(NSScrollerArrowsMinEnd, 1)
        self.assertEqual(NSScrollerArrowsDefaultSetting, 0)
        self.assertEqual(NSScrollerArrowsNone, 2)
        self.assertEqual(NSNoScrollerParts, 0)
        self.assertEqual(NSOnlyScrollerArrows, 1)
        self.assertEqual(NSAllScrollerParts, 2)
        self.assertEqual(NSScrollerNoPart, 0)
        self.assertEqual(NSScrollerDecrementPage, 1)
        self.assertEqual(NSScrollerKnob, 2)
        self.assertEqual(NSScrollerIncrementPage, 3)
        self.assertEqual(NSScrollerDecrementLine, 4)
        self.assertEqual(NSScrollerIncrementLine, 5)
        self.assertEqual(NSScrollerKnobSlot, 6)
        self.assertEqual(NSScrollerIncrementArrow, 0)
        self.assertEqual(NSScrollerDecrementArrow, 1)

    def testMethods(self):
        self.assertArgIsBOOL(NSScroller.drawArrow_highlight_, 1)
        self.assertArgIsBOOL(NSScroller.drawKnobSlotInRect_highlight_, 1)
        self.assertArgIsBOOL(NSScroller.highlight_, 0)


if __name__ == "__main__":
    main()
