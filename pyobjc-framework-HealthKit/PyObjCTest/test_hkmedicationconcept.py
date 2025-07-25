from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKMedicationConcept(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(HealthKit.HKMedicationGeneralForm, str)

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertEqual(HealthKit.HKMedicationGeneralFormCapsule, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormCream, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormDevice, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormDrops, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormFoam, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormGel, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormInhaler, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormInjection, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormLiquid, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormLotion, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormOintment, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormPatch, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormPowder, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormSpray, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormSuppository, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormTablet, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormTopical, str)
        self.assertEqual(HealthKit.HKMedicationGeneralFormUnknown, str)
