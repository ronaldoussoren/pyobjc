import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSScroller(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSScrollArrowPosition)
        self.assertIsEnumType(AppKit.NSScrollerArrow)
        self.assertIsEnumType(AppKit.NSScrollerKnobStyle)
        self.assertIsEnumType(AppKit.NSScrollerPart)
        self.assertIsEnumType(AppKit.NSScrollerStyle)
        self.assertIsEnumType(AppKit.NSUsableScrollerParts)

    def testConstants(self):
        self.assertEqual(AppKit.NSScrollerArrowsMaxEnd, 0)
        self.assertEqual(AppKit.NSScrollerArrowsMinEnd, 1)
        self.assertEqual(AppKit.NSScrollerArrowsDefaultSetting, 0)
        self.assertEqual(AppKit.NSScrollerArrowsNone, 2)

        self.assertEqual(AppKit.NSNoScrollerParts, 0)
        self.assertEqual(AppKit.NSOnlyScrollerArrows, 1)
        self.assertEqual(AppKit.NSAllScrollerParts, 2)

        self.assertEqual(AppKit.NSScrollerNoPart, 0)
        self.assertEqual(AppKit.NSScrollerDecrementPage, 1)
        self.assertEqual(AppKit.NSScrollerKnob, 2)
        self.assertEqual(AppKit.NSScrollerIncrementPage, 3)
        self.assertEqual(AppKit.NSScrollerDecrementLine, 4)
        self.assertEqual(AppKit.NSScrollerIncrementLine, 5)
        self.assertEqual(AppKit.NSScrollerKnobSlot, 6)

        self.assertEqual(AppKit.NSScrollerIncrementArrow, 0)
        self.assertEqual(AppKit.NSScrollerDecrementArrow, 1)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSScrollerStyleLegacy, 0)
        self.assertEqual(AppKit.NSScrollerStyleOverlay, 1)

        self.assertEqual(AppKit.NSScrollerKnobStyleDefault, 0)
        self.assertEqual(AppKit.NSScrollerKnobStyleDark, 1)
        self.assertEqual(AppKit.NSScrollerKnobStyleLight, 2)

        self.assertIsInstance(AppKit.NSPreferredScrollerStyleDidChangeNotification, str)

    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSScroller.drawArrow_highlight_, 1)
        self.assertArgIsBOOL(AppKit.NSScroller.drawKnobSlotInRect_highlight_, 1)
        self.assertArgIsBOOL(AppKit.NSScroller.highlight_, 0)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSScroller.isCompatibleWithOverlayScrollers)
