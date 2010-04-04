
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

    def tableView_sizeToFitWidthOfColumn_(self, tv, c): return 1
    def tableView_shouldReorderColumn_toColumn_(self, tv, c1, c2): return 1





class TestNSTableView (TestCase):
    def testConstants(self):
        self.assertEqual(NSTableViewDropOn, 0)
        self.assertEqual(NSTableViewDropAbove, 1)

        self.assertEqual(NSTableViewNoColumnAutoresizing, 0)
        self.assertEqual(NSTableViewUniformColumnAutoresizingStyle, 1)
        self.assertEqual(NSTableViewSequentialColumnAutoresizingStyle, 2)
        self.assertEqual(NSTableViewReverseSequentialColumnAutoresizingStyle, 3)
        self.assertEqual(NSTableViewLastColumnOnlyAutoresizingStyle, 4)
        self.assertEqual(NSTableViewFirstColumnOnlyAutoresizingStyle, 5)

        self.assertEqual(NSTableViewGridNone, 0)
        self.assertEqual(NSTableViewSolidVerticalGridLineMask, 1 << 0)
        self.assertEqual(NSTableViewSolidHorizontalGridLineMask, 1 << 1)

        self.assertEqual(NSTableViewSelectionHighlightStyleRegular, 0)
        self.assertEqual(NSTableViewSelectionHighlightStyleSourceList, 1)

        self.assertIsInstance(NSTableViewSelectionDidChangeNotification, unicode)
        self.assertIsInstance(NSTableViewColumnDidMoveNotification, unicode)
        self.assertIsInstance(NSTableViewColumnDidResizeNotification, unicode)
        self.assertIsInstance(NSTableViewSelectionIsChangingNotification, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSTableViewSelectionHighlightStyleNone, -1)
        self.assertEqual(NSTableViewDraggingDestinationFeedbackStyleNone, -1)
        self.assertEqual(NSTableViewDraggingDestinationFeedbackStyleRegular, 0)
        self.assertEqual(NSTableViewDraggingDestinationFeedbackStyleSourceList, 1)

    def testMethods(self):
        self.assertArgIsBOOL(NSTableView.setAllowsColumnReordering_, 0)
        self.assertResultIsBOOL(NSTableView.allowsColumnReordering)
        self.assertArgIsBOOL(NSTableView.setAllowsColumnResizing_, 0)
        self.assertResultIsBOOL(NSTableView.allowsColumnResizing)
        self.assertArgIsBOOL(NSTableView.setUsesAlternatingRowBackgroundColors_, 0)
        self.assertResultIsBOOL(NSTableView.usesAlternatingRowBackgroundColors)
        self.assertArgIsBOOL(NSTableView.setVerticalMotionCanBeginDrag_, 0)
        self.assertResultIsBOOL(NSTableView.verticalMotionCanBeginDrag)
        self.assertResultIsBOOL(NSTableView.canDragRowsWithIndexes_atPoint_)
        self.assertArgIsInOut(NSTableView.dragImageForRowsWithIndexes_tableColumns_event_offset_, 3)
        self.assertArgIsBOOL(NSTableView.setDraggingSourceOperationMask_forLocal_, 1)
        self.assertResultIsBOOL(NSTableView.verticalMotionCanBeginDrag)
        self.assertArgIsBOOL(NSTableView.setAllowsMultipleSelection_, 0)
        self.assertResultIsBOOL(NSTableView.allowsMultipleSelection)
        self.assertArgIsBOOL(NSTableView.setAllowsEmptySelection_, 0)
        self.assertResultIsBOOL(NSTableView.allowsEmptySelection)
        self.assertArgIsBOOL(NSTableView.setAllowsColumnSelection_, 0)
        self.assertResultIsBOOL(NSTableView.allowsColumnSelection)
        self.assertArgIsBOOL(NSTableView.selectColumnIndexes_byExtendingSelection_, 1)
        self.assertArgIsBOOL(NSTableView.selectRowIndexes_byExtendingSelection_, 1)
        self.assertResultIsBOOL(NSTableView.isColumnSelected_)
        self.assertResultIsBOOL(NSTableView.isRowSelected_)
        self.assertResultIsBOOL(NSTableView.textShouldBeginEditing_)
        self.assertResultIsBOOL(NSTableView.textShouldEndEditing_)
        self.assertArgIsBOOL(NSTableView.setAutosaveTableColumns_, 0)
        self.assertResultIsBOOL(NSTableView.autosaveTableColumns)
        self.assertArgIsBOOL(NSTableView.editColumn_row_withEvent_select_, 3)

        self.assertArgHasType(NSTableView.drawBackgroundInClipRect_, 0, NSRect.__typestr__)



        self.assertArgIsBOOL(NSTableView.setDrawsGrid_, 0)
        self.assertResultIsBOOL(NSTableView.drawsGrid)
        self.assertArgIsBOOL(NSTableView.selectColumn_byExtendingSelection_, 1)
        self.assertArgIsBOOL(NSTableView.selectRow_byExtendingSelection_, 1)
        self.assertArgIsInOut(NSTableView.dragImageForRows_event_dragImageOffset_, 2)
        self.assertArgIsBOOL(NSTableView.setAutoresizesAllColumnsToFit_, 0)
        self.assertResultIsBOOL(NSTableView.autoresizesAllColumnsToFit)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertArgIsBOOL(NSTableView.setAllowsTypeSelect_, 0)
        self.assertResultIsBOOL(NSTableView.allowsTypeSelect)

        self.assertArgHasType(NSTableView.columnIndexesInRect_, 0, NSRect.__typestr__)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSTableView.shouldFocusCell_atColumn_row_)


    def testProtocols(self):
        self.assertResultHasType(TestNSTableViewHelper.numberOfRowsInTableView_, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_objectValueForTableColumn_row_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_setObjectValue_forTableColumn_row_, 3, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_writeRowsWithIndexes_toPasteboard_)
        self.assertResultHasType(TestNSTableViewHelper.tableView_validateDrop_proposedRow_proposedDropOperation_, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_validateDrop_proposedRow_proposedDropOperation_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_validateDrop_proposedRow_proposedDropOperation_, 3, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_acceptDrop_row_dropOperation_)
        self.assertArgHasType(TestNSTableViewHelper.tableView_acceptDrop_row_dropOperation_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_acceptDrop_row_dropOperation_, 3, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_writeRows_toPasteboard_)


        self.assertArgHasType(TestNSTableViewHelper.tableView_willDisplayCell_forTableColumn_row_, 3, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_shouldEditTableColumn_row_)
        self.assertArgHasType(TestNSTableViewHelper.tableView_shouldEditTableColumn_row_, 2, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSTableViewHelper.selectionShouldChangeInTableView_)
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_shouldSelectTableColumn_)
        self.assertArgHasType(TestNSTableViewHelper.tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_, 2, b'N^' + NSRect.__typestr__)
        self.assertArgHasType(TestNSTableViewHelper.tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_, 4, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_, 5, NSPoint.__typestr__)
        self.assertResultHasType(TestNSTableViewHelper.tableView_heightOfRow_, objc._C_CGFloat)
        self.assertArgHasType(TestNSTableViewHelper.tableView_heightOfRow_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_typeSelectStringForTableColumn_row_, 2, objc._C_NSInteger)
        self.assertResultHasType(TestNSTableViewHelper.tableView_nextTypeSelectMatchFromRow_toRow_forString_, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_nextTypeSelectMatchFromRow_toRow_forString_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_nextTypeSelectMatchFromRow_toRow_forString_, 2, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_shouldTypeSelectForEvent_withCurrentSearchString_)
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_shouldShowCellExpansionForTableColumn_row_)
        self.assertArgHasType(TestNSTableViewHelper.tableView_shouldShowCellExpansionForTableColumn_row_, 2, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_shouldTrackCell_forTableColumn_row_)
        self.assertArgHasType(TestNSTableViewHelper.tableView_shouldTrackCell_forTableColumn_row_, 3, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_dataCellForTableColumn_row_, 2, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_isGroupRow_)
        self.assertArgHasType(TestNSTableViewHelper.tableView_isGroupRow_, 1, objc._C_NSInteger)

    @min_os_level('10.6')
    def testProtococols10_6(self):
        self.assertResultHasType(TestNSTableViewHelper.tableView_sizeToFitWidthOfColumn_, objc._C_CGFloat)
        self.assertArgHasType(TestNSTableViewHelper.tableView_sizeToFitWidthOfColumn_, 1, objc._C_NSInteger)

        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_shouldReorderColumn_toColumn_)
        self.assertArgHasType(TestNSTableViewHelper.tableView_shouldReorderColumn_toColumn_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_shouldReorderColumn_toColumn_, 2, objc._C_NSInteger)

if __name__ == "__main__":
    main()
