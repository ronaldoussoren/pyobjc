
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

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

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSScrollerStyleLegacy, 0)
        self.assertEqual(NSScrollerStyleOverlay, 1)

        self.assertEqual(NSScrollerKnobStyleDefault, 0)
        self.assertEqual(NSScrollerKnobStyleDark, 1)
        self.assertEqual(NSScrollerKnobStyleLight, 2)

        self.assertIsInstance(NSPreferredScrollerStyleDidChangeNotification, unicode)

    def testMethods(self):
        self.assertArgIsBOOL(NSScroller.drawArrow_highlight_, 1)
        self.assertArgIsBOOL(NSScroller.drawKnobSlotInRect_highlight_, 1)
        self.assertArgIsBOOL(NSScroller.highlight_, 0)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(NSScroller.isCompatibleWithOverlayScrollers)

if __name__ == "__main__":
    main()
