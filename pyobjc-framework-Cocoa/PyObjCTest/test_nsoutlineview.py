
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSOutlineViewHelper (NSObject):
    def outlineView_sizeToFitWidthOfColumn_(self, v, c): return 1
    def outlineView_shouldReorderColumn_toColumn_(self, v, c1, c2): return 1
    def outlineView_shouldShowOutlineCellForItem_(self, v, i): return 1
    def outlineView_child_ofItem_(self, ov, nr, item): return 1
    def outlineView_isItemExpandable_(self, ov, item): return 1
    def outlineView_numberOfChildrenOfItem_(self, ov, item): return 1
    def outlineView_objectValueForTableColumn_byItem_(self, ov, tc, item): return 1
    def outlineView_setObjectValue_forTableColumn_byItem_(self, ov, value, tc, item): pass
    def outlineView_itemForPersistentObject_(self, ov, po): return 1
    def outlineView_persistentObjectForItem_(self, ov, item): return 1
    def outlineView_sortDescriptorsDidChange_(self, ov, old): pass
    def outlineView_writeItems_toPasteboard_(self, ov, items, pb): return 1
    def outlineView_validateDrop_proposedItem_proposedChildIndex_(self, ov, dr, item, idx): return 1
    def outlineView_acceptDrop_item_childIndex_(self, ov, dr, it, idx): return 1
    def outlineView_namesOfPromisedFilesDroppedAtDestination_forDraggedItems_(self, ov, dr, it): return 1

    def outlineView_willDisplayCell_forTableColumn_item_(self, ov, c, tc, i): pass
    def outlineView_shouldEditTableColumn_item_(self, ov, tc, i): return 1
    def selectionShouldChangeInOutlineView_(self, ov): return 1
    def outlineView_selectionIndexesForProposedSelection_(self, ov, idx): return 1
    def outlineView_shouldSelectItem_(self, ov, tc): return 1
    def outlineView_shouldSelectTableColumn_(self, ov, tc): return 1
    def outlineView_toolTipForCell_rect_tableColumn_item_mouseLocation_(self, ov, c, r, tc, it, ml): return 1
    def outlineView_heightOfRowByItem_(self, ov, item):  return 1
    def outlineView_typeSelectStringForTableColumn_item_(self, ov, tc, item): return 1
    def outlineView_nextTypeSelectMatchFromItem_toItem_forString_(self, ov, si, ei, ss): return 1
    def outlineView_shouldTypeSelectForEvent_withCurrentSearchString_(self, ov, ev, ss): return 1
    def outlineView_shouldShowCellExpansionForTableColumn_item_(self, ov, tc, it): return 1
    def outlineView_shouldTrackCell_forTableColumn_item_(self, ov, c, tc, it): return 1
    def outlineView_dataCellForTableColumn_item_(self, ov, tc, it): return 1
    def outlineView_isGroupItem_(self, ov, item): return 1
    def outlineView_shouldExpandItem_(self, ov, it): return 1
    def outlineView_shouldCollapseItem_(self, ov, it): return 1
    def outlineView_willDisplayOutlineCell_forTableColumn_item_(self, ov, c, tc, i): pass

    def outlineView_draggingSession_willBeginAtPoint_(self, a, b, c): pass
    def outlineView_draggingSession_endedAtPoint_(self, a, b, c): pass



class TestNSOutlineView (TestCase):
    def testConstants(self):
        self.assertEqual(NSOutlineViewDropOnItemIndex, -1)

        self.assertIsInstance(NSOutlineViewSelectionDidChangeNotification, unicode)
        self.assertIsInstance(NSOutlineViewColumnDidMoveNotification, unicode)
        self.assertIsInstance(NSOutlineViewColumnDidResizeNotification, unicode)
        self.assertIsInstance(NSOutlineViewSelectionIsChangingNotification, unicode)
        self.assertIsInstance(NSOutlineViewItemWillExpandNotification, unicode)
        self.assertIsInstance(NSOutlineViewItemDidExpandNotification, unicode)
        self.assertIsInstance(NSOutlineViewItemWillCollapseNotification, unicode)
        self.assertIsInstance(NSOutlineViewItemDidCollapseNotification, unicode)


    def testMethods(self):
        self.assertResultIsBOOL(NSOutlineView.isExpandable_)
        self.assertArgIsBOOL(NSOutlineView.expandItem_expandChildren_, 1)
        self.assertArgIsBOOL(NSOutlineView.collapseItem_collapseChildren_, 1)
        self.assertArgIsBOOL(NSOutlineView.reloadItem_reloadChildren_, 1)
        self.assertResultIsBOOL(NSOutlineView.isItemExpanded_)
        self.assertResultIsBOOL(NSOutlineView.indentationMarkerFollowsCell)
        self.assertArgIsBOOL(NSOutlineView.setIndentationMarkerFollowsCell_, 0)
        self.assertResultIsBOOL(NSOutlineView.autoresizesOutlineColumn)
        self.assertArgIsBOOL(NSOutlineView.setAutoresizesOutlineColumn_, 0)
        self.assertResultIsBOOL(NSOutlineView.shouldCollapseAutoExpandedItemsForDeposited_)
        self.assertArgIsBOOL(NSOutlineView.shouldCollapseAutoExpandedItemsForDeposited_, 0)
        self.assertResultIsBOOL(NSOutlineView.autosaveExpandedItems)
        self.assertArgIsBOOL(NSOutlineView.setAutosaveExpandedItems_, 0)

    def testProtocols(self):
        self.assertArgHasType(TestNSOutlineViewHelper.outlineView_child_ofItem_, 1, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_isItemExpandable_)
        self.assertResultHasType(TestNSOutlineViewHelper.outlineView_numberOfChildrenOfItem_, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_writeItems_toPasteboard_)
        self.assertResultHasType(TestNSOutlineViewHelper.outlineView_validateDrop_proposedItem_proposedChildIndex_, objc._C_NSUInteger)
        self.assertArgHasType(TestNSOutlineViewHelper.outlineView_validateDrop_proposedItem_proposedChildIndex_, 3, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldEditTableColumn_item_)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.selectionShouldChangeInOutlineView_)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldSelectItem_)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldSelectTableColumn_)
        self.assertArgHasType(TestNSOutlineViewHelper.outlineView_toolTipForCell_rect_tableColumn_item_mouseLocation_, 2, b'N^' + NSRect.__typestr__)
        self.assertArgHasType(TestNSOutlineViewHelper.outlineView_toolTipForCell_rect_tableColumn_item_mouseLocation_, 5, NSPoint.__typestr__)
        self.assertResultHasType(TestNSOutlineViewHelper.outlineView_heightOfRowByItem_, objc._C_CGFloat)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldExpandItem_)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldCollapseItem_)

    @min_os_level('10.5')
    def testProtocols10_5(self):
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldTypeSelectForEvent_withCurrentSearchString_)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldShowCellExpansionForTableColumn_item_)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldTrackCell_forTableColumn_item_)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_isGroupItem_)


    @min_os_level('10.6')
    def testProtocols10_6(self):
        self.assertResultHasType(TestNSOutlineViewHelper.outlineView_sizeToFitWidthOfColumn_, objc._C_CGFloat)
        self.assertArgHasType(TestNSOutlineViewHelper.outlineView_sizeToFitWidthOfColumn_, 1, objc._C_NSInteger)
        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldReorderColumn_toColumn_)
        self.assertArgHasType(TestNSOutlineViewHelper.outlineView_shouldReorderColumn_toColumn_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSOutlineViewHelper.outlineView_shouldReorderColumn_toColumn_, 2, objc._C_NSInteger)

        self.assertResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldShowOutlineCellForItem_)

    @min_os_level('10.7')
    def testProtocols10_7(self):
        self.assertArgHasType(TestNSOutlineViewHelper.outlineView_draggingSession_willBeginAtPoint_, 2, NSPoint.__typestr__)
        self.assertArgHasType(TestNSOutlineViewHelper.outlineView_draggingSession_endedAtPoint_, 2, NSPoint.__typestr__)


if __name__ == "__main__":
    main()
