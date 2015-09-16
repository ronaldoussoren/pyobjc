from AppKit import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameEror:
    unicode = str

class TestNSCollectionViewLayout (TestCase):
    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertEqual(NSCollectionElementCategoryItem, 0)
        self.assertEqual(NSCollectionElementCategorySupplementaryView, 1)
        self.assertEqual(NSCollectionElementCategoryDecorationView, 2)
        self.assertEqual(NSCollectionElementCategoryInterItemGap, 3)

        self.assertEqual(NSCollectionUpdateActionInsert, 0)
        self.assertEqual(NSCollectionUpdateActionDelete, 1)
        self.assertEqual(NSCollectionUpdateActionReload, 2)
        self.assertEqual(NSCollectionUpdateActionMove, 3)
        self.assertEqual(NSCollectionUpdateActionNone, 4)

        self.assertIsInstance(NSCollectionElementKindInterItemGapIndicator, unicode)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertResultIsBOOL(NSCollectionViewLayoutAttributes.isHidden)
        self.assertArgIsBOOL(NSCollectionViewLayoutAttributes.setHidden_, 0)

        self.assertResultIsBOOL(NSCollectionViewLayoutInvalidationContext.invalidateEverything)
        self.assertResultIsBOOL(NSCollectionViewLayoutInvalidationContext.invalidateDataSourceCounts)

        self.assertResultIsBOOL(NSCollectionViewLayout.shouldInvalidateLayoutForBoundsChange_)
        self.assertResultIsBOOL(NSCollectionViewLayout.shouldInvalidateLayoutForPreferredLayoutAttributes_withOriginalAttributes_)

if __name__ == "__main__":
    main()
