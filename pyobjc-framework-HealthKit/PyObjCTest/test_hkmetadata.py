from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKMetadata(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKMetadataKeyDeviceSerialNumber, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyBodyTemperatureSensorLocation, str)

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

        self.assertIsInstance(HealthKit.HKMetadataKeyHeartRateSensorLocation, str)

        self.assertIsEnumType(HealthKit.HKHeartRateSensorLocation)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationOther, 0)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationChest, 1)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationWrist, 2)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationFinger, 3)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationHand, 4)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationEarLobe, 5)
        self.assertEqual(HealthKit.HKHeartRateSensorLocationFoot, 6)

        self.assertIsInstance(HealthKit.HKMetadataKeyHeartRateMotionContext, str)

        self.assertIsEnumType(HealthKit.HKHeartRateMotionContext)
        self.assertEqual(HealthKit.HKHeartRateMotionContextNotSet, 0)
        self.assertEqual(HealthKit.HKHeartRateMotionContextSedentary, 1)
        self.assertEqual(HealthKit.HKHeartRateMotionContextActive, 2)

        self.assertIsInstance(HealthKit.HKMetadataKeyUserMotionContext, str)

        self.assertIsEnumType(HealthKit.HKUserMotionContext)
        self.assertEqual(HealthKit.HKUserMotionContextNotSet, 0)
        self.assertEqual(HealthKit.HKUserMotionContextStationary, 1)
        self.assertEqual(HealthKit.HKUserMotionContextActive, 2)

        self.assertIsInstance(HealthKit.HKMetadataKeySessionEstimate, str)

        self.assertIsEnumType(HealthKit.HKHeartRateRecoveryTestType)
        self.assertEqual(HealthKit.HKHeartRateRecoveryTestTypeMaxExercise, 1)
        self.assertEqual(
            HealthKit.HKHeartRateRecoveryTestTypePredictionSubMaxExercise, 2
        )
        self.assertEqual(HealthKit.HKHeartRateRecoveryTestTypePredictionNonExercise, 3)

        self.assertIsInstance(HealthKit.HKMetadataKeyHeartRateRecoveryTestType, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyHeartRateRecoveryActivityType, str)
        self.assertIsInstance(
            HealthKit.HKMetadataKeyHeartRateRecoveryActivityDuration, str
        )
        self.assertIsInstance(
            HealthKit.HKMetadataKeyHeartRateRecoveryMaxObservedRecoveryHeartRate, str
        )
        self.assertIsInstance(HealthKit.HKMetadataKeyFoodType, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyUDIDeviceIdentifier, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyUDIProductionIdentifier, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyDigitalSignature, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyExternalUUID, str)
        self.assertIsInstance(HealthKit.HKMetadataKeySyncIdentifier, str)
        self.assertIsInstance(HealthKit.HKMetadataKeySyncVersion, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyTimeZone, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyDeviceName, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyDeviceManufacturerName, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyWasTakenInLab, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyReferenceRangeLowerLimit, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyReferenceRangeUpperLimit, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyWasUserEntered, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyWorkoutBrandName, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyGroupFitness, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyIndoorWorkout, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyCoachedWorkout, str)

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

        self.assertIsInstance(HealthKit.HKMetadataKeyWeatherCondition, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyWeatherTemperature, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyWeatherHumidity, str)
        self.assertIsInstance(HealthKit.HKMetadataKeySexualActivityProtectionUsed, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyMenstrualCycleStart, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyLapLength, str)

        self.assertIsEnumType(HealthKit.HKWorkoutSwimmingLocationType)
        self.assertEqual(HealthKit.HKWorkoutSwimmingLocationTypeUnknown, 0)
        self.assertEqual(HealthKit.HKWorkoutSwimmingLocationTypePool, 1)
        self.assertEqual(HealthKit.HKWorkoutSwimmingLocationTypeOpenWater, 2)

        self.assertIsInstance(HealthKit.HKMetadataKeySwimmingLocationType, str)

        self.assertIsEnumType(HealthKit.HKSwimmingStrokeStyle)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleUnknown, 0)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleMixed, 1)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleFreestyle, 2)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleBackstroke, 3)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleBreaststroke, 4)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleButterfly, 5)
        self.assertEqual(HealthKit.HKSwimmingStrokeStyleKickboard, 6)

        self.assertIsInstance(HealthKit.HKMetadataKeySwimmingStrokeStyle, str)

        self.assertIsEnumType(HealthKit.HKInsulinDeliveryReason)
        self.assertEqual(HealthKit.HKInsulinDeliveryReasonBasal, 1)
        self.assertEqual(HealthKit.HKInsulinDeliveryReasonBolus, 2)

        self.assertIsInstance(HealthKit.HKMetadataKeyInsulinDeliveryReason, str)

        self.assertIsEnumType(HealthKit.HKBloodGlucoseMealTime)
        self.assertEqual(HealthKit.HKBloodGlucoseMealTimePreprandial, 1)
        self.assertEqual(HealthKit.HKBloodGlucoseMealTimePostprandial, 2)

        self.assertIsInstance(HealthKit.HKMetadataKeyBloodGlucoseMealTime, str)

        self.assertIsEnumType(HealthKit.HKVO2MaxTestType)
        self.assertEqual(HealthKit.HKVO2MaxTestTypeMaxExercise, 1)
        self.assertEqual(HealthKit.HKVO2MaxTestTypePredictionSubMaxExercise, 2)
        self.assertEqual(HealthKit.HKVO2MaxTestTypePredictionNonExercise, 3)

        self.assertIsInstance(HealthKit.HKMetadataKeyVO2MaxTestType, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyAverageSpeed, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyMaximumSpeed, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyAlpineSlopeGrade, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyElevationAscended, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyElevationDescended, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyFitnessMachineDuration, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyIndoorBikeDistance, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyCrossTrainerDistance, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyHeartRateEventThreshold, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyAverageMETs, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyAudioExposureLevel, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyAudioExposureDuration, str)

        self.assertIsEnumType(HealthKit.HKAppleECGAlgorithmVersion)
        self.assertEqual(HealthKit.HKAppleECGAlgorithmVersion1, 1)
        self.assertEqual(HealthKit.HKAppleECGAlgorithmVersion2, 2)

        self.assertIsInstance(HealthKit.HKMetadataKeyAppleECGAlgorithmVersion, str)

        self.assertIsEnumType(HealthKit.HKDevicePlacementSide)
        self.assertEqual(HealthKit.HKDevicePlacementSideUnknown, 0)
        self.assertEqual(HealthKit.HKDevicePlacementSideLeft, 1)
        self.assertEqual(HealthKit.HKDevicePlacementSideRight, 2)
        self.assertEqual(HealthKit.HKDevicePlacementSideCentral, 3)

        self.assertIsInstance(HealthKit.HKMetadataKeyDevicePlacementSide, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyBarometricPressure, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyAppleDeviceCalibrated, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyVO2MaxValue, str)
        self.assertIsInstance(
            HealthKit.HKMetadataKeyLowCardioFitnessEventThreshold, str
        )
        self.assertIsInstance(
            HealthKit.HKMetadataKeyDateOfEarliestDataUsedForEstimate, str
        )
        self.assertIsInstance(HealthKit.HKMetadataKeyAlgorithmVersion, str)
        self.assertIsInstance(HealthKit.HKMetadataKeySWOLFScore, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyQuantityClampedToLowerBound, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyQuantityClampedToUpperBound, str)
        self.assertIsInstance(
            HealthKit.HKMetadataKeyGlassesPrescriptionDescription, str
        )

        self.assertIsEnumType(HealthKit.HKWaterSalinity)
        self.assertEqual(HealthKit.HKWaterSalinityFreshWater, 1)
        self.assertEqual(HealthKit.HKWaterSalinitySaltWater, 2)

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

        self.assertIsEnumType(HealthKit.HKPhysicalEffortEstimationType)
        self.assertEqual(HealthKit.HKPhysicalEffortEstimationTypeActivityLookup, 1)
        self.assertEqual(HealthKit.HKPhysicalEffortEstimationTypeDeviceSensed, 2)

    @min_os_level("13.3")
    def test_constants13_3(self):
        self.assertIsInstance(HealthKit.HKMetadataKeyHeadphoneGain, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(HealthKit.HKMetadataKeyAppleFitnessPlusSession, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyWaterSalinity, str)
        self.assertIsInstance(
            HealthKit.HKMetadataKeyCyclingFunctionalThresholdPowerTestType, str
        )
        self.assertIsInstance(HealthKit.HKMetadataKeyActivityType, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyPhysicalEffortEstimationType, str)
        self.assertIsInstance(HealthKit.HKMetadataKeyMaximumLightIntensity, str)
