
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTableViewHelper (NSObject):
    def numberOfRowsInTableView_(self, tv): return 1
    def tableView_objectValueForTableColumn_row_(self, tv, c, r): return 1
    def tableView_setObjectValue_forTableColumn_row_(self, o, tv, c, r): pass
    def tableView_writeRowsWithIndexes_toPasteboard_(self, tv, r, p): return 1
    def tableView_validateDrop_proposedRow_proposedDropOperation_(self, tv, dr, r, o): return 1
    def tableView_acceptDrop_row_dropOperation_(self, tv, dr, r, o): return 1
    def tableView_writeRows_toPasteboard_(self, tv, r, p): return 1

    def tableView_willDisplayCell_forTableColumn_row_(self, tv, c, tc, r): return 1
    def tableView_shouldEditTableColumn_row_(self, tv, tc, r): return 1
    def selectionShouldChangeInTableView_(self, tv): return 1
    def tableView_shouldSelectTableColumn_(self, tv, tc): return 1
    def tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_(self, tv, c, re, tc, r, l): return 1
    def tableView_heightOfRow_(self, tv, r): return 1
    def tableView_typeSelectStringForTableColumn_row_(self, tv, tc, r): return 1
    def tableView_nextTypeSelectMatchFromRow_toRow_forString_(self, tv, r1, r2, s): return 1
    def tableView_shouldTypeSelectForEvent_withCurrentSearchString_(self, tv, e, s): return 1
    def tableView_shouldShowCellExpansionForTableColumn_row_(self, tv, tc, r): return 1
    def tableView_shouldTrackCell_forTableColumn_row_(self, tv, c, tc, r): return 1
    def tableView_dataCellForTableColumn_row_(self, tv, tc, r): return 1
    def tableView_isGroupRow_(self, tv, r): return 1





class TestNSTableView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSTableViewDropOn, 0)
        self.failUnlessEqual(NSTableViewDropAbove, 1)

        self.failUnlessEqual(NSTableViewNoColumnAutoresizing, 0)
        self.failUnlessEqual(NSTableViewUniformColumnAutoresizingStyle, 1)
        self.failUnlessEqual(NSTableViewSequentialColumnAutoresizingStyle, 2)
        self.failUnlessEqual(NSTableViewReverseSequentialColumnAutoresizingStyle, 3)
        self.failUnlessEqual(NSTableViewLastColumnOnlyAutoresizingStyle, 4)
        self.failUnlessEqual(NSTableViewFirstColumnOnlyAutoresizingStyle, 5)

        self.failUnlessEqual(NSTableViewGridNone, 0)
        self.failUnlessEqual(NSTableViewSolidVerticalGridLineMask, 1 << 0)
        self.failUnlessEqual(NSTableViewSolidHorizontalGridLineMask, 1 << 1)

        self.failUnlessEqual(NSTableViewSelectionHighlightStyleRegular, 0)
        self.failUnlessEqual(NSTableViewSelectionHighlightStyleSourceList, 1)

        self.failUnlessIsInstance(NSTableViewSelectionDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSTableViewColumnDidMoveNotification, unicode)
        self.failUnlessIsInstance(NSTableViewColumnDidResizeNotification, unicode)
        self.failUnlessIsInstance(NSTableViewSelectionIsChangingNotification, unicode)


    def testMethods(self):
        self.failUnlessArgIsBOOL(NSTableView.setAllowsColumnReordering_, 0)
        self.failUnlessResultIsBOOL(NSTableView.allowsColumnReordering)
        self.failUnlessArgIsBOOL(NSTableView.setAllowsColumnResizing_, 0)
        self.failUnlessResultIsBOOL(NSTableView.allowsColumnResizing)
        self.failUnlessArgIsBOOL(NSTableView.setUsesAlternatingRowBackgroundColors_, 0)
        self.failUnlessResultIsBOOL(NSTableView.usesAlternatingRowBackgroundColors)
        self.failUnlessArgIsBOOL(NSTableView.setVerticalMotionCanBeginDrag_, 0)
        self.failUnlessResultIsBOOL(NSTableView.verticalMotionCanBeginDrag)
        self.failUnlessResultIsBOOL(NSTableView.canDragRowsWithIndexes_atPoint_)
        self.failUnlessArgIsInOut(NSTableView.dragImageForRowsWithIndexes_tableColumns_event_offset_, 3)
        self.failUnlessArgIsBOOL(NSTableView.setDraggingSourceOperationMask_forLocal_, 1)
        self.failUnlessResultIsBOOL(NSTableView.verticalMotionCanBeginDrag)
        self.failUnlessArgIsBOOL(NSTableView.setAllowsMultipleSelection_, 0)
        self.failUnlessResultIsBOOL(NSTableView.allowsMultipleSelection)
        self.failUnlessArgIsBOOL(NSTableView.setAllowsEmptySelection_, 0)
        self.failUnlessResultIsBOOL(NSTableView.allowsEmptySelection)
        self.failUnlessArgIsBOOL(NSTableView.setAllowsColumnSelection_, 0)
        self.failUnlessResultIsBOOL(NSTableView.allowsColumnSelection)
        self.failUnlessArgIsBOOL(NSTableView.selectColumnIndexes_byExtendingSelection_, 1)
        self.failUnlessArgIsBOOL(NSTableView.selectRowIndexes_byExtendingSelection_, 1)
        self.failUnlessResultIsBOOL(NSTableView.isColumnSelected_)
        self.failUnlessResultIsBOOL(NSTableView.isRowSelected_)
        self.failUnlessArgIsBOOL(NSTableView.setAllowsTypeSelect_, 0)
        self.failUnlessResultIsBOOL(NSTableView.allowsTypeSelect)
        self.failUnlessResultIsBOOL(NSTableView.textShouldBeginEditing_)
        self.failUnlessResultIsBOOL(NSTableView.textShouldEndEditing_)
        self.failUnlessArgIsBOOL(NSTableView.setAutosaveTableColumns_, 0)
        self.failUnlessResultIsBOOL(NSTableView.autosaveTableColumns)
        self.failUnlessArgIsBOOL(NSTableView.editColumn_row_withEvent_select_, 3)


        self.failUnlessArgIsBOOL(NSTableView.setDrawsGrid_, 0)
        self.failUnlessResultIsBOOL(NSTableView.drawsGrid)
        self.failUnlessArgIsBOOL(NSTableView.selectColumn_byExtendingSelection_, 1)
        self.failUnlessArgIsBOOL(NSTableView.selectRow_byExtendingSelection_, 1)
        self.failUnlessArgIsInOut(NSTableView.dragImageForRows_event_dragImageOffset_, 2)
        self.failUnlessArgIsBOOL(NSTableView.setAutoresizesAllColumnsToFit_, 0)
        self.failUnlessResultIsBOOL(NSTableView.autoresizesAllColumnsToFit)


    def testProtocols(self):
        self.failUnlessResultHasType(TestNSTableViewHelper.numberOfRowsInTableView_, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_objectValueForTableColumn_row_, 2, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_setObjectValue_forTableColumn_row_, 3, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSTableViewHelper.tableView_writeRowsWithIndexes_toPasteboard_)
        self.failUnlessResultHasType(TestNSTableViewHelper.tableView_validateDrop_proposedRow_proposedDropOperation_, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_validateDrop_proposedRow_proposedDropOperation_, 2, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_validateDrop_proposedRow_proposedDropOperation_, 3, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestNSTableViewHelper.tableView_acceptDrop_row_dropOperation_)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_acceptDrop_row_dropOperation_, 2, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_acceptDrop_row_dropOperation_, 3, objc._C_NSUInteger)
        self.failUnlessResultIsBOOL(TestNSTableViewHelper.tableView_writeRows_toPasteboard_)


        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_willDisplayCell_forTableColumn_row_, 3, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSTableViewHelper.tableView_shouldEditTableColumn_row_)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_shouldEditTableColumn_row_, 2, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSTableViewHelper.selectionShouldChangeInTableView_)
        self.failUnlessResultIsBOOL(TestNSTableViewHelper.tableView_shouldSelectTableColumn_)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_, 2, 'N^' + NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_, 4, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_, 5, NSPoint.__typestr__)
        self.failUnlessResultHasType(TestNSTableViewHelper.tableView_heightOfRow_, objc._C_CGFloat)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_heightOfRow_, 1, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_typeSelectStringForTableColumn_row_, 2, objc._C_NSInteger)
        self.failUnlessResultHasType(TestNSTableViewHelper.tableView_nextTypeSelectMatchFromRow_toRow_forString_, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_nextTypeSelectMatchFromRow_toRow_forString_, 1, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_nextTypeSelectMatchFromRow_toRow_forString_, 2, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSTableViewHelper.tableView_shouldTypeSelectForEvent_withCurrentSearchString_)
        self.failUnlessResultIsBOOL(TestNSTableViewHelper.tableView_shouldShowCellExpansionForTableColumn_row_)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_shouldShowCellExpansionForTableColumn_row_, 2, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSTableViewHelper.tableView_shouldTrackCell_forTableColumn_row_)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_shouldTrackCell_forTableColumn_row_, 3, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_dataCellForTableColumn_row_, 2, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSTableViewHelper.tableView_isGroupRow_)
        self.failUnlessArgHasType(TestNSTableViewHelper.tableView_isGroupRow_, 1, objc._C_NSInteger)



if __name__ == "__main__":
    main()
