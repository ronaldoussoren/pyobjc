
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

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
    def browser_selectionIndexesForProposedSelection_inColumn_(self, b, s, c): return 1

class TestNSBrowser (TestCase):
    def testConstants(self):
        self.assertEqual(NSBrowserNoColumnResizing, 0)
        self.assertEqual(NSBrowserAutoColumnResizing, 1)
        self.assertEqual(NSBrowserUserColumnResizing, 2)

        self.assertEqual(NSBrowserDropOn, 0)
        self.assertEqual(NSBrowserDropAbove, 1)

        self.assertIsInstance(NSBrowserColumnConfigurationDidChangeNotification, unicode)
        self.assertEqual(NSAppKitVersionNumberWithContinuousScrollingBrowser, 680.0)
        self.assertEqual(NSAppKitVersionNumberWithColumnResizingBrowser, 685.0)


    def testMethods(self):
        self.assertResultIsBOOL(NSBrowser.isLoaded)
        self.assertResultIsBOOL(NSBrowser.reusesColumns)
        self.assertArgIsBOOL(NSBrowser.setReusesColumns_, 0)
        self.assertResultIsBOOL(NSBrowser.hasHorizontalScroller)
        self.assertArgIsBOOL(NSBrowser.setHasHorizontalScroller_, 0)
        self.assertResultIsBOOL(NSBrowser.separatesColumns)
        self.assertArgIsBOOL(NSBrowser.setSeparatesColumns_, 0)
        self.assertResultIsBOOL(NSBrowser.isTitled)
        self.assertArgIsBOOL(NSBrowser.setTitled_, 0)
        self.assertResultIsBOOL(NSBrowser.allowsMultipleSelection)
        self.assertArgIsBOOL(NSBrowser.setAllowsMultipleSelection_, 0)
        self.assertResultIsBOOL(NSBrowser.allowsBranchSelection)
        self.assertArgIsBOOL(NSBrowser.setAllowsBranchSelection_, 0)
        self.assertResultIsBOOL(NSBrowser.allowsEmptySelection)
        self.assertArgIsBOOL(NSBrowser.setAllowsEmptySelection_, 0)
        self.assertResultIsBOOL(NSBrowser.takesTitleFromPreviousColumn)
        self.assertArgIsBOOL(NSBrowser.setTakesTitleFromPreviousColumn_, 0)
        self.assertResultIsBOOL(NSBrowser.acceptsArrowKeys)
        self.assertArgIsBOOL(NSBrowser.setAcceptsArrowKeys_, 0)
        self.assertResultIsBOOL(NSBrowser.sendsActionOnArrowKeys)
        self.assertArgIsBOOL(NSBrowser.setSendsActionOnArrowKeys_, 0)
        self.assertResultIsBOOL(NSBrowser.setPath_)
        self.assertResultIsBOOL(NSBrowser.sendAction)
        self.assertResultIsBOOL(NSBrowser.prefersAllColumnUserResizing)
        self.assertArgIsBOOL(NSBrowser.setPrefersAllColumnUserResizing_, 0)
        self.assertResultIsBOOL(NSBrowser.canDragRowsWithIndexes_inColumn_withEvent_)
        self.assertArgIsBOOL(NSBrowser.setDraggingSourceOperationMask_forLocal_, 1)
        self.assertResultIsBOOL(NSBrowser.allowsTypeSelect)
        self.assertArgIsBOOL(NSBrowser.setAllowsTypeSelect_, 0)

    def testDelegate(self):
        self.assertResultIsBOOL(TestNSBrowserHelper.browser_selectCellWithString_inColumn_)
        self.assertResultIsBOOL(TestNSBrowserHelper.browser_selectRow_inColumn_)
        self.assertResultIsBOOL(TestNSBrowserHelper.browser_isColumnValid_)
        self.assertArgIsBOOL(TestNSBrowserHelper.browser_shouldSizeColumn_forUserResize_toWidth_, 2)
        self.assertResultIsBOOL(TestNSBrowserHelper.browser_shouldShowCellExpansionForRow_column_)
        self.assertResultIsBOOL(TestNSBrowserHelper.browser_writeRowsWithIndexes_inColumn_toPasteboard_)
        self.assertResultIsBOOL(TestNSBrowserHelper.browser_canDragRowsWithIndexes_inColumn_withEvent_)
        self.assertResultIsBOOL(TestNSBrowserHelper.browser_acceptDrop_atRow_column_dropOperation_)

        self.assertResultIsBOOL(TestNSBrowserHelper.browser_shouldTypeSelectForEvent_withCurrentSearchString_)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBOOL(NSBrowser.setAutohidesScroller_, 0)
        self.assertResultIsBOOL(NSBrowser.autohidesScroller)
        self.assertResultIsBOOL(NSBrowser.isLeafItem_)
        self.assertResultIsBOOL(NSBrowser.getRow_column_forPoint_)
        self.assertArgIsOut(NSBrowser.getRow_column_forPoint_, 0)
        self.assertArgIsOut(NSBrowser.getRow_column_forPoint_, 1)
        self.assertArgIsBOOL(NSBrowser.editItemAtIndexPath_withEvent_select_, 2)

        self.assertArgHasType(TestNSBrowserHelper.browser_selectionIndexesForProposedSelection_inColumn_, 2, objc._C_NSInteger)

    @min_os_level('10.6')
    def testDelegate10_6(self):
        self.assertResultIsBOOL(TestNSBrowserHelper.browser_isLeafItem_)
        self.assertResultHasType(TestNSBrowserHelper.browser_heightOfRow_inColumn_, objc._C_CGFloat)
        self.assertArgHasType(TestNSBrowserHelper.browser_heightOfRow_inColumn_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSBrowserHelper.browser_heightOfRow_inColumn_, 2, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSBrowserHelper.browser_shouldEditItem_)
        self.assertResultHasType(TestNSBrowserHelper.browser_numberOfRowsInColumn_, objc._C_NSInteger)
        self.assertArgHasType(TestNSBrowserHelper.browser_numberOfRowsInColumn_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSBrowserHelper.browser_createRowsForColumn_inMatrix_, 1, objc._C_NSInteger)



if __name__ == "__main__":
    main()
