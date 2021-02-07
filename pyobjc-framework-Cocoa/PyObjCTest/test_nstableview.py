import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSTableViewHelper(AppKit.NSObject):
    def tableView_rowActionsForRow_edge_(self, a, b, c):
        pass

    def tableView_viewForTableColumn_row_(self, a, b, c):
        pass

    def tableView_rowViewForRow_(self, a, b):
        pass

    def tableView_didAddRowView_forRow_(self, a, b, c):
        pass

    def tableView_didRemoveRowView_forRow_(self, a, b, c):
        pass

    def tableView_draggingSession_willBeginAtPoint_forRowIndexes_(self, a, b, c, d):
        pass

    def tableView_draggingSession_endedAtPoint_operation_(self, a, b, c, d):
        pass

    def numberOfRowsInTableView_(self, tv):
        return 1

    def tableView_objectValueForTableColumn_row_(self, tv, c, r):
        return 1

    def tableView_setObjectValue_forTableColumn_row_(self, o, tv, c, r):
        pass

    def tableView_writeRowsWithIndexes_toPasteboard_(self, tv, r, p):
        return 1

    def tableView_validateDrop_proposedRow_proposedDropOperation_(self, tv, dr, r, o):
        return 1

    def tableView_acceptDrop_row_dropOperation_(self, tv, dr, r, o):
        return 1

    def tableView_writeRows_toPasteboard_(self, tv, r, p):
        return 1

    def tableView_willDisplayCell_forTableColumn_row_(self, tv, c, tc, r):
        return 1

    def tableView_shouldEditTableColumn_row_(self, tv, tc, r):
        return 1

    def selectionShouldChangeInTableView_(self, tv):
        return 1

    def tableView_shouldSelectRow_(self, tv, r):
        return 1

    def tableView_shouldSelectTableColumn_(self, tv, tc):
        return 1

    def tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_(
        self, tv, c, re, tc, r, l
    ):
        return 1

    def tableView_heightOfRow_(self, tv, r):
        return 1

    def tableView_typeSelectStringForTableColumn_row_(self, tv, tc, r):
        return 1

    def tableView_nextTypeSelectMatchFromRow_toRow_forString_(self, tv, r1, r2, s):
        return 1

    def tableView_shouldTypeSelectForEvent_withCurrentSearchString_(self, tv, e, s):
        return 1

    def tableView_shouldShowCellExpansionForTableColumn_row_(self, tv, tc, r):
        return 1

    def tableView_shouldTrackCell_forTableColumn_row_(self, tv, c, tc, r):
        return 1

    def tableView_dataCellForTableColumn_row_(self, tv, tc, r):
        return 1

    def tableView_isGroupRow_(self, tv, r):
        return 1

    def tableView_sizeToFitWidthOfColumn_(self, tv, c):
        return 1

    def tableView_shouldReorderColumn_toColumn_(self, tv, c1, c2):
        return 1

    def tableView_pasteboardWriterForRow_(self, tv, r):
        return 1


class TestNSTableView(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSTableViewDropOn, 0)
        self.assertEqual(AppKit.NSTableViewDropAbove, 1)

        self.assertEqual(AppKit.NSTableViewNoColumnAutoresizing, 0)
        self.assertEqual(AppKit.NSTableViewUniformColumnAutoresizingStyle, 1)
        self.assertEqual(AppKit.NSTableViewSequentialColumnAutoresizingStyle, 2)
        self.assertEqual(AppKit.NSTableViewReverseSequentialColumnAutoresizingStyle, 3)
        self.assertEqual(AppKit.NSTableViewLastColumnOnlyAutoresizingStyle, 4)
        self.assertEqual(AppKit.NSTableViewFirstColumnOnlyAutoresizingStyle, 5)

        self.assertEqual(AppKit.NSTableViewGridNone, 0)
        self.assertEqual(AppKit.NSTableViewSolidVerticalGridLineMask, 1 << 0)
        self.assertEqual(AppKit.NSTableViewSolidHorizontalGridLineMask, 1 << 1)

        self.assertEqual(AppKit.NSTableViewSelectionHighlightStyleRegular, 0)
        self.assertEqual(AppKit.NSTableViewSelectionHighlightStyleSourceList, 1)

        self.assertIsInstance(AppKit.NSTableViewSelectionDidChangeNotification, str)
        self.assertIsInstance(AppKit.NSTableViewColumnDidMoveNotification, str)
        self.assertIsInstance(AppKit.NSTableViewColumnDidResizeNotification, str)
        self.assertIsInstance(AppKit.NSTableViewSelectionIsChangingNotification, str)

        self.assertEqual(AppKit.NSTableViewStyleAutomatic, 0)
        self.assertEqual(AppKit.NSTableViewStyleFullWidth, 1)
        self.assertEqual(AppKit.NSTableViewStyleInset, 2)
        self.assertEqual(AppKit.NSTableViewStyleSourceList, 3)
        self.assertEqual(AppKit.NSTableViewStylePlain, 4)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertEqual(AppKit.NSTableViewSelectionHighlightStyleNone, -1)
        self.assertEqual(AppKit.NSTableViewDraggingDestinationFeedbackStyleNone, -1)
        self.assertEqual(AppKit.NSTableViewDraggingDestinationFeedbackStyleRegular, 0)
        self.assertEqual(
            AppKit.NSTableViewDraggingDestinationFeedbackStyleSourceList, 1
        )

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(AppKit.NSTableViewDashedHorizontalGridLineMask, 1 << 3)

        self.assertEqual(AppKit.NSTableViewRowSizeStyleDefault, -1)
        self.assertEqual(AppKit.NSTableViewRowSizeStyleCustom, 0)
        self.assertEqual(AppKit.NSTableViewRowSizeStyleSmall, 1)
        self.assertEqual(AppKit.NSTableViewRowSizeStyleMedium, 2)
        self.assertEqual(AppKit.NSTableViewRowSizeStyleLarge, 3)

        self.assertEqual(AppKit.NSTableViewAnimationEffectNone, 0)
        self.assertEqual(AppKit.NSTableViewAnimationEffectFade, 1)
        self.assertEqual(AppKit.NSTableViewAnimationEffectGap, 2)
        self.assertEqual(AppKit.NSTableViewAnimationSlideUp, 0x10)
        self.assertEqual(AppKit.NSTableViewAnimationSlideDown, 0x20)
        self.assertEqual(AppKit.NSTableViewAnimationSlideLeft, 0x30)
        self.assertEqual(AppKit.NSTableViewAnimationSlideRight, 0x40)

        self.assertIsInstance(AppKit.NSTableViewRowViewKey, str)

        self.assertEqual(AppKit.NSTableViewDashedHorizontalGridLineMask, 1 << 3)

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertEqual(AppKit.NSTableViewDraggingDestinationFeedbackStyleGap, 2)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(AppKit.NSTableRowActionEdgeLeading, 0)
        self.assertEqual(AppKit.NSTableRowActionEdgeTrailing, 1)

    def testMethods(self):
        self.assertArgIsBOOL(AppKit.NSTableView.setAllowsColumnReordering_, 0)
        self.assertResultIsBOOL(AppKit.NSTableView.allowsColumnReordering)
        self.assertArgIsBOOL(AppKit.NSTableView.setAllowsColumnResizing_, 0)
        self.assertResultIsBOOL(AppKit.NSTableView.allowsColumnResizing)
        self.assertArgIsBOOL(
            AppKit.NSTableView.setUsesAlternatingRowBackgroundColors_, 0
        )
        self.assertResultIsBOOL(AppKit.NSTableView.usesAlternatingRowBackgroundColors)
        self.assertArgIsBOOL(AppKit.NSTableView.setVerticalMotionCanBeginDrag_, 0)
        self.assertResultIsBOOL(AppKit.NSTableView.verticalMotionCanBeginDrag)
        self.assertResultIsBOOL(AppKit.NSTableView.canDragRowsWithIndexes_atPoint_)
        self.assertArgIsInOut(
            AppKit.NSTableView.dragImageForRowsWithIndexes_tableColumns_event_offset_, 3
        )
        self.assertArgIsBOOL(
            AppKit.NSTableView.setDraggingSourceOperationMask_forLocal_, 1
        )
        self.assertResultIsBOOL(AppKit.NSTableView.verticalMotionCanBeginDrag)
        self.assertArgIsBOOL(AppKit.NSTableView.setAllowsMultipleSelection_, 0)
        self.assertResultIsBOOL(AppKit.NSTableView.allowsMultipleSelection)
        self.assertArgIsBOOL(AppKit.NSTableView.setAllowsEmptySelection_, 0)
        self.assertResultIsBOOL(AppKit.NSTableView.allowsEmptySelection)
        self.assertArgIsBOOL(AppKit.NSTableView.setAllowsColumnSelection_, 0)
        self.assertResultIsBOOL(AppKit.NSTableView.allowsColumnSelection)
        self.assertArgIsBOOL(
            AppKit.NSTableView.selectColumnIndexes_byExtendingSelection_, 1
        )
        self.assertArgIsBOOL(
            AppKit.NSTableView.selectRowIndexes_byExtendingSelection_, 1
        )
        self.assertResultIsBOOL(AppKit.NSTableView.isColumnSelected_)
        self.assertResultIsBOOL(AppKit.NSTableView.isRowSelected_)
        self.assertResultIsBOOL(AppKit.NSTableView.textShouldBeginEditing_)
        self.assertResultIsBOOL(AppKit.NSTableView.textShouldEndEditing_)
        self.assertArgIsBOOL(AppKit.NSTableView.setAutosaveTableColumns_, 0)
        self.assertResultIsBOOL(AppKit.NSTableView.autosaveTableColumns)
        self.assertArgIsBOOL(AppKit.NSTableView.editColumn_row_withEvent_select_, 3)

        self.assertArgHasType(
            AppKit.NSTableView.drawBackgroundInClipRect_, 0, AppKit.NSRect.__typestr__
        )

        self.assertArgIsBOOL(AppKit.NSTableView.setDrawsGrid_, 0)
        self.assertResultIsBOOL(AppKit.NSTableView.drawsGrid)
        self.assertArgIsBOOL(AppKit.NSTableView.selectColumn_byExtendingSelection_, 1)
        self.assertArgIsBOOL(AppKit.NSTableView.selectRow_byExtendingSelection_, 1)
        self.assertArgIsInOut(
            AppKit.NSTableView.dragImageForRows_event_dragImageOffset_, 2
        )
        self.assertArgIsBOOL(AppKit.NSTableView.setAutoresizesAllColumnsToFit_, 0)
        self.assertResultIsBOOL(AppKit.NSTableView.autoresizesAllColumnsToFit)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsBOOL(AppKit.NSTableView.setAllowsTypeSelect_, 0)
        self.assertResultIsBOOL(AppKit.NSTableView.allowsTypeSelect)

        self.assertArgHasType(
            AppKit.NSTableView.columnIndexesInRect_, 0, AppKit.NSRect.__typestr__
        )

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSTableView.shouldFocusCell_atColumn_row_)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsBOOL(AppKit.NSTableView.viewAtColumn_row_makeIfNecessary_, 2)
        self.assertArgIsBOOL(AppKit.NSTableView.rowViewAtRow_makeIfNecessary_, 1)

        self.assertArgIsBlock(
            AppKit.NSTableView.enumerateAvailableRowViewsUsingBlock_,
            0,
            b"v@" + objc._C_NSInteger,
        )

        self.assertResultIsBOOL(AppKit.NSTableView.floatsGroupRows)
        self.assertArgIsBOOL(AppKit.NSTableView.setFloatsGroupRows_, 0)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(AppKit.NSTableView.usesStaticContents)
        self.assertArgIsBOOL(AppKit.NSTableView.setUsesStaticContents_, 0)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AppKit.NSTableView.rowActionsVisible)
        self.assertArgIsBOOL(AppKit.NSTableView.setRowActionsVisible_, 0)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(AppKit.NSTableView.usesAutomaticRowHeights)
        self.assertArgIsBOOL(AppKit.NSTableView.setUsesAutomaticRowHeights_, 0)

    @min_sdk_level("10.6")
    def testProtocolObjects(self):
        objc.protocolNamed("NSTableViewDelegate")
        objc.protocolNamed("NSTableViewDataSource")

    def testProtocols(self):
        self.assertResultHasType(
            TestNSTableViewHelper.numberOfRowsInTableView_, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_objectValueForTableColumn_row_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_setObjectValue_forTableColumn_row_,
            3,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(
            TestNSTableViewHelper.tableView_writeRowsWithIndexes_toPasteboard_
        )
        self.assertResultHasType(
            TestNSTableViewHelper.tableView_validateDrop_proposedRow_proposedDropOperation_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_validateDrop_proposedRow_proposedDropOperation_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_validateDrop_proposedRow_proposedDropOperation_,
            3,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestNSTableViewHelper.tableView_acceptDrop_row_dropOperation_
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_acceptDrop_row_dropOperation_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_acceptDrop_row_dropOperation_,
            3,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_writeRows_toPasteboard_)

        self.assertArgHasType(
            TestNSTableViewHelper.tableView_willDisplayCell_forTableColumn_row_,
            3,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(
            TestNSTableViewHelper.tableView_shouldEditTableColumn_row_
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_shouldEditTableColumn_row_,
            2,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(TestNSTableViewHelper.selectionShouldChangeInTableView_)
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_shouldSelectRow_)
        self.assertResultIsBOOL(
            TestNSTableViewHelper.tableView_shouldSelectTableColumn_
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_,
            2,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_,
            4,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_toolTipForCell_rect_tableColumn_row_mouseLocation_,
            5,
            AppKit.NSPoint.__typestr__,
        )
        self.assertResultHasType(
            TestNSTableViewHelper.tableView_heightOfRow_, objc._C_CGFloat
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_heightOfRow_, 1, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_typeSelectStringForTableColumn_row_,
            2,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSTableViewHelper.tableView_nextTypeSelectMatchFromRow_toRow_forString_,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_nextTypeSelectMatchFromRow_toRow_forString_,
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_nextTypeSelectMatchFromRow_toRow_forString_,
            2,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(
            TestNSTableViewHelper.tableView_shouldTypeSelectForEvent_withCurrentSearchString_
        )
        self.assertResultIsBOOL(
            TestNSTableViewHelper.tableView_shouldShowCellExpansionForTableColumn_row_
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_shouldShowCellExpansionForTableColumn_row_,
            2,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(
            TestNSTableViewHelper.tableView_shouldTrackCell_forTableColumn_row_
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_shouldTrackCell_forTableColumn_row_,
            3,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_dataCellForTableColumn_row_,
            2,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(TestNSTableViewHelper.tableView_isGroupRow_)
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_isGroupRow_, 1, objc._C_NSInteger
        )

    @min_os_level("10.6")
    def testProtocols10_6(self):
        self.assertResultHasType(
            TestNSTableViewHelper.tableView_sizeToFitWidthOfColumn_, objc._C_CGFloat
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_sizeToFitWidthOfColumn_,
            1,
            objc._C_NSInteger,
        )

        self.assertResultIsBOOL(
            TestNSTableViewHelper.tableView_shouldReorderColumn_toColumn_
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_shouldReorderColumn_toColumn_,
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_shouldReorderColumn_toColumn_,
            2,
            objc._C_NSInteger,
        )

    @min_os_level("10.7")
    def testProtocols10_7(self):
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_pasteboardWriterForRow_,
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_viewForTableColumn_row_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_rowViewForRow_, 1, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_didAddRowView_forRow_, 2, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_didRemoveRowView_forRow_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_draggingSession_willBeginAtPoint_forRowIndexes_,
            2,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_draggingSession_endedAtPoint_operation_,
            2,
            AppKit.NSPoint.__typestr__,
        )

    @min_os_level("10.11")
    def testProtococols10_11(self):
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_rowActionsForRow_edge_, 1, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestNSTableViewHelper.tableView_rowActionsForRow_edge_, 2, objc._C_NSInteger
        )
