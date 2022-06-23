from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKVisionPrescription(TestCase):
    def test_constants(self):
        self.assertEqual(HealthKit.HKVisionPrescriptionTypeGlasses, 1)
        self.assertEqual(HealthKit.HKVisionPrescriptionTypeContacts, 2)
