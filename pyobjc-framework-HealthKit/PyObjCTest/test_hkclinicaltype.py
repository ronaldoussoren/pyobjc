from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKClinicalType(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(HealthKit.HKClinicalTypeIdentifier, str)

        self.assertIsInstance(HealthKit.HKClinicalTypeIdentifierAllergyRecord, str)
        self.assertIsInstance(HealthKit.HKClinicalTypeIdentifierConditionRecord, str)
        self.assertIsInstance(HealthKit.HKClinicalTypeIdentifierImmunizationRecord, str)
        self.assertIsInstance(HealthKit.HKClinicalTypeIdentifierLabResultRecord, str)
        self.assertIsInstance(HealthKit.HKClinicalTypeIdentifierMedicationRecord, str)
        self.assertIsInstance(HealthKit.HKClinicalTypeIdentifierProcedureRecord, str)
        self.assertIsInstance(HealthKit.HKClinicalTypeIdentifierVitalSignRecord, str)
        self.assertIsInstance(HealthKit.HKClinicalTypeIdentifierCoverageRecord, str)
