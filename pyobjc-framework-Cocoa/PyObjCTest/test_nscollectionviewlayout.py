import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSCollectionViewLayout(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSCollectionElementCategory)
        self.assertIsEnumType(AppKit.NSCollectionUpdateAction)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(AppKit.NSCollectionElementCategoryItem, 0)
        self.assertEqual(AppKit.NSCollectionElementCategorySupplementaryView, 1)
        self.assertEqual(AppKit.NSCollectionElementCategoryDecorationView, 2)
        self.assertEqual(AppKit.NSCollectionElementCategoryInterItemGap, 3)

        self.assertEqual(AppKit.NSCollectionUpdateActionInsert, 0)
        self.assertEqual(AppKit.NSCollectionUpdateActionDelete, 1)
        self.assertEqual(AppKit.NSCollectionUpdateActionReload, 2)
        self.assertEqual(AppKit.NSCollectionUpdateActionMove, 3)
        self.assertEqual(AppKit.NSCollectionUpdateActionNone, 4)

        self.assertIsInstance(AppKit.NSCollectionElementKindInterItemGapIndicator, str)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AppKit.NSCollectionViewLayoutAttributes.isHidden)
        self.assertArgIsBOOL(AppKit.NSCollectionViewLayoutAttributes.setHidden_, 0)

        self.assertResultIsBOOL(
            AppKit.NSCollectionViewLayoutInvalidationContext.invalidateEverything
        )
        self.assertResultIsBOOL(
            AppKit.NSCollectionViewLayoutInvalidationContext.invalidateDataSourceCounts
        )

        self.assertResultIsBOOL(
            AppKit.NSCollectionViewLayout.shouldInvalidateLayoutForBoundsChange_
        )
        self.assertResultIsBOOL(
            AppKit.NSCollectionViewLayout.shouldInvalidateLayoutForPreferredLayoutAttributes_withOriginalAttributes_  # noqa: B950
        )
