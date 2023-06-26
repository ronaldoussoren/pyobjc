from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKCharacteristicValues(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKActivityMoveMode)
        self.assertEqual(HealthKit.HKActivityMoveModeActiveEnergy, 1)
        self.assertEqual(HealthKit.HKActivityMoveModeAppleMoveTime, 2)

        self.assertIsEnumType(HealthKit.HKBiologicalSex)
        self.assertEqual(HealthKit.HKBiologicalSexNotSet, 0)
        self.assertEqual(HealthKit.HKBiologicalSexFemale, 1)
        self.assertEqual(HealthKit.HKBiologicalSexMale, 2)
        self.assertEqual(HealthKit.HKBiologicalSexOther, 3)

        self.assertIsEnumType(HealthKit.HKBloodType)
        self.assertEqual(HealthKit.HKBloodTypeNotSet, 0)
        self.assertEqual(HealthKit.HKBloodTypeAPositive, 1)
        self.assertEqual(HealthKit.HKBloodTypeANegative, 2)
        self.assertEqual(HealthKit.HKBloodTypeBPositive, 3)
        self.assertEqual(HealthKit.HKBloodTypeBNegative, 4)
        self.assertEqual(HealthKit.HKBloodTypeABPositive, 5)
        self.assertEqual(HealthKit.HKBloodTypeABNegative, 6)
        self.assertEqual(HealthKit.HKBloodTypeOPositive, 7)
        self.assertEqual(HealthKit.HKBloodTypeONegative, 8)

        self.assertIsEnumType(HealthKit.HKFitzpatrickSkinType)
        self.assertEqual(HealthKit.HKFitzpatrickSkinTypeNotSet, 0)
        self.assertEqual(HealthKit.HKFitzpatrickSkinTypeI, 1)
        self.assertEqual(HealthKit.HKFitzpatrickSkinTypeII, 2)
        self.assertEqual(HealthKit.HKFitzpatrickSkinTypeIII, 3)
        self.assertEqual(HealthKit.HKFitzpatrickSkinTypeIV, 4)
        self.assertEqual(HealthKit.HKFitzpatrickSkinTypeV, 5)
        self.assertEqual(HealthKit.HKFitzpatrickSkinTypeVI, 6)

        self.assertIsEnumType(HealthKit.HKWheelchairUse)
        self.assertEqual(HealthKit.HKWheelchairUseNotSet, 0)
        self.assertEqual(HealthKit.HKWheelchairUseNo, 1)
        self.assertEqual(HealthKit.HKWheelchairUseYes, 2)
