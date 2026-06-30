from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKWorkoutSession(TestCase):
    def test_enums(self):
        self.assertIsEnumType(HealthKit.HKWorkoutSessionState)
        self.assertEqual(HealthKit.HKWorkoutSessionStateNotStarted, 1)
        self.assertEqual(HealthKit.HKWorkoutSessionStateRunning, 2)
        self.assertEqual(HealthKit.HKWorkoutSessionStateEnded, 3)
        self.assertEqual(HealthKit.HKWorkoutSessionStatePaused, 4)
        self.assertEqual(HealthKit.HKWorkoutSessionStatePrepared, 5)
        self.assertEqual(HealthKit.HKWorkoutSessionStateStopped, 6)

        self.assertIsEnumType(HealthKit.HKWorkoutSessionType)
        self.assertEqual(HealthKit.HKWorkoutSessionTypePrimary, 0)
        self.assertEqual(HealthKit.HKWorkoutSessionTypeMirrored, 1)

    def test_protocols(self):
        self.assertProtocolExists("HKWorkoutSessionDelegate", HealthKit)

    def test_methods(self):
        self.assertArgIsOut(HealthKit.HKWorkoutSession.initWithConfiguration_error_, 1)
        self.assertArgIsOut(
            HealthKit.HKWorkoutSession.initWithHealthStore_configuration_error_, 2
        )
