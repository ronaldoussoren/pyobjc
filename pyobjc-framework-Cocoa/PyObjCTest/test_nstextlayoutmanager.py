import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestNSTextLayoutManagerHelper(AppKit.NSObject):
    def textLayoutManager_shouldBreakLineBeforeLocation_hyphenating_(self, a, b, c):
        return 1


class TestNSTextLayoutManager(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSTextLayoutManagerSegmentOptions)
        self.assertIsEnumType(AppKit.NSTextLayoutManagerSegmentType)

    def test_constants(self):
        self.assertEqual(AppKit.NSTextLayoutManagerSegmentTypeStandard, 0)
        self.assertEqual(AppKit.NSTextLayoutManagerSegmentTypeSelection, 1)
        self.assertEqual(AppKit.NSTextLayoutManagerSegmentTypeHighlight, 2)

        self.assertEqual(AppKit.NSTextLayoutManagerSegmentOptionsNone, 0)
        self.assertEqual(
            AppKit.NSTextLayoutManagerSegmentOptionsRangeNotRequired, 1 << 0
        )
        self.assertEqual(
            AppKit.NSTextLayoutManagerSegmentOptionsMiddleFragmentsExcluded, 1 << 1
        )
        self.assertEqual(
            AppKit.NSTextLayoutManagerSegmentOptionsHeadSegmentExtended, 1 << 2
        )
        self.assertEqual(
            AppKit.NSTextLayoutManagerSegmentOptionsTailSegmentExtended, 1 << 3
        )
        self.assertEqual(
            AppKit.NSTextLayoutManagerSegmentOptionsUpstreamAffinity, 1 << 4
        )

    @min_sdk_level("12.0")
    def test_protocols(self):
        self.assertProtocolExists("NSTextLayoutManagerDelegate")

    def test_methods(self):
        self.assertResultIsBOOL(
            TestNSTextLayoutManagerHelper.textLayoutManager_shouldBreakLineBeforeLocation_hyphenating_
        )
        self.assertArgIsBOOL(
            TestNSTextLayoutManagerHelper.textLayoutManager_shouldBreakLineBeforeLocation_hyphenating_,
            2,
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(AppKit.NSTextLayoutManager.usesFontLeading)
        self.assertArgIsBOOL(AppKit.NSTextLayoutManager.setUsesFontLeading_, 0)

        self.assertResultIsBOOL(
            AppKit.NSTextLayoutManager.limitsLayoutForSuspiciousContents
        )
        self.assertArgIsBOOL(
            AppKit.NSTextLayoutManager.setLimitsLayoutForSuspiciousContents_, 0
        )

        self.assertResultIsBOOL(AppKit.NSTextLayoutManager.usesHyphenation)
        self.assertArgIsBOOL(AppKit.NSTextLayoutManager.setUsesHyphenation_, 0)

        self.assertArgIsBlock(
            AppKit.NSTextLayoutManager.enumerateTextLayoutFragmentsFromLocation_options_usingBlock_,
            2,
            b"Z@",
        )

        self.assertArgIsBOOL(
            AppKit.NSTextLayoutManager.enumerateRenderingAttributesFromLocation_reverse_usingBlock_,
            1,
        )
        self.assertArgIsBlock(
            AppKit.NSTextLayoutManager.enumerateRenderingAttributesFromLocation_reverse_usingBlock_,
            2,
            b"Z@@@",
        )

        self.assertArgIsBlock(
            AppKit.NSTextLayoutManager.enumerateTextSegmentsInRange_type_options_usingBlock_,
            3,
            b"Z@" + AppKit.NSRect.__typestr__ + b"d@",
        )
