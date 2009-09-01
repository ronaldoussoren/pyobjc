
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSBrowserHelper (NSObject):
    def browser_selectCellWithString_inColumn_(self, b, c, s): return 1
    def browser_selectRow_inColumn_(self, b, r, c): return 1
    def browser_isColumnValid_(self, b, c): return 1
    def browser_shouldSizeColumn_forUserResize_toWidth_(self, b, c, us, w): return 1
    def browser_shouldShowCellExpansionForRow_column_(self, b, r, c): return 1
    def browser_writeRowsWithIndexes_inColumn_toPasteboard_(self, b, r, c, p): return 1
    def browser_canDragRowsWithIndexes_inColumn_withEvent_(self, b, i, c, e): return 1
    def browser_acceptDrop_atRow_column_dropOperation_(self, b, a, r, c, o): return 1
    def browser_shouldTypeSelectForEvent_withCurrentSearchString_(self, b, e, s): return 1
    def browser_isLeafItem_(self, b, s): return 1
    def browser_heightOfRow_inColumn_(self, b, r, c): return 1
    def browser_shouldEditItem_(self, b, i): return 1
    def browser_numberOfRowsInColumn_(self, b, c): return 1
    def browser_createRowsForColumn_inMatrix_(self, b, c, m): return 1

class TestNSBrowser (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSBrowserNoColumnResizing, 0)
        self.failUnlessEqual(NSBrowserAutoColumnResizing, 1)
        self.failUnlessEqual(NSBrowserUserColumnResizing, 2)

        self.failUnlessEqual(NSBrowserDropOn, 0)
        self.failUnlessEqual(NSBrowserDropAbove, 1)

        self.failUnlessIsInstance(NSBrowserColumnConfigurationDidChangeNotification, unicode)
        self.failUnlessEqual(NSAppKitVersionNumberWithContinuousScrollingBrowser, 680.0)
        self.failUnlessEqual(NSAppKitVersionNumberWithColumnResizingBrowser, 685.0)
        

    def testMethods(self):
        self.failUnlessResultIsBOOL(NSBrowser.isLoaded)
        self.failUnlessResultIsBOOL(NSBrowser.reusesColumns)
        self.failUnlessResultIsBOOL(NSBrowser.hasHorizontalScroller)
        self.failUnlessArgIsBOOL(NSBrowser.setHasHorizontalScroller_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.separatesColumns)
        self.failUnlessArgIsBOOL(NSBrowser.setSeparatesColumns_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.isTitled)
        self.failUnlessArgIsBOOL(NSBrowser.setTitled_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.allowsMultipleSelection)
        self.failUnlessArgIsBOOL(NSBrowser.setAllowsMultipleSelection_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.allowsBranchSelection)
        self.failUnlessArgIsBOOL(NSBrowser.setAllowsBranchSelection_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.allowsEmptySelection)
        self.failUnlessArgIsBOOL(NSBrowser.setAllowsEmptySelection_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.takesTitleFromPreviousColumn)
        self.failUnlessArgIsBOOL(NSBrowser.setTakesTitleFromPreviousColumn_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.acceptsArrowKeys)
        self.failUnlessArgIsBOOL(NSBrowser.setAcceptsArrowKeys_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.sendsActionOnArrowKeys)
        self.failUnlessArgIsBOOL(NSBrowser.setSendsActionOnArrowKeys_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.setPath_)
        self.failUnlessResultIsBOOL(NSBrowser.sendAction)
        self.failUnlessResultIsBOOL(NSBrowser.prefersAllColumnUserResizing)
        self.failUnlessArgIsBOOL(NSBrowser.setPrefersAllColumnUserResizing_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.canDragRowsWithIndexes_inColumn_withEvent_)
        self.failUnlessArgIsBOOL(NSBrowser.setDraggingSourceOperationMask_forLocal_, 1)
        self.failUnlessResultIsBOOL(NSBrowser.allowsTypeSelect)
        self.failUnlessArgIsBOOL(NSBrowser.setAllowsTypeSelect_, 0)

    def testDelegate(self):
        self.failUnlessResultIsBOOL(TestNSBrowserHelper.browser_selectCellWithString_inColumn_)
        self.failUnlessResultIsBOOL(TestNSBrowserHelper.browser_selectRow_inColumn_)
        self.failUnlessResultIsBOOL(TestNSBrowserHelper.browser_isColumnValid_)
        self.failUnlessArgIsBOOL(TestNSBrowserHelper.browser_shouldSizeColumn_forUserResize_toWidth_, 2)
        self.failUnlessResultIsBOOL(TestNSBrowserHelper.browser_shouldShowCellExpansionForRow_column_)
        self.failUnlessResultIsBOOL(TestNSBrowserHelper.browser_writeRowsWithIndexes_inColumn_toPasteboard_)
        self.failUnlessResultIsBOOL(TestNSBrowserHelper.browser_canDragRowsWithIndexes_inColumn_withEvent_)
        self.failUnlessResultIsBOOL(TestNSBrowserHelper.browser_acceptDrop_atRow_column_dropOperation_)

        self.failUnlessResultIsBOOL(TestNSBrowserHelper.browser_shouldTypeSelectForEvent_withCurrentSearchString_)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessArgIsBOOL(NSBrowser.setAutohidesScroller_, 0)
        self.failUnlessResultIsBOOL(NSBrowser.autohidesScroller)
        self.failUnlessResultIsBOOL(NSBrowser.isLeafItem_)
        self.failUnlessResultIsBOOL(NSBrowser.getRow_column_forPoint_)
        self.failUnlessArgIsOut(NSBrowser.getRow_column_forPoint_, 0)
        self.failUnlessArgIsOut(NSBrowser.getRow_column_forPoint_, 1)
        self.failUnlessArgIsBOOL(NSBrowser.editItemAtIndexPath_withEvent_select_, 2)

    @min_os_level('10.6')
    def testDelegate10_6(self):
        self.failUnlessResultIsBOOL(TestNSBrowserHelper.browser_isLeafItem_)
        self.failUnlessResultHasType(TestNSBrowserHelper.browser_heightOfRow_inColumn_, objc._C_CGFloat)
        self.failUnlessArgHasType(TestNSBrowserHelper.browser_heightOfRow_inColumn_, 1, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSBrowserHelper.browser_heightOfRow_inColumn_, 2, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSBrowserHelper.browser_shouldEditItem_)
        self.failUnlessResultHasType(TestNSBrowserHelper.browser_numberOfRowsInColumn_, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSBrowserHelper.browser_numberOfRowsInColumn_, 1, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSBrowserHelper.browser_createRowsForColumn_inMatrix_, 1, objc._C_NSInteger)



if __name__ == "__main__":
    main()
