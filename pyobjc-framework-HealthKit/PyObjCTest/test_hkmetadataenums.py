from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKMetadataEnums(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKAppleECGAlgorithmVersion)
        self.assertEqual(HealthKit.HKAppleECGAlgorithmVersion1, 1)
        self.assertEqual(HealthKit.HKAppleECGAlgorithmVersion2, 2)

        self.assertIsEnumType(HealthKit.HKBloodGlucoseMealTime)
        self.assertEqual(HealthKit.HKBloodGlucoseMealTimePreprandial, 1)
        self.assertEqual(HealthKit.HKBloodGlucoseMealTimePostprandial, 2)

        self.assertIsEnumType(HealthKit.HKBodyTemperatureSensorLocation)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationOther, 0)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationArmpit, 1)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationBody, 2)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationEar, 3)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationFinger, 4)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationGastroIntestinal, 5)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationMouth, 6)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationRectum, 7)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationToe, 8)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationEarDrum, 9)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationTemporalArtery, 10)
        self.assertEqual(HealthKit.HKBodyTemperatureSensorLocationForehead, 11)

        self.assertIsEnumType(HealthKit.HKCyclingFunctionalThresholdPowerTestType)
        self.assertEqual(
            HealthKit.HKCyclingFunctionalThresholdPowerTestTypeMaxExercise60Minute, 1
        )
        self.assertEqual(
            HealthKit.HKCyclingFunctionalThresholdPowerTestTypeMaxExercise20Minute, 2
        )
        self.assertEqual(HealthKit.HKCyclingFunctionalThresholdPowerTestTypeRampTest, 3)
        self.assertEqual(
            HealthKit.HKCyclingFunctionalThresholdPowerTestTypePredictionExercise, 4
        )

        self.assertIsEnumType(HealthKit.HKDevicePlacementSide)
        self.assertEqual(HealthKit.HKDevicePlacementSideUnknown, 0)
        self.assertEqual(HealthKit.HKDevicePlacementSideLeft, 1)
        self.assertEqual(HealthKit.HKDevicePlacementSideRight, 2)
        self.assertEqual(HealthKit.HKDevicePlacementSideCentral, 3)

        self.assertIsEnumType(HealthKit.HKHeartRateMotionContext)
        self.assertEqual(HealthKit.HKHeartRateMotionContextNotSet, 0)
        self.assertEqual(HealthKit.HKHeartRateMotionContextSedentary, 1)
        self.assertEqual(HealthKit.HKHeartRateMotionContextActive, 2)

        self.assertIsEnumType(HealthKit.HKHeartRateRecoveryTestType)
        self.assertEqual(HealthKit.HKHeartRateRecoveryTestTypeMaxExercise, 1)
        self.assertEqual(
            HealthKit.HKHeartRateRecoveryTestTypePredictionSubMaxExercise, 2
        )
        self.assertEqual(HealthKit.HKHeartRateRecoveryTestTypePredictionNonExercise, 3)

        self.assertIsEnumType(HealthKit.HKHeartRateSensorLocation)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationOther, 0)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationChest, 1)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationWrist, 2)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationFinger, 3)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationHand, 4)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationEarLobe, 5)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationFoot, 6)

        self.assertIsEnumType(HealthKit.HKInsulinDeliveryReason)
        self.assertEqual(HealthKit.HKInsulinDeliveryReasonBasal, 1)
        self.assertEqual(HealthKit.HKInsulinDeliveryReasonBolus, 2)

        self.assertIsEnumType(HealthKit.HKPhysicalEffortEstimationType)
        self.assertEqual(HealthKit.HKPhysicalEffortEstimationTypeActivityLookup, 1)
        self.assertEqual(HealthKit.HKPhysicalEffortEstimationTypeDeviceSensed, 2)

        self.assertIsEnumType(HealthKit.HKSwimmingStrokeStyle)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleUnknown, 0)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleMixed, 1)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleFreestyle, 2)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleBackstroke, 3)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleBreaststroke, 4)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleButterfly, 5)

        self.assertIsEnumType(HealthKit.HKUserMotionContext)
        self.assertEqual(HealthKit.HKUserMotionContextNotSet, 0)
        self.assertEqual(HealthKit.HKUserMotionContextStationary, 1)
        self.assertEqual(HealthKit.HKUserMotionContextActive, 2)

        self.assertIsEnumType(HealthKit.HKVO2MaxTestType)
        self.assertEqual(HealthKit.HKVO2MaxTestTypeMaxExercise, 1)
        self.assertEqual(HealthKit.HKVO2MaxTestTypePredictionSubMaxExercise, 2)
        self.assertEqual(HealthKit.HKVO2MaxTestTypePredictionNonExercise, 3)
        self.assertEqual(HealthKit.HKVO2MaxTestTypePredictionStepTest, 4)

        self.assertIsEnumType(HealthKit.HKWaterSalinity)
        self.assertEqual(HealthKit.HKWaterSalinityFreshWater, 1)
        self.assertEqual(HealthKit.HKWaterSalinitySaltWater, 2)

        self.assertIsEnumType(HealthKit.HKWeatherCondition)
        self.assertEqual(HealthKit.HKWeatherConditionNone, 0)
        self.assertEqual(HealthKit.HKWeatherConditionClear, 1)
        self.assertEqual(HealthKit.HKWeatherConditionFair, 2)
        self.assertEqual(HealthKit.HKWeatherConditionPartlyCloudy, 3)
        self.assertEqual(HealthKit.HKWeatherConditionMostlyCloudy, 4)
        self.assertEqual(HealthKit.HKWeatherConditionCloudy, 5)
        self.assertEqual(HealthKit.HKWeatherConditionFoggy, 6)
        self.assertEqual(HealthKit.HKWeatherConditionHaze, 7)
        self.assertEqual(HealthKit.HKWeatherConditionWindy, 8)
        self.assertEqual(HealthKit.HKWeatherConditionBlustery, 9)
        self.assertEqual(HealthKit.HKWeatherConditionSmoky, 10)
        self.assertEqual(HealthKit.HKWeatherConditionDust, 11)
        self.assertEqual(HealthKit.HKWeatherConditionSnow, 12)
        self.assertEqual(HealthKit.HKWeatherConditionHail, 13)
        self.assertEqual(HealthKit.HKWeatherConditionSleet, 14)
        self.assertEqual(HealthKit.HKWeatherConditionFreezingDrizzle, 15)
        self.assertEqual(HealthKit.HKWeatherConditionFreezingRain, 16)
        self.assertEqual(HealthKit.HKWeatherConditionMixedRainAndHail, 17)
        self.assertEqual(HealthKit.HKWeatherConditionMixedRainAndSnow, 18)
        self.assertEqual(HealthKit.HKWeatherConditionMixedRainAndSleet, 19)
        self.assertEqual(HealthKit.HKWeatherConditionMixedSnowAndSleet, 20)
        self.assertEqual(HealthKit.HKWeatherConditionDrizzle, 21)
        self.assertEqual(HealthKit.HKWeatherConditionScatteredShowers, 22)
        self.assertEqual(HealthKit.HKWeatherConditionShowers, 23)
        self.assertEqual(HealthKit.HKWeatherConditionThunderstorms, 24)
        self.assertEqual(HealthKit.HKWeatherConditionTropicalStorm, 25)
        self.assertEqual(HealthKit.HKWeatherConditionHurricane, 26)
        self.assertEqual(HealthKit.HKWeatherConditionTornado, 27)

        self.assertIsEnumType(HealthKit.HKWorkoutSwimmingLocationType)
        self.assertEqual(HealthKit.HKWorkoutSwimmingLocationTypeUnknown, 0)
        self.assertEqual(HealthKit.HKWorkoutSwimmingLocationTypePool, 1)
        self.assertEqual(HealthKit.HKWorkoutSwimmingLocationTypeOpenWater, 2)
