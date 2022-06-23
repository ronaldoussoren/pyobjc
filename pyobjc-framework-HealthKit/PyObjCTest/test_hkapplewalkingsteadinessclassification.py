from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKAppleWalkingSteadinessClassification(TestCase):
    def test_constants(self):
        self.assertEqual(HealthKit.HKAppleWalkingSteadinessClassificationOK, 1)
        self.assertEqual(HealthKit.HKAppleWalkingSteadinessClassificationLow, 2)
        self.assertEqual(HealthKit.HKAppleWalkingSteadinessClassificationVeryLow, 3)

    def test_functions(self):
        self.assertResultIsBOOL(
            HealthKit.HKAppleWalkingSteadinessClassificationForQuantity
        )
        self.assertArgIsOut(
            HealthKit.HKAppleWalkingSteadinessClassificationForQuantity, 2
        )

        HealthKit.HKAppleWalkingSteadinessMinimumQuantityForClassification
        HealthKit.HKAppleWalkingSteadinessMaximumQuantityForClassification
