
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSOutlineViewHelper (NSObject):
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



class TestNSOutlineView (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSOutlineViewDropOnItemIndex, -1)

        self.failUnlessIsInstance(NSOutlineViewSelectionDidChangeNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewColumnDidMoveNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewColumnDidResizeNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewSelectionIsChangingNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewItemWillExpandNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewItemDidExpandNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewItemWillCollapseNotification, unicode)
        self.failUnlessIsInstance(NSOutlineViewItemDidCollapseNotification, unicode)


    def testMethods(self):
        self.failUnlessResultIsBOOL(NSOutlineView.isExpandable_)
        self.failUnlessArgIsBOOL(NSOutlineView.expandItem_expandChildren_, 1)
        self.failUnlessArgIsBOOL(NSOutlineView.collapseItem_collapseChildren_, 1)
        self.failUnlessArgIsBOOL(NSOutlineView.reloadItem_reloadChildren_, 1)
        self.failUnlessResultIsBOOL(NSOutlineView.isItemExpanded_)
        self.failUnlessResultIsBOOL(NSOutlineView.indentationMarkerFollowsCell)
        self.failUnlessArgIsBOOL(NSOutlineView.setIndentationMarkerFollowsCell_, 0)
        self.failUnlessResultIsBOOL(NSOutlineView.autoresizesOutlineColumn)
        self.failUnlessArgIsBOOL(NSOutlineView.setAutoresizesOutlineColumn_, 0)
        self.failUnlessResultIsBOOL(NSOutlineView.shouldCollapseAutoExpandedItemsForDeposited_)
        self.failUnlessArgIsBOOL(NSOutlineView.shouldCollapseAutoExpandedItemsForDeposited_, 0)
        self.failUnlessResultIsBOOL(NSOutlineView.autosaveExpandedItems)
        self.failUnlessArgIsBOOL(NSOutlineView.setAutosaveExpandedItems_, 0)

    def testProtocols(self):
        self.failUnlessArgHasType(TestNSOutlineViewHelper.outlineView_child_ofItem_, 1, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_isItemExpandable_)
        self.failUnlessResultHasType(TestNSOutlineViewHelper.outlineView_numberOfChildrenOfItem_, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_writeItems_toPasteboard_)
        self.failUnlessResultHasType(TestNSOutlineViewHelper.outlineView_validateDrop_proposedItem_proposedChildIndex_, objc._C_NSUInteger)
        self.failUnlessArgHasType(TestNSOutlineViewHelper.outlineView_validateDrop_proposedItem_proposedChildIndex_, 3, objc._C_NSInteger)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldEditTableColumn_item_)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.selectionShouldChangeInOutlineView_)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldSelectItem_)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldSelectTableColumn_)
        self.failUnlessArgHasType(TestNSOutlineViewHelper.outlineView_toolTipForCell_rect_tableColumn_item_mouseLocation_, 2, 'N^' + NSRect.__typestr__)
        self.failUnlessArgHasType(TestNSOutlineViewHelper.outlineView_toolTipForCell_rect_tableColumn_item_mouseLocation_, 5, NSPoint.__typestr__)
        self.failUnlessResultHasType(TestNSOutlineViewHelper.outlineView_heightOfRowByItem_, objc._C_CGFloat)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldExpandItem_)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldCollapseItem_)

    @min_os_level('10.5')
    def testProtocols10_5(self):
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldTypeSelectForEvent_withCurrentSearchString_)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldShowCellExpansionForTableColumn_item_)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_shouldTrackCell_forTableColumn_item_)
        self.failUnlessResultIsBOOL(TestNSOutlineViewHelper.outlineView_isGroupItem_)


if __name__ == "__main__":
    main()
