from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKWorkoutBuilder(TestCase):
    def test_methods(self):
        self.asssertArgIsBlock(
            HealthKit.HKWorkoutBuilder.beginCollectionWithStartDate_completion_,
            1,
            b"vZ@",
        )
        self.asssertArgIsBlock(
            HealthKit.HKWorkoutBuilder.addSample_completion_, 1, b"vZ@"
        )
        self.asssertArgIsBlock(
            HealthKit.HKWorkoutBuilder.addWorkoutEvents_completion_, 1, b"vZ@"
        )
        self.asssertArgIsBlock(
            HealthKit.HKWorkoutBuilder.addMetadata_completion_, 1, b"vZ@"
        )
        self.asssertArgIsBlock(
            HealthKit.HKWorkoutBuilder.addWorkoutActivity_completion_, 1, b"vZ@"
        )
        self.asssertArgIsBlock(
            HealthKit.HKWorkoutBuilder.updateActivityWithUUID_endDate_completion_,
            2,
            b"vZ@",
        )
        self.asssertArgIsBlock(
            HealthKit.HKWorkoutBuilder.updateActivityWithUUID_addMedatata_completion_,
            2,
            b"vZ@",
        )
        self.asssertArgIsBlock(
            HealthKit.HKWorkoutBuilder.finishWorkoutWithCompletion_, 0, b"v@@"
        )
