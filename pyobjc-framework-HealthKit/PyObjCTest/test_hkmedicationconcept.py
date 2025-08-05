from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKMedicationConcept(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(HealthKit.HKMedicationGeneralForm, str)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormCapsule, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormCream, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormDevice, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormDrops, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormFoam, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormGel, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormInhaler, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormInjection, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormLiquid, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormLotion, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormOintment, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormPatch, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormPowder, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormSpray, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormSuppository, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormTablet, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormTopical, str)
        self.assertIsInstance(HealthKit.HKMedicationGeneralFormUnknown, str)
