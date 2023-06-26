import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSOutlineViewHelper(AppKit.NSObject):
    def outlineView_sizeToFitWidthOfColumn_(self, v, c):
        return 1

    def outlineView_shouldReorderColumn_toColumn_(self, v, c1, c2):
        return 1

    def outlineView_shouldShowOutlineCellForItem_(self, v, i):
        return 1

    def outlineView_child_ofItem_(self, ov, nr, item):
        return 1

    def outlineView_isItemExpandable_(self, ov, item):
        return 1

    def outlineView_numberOfChildrenOfItem_(self, ov, item):
        return 1

    def outlineView_objectValueForTableColumn_byItem_(self, ov, tc, item):
        return 1

    def outlineView_setObjectValue_forTableColumn_byItem_(self, ov, value, tc, item):
        pass

    def outlineView_itemForPersistentObject_(self, ov, po):
        return 1

    def outlineView_persistentObjectForItem_(self, ov, item):
        return 1

    def outlineView_sortDescriptorsDidChange_(self, ov, old):
        pass

    def outlineView_writeItems_toPasteboard_(self, ov, items, pb):
        return 1

    def outlineView_validateDrop_proposedItem_proposedChildIndex_(
        self, ov, dr, item, idx
    ):
        return 1

    def outlineView_acceptDrop_item_childIndex_(self, ov, dr, it, idx):
        return 1

    def outlineView_namesOfPromisedFilesDroppedAtDestination_forDraggedItems_(
        self, ov, dr, it
    ):
        return 1

    def outlineView_willDisplayCell_forTableColumn_item_(self, ov, c, tc, i):
        pass

    def outlineView_shouldEditTableColumn_item_(self, ov, tc, i):
        return 1

    def selectionShouldChangeInOutlineView_(self, ov):
        return 1

    def outlineView_selectionIndexesForProposedSelection_(self, ov, idx):
        return 1

    def outlineView_shouldSelectItem_(self, ov, tc):
        return 1

    def outlineView_shouldSelectTableColumn_(self, ov, tc):
        return 1

    def outlineView_toolTipForCell_rect_tableColumn_item_mouseLocation_(
        self, ov, c, r, tc, it, ml
    ):
        return 1

    def outlineView_heightOfRowByItem_(self, ov, item):
        return 1

    def outlineView_typeSelectStringForTableColumn_item_(self, ov, tc, item):
        return 1

    def outlineView_nextTypeSelectMatchFromItem_toItem_forString_(self, ov, si, ei, ss):
        return 1

    def outlineView_shouldTypeSelectForEvent_withCurrentSearchString_(self, ov, ev, ss):
        return 1

    def outlineView_shouldShowCellExpansionForTableColumn_item_(self, ov, tc, it):
        return 1

    def outlineView_shouldTrackCell_forTableColumn_item_(self, ov, c, tc, it):
        return 1

    def outlineView_dataCellForTableColumn_item_(self, ov, tc, it):
        return 1

    def outlineView_isGroupItem_(self, ov, item):
        return 1

    def outlineView_shouldExpandItem_(self, ov, it):
        return 1

    def outlineView_shouldCollapseItem_(self, ov, it):
        return 1

    def outlineView_willDisplayOutlineCell_forTableColumn_item_(self, ov, c, tc, i):
        pass

    def outlineView_draggingSession_willBeginAtPoint_(self, a, b, c):
        pass

    def outlineView_draggingSession_endedAtPoint_(self, a, b, c):
        pass

    def outlineView_didAddRowView_forRow_(self, a, b, c):
        pass

    def outlineView_didRemoveRowView_forRow_(self, a, b, c):
        pass

    def outlineView_userCanChangeVisibilityOfTableColumn_(self, a, b):
        return 1


class TestNSOutlineView(TestCase):
    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(AppKit.NSOutlineViewDisclosureButtonKey, str)
        self.assertIsInstance(AppKit.NSOutlineViewShowHideButtonKey, str)

    def testConstants(self):
        self.assertEqual(AppKit.NSOutlineViewDropOnItemIndex, -1)

        self.assertIsInstance(AppKit.NSOutlineViewSelectionDidChangeNotification, str)
        self.assertIsInstance(AppKit.NSOutlineViewColumnDidMoveNotification, str)
        self.assertIsInstance(AppKit.NSOutlineViewColumnDidResizeNotification, str)
        self.assertIsInstance(AppKit.NSOutlineViewSelectionIsChangingNotification, str)
        self.assertIsInstance(AppKit.NSOutlineViewItemWillExpandNotification, str)
        self.assertIsInstance(AppKit.NSOutlineViewItemDidExpandNotification, str)
        self.assertIsInstance(AppKit.NSOutlineViewItemWillCollapseNotification, str)
        self.assertIsInstance(AppKit.NSOutlineViewItemDidCollapseNotification, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSOutlineView.isExpandable_)
        self.assertArgIsBOOL(AppKit.NSOutlineView.expandItem_expandChildren_, 1)
        self.assertArgIsBOOL(AppKit.NSOutlineView.collapseItem_collapseChildren_, 1)
        self.assertArgIsBOOL(AppKit.NSOutlineView.reloadItem_reloadChildren_, 1)
        self.assertResultIsBOOL(AppKit.NSOutlineView.isItemExpanded_)
        self.assertResultIsBOOL(AppKit.NSOutlineView.indentationMarkerFollowsCell)
        self.assertArgIsBOOL(AppKit.NSOutlineView.setIndentationMarkerFollowsCell_, 0)
        self.assertResultIsBOOL(AppKit.NSOutlineView.autoresizesOutlineColumn)
        self.assertArgIsBOOL(AppKit.NSOutlineView.setAutoresizesOutlineColumn_, 0)
        self.assertResultIsBOOL(
            AppKit.NSOutlineView.shouldCollapseAutoExpandedItemsForDeposited_
        )
        self.assertArgIsBOOL(
            AppKit.NSOutlineView.shouldCollapseAutoExpandedItemsForDeposited_, 0
        )
        self.assertResultIsBOOL(AppKit.NSOutlineView.autosaveExpandedItems)
        self.assertArgIsBOOL(AppKit.NSOutlineView.setAutosaveExpandedItems_, 0)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSOutlineView.stronglyReferencesItems)
        self.assertArgIsBOOL(AppKit.NSOutlineView.setStronglyReferencesItems_, 0)

    @min_sdk_level("10.6")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSOutlineViewDelegate")
        self.assertProtocolExists("NSOutlineViewDataSource")

    def testProtocols(self):
        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_child_ofItem_, 1, objc._C_NSInteger
        )
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_isItemExpandable_)
        self.assertResultHasType(
            TestNSOutlineViewHelper.outlineView_numberOfChildrenOfItem_,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.outlineView_writeItems_toPasteboard_
        )
        self.assertResultHasType(
            TestNSOutlineViewHelper.outlineView_validateDrop_proposedItem_proposedChildIndex_,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_validateDrop_proposedItem_proposedChildIndex_,
            3,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.outlineView_acceptDrop_item_childIndex_
        )
        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.outlineView_shouldEditTableColumn_item_
        )
        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.selectionShouldChangeInOutlineView_
        )
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldSelectItem_)
        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.outlineView_shouldSelectTableColumn_
        )
        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_toolTipForCell_rect_tableColumn_item_mouseLocation_,  # noqa: B950
            2,
            b"N^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_toolTipForCell_rect_tableColumn_item_mouseLocation_,  # noqa: B950
            5,
            AppKit.NSPoint.__typestr__,
        )
        self.assertResultHasType(
            TestNSOutlineViewHelper.outlineView_heightOfRowByItem_, objc._C_CGFloat
        )
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldExpandItem_)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldCollapseItem_)

        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_didAddRowView_forRow_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_didRemoveRowView_forRow_,
            2,
            objc._C_NSInteger,
        )

    @min_os_level("10.5")
    def testProtocols10_5(self):
        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.outlineView_shouldTypeSelectForEvent_withCurrentSearchString_  # noqa: B950
        )
        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.outlineView_shouldShowCellExpansionForTableColumn_item_
        )
        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.outlineView_shouldTrackCell_forTableColumn_item_
        )
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_isGroupItem_)

    @min_os_level("10.6")
    def testProtocols10_6(self):
        self.assertResultHasType(
            TestNSOutlineViewHelper.outlineView_sizeToFitWidthOfColumn_, objc._C_CGFloat
        )
        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_sizeToFitWidthOfColumn_,
            1,
            objc._C_NSInteger,
        )
        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.outlineView_shouldReorderColumn_toColumn_
        )
        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_shouldReorderColumn_toColumn_,
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_shouldReorderColumn_toColumn_,
            2,
            objc._C_NSInteger,
        )

        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.outlineView_shouldShowOutlineCellForItem_
        )

    @min_os_level("10.7")
    def testProtocols10_7(self):
        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_draggingSession_willBeginAtPoint_,
            2,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSOutlineViewHelper.outlineView_draggingSession_endedAtPoint_,
            2,
            AppKit.NSPoint.__typestr__,
        )

        self.assertResultIsBOOL(
            TestNSOutlineViewHelper.outlineView_userCanChangeVisibilityOfTableColumn_
        )
