from PyObjCTools.TestSupport import TestCase
import HealthKit


class TestHKWorkoutRouteBuilder(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            HealthKit.HKWorkoutRouteBuilder.insertRouteData_completion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKWorkoutRouteBuilder.addMetadata_completion_, 1, b"vZ@"
        )
        self.assertArgIsBlock(
            HealthKit.HKWorkoutRouteBuilder.finishRouteWithWorkout_metadata_completion_,
            2,
            b"v@@",
        )
