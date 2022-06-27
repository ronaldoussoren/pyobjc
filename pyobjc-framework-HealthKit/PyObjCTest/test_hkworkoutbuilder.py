from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKWorkoutBuilder(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKWorkoutBuilder.beginCollectionWithStartDate_completion_,
            1,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKWorkoutBuilder.addSamples_completion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKWorkoutBuilder.addWorkoutEvents_completion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKWorkoutBuilder.addMetadata_completion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKWorkoutBuilder.addWorkoutActivity_completion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKWorkoutBuilder.updateActivityWithUUID_endDate_completion_,
            2,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKWorkoutBuilder.updateActivityWithUUID_addMedatata_completion_,
            2,
            b"vZ@",
        )
        self.assertArgIsBlock(
            HealthKit.HKWorkoutBuilder.finishWorkoutWithCompletion_, 0, b"v@@"
        )
