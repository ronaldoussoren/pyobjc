from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSCollectionViewHelper (NSObject):
    def collectionView_acceptDrop_indexPath_dropOperation_(self, c, d, p, o): return 1
    def collectionView_validateDrop_proposedIndexPath_dropOperation_(self, c, d, p, o): return 1
    def collectionView_draggingImageForItemsAtIndexPaths_withEvent_offset_(self, v, p, e, o): return 1
    def collectionView_writeItemsAtIndexPaths_toPasteboard_(self, v, p, p2): return True
    def collectionView_canDragItemsAtIndexPaths_withEvent_(self, c, p, e): return True
    def numberOfSectionsInCollectionView_(self, v): return 1
    def collectionView_numberOfItemsInSection_(self, v, s): return 1
    def collectionView_canDragItemsAtIndexes_withEvent_(self, v, i, e): return 1
    def collectionView_writeItemsAtIndexes_toPasteboard_(self, v, i, p): return 1
    def collectionView_draggingImageForItemsAtIndexes_withEvent_offset_(self, v, i, e, o): return 1
    def collectionView_validateDrop_proposedIndex_dropOperation_(self, v, d, i, o): return 1
    def collectionView_acceptDrop_index_dropOperation_(self, v, d, i, o): return 1
    def collectionView_pasteboardWriterForItemAtIndex_(self, v, i): pass
    def collectionView_draggingSession_willBeginAtPoint_forItemsAtIndexes_(self, v, i, j, p): pass
    def collectionView_draggingSession_willBeginAtPoint_forItemsAtIndexPaths_(self, v, i, j, p): pass
    def collectionView_draggingSession_endedAtPoint_draggingOperation_(self, a, b, c, d): pass
    def collectionView_shouldChangeItemsAtIndexPaths_toHighlightState_(self, a, b, c): pass
    def collectionView_didChangeItemsAtIndexPaths_toHighlightState_(self, a, b, c): pass


class TestNSCollectionView (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSCollectionViewItem.isSelected)
        self.assertArgIsBOOL(NSCollectionViewItem.setSelected_, 0)

        self.assertResultIsBOOL(NSCollectionView.isFirstResponder)

        self.assertResultIsBOOL(NSCollectionView.isSelectable)
        self.assertArgIsBOOL(NSCollectionView.setSelectable_, 0)
        self.assertResultIsBOOL(NSCollectionView.allowsMultipleSelection)
        self.assertArgIsBOOL(NSCollectionView.setAllowsMultipleSelection_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultHasType(NSCollectionView.frameForItemAtIndex_, NSRect.__typestr__)
        self.assertArgIsBOOL(NSCollectionView.setDraggingSourceOperationMask_forLocal_, 1)
        self.assertArgHasType(NSCollectionView.draggingImageForItemsAtIndexes_withEvent_offset_, 2,
                b'N^' + NSPoint.__typestr__)

        self.assertResultIsBOOL(TestNSCollectionViewHelper.collectionView_canDragItemsAtIndexes_withEvent_)
        self.assertResultIsBOOL(TestNSCollectionViewHelper.collectionView_writeItemsAtIndexes_toPasteboard_)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_draggingImageForItemsAtIndexes_withEvent_offset_,
                3, b'N^' + NSPoint.__typestr__)

        self.assertResultHasType(TestNSCollectionViewHelper.collectionView_validateDrop_proposedIndex_dropOperation_,
                objc._C_NSInteger)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_validateDrop_proposedIndex_dropOperation_,
                2, b'N^' + objc._C_NSInteger)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_validateDrop_proposedIndex_dropOperation_,
                3, b'N^' + objc._C_NSInteger)

        self.assertResultIsBOOL(TestNSCollectionViewHelper.collectionView_acceptDrop_index_dropOperation_)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_acceptDrop_index_dropOperation_,
            2, objc._C_NSInteger)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_acceptDrop_index_dropOperation_,
            3, objc._C_NSInteger)

        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_pasteboardWriterForItemAtIndex_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_draggingSession_willBeginAtPoint_forItemsAtIndexes_,
                2, NSPoint.__typestr__)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_draggingSession_endedAtPoint_draggingOperation_,
                2, NSPoint.__typestr__)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_draggingSession_endedAtPoint_draggingOperation_,
                3, objc._C_NSInteger)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(NSCollectionView.allowsEmptySelection)
        self.assertArgIsBOOL(NSCollectionView.setAllowsEmptySelection_, 0)

        self.assertArgIsBlock(NSCollectionView.performBatchUpdates_completionHandler_, 0, b'v')
        self.assertArgIsBlock(NSCollectionView.performBatchUpdates_completionHandler_, 1, b'vZ')

        self.assertArgIsInOut(NSCollectionView.draggingImageForItemsAtIndexPaths_withEvent_offset_, 2)

        self.assertArgIsBlock(NSSet.enumerateIndexPathsWithOptions_usingBlock_, 1, b'v@o^Z')

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSCollectionView.backgroundViewScrollsWithContent)
        self.assertArgIsBOOL(NSCollectionView.setBackgroundViewScrollsWithContent_, 0)

    def testConstants(self):
        self.assertEqual(NSCollectionViewScrollPositionNone, 0)
        self.assertEqual(NSCollectionViewScrollPositionTop, 1 << 0)
        self.assertEqual(NSCollectionViewScrollPositionCenteredVertically, 1 << 1)
        self.assertEqual(NSCollectionViewScrollPositionBottom, 1 << 2)
        self.assertEqual(NSCollectionViewScrollPositionNearestHorizontalEdge, 1 << 9)
        self.assertEqual(NSCollectionViewScrollPositionLeft, 1 << 3)
        self.assertEqual(NSCollectionViewScrollPositionCenteredHorizontally, 1 << 4)
        self.assertEqual(NSCollectionViewScrollPositionRight, 1 << 5)
        self.assertEqual(NSCollectionViewScrollPositionLeadingEdge, 1 << 6)
        self.assertEqual(NSCollectionViewScrollPositionTrailingEdge, 1 << 7)
        self.assertEqual(NSCollectionViewScrollPositionNearestVerticalEdge, 1 << 8)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSCollectionViewDropOn, 0)
        self.assertEqual(NSCollectionViewDropBefore, 1)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertEqual(NSCollectionViewItemHighlightNone, 0)
        self.assertEqual(NSCollectionViewItemHighlightForSelection, 1)
        self.assertEqual(NSCollectionViewItemHighlightForDeselection, 2)
        self.assertEqual(NSCollectionViewItemHighlightAsDropTarget, 3)

    @min_sdk_level('10.10')
    def testProtocols(self):
        objc.protocolNamed('NSCollectionViewDelegate')

    @min_sdk_level('10.11')
    def testProtocols10_11(self):
        objc.protocolNamed('NSCollectionViewElement')

        objc.protocolNamed('NSCollectionViewDataSource')
        self.assertResultHasType(TestNSCollectionViewHelper.collectionView_numberOfItemsInSection_, objc._C_NSInteger)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_numberOfItemsInSection_, 1, objc._C_NSInteger)

        self.assertResultHasType(TestNSCollectionViewHelper.numberOfSectionsInCollectionView_, objc._C_NSInteger)

        objc.protocolNamed('NSCollectionViewDelegate')
        self.assertResultIsBOOL(TestNSCollectionViewHelper.collectionView_canDragItemsAtIndexPaths_withEvent_)
        self.assertResultIsBOOL(TestNSCollectionViewHelper.collectionView_writeItemsAtIndexPaths_toPasteboard_)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_draggingImageForItemsAtIndexPaths_withEvent_offset_, 3, b'N^' + NSPoint.__typestr__)

        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_validateDrop_proposedIndexPath_dropOperation_, 2, b'N^@')
        self.assertResultHasType(TestNSCollectionViewHelper.collectionView_validateDrop_proposedIndexPath_dropOperation_, objc._C_NSUInteger)

        self.assertResultIsBOOL(TestNSCollectionViewHelper.collectionView_acceptDrop_indexPath_dropOperation_)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_acceptDrop_indexPath_dropOperation_, 3, objc._C_NSInteger)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_draggingSession_willBeginAtPoint_forItemsAtIndexPaths_,
                2, NSPoint.__typestr__)

        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_shouldChangeItemsAtIndexPaths_toHighlightState_,
                2, objc._C_NSInteger)
        self.assertArgHasType(TestNSCollectionViewHelper.collectionView_didChangeItemsAtIndexPaths_toHighlightState_,
                2, objc._C_NSInteger)

    @min_sdk_level('10.12')
    def testProtocol10_12(self):
        objc.protocolNamed('NSCollectionViewSectionHeaderView')

    @min_sdk_level('10.13')
    def testProtocol10_13(self):
        objc.protocolNamed('NSCollectionViewPrefetching')

if __name__ == "__main__":
    main()
