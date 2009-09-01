from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSCollectionViewHelper (NSObject):
    def collectionView_canDragItemsAtIndexes_withEvent_(self, v, i, e): return 1
    def collectionView_writeItemsAtIndexes_toPasteboard_(self, v, i, p): return 1
    def collectionView_draggingImageForItemsAtIndexes_withEvent_offset_(self, v, i, e, o): return 1
    def collectionView_validateDrop_proposedIndex_dropOperation_(self, v, d, i, o): return 1
    def collectionView_acceptDrop_index_dropOperation_(self, v, d, i, o): return 1


class TestNSCollectionView (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSCollectionViewItem.isSelected)
        self.failUnlessArgIsBOOL(NSCollectionViewItem.setSelected_, 0)

        self.failUnlessResultIsBOOL(NSCollectionView.isFirstResponder)

        self.failUnlessResultIsBOOL(NSCollectionView.isSelectable)
        self.failUnlessArgIsBOOL(NSCollectionView.setSelectable_, 0)
        self.failUnlessResultIsBOOL(NSCollectionView.allowsMultipleSelection)
        self.failUnlessArgIsBOOL(NSCollectionView.setAllowsMultipleSelection_, 0)

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultHasType(NSCollectionView.frameForItemAtIndex_, NSRect.__typestr__)
        self.failUnlessArgIsBOOL(NSCollectionView.setDraggingSourceOperationMask_forLocal_, 1)
        self.failUnlessArgHasType(NSCollectionView.draggingImageForItemsAtIndexes_withEvent_offset_, 2,
                'N^' + NSPoint.__typestr__)

        self.failUnlessResultIsBOOL(TestNSCollectionViewHelper.collectionView_canDragItemsAtIndexes_withEvent_)
        self.failUnlessResultIsBOOL(TestNSCollectionViewHelper.collectionView_writeItemsAtIndexes_toPasteboard_)
        self.failUnlessArgHasType(TestNSCollectionViewHelper.collectionView_draggingImageForItemsAtIndexes_withEvent_offset_,
                3, 'N^' + NSPoint.__typestr__)

        self.failUnlessResultHasType(TestNSCollectionViewHelper.collectionView_validateDrop_proposedIndex_dropOperation_,
                objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSCollectionViewHelper.collectionView_validateDrop_proposedIndex_dropOperation_,
                2, 'N^' + objc._C_NSInteger) 
        self.failUnlessArgHasType(TestNSCollectionViewHelper.collectionView_validateDrop_proposedIndex_dropOperation_,
                3, 'N^' + objc._C_NSInteger)

        self.failUnlessResultIsBOOL(TestNSCollectionViewHelper.collectionView_acceptDrop_index_dropOperation_)
        self.failUnlessArgHasType(TestNSCollectionViewHelper.collectionView_acceptDrop_index_dropOperation_,
            2, objc._C_NSInteger)
        self.failUnlessArgHasType(TestNSCollectionViewHelper.collectionView_acceptDrop_index_dropOperation_,
            3, objc._C_NSInteger)


    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessEqual(NSCollectionViewDropOn, 0)
        self.failUnlessEqual(NSCollectionViewDropBefore, 1)

if __name__ == "__main__":
    main()
