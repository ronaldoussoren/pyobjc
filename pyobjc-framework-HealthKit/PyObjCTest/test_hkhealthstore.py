from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKHealthStore(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKUserPreferencesDidChangeNotification)

    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKHealthStore.isHealthDataAvailable)
        self.assertResultIsBOOL(HealthKit.HKHealthStore.supportsHealthRecords)
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.requestAuthorizationToShareTypes_readType_completion_,
            2,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.requestPerObjectReadAuthorizationForType_predicate_completion_,
            2,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.getRequestStatusForAuthorizationToShareTypes_readTypes_completion_,
            2,
            b"vQ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.handleAuthorizationForExtensionWithCompletion_,
            0,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.saveObject_withCompletion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.saveObjects_withCompletion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.deleteObject_withCompletion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.deleteObjects_withCompletion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.deleteObjectsOfType_predicate_withCompletion_,
            2,
            b"vZQ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.splitTotalEnergy_startDate_endDate_resultsHandler_,
            3,
            b"v@@@",
        )
        self.assertArgIsOut(HealthKit.HKHealthStore.dateOfBirthComponentsWithError_, 0)
        self.assertArgIsOut(HealthKit.HKHealthStore.biologicalSexWithError_, 0)
        self.assertArgIsOut(HealthKit.HKHealthStore.bloodTypeWithError_, 0)
        self.assertArgIsOut(HealthKit.HKHealthStore.fitzpatrickSkinTypeWithError_, 0)
        self.assertArgIsOut(HealthKit.HKHealthStore.wheelchairUseWithError__, 0)
        self.assertArgIsOut(HealthKit.HKHealthStore.activityMoveModeWithError_, 0)
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.addSamples_toWorkout_completion_, 3, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.startWatchAppWithWorkoutConfiguration_completion_,
            1,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.recoverActiveWorkoutSessionWithCompletion_completion_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.enableBackgroundDeliveryForType_frequency_withCompletion_,
            2,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.disableBackgroundDeliveryForType_withCompletion_,
            1,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.disableAllBackgroundDeliveryWithCompletion_,
            0,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.preferredUnitsForQuantityTypes__completion_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.recalibrateEstimatesForSampleType_atDate__completion_,
            2,
            b"vZ@",
        )
