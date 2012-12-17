
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSTableViewHelper (NSObject):
    def tableView_viewForTableColumn_row_(self, a, b, c): pass
    def tableView_rowViewForRow_(self, a, b): pass
    def tableView_didAddRowView_forRow_(self, a, b, c): pass
    def tableView_didRemoveRowView_forRow_(self, a, b, c): pass
    def tableView_pastboardWriterForRow_(self, a, b): pass
    def tableView_draggingSession_willBeginAtPoint_forRowIndexes_(self, a, b, c, d): pass
    def tableView_draggingSession_endedAtPoint_operation_(self, a, b, c, d): pass

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

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(NSTableViewDashedHorizontalGridLineMask, 1<<3)
        self.assertEqual(NSTableViewRowSizeStyleDefault, -1)
        self.assertEqual(NSTableViewRowSizeStyleCustom, 0)
        self.assertEqual(NSTableViewRowSizeStyleSmall, 1)
        self.assertEqual(NSTableViewRowSizeStyleMedium, 2)
        self.assertEqual(NSTableViewRowSizeStyleLarge, 3)

        self.assertEqual(NSTableViewAnimationEffectNone, 0)
        self.assertEqual(NSTableViewAnimationEffectFade, 1)
        self.assertEqual(NSTableViewAnimationEffectGap, 2)
        self.assertEqual(NSTableViewAnimationSlideUp, 0x10)
        self.assertEqual(NSTableViewAnimationSlideDown, 0x20)
        self.assertEqual(NSTableViewAnimationSlideLeft, 0x30)
        self.assertEqual(NSTableViewAnimationSlideRight, 0x40)

        self.assertIsInstance(NSTableViewRowViewKey, unicode)

        self.assertEqual(NSTableViewDashedHorizontalGridLineMask, 1<<3)

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

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertArgIsBOOL(NSTableView.viewAtColumn_row_makeIfNecessary_, 2)
        self.assertArgIsBOOL(NSTableView.rowViewAtRow_makeIfNecessary_, 1)

        self.assertArgIsBlock(NSTableView.enumerateAvailableRowViewsUsingBlock_, 0, b'v@' + objc._C_NSInteger)

        self.assertResultIsBOOL(NSTableView.floatsGroupRows)
        self.assertArgIsBOOL(NSTableView.setFloatsGroupRows_, 0)

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

    @min_os_level('10.7')
    def testProtococols10_7(self):
        self.assertArgHasType(TestNSTableViewHelper.tableView_viewForTableColumn_row_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_rowViewForRow_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_didAddRowView_forRow_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_didRemoveRowView_forRow_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_pastboardWriterForRow_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSTableViewHelper.tableView_draggingSession_willBeginAtPoint_forRowIndexes_, 2, NSPoint.__typestr__)
        self.assertArgHasType(TestNSTableViewHelper.tableView_draggingSession_endedAtPoint_operation_, 2, NSPoint.__typestr__)


if __name__ == "__main__":
    main()
