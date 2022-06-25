from PyObjCTools.TestSupport import TestCase
import HealthKit  # noqa: F401


class TestHKActivitySummary(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("HKLiveWorkoutBuilderDelegate")

    def test_methods(self):
        self.assertResultIsBOOL(
            HealthKit.HKLiveWorkoutBuilder.shouldCollectWorkoutEvents
        )
        self.assertArgIsBOOL(
            HealthKit.HKLiveWorkoutBuilder.setShouldCollectWorkoutEvents_, 0
        )
