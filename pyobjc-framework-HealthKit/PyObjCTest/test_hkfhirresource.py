from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKFHIRResource(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(HealthKit.HKFHIRResourceType, str)
        self.assertIsInstance(HealthKit.HKFHIRResourceTypeAllergyIntolerance, str)
        self.assertIsInstance(HealthKit.HKFHIRResourceTypeCondition, str)
        self.assertIsInstance(HealthKit.HKFHIRResourceTypeCoverage, str)
        self.assertIsInstance(HealthKit.HKFHIRResourceTypeImmunization, str)
        self.assertIsInstance(HealthKit.HKFHIRResourceTypeMedicationDispense, str)
        self.assertIsInstance(HealthKit.HKFHIRResourceTypeMedicationOrder, str)
        self.assertIsInstance(HealthKit.HKFHIRResourceTypeMedicationRequest, str)
        self.assertIsInstance(HealthKit.HKFHIRResourceTypeMedicationStatement, str)
        self.assertIsInstance(HealthKit.HKFHIRResourceTypeObservation, str)
        self.assertIsInstance(HealthKit.HKFHIRResourceTypeProcedure, str)
