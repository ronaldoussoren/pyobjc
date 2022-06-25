import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSScrubberHelper(AppKit.NSObject):
    def numberOfItemsForScrubber_(self, s):
        return 1

    def scrubber_viewForItemAtIndex_(self, s, i):
        return 1

    def scrubber_didSelectItemAtIndex_(self, s, i):
        return 1

    def scrubber_didHighlightItemAtIndex_(self, s, i):
        return 1

    def scrubber_didChangeVisibleRange_(self, s, i):
        return 1


class TestNSScrubber(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSScrubberAlignment)
        self.assertIsEnumType(AppKit.NSScrubberMode)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(AppKit.NSScrubberModeFixed, 0)
        self.assertEqual(AppKit.NSScrubberModeFree, 1)

        self.assertEqual(AppKit.NSScrubberAlignmentNone, 0)
        self.assertEqual(AppKit.NSScrubberAlignmentLeading, 1)
        self.assertEqual(AppKit.NSScrubberAlignmentTrailing, 2)
        self.assertEqual(AppKit.NSScrubberAlignmentCenter, 3)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultHasType(
            TestNSScrubberHelper.numberOfItemsForScrubber_, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSScrubberHelper.scrubber_viewForItemAtIndex_, 1, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSScrubberHelper.scrubber_didSelectItemAtIndex_, 1, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSScrubberHelper.scrubber_didHighlightItemAtIndex_, 1, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSScrubberHelper.scrubber_didChangeVisibleRange_,
            1,
            AppKit.NSRange.__typestr__,
        )

        self.assertResultIsBOOL(AppKit.NSScrubber.isContinuous)
        self.assertArgIsBOOL(AppKit.NSScrubber.setContinuous_, 0)

        self.assertResultIsBOOL(AppKit.NSScrubber.floatsSelectionViews)
        self.assertArgIsBOOL(AppKit.NSScrubber.setFloatsSelectionViews_, 0)

        self.assertResultIsBOOL(AppKit.NSScrubber.showsArrowButtons)
        self.assertArgIsBOOL(AppKit.NSScrubber.setShowsArrowButtons_, 0)

        self.assertResultIsBOOL(AppKit.NSScrubber.showsAdditionalContentIndicators)
        self.assertArgIsBOOL(AppKit.NSScrubber.setShowsAdditionalContentIndicators_, 0)

        self.assertArgIsBlock(AppKit.NSScrubber.performSequentialBatchUpdates_, 0, b"v")

    @min_sdk_level("10.12")
    def testProtocols(self):
        self.assertProtocolExists("NSScrubberDataSource")
        self.assertProtocolExists("NSScrubberDelegate")
