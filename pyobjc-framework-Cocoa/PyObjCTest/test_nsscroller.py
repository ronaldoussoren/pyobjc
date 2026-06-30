import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSScroller(TestCase):
    def test_enums(self):
        self.assertIsEnumType(AppKit.NSScrollArrowPosition)
        self.assertEqual(AppKit.NSScrollerArrowsMaxEnd, 0)
        self.assertEqual(AppKit.NSScrollerArrowsMinEnd, 1)
        self.assertEqual(AppKit.NSScrollerArrowsDefaultSetting, 0)
        self.assertEqual(AppKit.NSScrollerArrowsNone, 2)

        self.assertIsEnumType(AppKit.NSScrollerArrow)
        self.assertEqual(AppKit.NSNoScrollerParts, 0)
        self.assertEqual(AppKit.NSOnlyScrollerArrows, 1)
        self.assertEqual(AppKit.NSAllScrollerParts, 2)

        self.assertIsEnumType(AppKit.NSScrollerKnobStyle)
        self.assertEqual(AppKit.NSScrollerNoPart, 0)
        self.assertEqual(AppKit.NSScrollerDecrementPage, 1)
        self.assertEqual(AppKit.NSScrollerKnob, 2)
        self.assertEqual(AppKit.NSScrollerIncrementPage, 3)
        self.assertEqual(AppKit.NSScrollerDecrementLine, 4)
        self.assertEqual(AppKit.NSScrollerIncrementLine, 5)
        self.assertEqual(AppKit.NSScrollerKnobSlot, 6)

        self.assertIsEnumType(AppKit.NSScrollerPart)
        self.assertEqual(AppKit.NSScrollerIncrementArrow, 0)
        self.assertEqual(AppKit.NSScrollerDecrementArrow, 1)

        self.assertIsEnumType(AppKit.NSScrollerStyle)
        self.assertEqual(AppKit.NSScrollerStyleLegacy, 0)
        self.assertEqual(AppKit.NSScrollerStyleOverlay, 1)

        self.assertIsEnumType(AppKit.NSUsableScrollerParts)
        self.assertEqual(AppKit.NSScrollerKnobStyleDefault, 0)
        self.assertEqual(AppKit.NSScrollerKnobStyleDark, 1)
        self.assertEqual(AppKit.NSScrollerKnobStyleLight, 2)

    def test_constants(self):
        self.assertIsInstance(AppKit.NSPreferredScrollerStyleDidChangeNotification, str)

    def test_methods(self):
        self.assertArgIsBOOL(AppKit.NSScroller.drawArrow_highlight_, 1)
        self.assertArgIsBOOL(AppKit.NSScroller.drawKnobSlotInRect_highlight_, 1)
        self.assertArgIsBOOL(AppKit.NSScroller.highlight_, 0)

        self.assertResultIsBOOL(AppKit.NSScroller.isCompatibleWithOverlayScrollers)
