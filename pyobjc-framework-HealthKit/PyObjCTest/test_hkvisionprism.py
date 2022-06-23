from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKVisionPrism(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKPrismBase)
        self.assertEqual(HealthKit.HKPrismBaseNone, 0)
        self.assertEqual(HealthKit.HKPrismBaseUp, 1)
        self.assertEqual(HealthKit.HKPrismBaseDown, 2)
        self.assertEqual(HealthKit.HKPrismBaseIn, 3)
        self.assertEqual(HealthKit.HKPrismBaseOut, 4)

        self.assertIsEnumType(HealthKit.HKVisionEye)
        self.assertEqual(HealthKit.HKVisionEyeLeft, 1)
        self.assertEqual(HealthKit.HKVisionEyeRight, 2)
