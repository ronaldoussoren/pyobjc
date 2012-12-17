from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSCollectionViewHelper (NSObject):
    def collectionView_canDragItemsAtIndexes_withEvent_(self, v, i, e): return 1
    def collectionView_writeItemsAtIndexes_toPasteboard_(self, v, i, p): return 1
    def collectionView_draggingImageForItemsAtIndexes_withEvent_offset_(self, v, i, e, o): return 1
    def collectionView_validateDrop_proposedIndex_dropOperation_(self, v, d, i, o): return 1
    def collectionView_acceptDrop_index_dropOperation_(self, v, d, i, o): return 1
    def collectionView_pasteboardWriterForItemAtIndex_(self, v, i): pass
    def collectionView_draggingSession_willBeginAtPoint_forItemsAtIndexes_(self, v, i, j, p): pass
    def collectionView_draggingSession_endedAtPoint_draggingOperation_(self, a, b, c, d): pass


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


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertEqual(NSCollectionViewDropOn, 0)
        self.assertEqual(NSCollectionViewDropBefore, 1)

if __name__ == "__main__":
    main()
