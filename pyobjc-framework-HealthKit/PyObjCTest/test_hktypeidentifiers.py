from PyObjCTools.TestSupport import TestCase, min_os_level
import HealthKit


class TestHKTypeIdentifiers(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(HealthKit.HKQuantityTypeIdentifier, str)

        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierBodyMassIndex, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierBodyFatPercentage, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierHeight, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierBodyMass, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierLeanBodyMass, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierWaistCircumference, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierAppleSleepingWristTemperature, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierStepCount, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierDistanceWalkingRunning, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDistanceCycling, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDistanceWheelchair, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierBasalEnergyBurned, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierActiveEnergyBurned, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierFlightsClimbed, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierNikeFuel, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierAppleExerciseTime, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierPushCount, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDistanceSwimming, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierSwimmingStrokeCount, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierVO2Max, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierDistanceDownhillSnowSports, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierAppleStandTime, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierWalkingSpeed, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierWalkingDoubleSupportPercentage, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierWalkingAsymmetryPercentage, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierWalkingStepLength, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierSixMinuteWalkTestDistance, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierStairAscentSpeed, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierStairDescentSpeed, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierAppleMoveTime, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierAppleWalkingSteadiness, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierRunningStrideLength, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierRunningVerticalOscillation, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierRunningGroundContactTime, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierRunningPower, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierRunningSpeed, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierHeartRate, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierBodyTemperature, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierBasalBodyTemperature, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierBloodPressureSystolic, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierBloodPressureDiastolic, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierRespiratoryRate, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierRestingHeartRate, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierWalkingHeartRateAverage, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierHeartRateVariabilitySDNN, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierHeartRateRecoveryOneMinute, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierOxygenSaturation, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierPeripheralPerfusionIndex, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierBloodGlucose, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierNumberOfTimesFallen, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierElectrodermalActivity, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierInhalerUsage, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierInsulinDelivery, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierBloodAlcoholContent, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierForcedVitalCapacity, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierForcedExpiratoryVolume1, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierPeakExpiratoryFlowRate, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierEnvironmentalAudioExposure, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierHeadphoneAudioExposure, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierNumberOfAlcoholicBeverages, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryFatTotal, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierDietaryFatPolyunsaturated, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierDietaryFatMonounsaturated, str
        )
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierDietaryFatSaturated, str, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryCholesterol, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietarySodium, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierDietaryCarbohydrates, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryFiber, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietarySugar, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierDietaryEnergyConsumed, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryProtein, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryVitaminA, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryVitaminB6, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryVitaminB12, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryVitaminC, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryVitaminD, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryVitaminE, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryVitaminK, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryCalcium, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryIron, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryThiamin, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryRiboflavin, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryNiacin, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryFolate, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryBiotin, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierDietaryPantothenicAcid, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryPhosphorus, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryIodine, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryMagnesium, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryZinc, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietarySelenium, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryCopper, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryManganese, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryChromium, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryMolybdenum, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryChloride, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryPotassium, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryCaffeine, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierDietaryWater, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierUVExposure, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierAtrialFibrillationBurden, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierUnderwaterDepth, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierWaterTemperature, str)

        self.assertIsTypedEnum(HealthKit.HKCategoryTypeIdentifier, str)

        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierSleepAnalysis, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierAppleStandHour, str)
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierCervicalMucusQuality, str
        )
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierOvulationTestResult, str
        )
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierPregnancyTestResult, str
        )
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierProgesteroneTestResult, str
        )
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierMenstrualFlow, str)
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierIntermenstrualBleeding, str
        )
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierPersistentIntermenstrualBleeding, str
        )
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierProlongedMenstrualPeriods, str
        )
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierIrregularMenstrualCycles, str
        )
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierInfrequentMenstrualCycles, str
        )
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierSexualActivity, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierMindfulSession, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierHighHeartRateEvent, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierLowHeartRateEvent, str)
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierIrregularHeartRhythmEvent, str
        )
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierAudioExposureEvent, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierToothbrushingEvent, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierPregnancy, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierLactation, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierContraceptive, str)
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierEnvironmentalAudioExposureEvent, str
        )
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierHeadphoneAudioExposureEvent, str
        )
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierHandwashingEvent, str)
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierLowCardioFitnessEvent, str
        )
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierAppleWalkingSteadinessEvent, str
        )
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierAbdominalCramps, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierAcne, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierAppetiteChanges, str)
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierBladderIncontinence, str
        )
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierBloating, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierBreastPain, str)
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierChestTightnessOrPain, str
        )
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierChills, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierConstipation, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierCoughing, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierDiarrhea, str, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierDizziness, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierDrySkin, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierFainting, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierFatigue, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierFever, str)
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierGeneralizedBodyAche, str
        )
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierHairLoss, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierHeadache, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierHeartburn, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierHotFlashes, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierLossOfSmell, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierLossOfTaste, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierLowerBackPain, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierMemoryLapse, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierMoodChanges, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierNausea, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierNightSweats, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierPelvicPain, str)
        self.assertIsInstance(
            HealthKit.HKCategoryTypeIdentifierRapidPoundingOrFlutteringHeartbeat, str
        )
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierRunnyNose, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierShortnessOfBreath, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierSinusCongestion, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierSkippedHeartbeat, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierSleepChanges, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierSoreThroat, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierVaginalDryness, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierVomiting, str)
        self.assertIsInstance(HealthKit.HKCategoryTypeIdentifierWheezing, str)

        self.assertIsTypedEnum(HealthKit.HKCharacteristicTypeIdentifier, str)

        self.assertIsInstance(
            HealthKit.HKCharacteristicTypeIdentifierBiologicalSex, str
        )
        self.assertIsInstance(HealthKit.HKCharacteristicTypeIdentifierBloodType, str)
        self.assertIsInstance(HealthKit.HKCharacteristicTypeIdentifierDateOfBirth, str)
        self.assertIsInstance(
            HealthKit.HKCharacteristicTypeIdentifierFitzpatrickSkinType, str
        )
        self.assertIsInstance(
            HealthKit.HKCharacteristicTypeIdentifierWheelchairUse, str
        )
        self.assertIsInstance(
            HealthKit.HKCharacteristicTypeIdentifierActivityMoveMode, str
        )

        self.assertIsTypedEnum(HealthKit.HKCorrelationTypeIdentifier, str)

        self.assertIsInstance(HealthKit.HKCorrelationTypeIdentifierBloodPressure, str)
        self.assertIsInstance(HealthKit.HKCorrelationTypeIdentifierFood, str)

        self.assertIsTypedEnum(HealthKit.HKDocumentTypeIdentifier, str)

        self.assertIsInstance(HealthKit.HKDocumentTypeIdentifierCDA, str)
        self.assertIsInstance(HealthKit.HKWorkoutTypeIdentifier, str)
        self.assertIsInstance(HealthKit.HKWorkoutRouteTypeIdentifier, str)
        self.assertIsInstance(HealthKit.HKDataTypeIdentifierHeartbeatSeries, str)
        self.assertIsInstance(HealthKit.HKVisionPrescriptionTypeIdentifier, str)

    @min_os_level("14.0")
    def test_constants14_0(self):
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierCyclingCadence, str)
        self.assertIsInstance(
            HealthKit.HKQuantityTypeIdentifierCyclingFunctionalThresholdPower, str
        )
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierCyclingPower, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierCyclingSpeed, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierPhysicalEffort, str)
        self.assertIsInstance(HealthKit.HKQuantityTypeIdentifierTimeInDaylight, str)
