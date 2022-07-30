from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKElectrocardiogram(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKElectrocardiogramLead)
        self.assertEqual(HealthKit.HKElectrocardiogramLeadAppleWatchSimilarToLeadI, 1)

        self.assertIsEnumType(HealthKit.HKElectrocardiogramClassification)
        self.assertEqual(HealthKit.HKElectrocardiogramClassificationNotSet, 0)
        self.assertEqual(HealthKit.HKElectrocardiogramClassificationSinusRhythm, 1)
        self.assertEqual(
            HealthKit.HKElectrocardiogramClassificationAtrialFibrillation, 2
        )
        self.assertEqual(
            HealthKit.HKElectrocardiogramClassificationInconclusiveLowHeartRate, 3
        )
        self.assertEqual(
            HealthKit.HKElectrocardiogramClassificationInconclusiveHighHeartRate, 4
        )
        self.assertEqual(
            HealthKit.HKElectrocardiogramClassificationInconclusivePoorReading, 5
        )
        self.assertEqual(
            HealthKit.HKElectrocardiogramClassificationInconclusiveOther, 6
        )
        self.assertEqual(HealthKit.HKElectrocardiogramClassificationUnrecognized, 100)

        self.assertIsEnumType(HealthKit.HKElectrocardiogramSymptomsStatus)
        self.assertEqual(HealthKit.HKElectrocardiogramSymptomsStatusNotSet, 0)
        self.assertEqual(HealthKit.HKElectrocardiogramSymptomsStatusNone, 1)
        self.assertEqual(HealthKit.HKElectrocardiogramSymptomsStatusPresent, 2)

        self.assertIsInstance(HealthKit.HKPredicateKeyPathAverageHeartRate, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathECGClassification, str)
        self.assertIsInstance(HealthKit.HKPredicateKeyPathECGSymptomsStatus, str)
