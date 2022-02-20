import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSTextContainer(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSLineMovementDirection)
        self.assertIsEnumType(AppKit.NSLineSweepDirection)

    def testConstants(self):
        self.assertEqual(AppKit.NSLineSweepLeft, 0)
        self.assertEqual(AppKit.NSLineSweepRight, 1)
        self.assertEqual(AppKit.NSLineSweepDown, 2)
        self.assertEqual(AppKit.NSLineSweepUp, 3)

        self.assertEqual(AppKit.NSLineDoesntMove, 0)
        self.assertEqual(AppKit.NSLineMovesLeft, 1)
        self.assertEqual(AppKit.NSLineMovesRight, 2)
        self.assertEqual(AppKit.NSLineMovesDown, 3)
        self.assertEqual(AppKit.NSLineMovesUp, 4)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTextContainer.widthTracksTextView)
        self.assertArgIsBOOL(AppKit.NSTextContainer.setWidthTracksTextView_, 0)
        self.assertResultIsBOOL(AppKit.NSTextContainer.heightTracksTextView)
        self.assertArgIsBOOL(AppKit.NSTextContainer.setHeightTracksTextView_, 0)
        self.assertResultIsBOOL(AppKit.NSTextContainer.isSimpleRectangularTextContainer)
        self.assertResultIsBOOL(AppKit.NSTextContainer.containsPoint_)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsOut(
            AppKit.NSTextContainer.lineFragmentRectForProposedRect_atIndex_writingDirection_remainingRect_,  # noqa: B950
            3,
        )
