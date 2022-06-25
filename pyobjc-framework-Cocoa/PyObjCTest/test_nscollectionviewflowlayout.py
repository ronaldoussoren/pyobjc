import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSCollectionViewFlowLayoutHelper(AppKit.NSObject):
    def collectionView_layout_sizeForItemAtIndexPath_(self, cv, x, p):
        return 1

    def collectionView_layout_insetForSectionAtIndex_(self, cv, x, p):
        return 1

    def collectionView_layout_minimumLineSpacingForSectionAtIndex_(self, cv, x, p):
        return 1

    def collectionView_layout_minimumInteritemSpacingForSectionAtIndex_(self, cv, x, p):
        return 1

    def collectionView_layout_referenceSizeForHeaderInSection_(self, cv, x, p):
        return 1

    def collectionView_layout_referenceSizeForFooterInSection_(self, cv, x, p):
        return 1


class TestNSCollectionViewFlowLayout(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSCollectionViewScrollDirection)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(AppKit.NSCollectionViewScrollDirectionVertical, 0)
        self.assertEqual(AppKit.NSCollectionViewScrollDirectionHorizontal, 1)
        self.assertIsInstance(AppKit.NSCollectionElementKindSectionHeader, str)
        self.assertIsInstance(AppKit.NSCollectionElementKindSectionFooter, str)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(
            AppKit.NSCollectionViewFlowLayoutInvalidationContext.invalidateFlowLayoutDelegateMetrics  # noqa: B950
        )
        self.assertArgIsBOOL(
            AppKit.NSCollectionViewFlowLayoutInvalidationContext.setInvalidateFlowLayoutDelegateMetrics_,  # noqa: B950
            0,
        )
        self.assertResultIsBOOL(
            AppKit.NSCollectionViewFlowLayoutInvalidationContext.invalidateFlowLayoutAttributes
        )
        self.assertArgIsBOOL(
            AppKit.NSCollectionViewFlowLayoutInvalidationContext.setInvalidateFlowLayoutAttributes_,  # noqa: B950
            0,
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(
            AppKit.NSCollectionViewFlowLayout.sectionHeadersPinToVisibleBounds
        )
        self.assertArgIsBOOL(
            AppKit.NSCollectionViewFlowLayout.setSectionHeadersPinToVisibleBounds_, 0
        )

        self.assertResultIsBOOL(
            AppKit.NSCollectionViewFlowLayout.sectionFootersPinToVisibleBounds
        )
        self.assertArgIsBOOL(
            AppKit.NSCollectionViewFlowLayout.setSectionFootersPinToVisibleBounds_, 0
        )

        self.assertResultIsBOOL(
            AppKit.NSCollectionViewFlowLayout.sectionAtIndexIsCollapsed_
        )

    @min_os_level("10.11")
    def testProtocols10_11(self):
        self.assertProtocolExists("NSCollectionViewDelegateFlowLayout")

        self.assertResultHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_sizeForItemAtIndexPath_,
            AppKit.NSSize.__typestr__,
        )

        self.assertResultHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_insetForSectionAtIndex_,
            AppKit.NSEdgeInsets.__typestr__,
        )
        self.assertArgHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_insetForSectionAtIndex_,
            2,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_minimumLineSpacingForSectionAtIndex_,  # noqa: B950
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_minimumLineSpacingForSectionAtIndex_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_minimumInteritemSpacingForSectionAtIndex_,  # noqa: B950
            objc._C_CGFloat,
        )
        self.assertArgHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_minimumInteritemSpacingForSectionAtIndex_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_referenceSizeForHeaderInSection_,  # noqa: B950
            AppKit.NSSize.__typestr__,
        )
        self.assertArgHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_referenceSizeForHeaderInSection_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_referenceSizeForFooterInSection_,  # noqa: B950
            AppKit.NSSize.__typestr__,
        )
        self.assertArgHasType(
            TestNSCollectionViewFlowLayoutHelper.collectionView_layout_referenceSizeForFooterInSection_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )
