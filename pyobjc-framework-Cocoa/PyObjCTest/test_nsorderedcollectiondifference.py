from PyObjCTools.TestSupport import *
from Foundation import *


class TestNSOrderedCollectionDifference(TestCase):
    def test_constants(self):
        self.assertEqual(
            NSOrderedCollectionDifferenceCalculationOmitInsertedObjects, 1 << 0
        )
        self.assertEqual(
            NSOrderedCollectionDifferenceCalculationOmitRemovedObjects, 1 << 1
        )
        self.assertEqual(NSOrderedCollectionDifferenceCalculationInferMoves, 1 << 2)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsBOOL(NSOrderedCollectionDifference.hasChanges)
        self.assertArgIsBlock(
            NSOrderedCollectionDifference.differenceByTransformingChangesWithBlock_,
            0,
            b"@@",
        )


if __name__ == "__main__":
    main()
