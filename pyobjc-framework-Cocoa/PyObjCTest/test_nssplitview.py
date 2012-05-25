
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSSplitViewHelper (NSObject):
    def splitView_canCollapseSubview_(self, sp, sv): return 1
    def splitView_shouldCollapseSubview_forDoubleClickOnDividerAtIndex_(self, sp, sv, i): return 1
    def splitView_constrainMinCoordinate_ofSubviewAt_(self, sv, c, i): return 1
    def splitView_constrainMaxCoordinate_ofSubviewAt_(self, sv, c, i): return 1
    def splitView_constrainSplitPosition_ofSubviewAt_(self, sv, c, i): return 1
    def splitView_resizeSubviewsWithOldSize_(self, sv, sz): pass
    def splitView_shouldHideDividerAtIndex_(self, sv, i): return 1
    def splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_(self, sv, er, dr, i): return 1
    def splitView_additionalEffectiveRectOfDividerAtIndex_(self, sv, i): return 1
    def splitViewWillResizeSubviews_(self, nt): pass
    def splitViewDidResizeSubviews_(self, nt): pass
    def splitView_shouldAdjustSizeOfSubview_(self, s, sv): return 1

class TestNSSplitView (TestCase):
    def testConstants(self):
        self.assertEqual(NSSplitViewDividerStyleThick, 1)
        self.assertEqual(NSSplitViewDividerStyleThin, 2)

        self.assertIsInstance(NSSplitViewWillResizeSubviewsNotification, unicode)
        self.assertIsInstance(NSSplitViewDidResizeSubviewsNotification, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSSplitViewDividerStylePaneSplitter, 3)


    def testMethods(self):
        self.assertResultIsBOOL(NSSplitView.isVertical)
        self.assertArgIsBOOL(NSSplitView.setVertical_, 0)
        self.assertResultIsBOOL(NSSplitView.isSubviewCollapsed_)
        self.assertResultIsBOOL(NSSplitView.isPaneSplitter)
        self.assertArgIsBOOL(NSSplitView.setIsPaneSplitter_, 0)

    def testProtocol(self):
        self.assertResultIsBOOL(TestNSSplitViewHelper.splitView_canCollapseSubview_)
        self.assertResultIsBOOL(TestNSSplitViewHelper.splitView_shouldCollapseSubview_forDoubleClickOnDividerAtIndex_)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_shouldCollapseSubview_forDoubleClickOnDividerAtIndex_, 2, objc._C_NSInteger)
        self.assertResultHasType(TestNSSplitViewHelper.splitView_constrainMinCoordinate_ofSubviewAt_, objc._C_CGFloat)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_constrainMinCoordinate_ofSubviewAt_, 1, objc._C_CGFloat)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_constrainMinCoordinate_ofSubviewAt_, 2, objc._C_NSInteger)
        self.assertResultHasType(TestNSSplitViewHelper.splitView_constrainMaxCoordinate_ofSubviewAt_, objc._C_CGFloat)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_constrainMaxCoordinate_ofSubviewAt_, 1, objc._C_CGFloat)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_constrainMaxCoordinate_ofSubviewAt_, 2, objc._C_NSInteger)
        self.assertResultHasType(TestNSSplitViewHelper.splitView_constrainSplitPosition_ofSubviewAt_, objc._C_CGFloat)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_constrainSplitPosition_ofSubviewAt_, 1, objc._C_CGFloat)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_constrainSplitPosition_ofSubviewAt_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_resizeSubviewsWithOldSize_, 1, NSSize.__typestr__)

    @min_os_level('10.5')
    def testProtocol10_5(self):
        self.assertResultIsBOOL(TestNSSplitViewHelper.splitView_shouldHideDividerAtIndex_)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_shouldHideDividerAtIndex_, 1, objc._C_NSInteger)

        self.assertResultHasType(TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_, NSRect.__typestr__)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_, 1, NSRect.__typestr__)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_, 2, NSRect.__typestr__)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_, 3, objc._C_NSInteger)

        self.assertResultHasType(TestNSSplitViewHelper.splitView_additionalEffectiveRectOfDividerAtIndex_, NSRect.__typestr__)
        self.assertArgHasType(TestNSSplitViewHelper.splitView_additionalEffectiveRectOfDividerAtIndex_, 1, objc._C_NSInteger)

    @min_os_level('10.6')
    def testProtocol10_6(self):
        self.assertResultIsBOOL(TestNSSplitViewHelper.splitView_shouldAdjustSizeOfSubview_)

if __name__ == "__main__":
    main()
