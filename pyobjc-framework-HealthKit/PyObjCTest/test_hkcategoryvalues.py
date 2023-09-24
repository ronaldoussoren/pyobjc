from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKCategoryValues(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKCategoryValue)
        self.assertEqual(HealthKit.HKCategoryValueNotApplicable, 0)

        self.assertIsEnumType(HealthKit.HKCategoryValueAppetiteChanges)
        self.assertEqual(HealthKit.HKCategoryValueAppetiteChangesUnspecified, 0)
        self.assertEqual(HealthKit.HKCategoryValueAppetiteChangesNoChange, 1)
        self.assertEqual(HealthKit.HKCategoryValueAppetiteChangesDecreased, 2)
        self.assertEqual(HealthKit.HKCategoryValueAppetiteChangesIncreased, 3)

        self.assertIsEnumType(HealthKit.HKCategoryValueAppleStandHour)
        self.assertEqual(HealthKit.HKCategoryValueAppleStandHourStood, 0)
        self.assertEqual(HealthKit.HKCategoryValueAppleStandHourIdle, 1)

        self.assertIsEnumType(HealthKit.HKCategoryValueAppleWalkingSteadinessEvent)
        self.assertEqual(
            HealthKit.HKCategoryValueAppleWalkingSteadinessEventInitialLow, 1
        )
        self.assertEqual(
            HealthKit.HKCategoryValueAppleWalkingSteadinessEventInitialVeryLow, 2
        )
        self.assertEqual(
            HealthKit.HKCategoryValueAppleWalkingSteadinessEventRepeatLow, 3
        )
        self.assertEqual(
            HealthKit.HKCategoryValueAppleWalkingSteadinessEventRepeatVeryLow, 4
        )

        self.assertIsEnumType(HealthKit.HKCategoryValueCervicalMucusQuality)
        self.assertEqual(HealthKit.HKCategoryValueCervicalMucusQualityDry, 1)
        self.assertEqual(HealthKit.HKCategoryValueCervicalMucusQualitySticky, 2)
        self.assertEqual(HealthKit.HKCategoryValueCervicalMucusQualityCreamy, 3)
        self.assertEqual(HealthKit.HKCategoryValueCervicalMucusQualityWatery, 4)
        self.assertEqual(HealthKit.HKCategoryValueCervicalMucusQualityEggWhite, 5)

        self.assertIsEnumType(HealthKit.HKCategoryValueContraceptive)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveUnspecified, 1)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveImplant, 2)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveInjection, 3)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveIntrauterineDevice, 4)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveIntravaginalRing, 5)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveOral, 6)
        self.assertEqual(HealthKit.HKCategoryValueContraceptivePatch, 7)

        self.assertIsEnumType(HealthKit.HKCategoryValueEnvironmentalAudioExposureEvent)
        self.assertEqual(
            HealthKit.HKCategoryValueEnvironmentalAudioExposureEventMomentaryLimit, 1
        )

        self.assertIsEnumType(HealthKit.HKCategoryValueHeadphoneAudioExposureEvent)
        self.assertEqual(
            HealthKit.HKCategoryValueHeadphoneAudioExposureEventSevenDayLimit, 1
        )

        self.assertIsEnumType(HealthKit.HKCategoryValueLowCardioFitnessEvent)
        self.assertEqual(HealthKit.HKCategoryValueLowCardioFitnessEventLowFitness, 1)

        self.assertIsEnumType(HealthKit.HKCategoryValueMenstrualFlow)
        self.assertEqual(HealthKit.HKCategoryValueMenstrualFlowUnspecified, 1)
        self.assertEqual(HealthKit.HKCategoryValueMenstrualFlowLight, 2)
        self.assertEqual(HealthKit.HKCategoryValueMenstrualFlowMedium, 3)
        self.assertEqual(HealthKit.HKCategoryValueMenstrualFlowHeavy, 4)
        self.assertEqual(HealthKit.HKCategoryValueMenstrualFlowNone, 5)

        self.assertIsEnumType(HealthKit.HKCategoryValueOvulationTestResult)
        self.assertEqual(HealthKit.HKCategoryValueOvulationTestResultNegative, 1)
        self.assertEqual(
            HealthKit.HKCategoryValueOvulationTestResultLuteinizingHormoneSurge, 2
        )
        self.assertEqual(
            HealthKit.HKCategoryValueOvulationTestResultPositive,
            HealthKit.HKCategoryValueOvulationTestResultLuteinizingHormoneSurge,
        )
        self.assertEqual(HealthKit.HKCategoryValueOvulationTestResultIndeterminate, 3)
        self.assertEqual(HealthKit.HKCategoryValueOvulationTestResultEstrogenSurge, 4)

        self.assertIsEnumType(HealthKit.HKCategoryValuePregnancyTestResult)
        self.assertEqual(HealthKit.HKCategoryValuePregnancyTestResultNegative, 1)
        self.assertEqual(HealthKit.HKCategoryValuePregnancyTestResultPositive, 2)
        self.assertEqual(HealthKit.HKCategoryValuePregnancyTestResultIndeterminate, 3)

        self.assertIsEnumType(HealthKit.HKCategoryValuePresence)
        self.assertEqual(HealthKit.HKCategoryValuePresencePresent, 0)
        self.assertEqual(HealthKit.HKCategoryValuePresenceNotPresent, 1)

        self.assertIsEnumType(HealthKit.HKCategoryValueProgesteroneTestResult)
        self.assertEqual(HealthKit.HKCategoryValueProgesteroneTestResultNegative, 1)
        self.assertEqual(HealthKit.HKCategoryValueProgesteroneTestResultPositive, 2)
        self.assertEqual(
            HealthKit.HKCategoryValueProgesteroneTestResultIndeterminate, 3
        )

        self.assertIsEnumType(HealthKit.HKCategoryValueSeverity)
        self.assertEqual(HealthKit.HKCategoryValueSeverityUnspecified, 0)
        self.assertEqual(HealthKit.HKCategoryValueSeverityNotPresent, 1)
        self.assertEqual(HealthKit.HKCategoryValueSeverityMild, 2)
        self.assertEqual(HealthKit.HKCategoryValueSeverityModerate, 3)
        self.assertEqual(HealthKit.HKCategoryValueSeveritySevere, 4)

        self.assertIsEnumType(HealthKit.HKCategoryValueSleepAnalysis)
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisInBed, 0)
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisAsleepUnspecified, 1)
        self.assertEqual(
            HealthKit.HKCategoryValueSleepAnalysisAsleep,
            HealthKit.HKCategoryValueSleepAnalysisAsleepUnspecified,
        )
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisAwake, 2)
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisAsleepDeep, 4)
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisAsleepREM, 5)

        self.assertIsEnumType(HealthKit.HKCategoryValueAudioExposureEvent)
        self.assertEqual(HealthKit.HKCategoryValueAudioExposureEventLoudEnvironment, 1)
