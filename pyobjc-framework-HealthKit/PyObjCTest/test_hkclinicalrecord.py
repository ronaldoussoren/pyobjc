from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKClinicalRecord(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            HealthKit.HKPredicateKeyPathClinicalRecordFHIRResourceIdentifier, str
        )
        self.assertIsInstance(
            HealthKit.HKPredicateKeyPathClinicalRecordFHIRResourceType, str
        )
