from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKDefines(TestCase):
    def test_constants(self):
        self.assertIsEnumType(HealthKit.HKErrorCode)
        self.assertEqual(HealthKit.HKUnknownError, 0)
        self.assertEqual(HealthKit.HKNoError, HealthKit.HKUnknownError)
        self.assertEqual(HealthKit.HKErrorHealthDataUnavailable, 1)
        self.assertEqual(HealthKit.HKErrorHealthDataRestricted, 2)
        self.assertEqual(HealthKit.HKErrorInvalidArgument, 3)
        self.assertEqual(HealthKit.HKErrorAuthorizationDenied, 4)
        self.assertEqual(HealthKit.HKErrorAuthorizationNotDetermined, 5)
        self.assertEqual(HealthKit.HKErrorDatabaseInaccessible, 6)
        self.assertEqual(HealthKit.HKErrorUserCanceled, 7)
        self.assertEqual(HealthKit.HKErrorAnotherWorkoutSessionStarted, 8)
        self.assertEqual(HealthKit.HKErrorUserExitedWorkoutSession, 9)
        self.assertEqual(HealthKit.HKErrorRequiredAuthorizationDenied, 10)
        self.assertEqual(HealthKit.HKErrorNoData, 11)
        self.assertEqual(HealthKit.HKErrorWorkoutActivityNotAllowed, 12)
        self.assertEqual(HealthKit.HKErrorDataSizeExceeded, 13)
        self.assertEqual(HealthKit.HKErrorBackgroundWorkoutSessionNotAllowed, 14)

        self.assertIsEnumType(HealthKit.HKUpdateFrequency)
        self.assertEqual(HealthKit.HKUpdateFrequencyImmediate, 1)
        self.assertEqual(HealthKit.HKUpdateFrequencyHourly, 2)
        self.assertEqual(HealthKit.HKUpdateFrequencyDaily, 3)
        self.assertEqual(HealthKit.HKUpdateFrequencyWeekly, 4)

        self.assertIsEnumType(HealthKit.HKAuthorizationStatus)
        self.assertEqual(HealthKit.HKAuthorizationStatusNotDetermined, 0)
        self.assertEqual(HealthKit.HKAuthorizationStatusSharingDenied, 1)
        self.assertEqual(HealthKit.HKAuthorizationStatusSharingAuthorized, 2)

        self.assertIsEnumType(HealthKit.HKAuthorizationRequestStatus)
        self.assertEqual(HealthKit.HKAuthorizationRequestStatusUnknown, 0)
        self.assertEqual(HealthKit.HKAuthorizationRequestStatusShouldRequest, 1)
        self.assertEqual(HealthKit.HKAuthorizationRequestStatusUnnecessary, 2)

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

        self.assertIsEnumType(HealthKit.HKCategoryValueSleepAnalysis)
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisInBed, 0)
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisAsleepUnspecified, 1)
        self.assertEqual(
            HealthKit.HKCategoryValueSleepAnalysisAsleep,
            HealthKit.HKCategoryValueSleepAnalysisAsleepUnspecified,
        )
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisAwake, 2)
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisAsleepCore, 3)
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisAsleepDeep, 4)
        self.assertEqual(HealthKit.HKCategoryValueSleepAnalysisAsleepREM, 5)

        self.assertIsEnumType(HealthKit.HKCategoryValueAppleStandHour)
        self.assertEqual(HealthKit.HKCategoryValueAppleStandHourStood, 0)
        self.assertEqual(HealthKit.HKCategoryValueAppleStandHourIdle, 1)

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

        self.assertIsEnumType(HealthKit.HKCategoryValueCervicalMucusQuality)
        self.assertEqual(HealthKit.HKCategoryValueCervicalMucusQualityDry, 1)
        self.assertEqual(HealthKit.HKCategoryValueCervicalMucusQualitySticky, 2)
        self.assertEqual(HealthKit.HKCategoryValueCervicalMucusQualityCreamy, 3)
        self.assertEqual(HealthKit.HKCategoryValueCervicalMucusQualityWatery, 4)
        self.assertEqual(HealthKit.HKCategoryValueCervicalMucusQualityEggWhite, 5)

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

        self.assertIsEnumType(HealthKit.HKCategoryValueProgesteroneTestResult)
        self.assertEqual(HealthKit.HKCategoryValueProgesteroneTestResultNegative, 1)
        self.assertEqual(HealthKit.HKCategoryValueProgesteroneTestResultPositive, 2)
        self.assertEqual(
            HealthKit.HKCategoryValueProgesteroneTestResultIndeterminate, 3
        )

        self.assertIsEnumType(HealthKit.HKCategoryValueMenstrualFlow)
        self.assertEqual(HealthKit.HKCategoryValueMenstrualFlowUnspecified, 1)
        self.assertEqual(HealthKit.HKCategoryValueMenstrualFlowLight, 2)
        self.assertEqual(HealthKit.HKCategoryValueMenstrualFlowMedium, 3)
        self.assertEqual(HealthKit.HKCategoryValueMenstrualFlowHeavy, 4)
        self.assertEqual(HealthKit.HKCategoryValueMenstrualFlowNone, 5)

        self.assertIsEnumType(HealthKit.HKCategoryValue)
        self.assertEqual(HealthKit.HKCategoryValueNotApplicable, 0)

        self.assertIsEnumType(HealthKit.HKCategoryValueAudioExposureEvent)
        self.assertEqual(HealthKit.HKCategoryValueAudioExposureEventLoudEnvironment, 1)

        self.assertIsEnumType(HealthKit.HKCategoryValueEnvironmentalAudioExposureEvent)
        self.assertEqual(
            HealthKit.HKCategoryValueEnvironmentalAudioExposureEventMomentaryLimit, 1
        )

        self.assertIsEnumType(HealthKit.HKCategoryValueContraceptive)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveUnspecified, 1)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveImplant, 2)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveInjection, 3)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveIntrauterineDevice, 4)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveIntravaginalRing, 5)
        self.assertEqual(HealthKit.HKCategoryValueContraceptiveOral, 6)
        self.assertEqual(HealthKit.HKCategoryValueContraceptivePatch, 7)

        self.assertIsEnumType(HealthKit.HKCategoryValueSeverity)
        self.assertEqual(HealthKit.HKCategoryValueSeverityUnspecified, 0)
        self.assertEqual(HealthKit.HKCategoryValueSeverityNotPresent, 1)
        self.assertEqual(HealthKit.HKCategoryValueSeverityMild, 2)
        self.assertEqual(HealthKit.HKCategoryValueSeverityModerate, 3)
        self.assertEqual(HealthKit.HKCategoryValueSeveritySevere, 4)

        self.assertIsEnumType(HealthKit.HKCategoryValueAppetiteChanges)
        self.assertEqual(HealthKit.HKCategoryValueAppetiteChangesUnspecified, 0)
        self.assertEqual(HealthKit.HKCategoryValueAppetiteChangesNoChange, 1)
        self.assertEqual(HealthKit.HKCategoryValueAppetiteChangesDecreased, 2)
        self.assertEqual(HealthKit.HKCategoryValueAppetiteChangesIncreased, 3)

        self.assertIsEnumType(HealthKit.HKCategoryValuePresence)
        self.assertEqual(HealthKit.HKCategoryValuePresencePresent, 0)
        self.assertEqual(HealthKit.HKCategoryValuePresenceNotPresent, 1)

        self.assertIsEnumType(HealthKit.HKCategoryValueHeadphoneAudioExposureEvent)
        self.assertEqual(
            HealthKit.HKCategoryValueHeadphoneAudioExposureEventSevenDayLimit, 1
        )

        self.assertIsEnumType(HealthKit.HKCategoryValueLowCardioFitnessEvent)
        self.assertEqual(HealthKit.HKCategoryValueLowCardioFitnessEventLowFitness, 1)

        self.assertIsEnumType(HealthKit.HKActivityMoveMode)
        self.assertEqual(HealthKit.HKActivityMoveModeActiveEnergy, 1)
        self.assertEqual(HealthKit.HKActivityMoveModeAppleMoveTime, 2)

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

    def test_functions(self):
        HealthKit.HKCategoryValueSleepAnalysisAsleepValues
