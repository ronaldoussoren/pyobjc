import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSOrderedCollectionDifference(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(
            Foundation.NSOrderedCollectionDifferenceCalculationOptions
        )

    def test_constants(self):
        self.assertEqual(
            Foundation.NSOrderedCollectionDifferenceCalculationOmitInsertedObjects,
            1 << 0,
        )
        self.assertEqual(
            Foundation.NSOrderedCollectionDifferenceCalculationOmitRemovedObjects,
            1 << 1,
        )
        self.assertEqual(
            Foundation.NSOrderedCollectionDifferenceCalculationInferMoves, 1 << 2
        )

    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSOrderedCollectionDifference.hasChanges)
        self.assertArgIsBlock(
            Foundation.NSOrderedCollectionDifference.differenceByTransformingChangesWithBlock_,
            0,
            b"@@",
        )
