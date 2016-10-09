from AppKit import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameEror:
    unicode = str

class TestNSCollectionViewFlowLayoutHelper (NSObject):
    def collectionView_layout_sizeForItemAtIndexPath_(self, cv, l, p): return 1
    def collectionView_layout_insetForSectionAtIndex_(self, cv, l, p): return 1
    def collectionView_layout_minimumLineSpacingForSectionAtIndex_(self, cv, l, p): return 1
    def collectionView_layout_minimumInteritemSpacingForSectionAtIndex_(self, cv, l, p): return 1
    def collectionView_layout_referenceSizeForHeaderInSection_(self, cv, l, p): return 1
    def collectionView_layout_referenceSizeForFooterInSection_(self, cv, l, p): return 1


class TestNSCollectionViewFlowLayout (TestCase):
    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertEqual(NSCollectionViewScrollDirectionVertical, 0)
        self.assertEqual(NSCollectionViewScrollDirectionHorizontal, 1)
        self.assertIsInstance(NSCollectionElementKindSectionHeader, unicode)
        self.assertIsInstance(NSCollectionElementKindSectionFooter, unicode)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(NSCollectionViewFlowLayoutInvalidationContext.invalidateFlowLayoutDelegateMetrics)
        self.assertArgIsBOOL(NSCollectionViewFlowLayoutInvalidationContext.setInvalidateFlowLayoutDelegateMetrics_, 0)
        self.assertResultIsBOOL(NSCollectionViewFlowLayoutInvalidationContext.invalidateFlowLayoutAttributes)
        self.assertArgIsBOOL(NSCollectionViewFlowLayoutInvalidationContext.setInvalidateFlowLayoutAttributes_, 0)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSCollectionViewFlowLayout.sectionHeadersPinToVisibleBounds)
        self.assertArgIsBOOL(NSCollectionViewFlowLayout.setSectionHeadersPinToVisibleBounds_, 0)

        self.assertResultIsBOOL(NSCollectionViewFlowLayout.sectionFootersPinToVisibleBounds)
        self.assertArgIsBOOL(NSCollectionViewFlowLayout.setSectionFootersPinToVisibleBounds_, 0)

        self.assertResultIsBOOL(NSCollectionViewFlowLayout.sectionAtIndexIsCollapsed_)

    @min_os_level('10.11')
    def testProtocols10_11(self):
        objc.protocolNamed('NSCollectionViewDelegateFlowLayout')

        self.assertResultHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_sizeForItemAtIndexPath_, NSSize.__typestr__)

        self.assertResultHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_insetForSectionAtIndex_, NSEdgeInsets.__typestr__)
        self.assertArgHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_insetForSectionAtIndex_, 2, objc._C_NSInteger)

        self.assertResultHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_minimumLineSpacingForSectionAtIndex_, objc._C_CGFloat)
        self.assertArgHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_minimumLineSpacingForSectionAtIndex_, 2, objc._C_NSInteger)

        self.assertResultHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_minimumInteritemSpacingForSectionAtIndex_, objc._C_CGFloat)
        self.assertArgHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_minimumInteritemSpacingForSectionAtIndex_, 2, objc._C_NSInteger)

        self.assertResultHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_referenceSizeForHeaderInSection_, NSSize.__typestr__)
        self.assertArgHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_referenceSizeForHeaderInSection_, 2, objc._C_NSInteger)

        self.assertResultHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_referenceSizeForFooterInSection_, NSSize.__typestr__)
        self.assertArgHasType(TestNSCollectionViewFlowLayoutHelper.collectionView_layout_referenceSizeForFooterInSection_, 2, objc._C_NSInteger)


if __name__ == "__main__":
    main()
