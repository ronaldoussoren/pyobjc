
from PyObjCTools.TestSupport import *
from AppKit import *

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

class TestNSSplitView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSSplitViewDividerStyleThick, 1)
        self.failUnlessEqual(NSSplitViewDividerStyleThin, 2)

        self.failUnlessIsInstance(NSSplitViewWillResizeSubviewsNotification, unicode)
        self.failUnlessIsInstance(NSSplitViewDidResizeSubviewsNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSplitView.isVertical)
        self.failUnlessArgIsBOOL(NSSplitView.setVertical_, 0)
        self.failUnlessResultIsBOOL(NSSplitView.isSubviewCollapsed_)
        self.failUnlessResultIsBOOL(NSSplitView.isPaneSplitter)
        self.failUnlessArgIsBOOL(NSSplitView.setIsPaneSplitter_, 0)

    def testProtocol(self):
        self.failUnlessResultIsBOOL(TestNSSplitViewHelper.splitView_canCollapseSubview_)
        self.failUnlessResultIsBOOL(TestNSSplitViewHelper.splitView_shouldCollapseSubview_forDoubleClickOnDividerAtIndex_)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_shouldCollapseSubview_forDoubleClickOnDividerAtIndex_, 2, objc._C_NSInteger)
        self.failUnlessResultHasType(TestNSSplitViewHelper.splitView_constrainMinCoordinate_ofSubviewAt_, objc._C_CGFloat)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_constrainMinCoordinate_ofSubviewAt_, 1, objc._C_CGFloat)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_constrainMinCoordinate_ofSubviewAt_, 2, objc._C_NSInteger)
        self.failUnlessResultHasType(TestNSSplitViewHelper.splitView_constrainMaxCoordinate_ofSubviewAt_, objc._C_CGFloat)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_constrainMaxCoordinate_ofSubviewAt_, 1, objc._C_CGFloat)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_constrainMaxCoordinate_ofSubviewAt_, 2, objc._C_NSInteger)
        self.failUnlessResultHasType(TestNSSplitViewHelper.splitView_constrainSplitPosition_ofSubviewAt_, objc._C_CGFloat)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_constrainSplitPosition_ofSubviewAt_, 1, objc._C_CGFloat)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_constrainSplitPosition_ofSubviewAt_, 2, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_resizeSubviewsWithOldSize_, 1, NSSize.__typestr__)

    @min_os_level('10.5')
    def testProtocol10_5(self):
        self.failUnlessResultIsBOOL(TestNSSplitViewHelper.splitView_shouldHideDividerAtIndex_)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_shouldHideDividerAtIndex_, 1, objc._C_NSInteger)

        self.failUnlessResultHasType(TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_, 1, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_, 2, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_effectiveRect_forDrawnRect_ofDividerAtIndex_, 3, objc._C_NSInteger)

        self.failUnlessResultHasType(TestNSSplitViewHelper.splitView_additionalEffectiveRectOfDividerAtIndex_, NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSSplitViewHelper.splitView_additionalEffectiveRectOfDividerAtIndex_, 1, objc._C_NSInteger)

if __name__ == "__main__":
    main()
