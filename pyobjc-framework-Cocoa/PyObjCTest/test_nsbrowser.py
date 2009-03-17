
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



if __name__ == "__main__":
    main()
