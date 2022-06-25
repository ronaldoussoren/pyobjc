import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSSplitViewHelper(AppKit.NSObject):
    def splitView_canCollapseSubview_(self, sp, sv):
        return 1

    def splitView_shouldCollapseSubview_forDoubleClickOnDividerAtIndex_(
        self, sp, sv, i
    ):
        return 1

    def splitView_constrainMinCoordinate_ofSubviewAt_(self, sv, c, i):
        return 1

    def splitView_constrainMaxCoordinate_ofSubviewAt_(self, sv, c, i):
        return 1

    def splitView_constrainSplitPosition_ofSubviewAt_(self, sv, c, i):
        return 1

    def splitView_resizeSubviewsWithOldSize_(self, sv, sz):
        pass

    def splitView_shouldHideDividerAtIndex_(self, sv, i):
        return 1

    def splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_(self, sv, er, dr, i):
        return 1

    def splitView_additionalEffectiveRectOfDividerAtIndex_(self, sv, i):
        return 1

    def splitViewWillResizeSubviews_(self, nt):
        pass

    def splitViewDidResizeSubviews_(self, nt):
        pass

    def splitView_shouldAdjustSizeOfSubview_(self, s, sv):
        return 1


class TestNSSplitView(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSSplitViewDividerStyle)

    def testConstants(self):
        self.assertEqual(AppKit.NSSplitViewDividerStyleThick, 1)
        self.assertEqual(AppKit.NSSplitViewDividerStyleThin, 2)

        self.assertIsInstance(AppKit.NSSplitViewWillResizeSubviewsNotification, str)
        self.assertIsInstance(AppKit.NSSplitViewDidResizeSubviewsNotification, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSSplitViewDividerStylePaneSplitter, 3)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSplitView.isVertical)
        self.assertArgIsBOOL(AppKit.NSSplitView.setVertical_, 0)
        self.assertResultIsBOOL(AppKit.NSSplitView.isSubviewCollapsed_)
        self.assertResultIsBOOL(AppKit.NSSplitView.isPaneSplitter)
        self.assertArgIsBOOL(AppKit.NSSplitView.setIsPaneSplitter_, 0)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AppKit.NSSplitView.arrangesAllSubviews)
        self.assertArgIsBOOL(AppKit.NSSplitView.setArrangesAllSubviews_, 0)

    @min_sdk_level("10.7")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSSplitViewDelegate")

    def testProtocol(self):
        self.assertResultIsBOOL(TestNSSplitViewHelper.splitView_canCollapseSubview_)
        self.assertResultIsBOOL(
            TestNSSplitViewHelper.splitView_shouldCollapseSubview_forDoubleClickOnDividerAtIndex_  # noqa: B950
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_shouldCollapseSubview_forDoubleClickOnDividerAtIndex_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSSplitViewHelper.splitView_constrainMinCoordinate_ofSubviewAt_,
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_constrainMinCoordinate_ofSubviewAt_,
            1,
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_constrainMinCoordinate_ofSubviewAt_,
            2,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSSplitViewHelper.splitView_constrainMaxCoordinate_ofSubviewAt_,
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_constrainMaxCoordinate_ofSubviewAt_,
            1,
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_constrainMaxCoordinate_ofSubviewAt_,
            2,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSSplitViewHelper.splitView_constrainSplitPosition_ofSubviewAt_,
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_constrainSplitPosition_ofSubviewAt_,
            1,
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_constrainSplitPosition_ofSubviewAt_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_resizeSubviewsWithOldSize_,
            1,
            AppKit.NSSize.__typestr__,
        )

    @min_os_level("10.5")
    def testProtocol10_5(self):
        self.assertResultIsBOOL(
            TestNSSplitViewHelper.splitView_shouldHideDividerAtIndex_
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_shouldHideDividerAtIndex_,
            1,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_,
            1,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_,
            2,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_,
            3,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestNSSplitViewHelper.splitView_additionalEffectiveRectOfDividerAtIndex_,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSSplitViewHelper.splitView_additionalEffectiveRectOfDividerAtIndex_,
            1,
            objc._C_NSInteger,
        )

    @min_os_level("10.6")
    def testProtocol10_6(self):
        self.assertResultIsBOOL(
            TestNSSplitViewHelper.splitView_shouldAdjustSizeOfSubview_
        )
