import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc

NSCollectionViewCompositionalLayoutSectionProvider = b"@q@"
NSCollectionLayoutSectionVisibleItemsInvalidationHandler = (
    b"v@" + AppKit.NSPoint.__typestr__ + b"@"
)

NSCollectionViewDiffableDataSourceItemProvider = b"@@@" + objc._C_NSInteger
NSCollectionViewDiffableDataSourceSupplementaryViewProvider = b"@@@@"


class TestNSCollectionViewCompositionalLayoutHelper(AppKit.NSObject):
    def contentSize(self):
        return 1

    def effectiveContentSize(self):
        return 1

    def contentInsets(self):
        return 1

    def effectiveContentInsets(self):
        return 1

    def alpha(self):
        return 1

    def zIndex(self):
        return 1

    def isHidden(self):
        return 1

    def frame(self):
        return 1

    def bounds(self):
        return 1

    def representedElementCategory(self):
        return 1


class TestNSCollectionViewCompositionalLayout(TestCase):
    def test_constants(self):
        self.assertEqual(AppKit.NSDirectionalRectEdgeNone, 0)
        self.assertEqual(AppKit.NSDirectionalRectEdgeTop, 1 << 0)
        self.assertEqual(AppKit.NSDirectionalRectEdgeLeading, 1 << 1)
        self.assertEqual(AppKit.NSDirectionalRectEdgeBottom, 1 << 2)
        self.assertEqual(AppKit.NSDirectionalRectEdgeTrailing, 1 << 3)
        self.assertEqual(
            AppKit.NSDirectionalRectEdgeAll,
            AppKit.NSDirectionalRectEdgeTop
            | AppKit.NSDirectionalRectEdgeLeading
            | AppKit.NSDirectionalRectEdgeBottom
            | AppKit.NSDirectionalRectEdgeTrailing,
        )

        self.assertEqual(AppKit.NSRectAlignmentNone, 0)
        self.assertEqual(AppKit.NSRectAlignmentTop, 1)
        self.assertEqual(AppKit.NSRectAlignmentTopLeading, 2)
        self.assertEqual(AppKit.NSRectAlignmentLeading, 3)
        self.assertEqual(AppKit.NSRectAlignmentBottomLeading, 4)
        self.assertEqual(AppKit.NSRectAlignmentBottom, 5)
        self.assertEqual(AppKit.NSRectAlignmentBottomTrailing, 6)
        self.assertEqual(AppKit.NSRectAlignmentTrailing, 7)
        self.assertEqual(AppKit.NSRectAlignmentTopTrailing, 8)

        self.assertEqual(
            AppKit.NSCollectionLayoutSectionOrthogonalScrollingBehaviorNone, 0
        )
        self.assertEqual(
            AppKit.NSCollectionLayoutSectionOrthogonalScrollingBehaviorContinuous, 1
        )
        self.assertEqual(
            AppKit.NSCollectionLayoutSectionOrthogonalScrollingBehaviorContinuousGroupLeadingBoundary,  # noqa: B950
            2,
        )
        self.assertEqual(
            AppKit.NSCollectionLayoutSectionOrthogonalScrollingBehaviorPaging, 3
        )
        self.assertEqual(
            AppKit.NSCollectionLayoutSectionOrthogonalScrollingBehaviorGroupPaging, 4
        )
        self.assertEqual(
            AppKit.NSCollectionLayoutSectionOrthogonalScrollingBehaviorGroupPagingCentered,
            5,
        )

    @min_os_level("10.15")
    def test_contants10_15(self):
        self.assertIsInstance(
            AppKit.NSDirectionalEdgeInsetsZero, AppKit.NSDirectionalEdgeInsets
        )

    def test_structs(self):
        v = AppKit.NSDirectionalEdgeInsets()
        self.assertEqual(v.top, 0.0)
        self.assertEqual(v.leading, 0.0)
        self.assertEqual(v.bottom, 0.0)
        self.assertEqual(v.trailing, 0.0)

    @min_sdk_level("10.15")
    def test_functions_10_15(self):
        v = AppKit.NSDirectionalEdgeInsetsMake(1, 2, 3, 4)
        self.assertIsInstance(v, AppKit.NSDirectionalEdgeInsets)
        self.assertEqual(v.top, 1.0)
        self.assertEqual(v.leading, 2.0)
        self.assertEqual(v.bottom, 3.0)
        self.assertEqual(v.trailing, 4.0)

    @min_os_level("10.15")
    def test_methods_10_15(self):
        self.assertArgIsBlock(
            AppKit.NSCollectionViewCompositionalLayout.initWithSectionProvider_,
            0,
            NSCollectionViewCompositionalLayoutSectionProvider,
        )
        self.assertArgIsBlock(
            AppKit.NSCollectionViewCompositionalLayout.initWithSectionProvider_configuration_,
            0,
            NSCollectionViewCompositionalLayoutSectionProvider,
        )

        self.assertResultIsBOOL(
            AppKit.NSCollectionLayoutSection.supplementariesFollowContentInsets
        )
        self.assertArgIsBOOL(
            AppKit.NSCollectionLayoutSection.setSupplementariesFollowContentInsets_, 0
        )

        self.assertResultIsBlock(
            AppKit.NSCollectionLayoutSection.visibleItemsInvalidationHandler,
            NSCollectionLayoutSectionVisibleItemsInvalidationHandler,
        )
        self.assertArgIsBlock(
            AppKit.NSCollectionLayoutSection.setVisibleItemsInvalidationHandler_,
            0,
            NSCollectionLayoutSectionVisibleItemsInvalidationHandler,
        )

        self.assertResultIsBOOL(AppKit.NSCollectionLayoutDimension.isFractionalWidth)
        self.assertResultIsBOOL(AppKit.NSCollectionLayoutDimension.isFractionalHeight)
        self.assertResultIsBOOL(AppKit.NSCollectionLayoutDimension.isAbsolute)
        self.assertResultIsBOOL(AppKit.NSCollectionLayoutDimension.isEstimated)

        self.assertResultIsBOOL(AppKit.NSCollectionLayoutSpacing.isFlexibleSpacing)
        self.assertResultIsBOOL(AppKit.NSCollectionLayoutSpacing.isFixedSpacing)

        self.assertResultIsBOOL(AppKit.NSCollectionLayoutAnchor.isAbsoluteOffset)
        self.assertResultIsBOOL(AppKit.NSCollectionLayoutAnchor.isFractionalOffset)

        self.assertResultHasType(
            TestNSCollectionViewCompositionalLayoutHelper.contentSize,
            AppKit.NSSize.__typestr__,
        )
        self.assertResultHasType(
            TestNSCollectionViewCompositionalLayoutHelper.effectiveContentSize,
            AppKit.NSSize.__typestr__,
        )
        self.assertResultHasType(
            TestNSCollectionViewCompositionalLayoutHelper.contentInsets,
            AppKit.NSDirectionalEdgeInsets.__typestr__,
        )
        self.assertResultHasType(
            TestNSCollectionViewCompositionalLayoutHelper.effectiveContentInsets,
            AppKit.NSDirectionalEdgeInsets.__typestr__,
        )
        self.assertResultHasType(
            TestNSCollectionViewCompositionalLayoutHelper.alpha, objc._C_CGFloat
        )
        self.assertResultHasType(
            TestNSCollectionViewCompositionalLayoutHelper.zIndex, objc._C_NSInteger
        )
        self.assertResultHasType(
            TestNSCollectionViewCompositionalLayoutHelper.isHidden, objc._C_NSBOOL
        )
        self.assertResultHasType(
            TestNSCollectionViewCompositionalLayoutHelper.frame,
            AppKit.NSRect.__typestr__,
        )
        self.assertResultHasType(
            TestNSCollectionViewCompositionalLayoutHelper.bounds,
            AppKit.NSRect.__typestr__,
        )
        self.assertResultHasType(
            TestNSCollectionViewCompositionalLayoutHelper.representedElementCategory,
            objc._C_NSInteger,
        )

        self.assertArgIsBlock(
            AppKit.NSCollectionViewDiffableDataSource.initWithCollectionView_itemProvider_,
            1,
            NSCollectionViewDiffableDataSourceItemProvider,
        )
        self.assertArgIsBOOL(
            AppKit.NSCollectionViewDiffableDataSource.applySnapshot_animatingDifferences_,
            1,
        )

        self.assertResultIsBlock(
            AppKit.NSCollectionViewDiffableDataSource.supplementaryViewProvider,
            NSCollectionViewDiffableDataSourceSupplementaryViewProvider,
        )
        self.assertArgIsBlock(
            AppKit.NSCollectionViewDiffableDataSource.setSupplementaryViewProvider_,
            0,
            NSCollectionViewDiffableDataSourceSupplementaryViewProvider,
        )

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("NSCollectionLayoutContainer")
        objc.protocolNamed("NSCollectionLayoutEnvironment")
        objc.protocolNamed("NSCollectionLayoutVisibleItem")
