from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import HealthKit


class TestHKHealthStore(TestCase):
    def test_constants(self):
        self.assertIsInstance(HealthKit.HKUserPreferencesDidChangeNotification, str)

    def test_methods(self):
        self.assertResultIsBOOL(HealthKit.HKHealthStore.isHealthDataAvailable)
        self.assertResultIsBOOL(HealthKit.HKHealthStore.supportsHealthRecords)
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.requestAuthorizationToShareTypes_readTypes_completion_,
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
            b"vq@",
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
        self.assertArgIsOut(HealthKit.HKHealthStore.wheelchairUseWithError_, 0)
        self.assertArgIsOut(HealthKit.HKHealthStore.activityMoveModeWithError_, 0)
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.addSamples_toWorkout_completion_, 2, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.startWatchAppWithWorkoutConfiguration_completion_,
            1,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.recoverActiveWorkoutSessionWithCompletion_,
            0,
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
            HealthKit.HKHealthStore.preferredUnitsForQuantityTypes_completion_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            HealthKit.HKHealthStore.recalibrateEstimatesForSampleType_atDate_completion_,
            2,
            b"vZ@",
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        with self.subTest("setWorkoutSessionMirroringStartHandler:"):
            self.assertArgIsBlock(
                HealthKit.HKHealthStore.setWorkoutSessionMirroringStartHandler_,
                0,
                b"v@",
            )

    @min_os_level("14.0")
    @expectedFailure
    def test_methods14_0_missing(self):
        with self.subTest("workoutSessionMirroringStartHandler"):
            self.assertResultIsBlock(
                HealthKit.HKHealthStore.workoutSessionMirroringStartHandler,
                b"v@",
            )
